"use strict";

/**
 *
 */

var App = (function () {

  var foo = document.getElementById('form__blog'),
      fileField = document.querySelector('[type="file"]');

  function _run() {
    var data,
        snackbar = document.getElementById('snackbar'),
        url = document.location.pathname.split('/');

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
            /**
             * Append blog id to form action
             */
            if ( /[0-9]{1,}/.test(foo.getAttribute('action')) == false ) {
              foo.setAttribute('action', foo.getAttribute('action') + resp.blog_id);
            }
            snackbar.MaterialSnackbar.showSnackbar({
              message: 'Blog Saved',
              actionHandler: function(event) {
                event.preventDefault();

                window.open('/post/'+ resp.blog_slug +'/', '_blank');
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
