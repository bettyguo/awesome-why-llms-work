/* Shared site chrome: top nav. Imported by every docs/*.html page. */

(function initNav() {
  const here = location.pathname.split('/').pop() || 'index.html';
  const link = (href, label) => {
    const active = href === here;
    return `<a href="${href}"
              class="px-3 py-1.5 rounded-md text-sm font-medium transition-colors
                     ${active
                       ? 'bg-slate-900 text-white dark:bg-slate-100 dark:text-slate-900'
                       : 'text-slate-600 hover:text-slate-900 dark:text-slate-400 dark:hover:text-slate-100'}">
              ${label}
            </a>`;
  };
  const html = `
    <header class="sticky top-0 z-40 backdrop-blur bg-white/70 dark:bg-slate-900/70 border-b border-slate-200/60 dark:border-slate-800/60">
      <div class="max-w-6xl mx-auto px-6 py-3 flex items-center gap-4">
        <a href="index.html" class="font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
          <span class="inline-block w-2.5 h-2.5 rounded-full"
                style="background: linear-gradient(135deg, #2563eb 0%, #ea580c 100%);"></span>
          why-llms-work
        </a>
        <nav class="flex items-center gap-1 ml-2">
          ${link('index.html', 'Programmes')}
          ${link('ledger.html', 'Ledger')}
          ${link('superposition-demo.html', 'Demo')}
        </nav>
        <div class="ml-auto flex items-center gap-3 text-sm">
          <a href="https://github.com/bettyguo/awesome-why-llms-work"
             class="text-slate-600 hover:text-slate-900 dark:text-slate-400 dark:hover:text-slate-100 font-medium">
             GitHub →
          </a>
        </div>
      </div>
    </header>
  `;
  document.getElementById('site-nav')?.insertAdjacentHTML('beforeend', html);
})();
