(function () {
  var links = Array.prototype.slice.call(document.querySelectorAll('.nav-link'));
  var pages = Array.prototype.slice.call(document.querySelectorAll('.page'));
  var sidebar = document.getElementById('sidebar');
  var overlay = document.getElementById('overlay');
  var menuBtn = document.getElementById('menuBtn');
  var search = document.getElementById('search');

  function idFromHash() {
    var h = location.hash.replace('#', '');
    return h || 'home';
  }

  function show(id) {
    var target = document.getElementById(id);
    if (!target || !target.classList.contains('page')) id = 'home';
    pages.forEach(function (p) { p.classList.toggle('active', p.id === id); });
    links.forEach(function (a) {
      a.classList.toggle('active', a.getAttribute('href') === '#' + id);
    });
    window.scrollTo(0, 0);
    closeSidebar();
    var t = document.querySelector('.nav-link.active');
    if (t && t.scrollIntoView) t.scrollIntoView({ block: 'nearest' });
  }

  function openSidebar() { sidebar.classList.add('open'); }
  function closeSidebar() { sidebar.classList.remove('open'); }

  menuBtn.addEventListener('click', function () {
    sidebar.classList.toggle('open');
  });
  overlay.addEventListener('click', closeSidebar);

  window.addEventListener('hashchange', function () { show(idFromHash()); });
  show(idFromHash());

  function runSearch(q) {
    q = q.trim().toLowerCase();
    links.forEach(function (a) {
      var match = !q || a.textContent.toLowerCase().indexOf(q) !== -1;
      a.classList.toggle('search-hidden', !match);
    });
    document.querySelectorAll('.nav-group').forEach(function (g) {
      var any = g.querySelectorAll('.nav-link:not(.search-hidden)').length > 0;
      g.classList.toggle('search-hidden', !any && !!q);
    });
    if (q) {
      var visible = links.filter(function (a) { return !a.classList.contains('search-hidden'); });
      if (visible.length === 1) {
        location.hash = visible[0].getAttribute('href');
      }
    }
  }
  search.addEventListener('input', function () { runSearch(this.value); });

  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement !== search) {
      e.preventDefault();
      search.focus();
    }
    if (e.key === 'Escape') {
      search.blur();
      closeSidebar();
    }
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      search.focus();
      search.select();
    }
  });
})();
