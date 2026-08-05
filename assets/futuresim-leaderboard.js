(function () {
  const root = document.querySelector('[data-futuresim-q2-results]');
  if (!root) return;

  const buttons = root.querySelectorAll('[data-futuresim-metric]');
  const plots = root.querySelectorAll('[data-futuresim-plot]');

  for (const button of buttons) {
    button.addEventListener('click', () => {
      const metric = button.dataset.futuresimMetric;
      for (const item of buttons) item.setAttribute('aria-pressed', String(item === button));
      for (const plot of plots) plot.hidden = plot.dataset.futuresimPlot !== metric;
    });
  }
})();
