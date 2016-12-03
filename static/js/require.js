"use strict";

function require ( file, callback ) {
    var s, r = false, h = document.querySelector( 'head' ),
        d = new Date();

        if ( document.querySelector('script[src="/static/js/'+ file +'"]') == null) {
          s = document.createElement( 'script' );
          s.src = '/static/js/'+ file;
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
    }
}
