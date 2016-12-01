"use strict";

/**
 *
 */

var App = (function () {

  var foo = document.getElementById('form__blog');

  function _run() {
    var url = document.location.pathname.split('/');
    if ( typeof parseInt(url.pop()) !== 'NaN' ) {
      foo.setAttribute('action', document.location.pathname);
    }

    foo.addEventListener('submit', function(e) {
      e.preventDefault();

      require('http.js', function() {
        http.post(foo.getAttribute('action'), {
            'blog_title': 'Hello Kitty',
            'blog_content': 'Eat some Pussy'
          }, {'Content_Type': 'application/json'})
        .then(function ( resp ) {
          console.log( resp );
        });
      });
    });

    console.log('Hello');
  }

  return {
    run: _run
  }
})();
