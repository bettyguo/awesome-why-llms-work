/* Interactive falsification ledger:
   - filterable by programme + status
   - searchable by claim text
   - rows expand to reveal supporting/refuting citations
*/

const STATUS_KEY = {
  supported: { emoji: '🟢', label: 'Supported' },
  contested: { emoji: '🟡', label: 'Contested' },
  refuted:   { emoji: '🔴', label: 'Refuted'   },
  open:      { emoji: '⚪', label: 'Open'      },
};

function normalizeStatus(s) {
  if (!s) return 'open';
  if (s.includes('🟢')) return 'supported';
  if (s.includes('🟡')) return 'contested';
  if (s.includes('🔴')) return 'refuted';
  if (s.includes('⚪')) return 'open';
  return 'open';
}

const state = {
  rows: [],
  filterProgramme: 'all',
  filterStatus: 'all',
  query: '',
};

async function loadLedger() {
  const res = await fetch('data/ledger.json');
  if (!res.ok) throw new Error('failed to load ledger.json');
  const data = await res.json();
  state.rows = [];
  for (const p of data.programmes) {
    for (const claim of p.claims) {
      state.rows.push({
        programme_id: p.id,
        programme_title: p.title,
        programme_color: p.color,
        claim_id: claim.id,
        text: claim.text,
        status: claim.status,
        status_key: normalizeStatus(claim.status),
        supporting: claim.supporting,
        refuting: claim.refuting,
      });
    }
  }
  return data;
}

function filterRows() {
  return state.rows.filter(r => {
    if (state.filterProgramme !== 'all' && r.programme_id !== state.filterProgramme) return false;
    if (state.filterStatus !== 'all' && r.status_key !== state.filterStatus) return false;
    if (state.query) {
      const q = state.query.toLowerCase();
      if (!r.text.toLowerCase().includes(q) && !r.claim_id.toLowerCase().includes(q)) return false;
    }
    return true;
  });
}

function renderRows() {
  const body = document.getElementById('ledger-body');
  const rows = filterRows();
  document.getElementById('results-count').textContent = rows.length;
  document.getElementById('total-count').textContent = state.rows.length;
  if (rows.length === 0) {
    body.innerHTML = `
      <tr><td colspan="3" class="px-4 py-12 text-center text-slate-500">
        No claims match the current filters.
      </td></tr>`;
    return;
  }
  body.innerHTML = rows.map(r => `
    <tr class="ledger-row align-top" data-row-id="${r.claim_id}">
      <td class="px-4 py-3 claim-id whitespace-nowrap">
        <span class="inline-flex items-center gap-2">
          <span class="inline-block w-2 h-2 rounded-full" style="background:${r.programme_color}"></span>
          ${r.claim_id}
        </span>
      </td>
      <td class="px-4 py-3">
        <button class="text-left w-full" onclick="toggleRow('${r.claim_id}')">${r.text}</button>
        <div class="row-detail mt-2 text-xs text-slate-600 dark:text-slate-400 hidden" id="detail-${r.claim_id}">
          <div class="grid md:grid-cols-2 gap-3 mt-2 p-3 rounded-md bg-slate-50 dark:bg-slate-800/50">
            <div>
              <div class="font-semibold mb-1 text-slate-700 dark:text-slate-300">Best supporting</div>
              <div>${r.supporting || '<span class="text-slate-400">—</span>'}</div>
            </div>
            <div>
              <div class="font-semibold mb-1 text-slate-700 dark:text-slate-300">Best refuting / contesting</div>
              <div>${r.refuting || '<span class="text-slate-400">—</span>'}</div>
            </div>
          </div>
        </div>
      </td>
      <td class="px-4 py-3 whitespace-nowrap">
        <span class="pill" data-status="${r.status_key}">
          ${STATUS_KEY[r.status_key].emoji} ${STATUS_KEY[r.status_key].label}
        </span>
      </td>
    </tr>
  `).join('');
}

window.toggleRow = function (id) {
  const el = document.getElementById(`detail-${id}`);
  if (el) el.classList.toggle('hidden');
};

function bindFilters() {
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const group = btn.dataset.filter;
      // Reset siblings in the same group.
      document.querySelectorAll(`.filter-btn[data-filter="${group}"]`).forEach(b => {
        b.dataset.active = 'false';
      });
      btn.dataset.active = 'true';
      if (group === 'programme') state.filterProgramme = btn.dataset.value;
      if (group === 'status')    state.filterStatus    = btn.dataset.value;
      renderRows();
    });
  });
  const search = document.getElementById('ledger-search');
  if (search) {
    search.addEventListener('input', (e) => {
      state.query = e.target.value;
      renderRows();
    });
  }
}

(async () => {
  try {
    await loadLedger();
    bindFilters();
    renderRows();
  } catch (e) {
    console.error(e);
    document.getElementById('ledger-body').innerHTML = `
      <tr><td colspan="3" class="px-4 py-12 text-center text-slate-500">
        Failed to load ledger data. Try reloading.
      </td></tr>`;
  }
})();
