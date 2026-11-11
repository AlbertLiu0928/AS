/* Aperture Science — shared behaviour */
(function () {
  'use strict';

  // Email is assembled in script (same approach as the original site) to reduce scraping.
  var targetEmail = 'Admin' + '@' + 'Aperturescience.com.tw';

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-email]').forEach(function (el) {
      el.textContent = targetEmail;
    });

    // Shrinking nav on scroll
    var nav = document.getElementById('main-nav');
    var navContainer = document.getElementById('nav-container');
    function onScroll() {
      if (!nav || !navContainer) return;
      if (window.scrollY > 50) {
        navContainer.classList.remove('h-20');
        navContainer.classList.add('h-16');
        nav.classList.add('shadow-md');
      } else {
        navContainer.classList.remove('h-16');
        navContainer.classList.add('h-20');
        nav.classList.remove('shadow-md');
      }
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    // Mobile menu
    var btn = document.getElementById('menu-btn');
    var menu = document.getElementById('mobile-menu');
    if (btn && menu) {
      btn.addEventListener('click', function () {
        var open = menu.classList.toggle('hidden') === false;
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
    }

    // Contact form (mailto flow, unchanged from the original site)
    var form = document.getElementById('contact-form');
    if (form) {
      // Prefill from ?topic=...&product=...
      var params = new URLSearchParams(window.location.search);
      var topic = params.get('topic');
      var product = params.get('product');
      var typeEl = document.getElementById('inquiry_type');
      var msgEl = document.getElementById('message');
      if (topic && typeEl) {
        Array.prototype.forEach.call(typeEl.options, function (o) {
          if (o.value === topic) typeEl.value = topic;
        });
      }
      if (product && msgEl && !msgEl.value) {
        msgEl.value = '想了解的產品／方案：' + product.slice(0, 80) + '\n';
      }

      form.addEventListener('submit', function (e) {
        e.preventDefault();
        if (document.getElementById('hp_name').value) { return; } // honeypot

        function clean(str) {
          var t = document.createElement('div');
          t.textContent = str;
          return t.innerHTML.replace(/[<>'"&]/g, '');
        }
        var company = clean(document.getElementById('company').value);
        var name = clean(document.getElementById('contact_name').value);
        var type = clean(document.getElementById('inquiry_type').value);
        var email = clean(document.getElementById('email').value);
        var msg = clean(document.getElementById('message').value);

        var statusBox = document.getElementById('form-status');
        statusBox.classList.remove('hidden');

        var subject = encodeURIComponent('[Aperture Science 官網諮詢] - ' + type + ' - ' + company);
        var body = encodeURIComponent(
          '公司名稱: ' + company + '\n' +
          '聯絡人: ' + name + '\n' +
          '回覆信箱: ' + email + '\n' +
          '諮詢類型: ' + type + '\n' +
          '----------------------------------------\n' +
          '需求描述:\n' + msg + '\n\n' +
          '-- 此郵件由 www.aperturescience.com.tw 官方表單產出 --'
        );
        var link = 'mailto:' + targetEmail + '?subject=' + subject + '&body=' + body;
        setTimeout(function () {
          window.location.href = link;
          statusBox.textContent = '已嘗試開啟您的郵件軟體。若無反應，請手動寄信至 ' + targetEmail;
        }, 800);
      });
    }
  });
})();

/* Redirect old one-page hash links (e.g. /#products) to the new multi-page URLs. */
(function () {
  var map = {
    '#about': '/about/', '#products': '/products/', '#products-instruments': '/products/instruments/',
    '#products-ai': '/ai-inspection/', '#products-ir': '/products/', '#industries': '/industries/',
    '#contact': '/contact/', '#privacy': '/privacy/', '#terms': '/terms/'
  };
  if (window.location.pathname === '/' && map[window.location.hash]) {
    window.location.replace(map[window.location.hash]);
  }
})();
