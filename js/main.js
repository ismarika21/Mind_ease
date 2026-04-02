/* ============================
   MindEase – main.js
   ============================ */

(function () {

  /* ── Navbar ── */
  const navbar       = document.querySelector('.navbar');
  const hamburger    = document.querySelector('.hamburger');
  const mobileMenu   = document.querySelector('.mobile-menu');
  const navLinks     = document.querySelectorAll('.nav-link');

  // Active link
  const currentPage = location.pathname.split('/').pop() || 'index.html';
  navLinks.forEach(l => {
    const href = l.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      l.classList.add('active');
    }
  });

  // Scroll class
  window.addEventListener('scroll', () => {
    navbar?.classList.toggle('scrolled', window.scrollY > 20);
  });

  // Hamburger toggle
  hamburger?.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    mobileMenu?.classList.toggle('open');
  });

  // Close mobile menu on link click
  document.querySelectorAll('.mobile-menu .nav-link').forEach(l => {
    l.addEventListener('click', () => {
      hamburger?.classList.remove('open');
      mobileMenu?.classList.remove('open');
    });
  });

  /* ── Scroll Animations ── */
  const animateEls = document.querySelectorAll('.animate');
  const observer   = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('is-visible');
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  animateEls.forEach(el => observer.observe(el));

  /* ── Bar chart animation ── */
  const barObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.querySelectorAll('.bar-fill').forEach(fill => {
          const w = fill.getAttribute('data-width') || '0';
          fill.style.width = w + '%';
        });
        e.target.querySelectorAll('.progress-fill').forEach(fill => {
          const w = fill.getAttribute('data-width') || '0';
          fill.style.width = w + '%';
        });
        barObserver.unobserve(e.target);
      }
    });
  }, { threshold: 0.2 });
  document.querySelectorAll('.bar-chart-visual, .progress-wrap').forEach(el => barObserver.observe(el));

  /* Password strength is handled by signup.html's own inline script */

  /* contactForm submission is fully handled by contact.html's own validated script */

  /* signupForm submission is fully handled by signup.html's own validated script */

  /* ── Toast notification ── */
  function showToast(msg) {
    const prev = document.querySelector('.toast');
    prev?.remove();
    const t = document.createElement('div');
    t.className = 'toast';
    t.innerHTML = `<span>${msg}</span>`;
    Object.assign(t.style, {
      position: 'fixed', bottom: '28px', right: '28px', zIndex: 9999,
      background: 'linear-gradient(135deg,#7C3AED,#3B82F6)',
      color: '#fff', padding: '14px 24px', borderRadius: '12px',
      boxShadow: '0 8px 30px rgba(0,0,0,.2)',
      fontSize: '.9rem', fontFamily: 'Inter,sans-serif', fontWeight: 500,
      transform: 'translateY(20px)', opacity: '0',
      transition: 'all .35s cubic-bezier(.4,0,.2,1)',
      maxWidth: '320px'
    });
    document.body.appendChild(t);
    requestAnimationFrame(() => {
      t.style.transform = 'translateY(0)';
      t.style.opacity = '1';
    });
    setTimeout(() => {
      t.style.transform = 'translateY(20px)';
      t.style.opacity = '0';
      setTimeout(() => t.remove(), 400);
    }, 3500);
  }

  /* ── Counter animation ── */
  function animateCounter(el, target, duration = 1800) {
    let start = 0;
    const step = timestamp => {
      if (!start) start = timestamp;
      const progress = Math.min((timestamp - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(eased * target).toLocaleString();
      if (progress < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }

  const counterObserver = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        const el  = e.target;
        const val = parseInt(el.getAttribute('data-count') || '0', 10);
        animateCounter(el, val);
        counterObserver.unobserve(el);
      }
    });
  }, { threshold: 0.4 });
  document.querySelectorAll('[data-count]').forEach(el => counterObserver.observe(el));

  /* ── Smooth scroll for hash links ── */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  /* ── Mobile mood dots ── */
  document.querySelectorAll('.mood-dot').forEach(dot => {
    dot.addEventListener('click', () => {
      document.querySelectorAll('.mood-dot').forEach(d => d.classList.remove('active'));
      dot.classList.add('active');
    });
  });

})();
