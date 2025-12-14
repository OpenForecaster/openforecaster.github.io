(() => {
  const config = window.SITE_CONFIG || {};
  const links = config.links || {};

  for (const [key, href] of Object.entries(links)) {
    document.querySelectorAll(`[data-link="${key}"]`).forEach((el) => {
      if (typeof href === "string" && href.trim().length > 0) el.setAttribute("href", href);
    });
  }

  const lastUpdated = document.getElementById("last-updated");
  if (lastUpdated) {
    const modified = new Date(document.lastModified);
    if (!Number.isNaN(modified.getTime())) {
      const yyyy = modified.getFullYear();
      const mm = String(modified.getMonth() + 1).padStart(2, "0");
      const dd = String(modified.getDate()).padStart(2, "0");
      lastUpdated.dateTime = `${yyyy}-${mm}-${dd}`;
      lastUpdated.textContent = new Intl.DateTimeFormat(undefined, {
        year: "numeric",
        month: "short",
        day: "2-digit",
      }).format(modified);
    }
  }

  const icons = {
    github:
      '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .7a11.3 11.3 0 0 0-3.6 22c.6.1.8-.3.8-.6v-2.2c-3.3.8-4-1.4-4-1.4-.6-1.5-1.4-1.9-1.4-1.9-1.1-.8.1-.8.1-.8 1.2.1 1.9 1.3 1.9 1.3 1.1 1.9 2.8 1.3 3.5 1 .1-.8.4-1.3.7-1.6-2.7-.3-5.5-1.4-5.5-6.1 0-1.3.5-2.4 1.2-3.3-.1-.3-.5-1.5.1-3.1 0 0 1-.3 3.3 1.2a11.2 11.2 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.6 1.6.2 2.8.1 3.1.8.9 1.2 2 1.2 3.3 0 4.7-2.8 5.8-5.5 6.1.4.4.8 1.1.8 2.3v3.4c0 .3.2.7.8.6A11.3 11.3 0 0 0 12 .7z"/></svg>',
    arxiv:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 17l5-10h2l5 10"/><path d="M7.2 12h9.6"/><path d="M16.8 17l-2.2-4.5"/><path d="M7.2 17l2.2-4.5"/><path d="M18.5 17h2"/></svg>',
    hf:
      '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6 7a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm12 0a3 3 0 1 1 0 6 3 3 0 0 1 0-6ZM7.5 14.5c1.6 0 3 .8 4.5 2.1 1.5-1.3 2.9-2.1 4.5-2.1 2.6 0 4.5 1.8 4.5 4.3v.5H3v-.5c0-2.5 1.9-4.3 4.5-4.3Z"/></svg>',
    discord:
      '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20 4.5A16 16 0 0 0 16.4 3c-.2.4-.4.9-.6 1.3-1.3-.2-2.6-.2-3.9 0-.2-.4-.4-.9-.6-1.3A16 16 0 0 0 7.7 4.5C5.9 7.2 5.4 9.8 5.6 12.4c1.1.8 2.2 1.3 3.4 1.7.3-.4.6-.8.8-1.2-.5-.2-1-.4-1.5-.7l.3-.2c2.8 1.3 5.8 1.3 8.6 0l.3.2c-.5.3-1 .5-1.5.7.3.4.5.8.8 1.2 1.2-.4 2.3-1 3.4-1.7.2-2.6-.3-5.2-2.1-7.9ZM9.5 13c-.7 0-1.2-.6-1.2-1.3 0-.7.5-1.3 1.2-1.3s1.2.6 1.2 1.3c0 .7-.5 1.3-1.2 1.3Zm5 0c-.7 0-1.2-.6-1.2-1.3 0-.7.5-1.3 1.2-1.3s1.2.6 1.2 1.3c0 .7-.5 1.3-1.2 1.3Z"/></svg>',
    pdf:
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M7 3h7l3 3v15a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z"/><path d="M14 3v4a2 2 0 0 0 2 2h4"/><path d="M7.5 14h9"/><path d="M7.5 17h9"/></svg>',
  };

  document.querySelectorAll("[data-icon]").forEach((el) => {
    const name = el.getAttribute("data-icon");
    if (!name || !icons[name]) return;
    el.innerHTML = icons[name];
  });

  document.querySelectorAll('[data-tabs="results"]').forEach((root) => {
    const tablist = root.querySelector('[role="tablist"]');
    const tabs = Array.from(root.querySelectorAll('[role="tab"]'));
    const panesRoot = root.querySelector("[data-panes]");
    const panes = panesRoot ? Array.from(panesRoot.querySelectorAll('[role="tabpanel"]')) : [];
    if (!tablist || tabs.length === 0 || panes.length === 0) return;

    const prefersReducedMotion =
      typeof window.matchMedia === "function" && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const cycleMs = 6500;
    let activeIndex = 0;
    let timer = null;
    let userStopped = false;

    const setActive = (index, { focus = false } = {}) => {
      activeIndex = index;
      tabs.forEach((tab, i) => {
        const selected = i === index;
        tab.setAttribute("aria-selected", selected ? "true" : "false");
        tab.tabIndex = selected ? 0 : -1;
      });
      panes.forEach((pane, i) => {
        const selected = i === index;
        pane.setAttribute("aria-hidden", selected ? "false" : "true");
        pane.toggleAttribute("inert", !selected);
      });
      if (panesRoot) panesRoot.style.setProperty("--active", String(index));
      if (focus) tabs[index]?.focus();
    };

    const stop = ({ permanent = false } = {}) => {
      if (timer) window.clearInterval(timer);
      timer = null;
      if (permanent) userStopped = true;
    };

    const start = () => {
      if (prefersReducedMotion || userStopped || timer) return;
      timer = window.setInterval(() => {
        setActive((activeIndex + 1) % tabs.length);
      }, cycleMs);
    };

    tabs.forEach((tab, i) =>
      tab.addEventListener("click", () => {
        setActive(i);
        stop({ permanent: true });
      }),
    );

    tablist.addEventListener("keydown", (e) => {
      const current = tabs.findIndex((t) => t.getAttribute("aria-selected") === "true");
      if (current < 0) return;
      const last = tabs.length - 1;

      if (e.key === "ArrowRight") {
        e.preventDefault();
        setActive(current === last ? 0 : current + 1, { focus: true });
        stop({ permanent: true });
      } else if (e.key === "ArrowLeft") {
        e.preventDefault();
        setActive(current === 0 ? last : current - 1, { focus: true });
        stop({ permanent: true });
      } else if (e.key === "Home") {
        e.preventDefault();
        setActive(0, { focus: true });
        stop({ permanent: true });
      } else if (e.key === "End") {
        e.preventDefault();
        setActive(last, { focus: true });
        stop({ permanent: true });
      }
    });

    setActive(0);
    start();

    root.addEventListener("pointerenter", () => stop());
    root.addEventListener("pointerleave", () => start());
    root.addEventListener("focusin", () => stop());
    root.addEventListener("focusout", () => {
      window.setTimeout(() => {
        if (!root.contains(document.activeElement)) start();
      }, 0);
    });

    document.addEventListener("visibilitychange", () => {
      if (document.hidden) stop();
      else start();
    });
  });
})();
