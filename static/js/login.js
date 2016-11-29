"use strict";

/**
 * 
 */

var App = (function() {
    var foo = document.getElementById('form__login'),
        fields = ['user_mail', 'user_pwd'];

    function _run() {
        foo.querySelector('[type="submit"]').addEventListener('click', function (e) {
            e.preventDefault();

            var inValidFields = _validateFields(); // TODO: Rename function
            if (inValidFields.length > 0) {
                for (var f in inValidFields) {
                    var field = inValidFields[f],
                        css = field.getAttribute('class'),
                        snackbar = document.querySelector('#snackbar'),
                        label = document.querySelector('[for="'+ field.getAttribute('id') +'"]');

                    snackbar.MaterialSnackbar.showSnackbar({
                        'message': 'The field '+ label.innerText +' is required!'
                    });
                    break;
                }
            } else {
                //FIXME: Should be more dynamic
                if (foo.onsubmit) {
                    foo.onsubmit();
                } else if (foo.submit) {
                    foo.submit();
                }
            }
        });
    }

    function _validateFields() {
        var valid = [];
        for (var f in fields) {
            var field = foo.querySelector('[name="'+ fields[f] +'"]')
            if (field.hasAttribute('required')) {
                if (field.hasAttribute('required') && field.value == '') {
                    valid.push(field);
                }
            }
        }
        return valid;
    }

    return {
        run: _run
    }
})();
