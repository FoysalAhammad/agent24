(function(){
  var links = Array.prototype.slice.call(document.querySelectorAll('.topnav a[href^="#"], .brand[href^="#"]'));
  var sections = Array.prototype.slice.call(document.querySelectorAll('section[id]'));

  function onScroll(){
    var pos = window.scrollY + 140;
    var current = sections[0] ? sections[0].id : '';
    for (var i = 0; i < sections.length; i++) {
      if (sections[i].offsetTop <= pos) current = sections[i].id;
    }
    links.forEach(function(a){
      var href = a.getAttribute('href').slice(1);
      if (href === current) a.classList.add('active');
      else a.classList.remove('active');
    });
  }

  var ticking = false;
  window.addEventListener('scroll', function(){
    if (!ticking) {
      window.requestAnimationFrame(function(){ onScroll(); ticking = false; });
      ticking = true;
    }
  }, {passive:true});

  links.forEach(function(a){
    a.addEventListener('click', function(e){
      var id = a.getAttribute('href').slice(1);
      var el = document.getElementById(id);
      if (el) {
        e.preventDefault();
        window.scrollTo({top: el.offsetTop - 90, behavior:'smooth'});
        history.replaceState(null, '', '#' + id);
      }
    });
  });

  // reveal-on-scroll for cards
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if (en.isIntersecting) { en.target.style.opacity = 1; en.target.style.transform = 'none'; io.unobserve(en.target); }
      });
    }, {threshold:.12});
    document.querySelectorAll('.proj-card, .skill-card, .about-card, .contact-card').forEach(function(el){
      el.style.opacity = 0;
      el.style.transform = 'translateY(16px)';
      el.style.transition = 'opacity .5s cubic-bezier(.22,1,.36,1), transform .5s cubic-bezier(.22,1,.36,1), box-shadow .25s';
      io.observe(el);
    });
  }

  // respect reduced motion
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('.proj-card, .skill-card, .about-card, .contact-card').forEach(function(el){
      el.style.opacity = 1; el.style.transform = 'none';
    });
  }

  onScroll();
})();
