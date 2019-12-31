function reflectToFuncs(reflectForFuncs){
    var funcs_results = {};
    for(var i=0; i<reflectForFuncs.methods.length; i++){
        var func_result = {};
        var func_info = reflectForFuncs.methods[i];
        var func_name = func_info.name;
        if(eval(func_name + ".prototype.reflect.name") == func_name){continue;} // bypass contructor classes
        func_result.dataType = func_info.dataType;
        func_result.description = func_info.description;
        func_result.help = func_info.help;
        func_result.isCollection = func_info.isCollection;
        // function args
        func_result.arguments = {}
        if(typeof func_info.arguments != "undefined"){
            for(var j=0; j<func_info.arguments.length; j++){
                var arg_result = {};
                var arg_info = func_info.arguments[j];
                var arg_name = arg_info.name;
                arg_result.dataType = arg_info.dataType;
                arg_result.defaultValue = arg_info.defaultValue;
                arg_result.description = arg_info.description;
                arg_result.help = arg_info.help;
                func_result.arguments[arg_name] = arg_result;
            }
        }
        funcs_results[func_name] = func_result;
    }
    return funcs_results
}

function rootReflectToDict(){
    //$.writeln(reflect.name);
    //$.writeln(" ");
    var result = {};
    var objReflect = reflect;
    // simple infos
    result.name = objReflect.name;
    result.type = "root";
    result.description = objReflect.description;
    result.help = objReflect.help;

    // properties
    result.props = {};
    for(var i in objReflect.properties){
        var property_result = {};
        var property_info = objReflect.properties[i];
        var property_name = property_info.name;
        if(property_name == "__proto__" || property_name == "anonymous" || property_name == "reflect"){continue;}
        property_result.dataType = property_info.dataType;
        property_result.defaultValue = property_info.defaultValue;
        property_result.description = property_info.description;
        property_result.help = property_info.help;
        property_result.isCollection = property_info.isCollection;
        property_result.max = property_info.max;
        property_result.min = property_info.min;
        property_result.type = property_info.type;
        result.props[property_name] = property_result;
    }

    // functions
    result.funcs = reflectToFuncs(objReflect);

    return result
}

JSON.stringify(rootReflectToDict());