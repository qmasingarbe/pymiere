// enable QE, second undocumented hidden API used by Adobe Quality Engineering team to do automated test, contains some juicy stuff
app.enableQE();
qe.setDebugDatabaseEntry("dvascripting.EnabledInternalDOM", "true");

// polyfill 'indexOf' method on ExtendScript arrays
if(!Array.prototype.indexOf){
	Array.prototype.indexOf = function(item){
		var i = this.length;
		while (i--){
			if (this[i] === item) return i;
		}
		return -1;
	}
}

// init variable used by pymiere
if($.hasOwnProperty('_pymiere') === false){
	$._pymiere = {generatedIds:[]}
}

// register function to generate new object id for pymiere
$._pymiere.generateId = function(){
	var result = '';
	var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
	for (var i = 0; i < 10; i++ ) {
		result += characters.charAt(Math.floor(Math.random() * characters.length));
	}
	if($._pymiere.generatedIds.indexOf(result) >= 0) {
		result = $._pymiere.generateId();
	}
	$._pymiere.generatedIds.push(result);
	return result;
}

// replacer function to pass to ExtendJSON.stringify preventing infinite loop for $ objects
function internal_variables_replacer(key, value){if(key !== "tmp" && key !== "_pymiere"){return value}}


// load ExtendJson custom json converter for extendscript (not in a separate file because sometimes it doesn't load...)
/*
    json2.js
    2014-02-04

    Public Domain.

    Modified to add depth param on stringify + use the reflect interface in extend script
	to list properties on objects
*/


// Create a ExtendJSON object only if one does not already exist. We create the
// methods in a closure to avoid creating global variables.

if (typeof ExtendJSON !== 'object') {
    ExtendJSON = {};
}

