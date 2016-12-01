"use strict";

/**
 * Promise HTTP lib
 */

var http = (function () {
  var core = {
    ajax: function (method, url, args, headers) {
      return new Promise (function (resolve, reject) {
        var client = new XMLHttpRequest(),
            uri = url;
        if ( args && (method === 'POST') ) {
          uri += '?';
          var argCount = 0;
          for ( var key in args ) {
            if ( args.hasOwnProperty(key) ) {
              if ( argCount++ ) {
                uri += '&';
              }
              uri += encodeURIComponent(key) + '=' + encodeURIComponent(args[key]);
            }
          }
        }
        client.open( method, uri );
        if ( headers !== undefined ) {
          for ( var key in headers ) {
            if ( headers.hasOwnProperty(key) ) {
              client.setRequestHeader( key, headers[key] );
            }
          }
        }
        client.send();
        client.onload = function () {
          if ( this.status >= 200 && this.status < 300 ) {
            resolve ( this.response );
          } else {
            reject ( {'status': this.status, 'text': this.statusText} );
          }
        };
        client.onerror = function () {
          reject ( this.statusText );
        }
      });
    }
  };

  return {
    'get': function ( url, args, headers ) {
      return core.ajax('GET', url, args, headers);
    },
    'post': function ( url, args, headers ) {
      return core.ajax('POST', url, args, headers);
    }
  };
})();
