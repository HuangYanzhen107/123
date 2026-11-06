(function () {
  'use strict';

  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const small = matchMedia('(max-width: 700px)');
  const connection = navigator.connection;
  const films = Array.from(document.querySelectorAll('.campaign-film'));
  const visibleFilms = new Set();

  function updateFilm(video) {
    const source = (small.matches && video.dataset.videoMobile) || video.dataset.videoDesktop;
    const current = video.getAttribute('src');
    const still = reduced.matches || connection?.saveData;
    const canPlay = visibleFilms.has(video) && !document.hidden && !document.querySelector('dialog[open]');

    if (still || !canPlay) {
      video.pause();
      if (current && (still || current !== source)) {
        video.classList.remove('has-frame');
        video.removeAttribute('src');
        video.load();
      }
      return;
    }

    if (current !== source) {
      video.classList.remove('has-frame');
      video.muted = true;
      video.src = source;
    }
    if (current !== source || video.paused) video.play().catch(() => {});
  }

  const updateFilms = () => films.forEach(updateFilm);
  films.forEach(video => {
    video.addEventListener('playing', () => video.classList.add('has-frame'));
    video.addEventListener('error', () => video.classList.remove('has-frame'));
  });
  if ('IntersectionObserver' in window) {
    const filmThreshold = 0.12;
    const observer = new IntersectionObserver(entries => {
      for (const {target, intersectionRatio} of entries) {
        if (intersectionRatio >= filmThreshold) visibleFilms.add(target);
        else visibleFilms.delete(target);
        updateFilm(target);
      }
    }, {threshold: filmThreshold});
    films.forEach(video => observer.observe(video));
  }
  // Browsers without viewport observation show the posters.
  document.addEventListener('visibilitychange', updateFilms);
  small.addEventListener('change', updateFilms);
  connection?.addEventListener('change', updateFilms);
  const modalObserver = new MutationObserver(updateFilms);
  document.querySelectorAll('dialog').forEach(dialog => {
    modalObserver.observe(dialog, {attributes: true, attributeFilter: ['open']});
  });

  const ringVideo = document.getElementById('ringVideo');
  const ringPoster = document.getElementById('ringPoster');
  const tones = Array.from(document.querySelectorAll('[data-ring-tone]'));
  tones.forEach(button => {
    button.addEventListener('click', () => {
      if (button.getAttribute('aria-pressed') === 'true') return;
      const tone = button.dataset.ringTone;
      tones.forEach(option => option.setAttribute('aria-pressed', String(option === button)));
      ringPoster.src = '/assets/campaign/ring-' + tone + '.webp';
      ringPoster.dataset.altEn = tone === 'gold' ? 'Gold-colour ring product reference' : 'Silver-colour ring product reference';
      ringPoster.dataset.altZh = tone === 'gold' ? '金色戒指商品参考图' : '银色戒指商品参考图';
      ringPoster.alt = document.documentElement.lang === 'zh-CN' ? ringPoster.dataset.altZh : ringPoster.dataset.altEn;
      ringVideo.dataset.videoDesktop = '/assets/campaign/ring-' + tone + '-loop.mp4';
      updateFilm(ringVideo);
    });
  });

  const dialog = document.getElementById('stylingDialog');
  const tabs = Array.from(dialog.querySelectorAll('[data-style-tab]'));

  function selectTab(key, focus = false) {
    tabs.forEach(tab => {
      const selected = tab.dataset.styleTab === key;
      tab.setAttribute('aria-selected', String(selected));
      tab.tabIndex = selected ? 0 : -1;
      document.getElementById(tab.getAttribute('aria-controls')).hidden = !selected;
      if (selected && focus) tab.focus();
    });
  }

  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => selectTab(tab.dataset.styleTab));
    tab.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      else if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
      else if (event.key === 'Home') next = 0;
      else if (event.key === 'End') next = tabs.length - 1;
      else return;
      event.preventDefault();
      selectTab(tabs[next].dataset.styleTab, true);
    });
  });
  document.querySelectorAll('[data-open="stylingDialog"]').forEach(button => {
    button.addEventListener('click', () => selectTab(button.dataset.stylingTab || 'earring'));
  });

  function updateMotion() {
    document.documentElement.classList.toggle('cover-motion', !reduced.matches);
    updateFilms();
  }

  reduced.addEventListener('change', updateMotion);
  updateMotion();
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    }, {threshold: 0.1});
    document.querySelectorAll('.story-copy, .earring-copy, .brand-philosophy-inner, .edit-heading, .edit-card').forEach(item => {
      item.classList.add('cover-reveal');
      observer.observe(item);
    });
  }
})();
