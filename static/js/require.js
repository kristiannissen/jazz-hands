"use strict";

function require ( file, callback ) {
    var s, r = false, h = document.querySelector( 'head' ),
        d = new Date(), name = file.split('.').shift();

    if ( document.getElementById('asset-'+ name) == null) {
      s = document.createElement( 'script' );
      s.src = '/static/js/'+ file;
      s.setAttribute('id', 'asset-'+ name);
      s.setAttribute('data-added', d.getTime() );
      s.onload = s.onreadystatechange = function() {
          // console.log( this.readyState ); //uncomment this line to see which ready states are called.
          if ( !r && (!this.readyState || this.readyState == 'complete') ) {
              r = true;
              if ( typeof callback == 'function') {
                callback();
              } else {
                App.run();
              }
          }
      };
      h.appendChild( s );
    } else if ( document.getElementById('asset-'+ name) !== null && typeof callback == 'function' ) {
      callback();
    }
}
