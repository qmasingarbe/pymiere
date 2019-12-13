function reflectToFuncs(reflectForFuncs){
    var funcs_results = {};
    for(var i=0; i<reflectForFuncs.methods.length; i++){
        var func_result = {};
        var func_info = reflectForFuncs.methods[i];
        var func_name = func_info.name;
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

function reflectToDict(obj, exclude_property){
    //$.writeln(obj.reflect.name);
    //$.writeln(" ");
    var exclude_property = exclude_property || " "
    var result = {};
    var objReflect = obj.reflect;
    // simple infos
    result.name = objReflect.name;
    result.type = typeof obj;
    result.description = objReflect.description;
    result.help = objReflect.help;
    
    // properties
    result.props = {};
    for(var i in objReflect.properties){
        var property_result = {};
        var property_info = objReflect.properties[i];
        var property_name = property_info.name;
        if(property_name == "__proto__" || property_name == "anonymous" || property_name == exclude_property || property_name == "reflect"){continue;}
        property_result.dataType = property_info.dataType;
        property_result.defaultValue = property_info.defaultValue;
        property_result.description = property_info.description;
        property_result.help = property_info.help;
        property_result.isCollection = property_info.isCollection;
        property_result.max = property_info.max;
        property_result.min = property_info.min;
        property_result.type = property_info.type;
        if (property_result.dataType == "boolean" || property_result.dataType == "number" || property_result.dataType == "string" || property_result.dataType == "any" || property_result.dataType == "undefined"){
            // property contains data of builtin type
            property_result.value = obj[property_name];
        }else if(typeof obj[property_name] === "undefined"){
            // property has undefinied value
            property_result.value = undefined;
        }else if(property_result.dataType == "MarkerCollection"){
            // property is a marker collection => not the same as other collections, cannot access markers through array
            property_result.value = reflectToDict(obj[property_name]);
        }else if(property_result.dataType.indexOf('ollection') !== -1 || property_result.isCollection == true){
            // property hold a collection of Objects
            // find name of proprety holding number of item in collection
            var collectionLength = undefined;
            for(var j in obj[property_name]){if(j.indexOf('num') == 0){collectionLength = j;}}
            // collect representation of the objects inside the collection
            var collectionContent = [];
            for(var j=0; j<obj[property_name][collectionLength]; j++){
                collectionContent.push(reflectToDict(obj[property_name][j]));
            }
            property_result.value = reflectToDict(obj[property_name]);
            property_result.value.collectionContent = collectionContent;
        }else{
            // property contains an Object
            //$.writeln(property_name);
            property_result.value = reflectToDict(obj[property_name]);
        }
        result.props[property_name] =property_result;
    }

    // functions
    result.funcs = reflectToFuncs(objReflect);
    
    return result
}

//delete $.global.test;
//JSON.stringify(reflectToDict($.global, "$"));
JSON.stringify(reflectToDict(qe.project.getActiveSequence().getVideoTrackAt(0).getItemAt(0), "babababa"));
//JSON.stringify(reflectToDict(app.project.activeSequence.markers.getFirstMarker()));