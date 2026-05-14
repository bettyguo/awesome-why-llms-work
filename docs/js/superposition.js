/* Interactive in-browser toy-superposition demo (Elhage et al. 2022).
   Two-layer model with d=2 bottleneck, n binary-sparse features.
   Trains with plain SGD + L2; visualizes the encoder columns as the
   feature directions in the 2-D bottleneck plane.

   No dependencies; vanilla JS + SVG. Runs in well under a second per
   training session at n≤9, steps≤3000.
*/

const D = 2;            // bottleneck dim (fixed for visualization)
const BATCH = 64;
const LR = 0.04;
const SEED_BASE = 7;

// ----- tiny deterministic RNG (mulberry32) -----
function mulberry32(seed) {
  let a = seed | 0;
  return function () {
    a = (a + 0x6d2b79f5) | 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// ----- model state -----
function makeModel(n, seed) {
  const rng = mulberry32(seed);
  // W is d × n (encoder columns are feature directions); decoder tied.
  const W = new Float32Array(D * n);
  for (let i = 0; i < W.length; i++) W[i] = (rng() - 0.5) * 0.1;
  const b = new Float32Array(n);
  // Feature importances slightly decay across features (matches Elhage convention).
  const importance = new Float32Array(n);
  for (let i = 0; i < n; i++) importance[i] = 1.0 - 0.3 * (i / Math.max(1, n - 1));
  return { n, W, b, importance, rng };
}

function sampleBatch(model, p, batch) {
  // x[batch][n]: x_i = U(0,1) if Bernoulli(p) else 0.
  const X = new Float32Array(batch * model.n);
  for (let b = 0; b < batch; b++) {
    for (let i = 0; i < model.n; i++) {
      if (model.rng() < p) X[b * model.n + i] = model.rng();
    }
  }
  return X;
}

/* Forward + loss + grads.
   x: (B,n)  W: (d,n)  -> h = x W^T  : (B,d)
   y_pred = ReLU(h W + b) : (B,n)
   loss = mean over batch of importance .* (y_pred - x)^2

   We implement the gradient by hand (it's small).
*/
function trainStep(model, X, batch) {
  const { n, W, b, importance } = model;

  // h = X @ W^T   shape (B, d)
  const H = new Float32Array(batch * D);
  for (let bi = 0; bi < batch; bi++) {
    for (let dj = 0; dj < D; dj++) {
      let s = 0;
      for (let ni = 0; ni < n; ni++) s += X[bi * n + ni] * W[dj * n + ni];
      H[bi * D + dj] = s;
    }
  }
  // y_pre = h @ W + b   shape (B, n);   y = relu(y_pre)
  const Ypre = new Float32Array(batch * n);
  const Y = new Float32Array(batch * n);
  for (let bi = 0; bi < batch; bi++) {
    for (let ni = 0; ni < n; ni++) {
      let s = b[ni];
      for (let dj = 0; dj < D; dj++) s += H[bi * D + dj] * W[dj * n + ni];
      Ypre[bi * n + ni] = s;
      Y[bi * n + ni] = s > 0 ? s : 0;
    }
  }
  // Loss + dL/dY  = 2 * imp * (Y - X) / B
  let loss = 0;
  const dY = new Float32Array(batch * n);
  for (let bi = 0; bi < batch; bi++) {
    for (let ni = 0; ni < n; ni++) {
      const diff = Y[bi * n + ni] - X[bi * n + ni];
      loss += importance[ni] * diff * diff;
      dY[bi * n + ni] = (2.0 * importance[ni] * diff) / batch;
    }
  }
  loss /= batch;

  // dY_pre = dY * (Ypre > 0)
  const dYpre = new Float32Array(batch * n);
  for (let k = 0; k < dYpre.length; k++) dYpre[k] = Ypre[k] > 0 ? dY[k] : 0;

  // db = sum over batch of dYpre
  const db = new Float32Array(n);
  for (let bi = 0; bi < batch; bi++)
    for (let ni = 0; ni < n; ni++) db[ni] += dYpre[bi * n + ni];

  // dW from the decoder side: dW_dec[d,n] = sum_b H[b,d] * dYpre[b,n]
  const dW_dec = new Float32Array(D * n);
  for (let bi = 0; bi < batch; bi++)
    for (let dj = 0; dj < D; dj++)
      for (let ni = 0; ni < n; ni++)
        dW_dec[dj * n + ni] += H[bi * D + dj] * dYpre[bi * n + ni];

  // dH[b,d] = sum_n dYpre[b,n] * W[d,n]
  const dH = new Float32Array(batch * D);
  for (let bi = 0; bi < batch; bi++)
    for (let dj = 0; dj < D; dj++) {
      let s = 0;
      for (let ni = 0; ni < n; ni++) s += dYpre[bi * n + ni] * W[dj * n + ni];
      dH[bi * D + dj] = s;
    }

  // dW from encoder side: dW_enc[d,n] = sum_b dH[b,d] * X[b,n]
  const dW_enc = new Float32Array(D * n);
  for (let bi = 0; bi < batch; bi++)
    for (let dj = 0; dj < D; dj++)
      for (let ni = 0; ni < n; ni++)
        dW_enc[dj * n + ni] += dH[bi * D + dj] * X[bi * n + ni];

  // Step
  for (let k = 0; k < W.length; k++) W[k] -= LR * (dW_dec[k] + dW_enc[k]);
  for (let k = 0; k < b.length; k++) model.b[k] -= LR * db[k];

  return loss;
}

function trainModel(n, p, steps, onProgress) {
  const model = makeModel(n, SEED_BASE + Math.floor(p * 1000) + n);
  let lastLoss = NaN;
  for (let s = 0; s < steps; s++) {
    const X = sampleBatch(model, p, BATCH);
    lastLoss = trainStep(model, X, BATCH);
  }
  if (onProgress) onProgress(steps, lastLoss);
  return { model, loss: lastLoss };
}

// ---------- rendering ----------

function renderSVG(model) {
  const svg = document.getElementById('demo-svg');
  if (!svg) return;
  const { n, W } = model;
  // Programme 02 hue scale.
  const hues = [
    '#059669', '#0ea5e9', '#7c3aed', '#ec4899', '#f97316',
    '#facc15', '#84cc16', '#14b8a6', '#6366f1',
  ];

  let html = '';
  // Grid + axes for context.
  html += `<g stroke="#cbd5e1" stroke-width="0.005" opacity="0.6">
    <line x1="-1" y1="0" x2="1" y2="0"/>
    <line x1="0" y1="-1" x2="0" y2="1"/>
    <circle cx="0" cy="0" r="1" fill="none" stroke="#cbd5e1" stroke-dasharray="0.02,0.015"/>
  </g>`;
  // Arrows (each column of W is a feature direction).
  // Normalize for plot by clipping length to 1 (keeps demo readable when
  // the model overshoots during training).
  const eps = 0.01;
  for (let i = 0; i < n; i++) {
    const dx = W[0 * n + i];
    const dy = W[1 * n + i];
    const len = Math.hypot(dx, dy);
    if (len < eps) continue;
    const scale = Math.min(1, len) / len;
    const x = dx * scale;
    const y = dy * scale;          // svg y is flipped, but our coords are abstract
    const color = hues[i % hues.length];
    html += `<g stroke="${color}" fill="${color}" opacity="0.9" stroke-linecap="round">
      <line x1="0" y1="0" x2="${x}" y2="${y}" stroke-width="0.018"/>
      <circle cx="${x}" cy="${y}" r="0.030"/>
      <text x="${x * 1.10}" y="${y * 1.10}" font-size="0.075"
            fill="${color}" font-weight="700" text-anchor="middle"
            dominant-baseline="middle" font-family="JetBrains Mono">${i}</text>
    </g>`;
  }
  svg.innerHTML = html;
}

// ---------- controls ----------

const $ = (id) => document.getElementById(id);

function readP() {
  // The slider is in log10(p); we want p in [0.001, 0.9].
  const logp = parseFloat($('ctl-p').value);
  return Math.min(0.9, Math.max(0.001, Math.pow(10, logp)));
}
function readN() { return parseInt($('ctl-n').value, 10); }
function readSteps() { return parseInt($('ctl-steps').value, 10); }

function updateReadout(loss, step) {
  $('readout-loss').textContent = isFinite(loss) ? loss.toFixed(4) : '—';
  $('readout-step').textContent = step;
}
function syncSliderLabels() {
  $('val-n').textContent = readN();
  $('val-steps').textContent = readSteps();
  $('val-p').textContent = `p = ${readP().toFixed(3)}`;
}
function retrain() {
  const n = readN();
  const p = readP();
  const steps = readSteps();
  syncSliderLabels();
  // Use a small setTimeout to let the UI update.
  setTimeout(() => {
    const { model, loss } = trainModel(n, p, steps);
    renderSVG(model);
    updateReadout(loss, steps);
  }, 0);
}

['ctl-n', 'ctl-p', 'ctl-steps'].forEach(id => {
  $(id).addEventListener('input', () => {
    syncSliderLabels();
  });
  $(id).addEventListener('change', retrain);
});
$('btn-train').addEventListener('click', retrain);
$('btn-reset').addEventListener('click', () => {
  $('ctl-n').value = 6;
  $('ctl-p').value = -1.7;
  $('ctl-steps').value = 1500;
  retrain();
});

// Initial run.
retrain();
