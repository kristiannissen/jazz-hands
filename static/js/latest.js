"use strict";

/**
 * Load list of latest content
 */
var App = (function() {

  function _run() {
    require('http.js');

    var i, t = null, posts = document.querySelectorAll('[data-blog-id]');
    for ( i = 0; i < posts.length; i++ ) {
      var p = posts[i];
      p.addEventListener('change', function (e) {
        t = e.target;

        console.log( t );
      });
    }
  }
  /**
   * Public methods
   */
  return {
      run: _run
  }
})();
