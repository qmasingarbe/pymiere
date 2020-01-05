//@include 'json2.jsx';

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
if($.hasOwnProperty('_pymiere') == false){
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

// debug function to interact with javascript in panel
$._jsxFunctions = {
	debug_print : function(data) {
		alert(data);
	},
	
	returnSomething : function(){
		return "String from jsx"
	}
};

// replacer function to pass to json.stringify preventing infinite loop for $ objects
function internal_variables_replacer(key, value){if(key !== "tmp" && key !== "_pymiere"){return value}}