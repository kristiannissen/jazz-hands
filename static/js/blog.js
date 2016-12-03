"use strict";

/**
 *
 */

var App = (function () {

  var foo = document.getElementById('form__blog');

  function _run() {
    var data,
        snackbar = document.getElementById('snackbar'),
        url = document.location.pathname.split('/');

    if ( typeof parseInt(url.pop()) !== 'NaN' ) {
      foo.setAttribute('action', document.location.pathname);
      require( 'http.js', function () {
        http.get( document.location.pathname, {
          'Content_Type': 'application/json'
        }).then( function ( resp ) {
          console.log( resp );  
        });
      });
    }

    foo.addEventListener('submit', function(e) {
      e.preventDefault();

      /**
       * Serialize form data
       * Post data to endpoint
       * Show snackbox when all is good
       */
      require( 'http.js', function () {
        data = http.serialize( foo );

        http.post( foo.getAttribute( 'action' ), data)
          .then( function ( resp ) {

            snackbar.MaterialSnackbar.showSnackbar({
              message: 'Blog Post Created',
              actionHandler: function(event) {
                event.preventDefault();

                window.open('/'+ resp.blog_slug, '_blank');
              },
              actionText: 'Preview'
            }); 
          });
      });
    });
  }

  return {
    run: _run
  }
})();
