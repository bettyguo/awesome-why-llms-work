/* Landing-page interactivity: loads ledger.json, paints programmes grid + snapshot. */

const STATUS_KEY = {
  'supported': { emoji: '🟢', label: 'Supported' },
  'contested': { emoji: '🟡', label: 'Contested' },
  'refuted':   { emoji: '🔴', label: 'Refuted'   },
  'open':      { emoji: '⚪', label: 'Open'      },
};

function normalizeStatus(s) {
  if (!s) return 'open';
  if (s.includes('🟢')) return 'supported';
  if (s.includes('🟡')) return 'contested';
  if (s.includes('🔴')) return 'refuted';
  if (s.includes('⚪')) return 'open';
  // Multi-status rows like "🟢 / 🟡" — count the first.
  return 'open';
}

function countStatuses(programme) {
  const c = { supported: 0, contested: 0, refuted: 0, open: 0 };
  for (const claim of programme.claims) {
    c[normalizeStatus(claim.status)]++;
  }
  return c;
}

async function load() {
  const res = await fetch('data/ledger.json');
  if (!res.ok) throw new Error('failed to load ledger.json');
  return res.json();
}

function renderProgrammesGrid(programmes) {
  const grid = document.getElementById('programmes-grid');
  if (!grid) return;
  grid.innerHTML = programmes.map(p => {
    const c = countStatuses(p);
    const id = p.id;
    const fileUrl = `https://github.com/OWNER/awesome-why-llms-work/blob/main/${p.file}`;
    return `
      <a href="${fileUrl}" data-pid="${id}" class="programme-card block">
        <div class="flex items-start gap-3 mb-3">
          <div class="prog-id">${id}</div>
          <div>
            <h3 class="font-bold text-lg leading-tight">${p.title}</h3>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
              ${p.claims.length} tracked claims
            </p>
          </div>
        </div>
        <p class="text-sm text-slate-700 dark:text-slate-300 mb-4">
          <span class="font-medium">Hard core:</span> ${p.hard_core || '(see programme file)'}
        </p>
        <div class="flex flex-wrap gap-1.5">
          ${c.supported ? `<span class="pill" data-status="supported">🟢 ${c.supported}</span>` : ''}
          ${c.contested ? `<span class="pill" data-status="contested">🟡 ${c.contested}</span>` : ''}
          ${c.refuted   ? `<span class="pill" data-status="refuted">🔴 ${c.refuted}</span>`     : ''}
          ${c.open      ? `<span class="pill" data-status="open">⚪ ${c.open}</span>`            : ''}
        </div>
      </a>
    `;
  }).join('');
}

function renderStatusSnapshot(programmes) {
  const root = document.getElementById('status-snapshot');
  if (!root) return;
  const totals = { supported: 0, contested: 0, refuted: 0, open: 0 };
  for (const p of programmes) {
    const c = countStatuses(p);
    for (const k of Object.keys(c)) totals[k] += c[k];
  }
  const grandTotal = Object.values(totals).reduce((a, b) => a + b, 0) || 1;
  const order = ['supported', 'contested', 'refuted', 'open'];
  const palette = {
    supported: '#34d399', contested: '#fbbf24',
    refuted:   '#f87171', open:      '#94a3b8',
  };
  root.innerHTML = order.map(k => {
    const pct = (totals[k] / grandTotal) * 100;
    return `
      <div>
        <div class="flex items-center justify-between text-sm mb-1">
          <span class="text-slate-200">${STATUS_KEY[k].emoji} ${STATUS_KEY[k].label}</span>
          <span class="font-mono text-slate-400">${totals[k]}</span>
        </div>
        <div class="h-1.5 rounded-full bg-white/10 overflow-hidden">
          <div class="h-full" style="width:${pct}%; background:${palette[k]}"></div>
        </div>
      </div>
    `;
  }).join('');
}

(async () => {
  try {
    const data = await load();
    renderProgrammesGrid(data.programmes);
    renderStatusSnapshot(data.programmes);
    const el = document.getElementById('generated-at');
    if (el) el.textContent = data.generated_at;
  } catch (e) {
    console.error(e);
    const grid = document.getElementById('programmes-grid');
    if (grid) grid.innerHTML = `<p class="text-sm text-slate-500">Failed to load ledger data. Try reloading.</p>`;
  }
})();
