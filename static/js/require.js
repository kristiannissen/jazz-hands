"use strict";

function require ( file ) {
    var s, r = false, h = document.querySelector( 'head' );
        s = document.createElement( 'script' );
        s.src = '/static/js/'+ file;
        s.onload = s.onreadystatechange = function() {
            // console.log( this.readyState ); //uncomment this line to see which ready states are called.
            if ( !r && (!this.readyState || this.readyState == 'complete') ) {
                r = true;
                App.run();
            }
        };
    h.appendChild( s );
}