(function () {
    'use strict';

    function f(n) {
        // Format integers to have at least two digits.
        return n < 10 ? '0' + n : n;
    }

    if (typeof Date.prototype.toJSON !== 'function') {

        Date.prototype.toJSON = function () {

            return isFinite(this.valueOf())
                ? this.getUTCFullYear()     + '-' +
                    f(this.getUTCMonth() + 1) + '-' +
                    f(this.getUTCDate())      + 'T' +
                    f(this.getUTCHours())     + ':' +
                    f(this.getUTCMinutes())   + ':' +
                    f(this.getUTCSeconds())   + 'Z'
                : null;
        };

        String.prototype.toJSON      =
            Number.prototype.toJSON  =
            Boolean.prototype.toJSON = function () {
                return this.valueOf();
            };
    }

    var cx,
        escapable,
        gap,
        indent,
        meta,
		maxdepth,
        rep;


    function quote(string) {

// If the string contains no control characters, no quote characters, and no
// backslash characters, then we can safely slap some quotes around it.
// Otherwise we must also replace the offending characters with safe escape
// sequences.

        escapable.lastIndex = 0;
        return escapable.test(string) ? '"' + string.replace(escapable, function (a) {
            var c = meta[a];
            return typeof c === 'string'
                ? c
                : '\\u' + ('0000' + a.charCodeAt(0).toString(16)).slice(-4);
        }) + '"' : '"' + string + '"';
    }


    function str(key, holder, dstatus) {

// Produce a string from holder[key].

        var i,          // The loop counter.
            k,          // The member key.
            v,          // The member value.
            length,
            mind = gap,
            partial,
            value = holder[key],
			nextdepth,
			currentdepth;

		currentdepth = dstatus;
		nextdepth = (dstatus === -1) ? -1 : 1;



// If the value has a toJSON method, call it to obtain a replacement value.

        if (value && typeof value === 'object' &&
                typeof value.toJSON === 'function') {
            value = value.toJSON(key);
        }

// If we were called with a replacer function, then call the replacer to
// obtain a replacement value.

        if (typeof rep === 'function') {
            value = rep.call(holder, key, value);
        }

// What happens next depends on the value's type.
        switch (typeof value) {
		case 'string':
            return quote(value);

        case 'number':
// ExtendJSON numbers must be finite. Encode non-finite numbers as null.
            return isFinite(value) ? String(value) : 'null';

        case 'boolean':
        case 'null':

// If the value is a boolean or null, convert it to a string. Note:
// typeof null does not produce 'null'. The case is included here in
// the remote chance that this gets fixed someday.

            return String(value);

// If the type is 'object', we might be dealing with an object or an array or
// null.

        case 'object':

// Due to a specification blunder in ECMAScript, typeof null is 'object',
// so watch out for that case.

            if (!value) {
                return 'null';
            }

// Make an array to hold the partial results of stringifying this object value.

            gap += indent;
            partial = [];

// Is the value an array?

            if (Object.prototype.toString.apply(value) === '[object Array]') {

// The value is an array. Stringify every element. Use null as a placeholder
// for non-ExtendJSON values.

                v = '{"length" : ' + str("length", value) + '}';
                return v;
            }

// If the replacer is an array, use it to select the members to be stringified.

            if (rep && typeof rep === 'object') {
                length = rep.length;
                for (i = 0; i < length; i += 1) {
                    if (typeof rep[i] === 'string') {
                        k = rep[i];
						if(dstatus === 1){
							v = quote(value[k].constructor.name);
						}else{
							v = str(k, value, (dstatus === -1) ? -1 : 1);
						}
                        if (v) {
                            partial.push(quote(k) + (gap ? ': ' : ':') + v);
                        }
                    }
                }
            } else {

// Otherwise, iterate through all of the keys in the object.
				// modify to use rflect to list properties
				var all_keys = [];
				for (k in value){all_keys.push(k)}; // classic method
				if (typeof value.reflect !== 'undefined') { // add reflect method
					for (p in value.reflect.properties){
						if(isFinite(p) === false){continue}
						if(value.reflect.properties[p] == "anonymous" || value.reflect.properties[p] == "__proto__"){continue}
						if(all_keys.indexOf(value.reflect.properties[p]) == -1){
							all_keys.push(value.reflect.properties[p]);
						}
					}
				}
				for (i=0; i<all_keys.length; i++) {
                    k = all_keys[i];
                    if (Object.prototype.hasOwnProperty.call(value, k)) {
                        if(dstatus === 1){
							v = (typeof value === "undefined" || typeof value[k] === "undefined") ? 'null' : quote(value[k].constructor.name);
						}else{
							v = str(k, value, (dstatus === -1) ? -1 : 1);
						}
                        if (v) {
                            partial.push(quote(k) + (gap ? ': ' : ':') + v);
                        }
                    }
                }
            }

// Join all of the member texts together, separated with commas,
// and wrap them in braces.

            v = partial.length === 0
                ? '{}'
                : gap
                ? '{\n' + gap + partial.join(',\n' + gap) + '\n' + mind + '}'
                : '{' + partial.join(',') + '}';
            gap = mind;
            return v;
        }
    }

// If the ExtendJSON object does not yet have a stringify method, give it one.

    if (typeof ExtendJSON.stringify !== 'function') {
        escapable = /[\\\"\x00-\x1f\x7f-\x9f\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g;
        meta = {    // table of character substitutions
            '\b': '\\b',
            '\t': '\\t',
            '\n': '\\n',
            '\f': '\\f',
            '\r': '\\r',
            '"' : '\\"',
            '\\': '\\\\'
        };
        ExtendJSON.stringify = function (value, replacer, space, depth) {

// The stringify method takes a value and an optional replacer, and an optional
// space parameter, and returns a ExtendJSON text. The replacer can be a function
// that can replace values, or an array of strings that will select the keys.
// A default replacer method can be provided. Use of the space parameter can
// produce text that is more easily readable.
// if depth is set at any value, ExtendJSON will only stringify two level of depth in objects
            var i;
            gap = '';
            indent = '';

			depth = (typeof depth === 'undefined') ? -1 : 0;

// If the space parameter is a number, make an indent string containing that
// many spaces.

            if (typeof space === 'number') {
                for (i = 0; i < space; i += 1) {
                    indent += ' ';
                }

// If the space parameter is a string, it will be used as the indent string.

            } else if (typeof space === 'string') {
                indent = space;
            }

// If there is a replacer, it must be a function or an array.
// Otherwise, throw an error.

            rep = replacer;
            if (replacer && typeof replacer !== 'function' &&
                    (typeof replacer !== 'object' ||
                    typeof replacer.length !== 'number')) {
                throw new Error('ExtendJSON.stringify');
            }

// Make a fake root object containing our value under the key of ''.
// Return the result of stringifying the value.

            return str('', {'': value}, depth);
        };
    }


// If the ExtendJSON object does not yet have a parse method, give it one.

    if (typeof ExtendJSON.parse !== 'function') {
        cx = /[\u0000\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g;
        ExtendJSON.parse = function (text, reviver) {

// The parse method takes a text and an optional reviver function, and returns
// a JavaScript value if the text is a valid ExtendJSON text.

            var j;

            function walk(holder, key) {

// The walk method is used to recursively walk the resulting structure so
// that modifications can be made.

                var k, v, value = holder[key];
                if (value && typeof value === 'object') {
                    for (k in value) {
                        if (Object.prototype.hasOwnProperty.call(value, k)) {
                            v = walk(value, k);
                            if (v !== undefined) {
                                value[k] = v;
                            } else {
                                delete value[k];
                            }
                        }
                    }
                }
                return reviver.call(holder, key, value);
            }


// Parsing happens in four stages. In the first stage, we replace certain
// Unicode characters with escape sequences. JavaScript handles many characters
// incorrectly, either silently deleting them, or treating them as line endings.

            text = String(text);
            cx.lastIndex = 0;
            if (cx.test(text)) {
                text = text.replace(cx, function (a) {
                    return '\\u' +
                        ('0000' + a.charCodeAt(0).toString(16)).slice(-4);
                });
            }

// In the second stage, we run the text against regular expressions that look
// for non-ExtendJSON patterns. We are especially concerned with '()' and 'new'
// because they can cause invocation, and '=' because it can cause mutation.
// But just to be safe, we want to reject all unexpected forms.

// We split the second stage into 4 regexp operations in order to work around
// crippling inefficiencies in IE's and Safari's regexp engines. First we
// replace the ExtendJSON backslash pairs with '@' (a non-ExtendJSON character). Second, we
// replace all simple value tokens with ']' characters. Third, we delete all
// open brackets that follow a colon or comma or that begin the text. Finally,
// we look to see that the remaining characters are only whitespace or ']' or
// ',' or ':' or '{' or '}'. If that is so, then the text is safe for eval.

            if (/^[\],:{}\s]*$/
                    .test(text.replace(/\\(?:["\\\/bfnrt]|u[0-9a-fA-F]{4})/g, '@')
                        .replace(/"[^"\\\n\r]*"|true|false|null|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?/g, ']')
                        .replace(/(?:^|:|,)(?:\s*\[)+/g, ''))) {

// In the third stage we use the eval function to compile the text into a
// JavaScript structure. The '{' operator is subject to a syntactic ambiguity
// in JavaScript: it can begin a block or an object literal. We wrap the text
// in parens to eliminate the ambiguity.

                j = eval('(' + text + ')');

// In the optional fourth stage, we recursively walk the new structure, passing
// each name/value pair to a reviver function for possible transformation.

                return typeof reviver === 'function'
                    ? walk({'': j}, '')
                    : j;
            }

// If the text is not ExtendJSON parseable, then a SyntaxError is thrown.

            throw new SyntaxError('ExtendJSON.parse');
        };
    }
}());
