import os
from pymiere.utils import MyStr, TYPE_CORRESPONDENCE, read_json_file

from pymiere import utils
import pymiere
import keyword

# todo try using https://github.com/Adobe-CEP/Samples/tree/master/PProPanel/jsx PremierePro.d.ts for docstrings


def generate_class(object_data, all_classes_names):
    is_collection = False
    # checks
    if list(object_data.keys()) != ["name", "type", "description", "help", "props", "funcs"]:
        is_collection = True
        if list(object_data.keys()) != ["name", "type", "description", "help", "props", "funcs", "collectionContent"]:
            raise ValueError("Wrong keys found : {}".format(object_data.keys()))

    if is_collection:
        return generate_collection_class(object_data)

    # ----- INIT CLASS ------
    code = utils.MyStr()
    # definition
    code = code.add_line("class {}(object):".format(object_data.get("name")))
    # docstring
    if object_data.get("help") or object_data.get("description"):
        raise NotImplementedError()
    # init
    properties = ["{}=None".format(p) for p in object_data.get("props").keys()]
    if object_data.get("name") == "$":  # absorb extra things in $ object
        code = code.add_line("def __init__(self, {}, **kwargs):".format(", ".join(properties)), indent=1)
    else:
        code = code.add_line("def __init__(self, {}):".format(", ".join(properties)), indent=1)
    properties_dict = ["'{0}':{0}".format(p) for p in object_data.get("props").keys()]
    code = code.add_line("PymiereBaseObject._check_init_args({"+ ", ".join(properties_dict) +"})", indent=2)
    code = code.add_line("super({}, self).__init__()".format(object_data.get("name")), indent=2)
    for prop_name in object_data.get("props").keys():
        code = code.add_line("self.__{0} = {0}".format(prop_name), indent=2)

    # ----- CLASS PROPERTIES -----
    code = code.add_empty_line()
    code = code.add_line("# ----- PROPERTIES -----", indent=1)
    for prop_name, prop_info in object_data.get("props").items():
        # docstring$
        if prop_info.get("help"):
            raise NotImplementedError("help")
        # getter
        code = code.add_line("@property", indent=1)
        code = code.add_line("def {}(self):".format(prop_name), indent=1)
        if prop_info.get("description"):
            code = code.add_line('"""{}"""'.format(prop_info.get("description")), indent=2)
        if prop_info.get("dataType") in utils.TYPE_CORRESPONDENCE:
            code = code.add_line("self.__{0} = _eval_on_global_object('{0}')".format(prop_name), indent=2)
        elif prop_info.get("dataType") not in all_classes_names:
            print("Return type '{}' for property getter '{}.{}' seems unknown, using automatic ES class to py object".format(prop_info.get("dataType"), object_data.get("name"), prop_name))
            code = code.add_line("self.__{0} = _format_object_to_py(_eval_script_returning_object('{0}'))".format(prop_name), indent=2)
        else:
            code = code.add_line("self.__{0} = {1}(**_eval_script_returning_object('{0}', as_kwargs=True))".format(prop_name, prop_info.get("dataType")), indent=2)
        code = code.add_line("return self.__{}".format(prop_name), indent=2)
        # setter
        code = code.add_line("@{}.setter".format(prop_name), indent=1)
        code = code.add_line("def {0}(self, {0}):".format(prop_name), indent=1)
        if prop_info.get("type") == "readwrite":
            check_cls = utils.TYPE_CORRESPONDENCE[prop_info.get("dataType")] if prop_info.get("dataType") in utils.TYPE_CORRESPONDENCE else prop_info.get("dataType")
            if check_cls in all_classes_names or check_cls in utils.TYPE_CORRESPONDENCE.values():
                code = code.add_line("PymiereBaseObject._check_type({0}, {1}, '{2}.{0}')".format(prop_name, check_cls, object_data.get("name")), indent=2)
            else:
                print("value type '{}' for property setter of '{}.{}' seems unknown, no check for type will be performed".format(check_cls, object_data.get("name"), prop_name))
            line = """_eval_on_global_object("{0} = {{}}".format(_format_object_to_es({0})))"""
            code = code.add_line(line.format(prop_name), indent=2)
            code = code.add_line("self.__{0} = {0}".format(prop_name), indent=2)
        elif prop_info.get("type") == "readonly":
            code = code.add_line("""raise AttributeError("Attribute '{}' is read-only")""".format(prop_name), indent=2)
        else:
            raise ValueError("Not supported type for attribute '{}'".format(prop_info.get("type")))
        code = code.add_empty_line()

    # ----- FUNCTIONS -----
    code = code.add_empty_line()
    code = code.add_line("# ----- FUNCTIONS -----", indent=1)
    for func_name, func_info in object_data.get("funcs").items():
        # docstring
        if func_info.get("help"):
            raise NotImplementedError("help")
        # definition
        args = ""
        if func_info.get("arguments"):
            args = ", ".join([""] + list(func_info.get("arguments").keys()))
        code = code.add_line("def {}(self{}):".format(func_name, args), indent=1)

        # docstring
        if func_info.get("arguments") or func_info.get("description"):
            # pycharm compatible docstring for arg types
            code = code.add_line('"""', indent=2)
            if func_info.get("description"):
                code = code.add_line(func_info.get("description"), indent=2)
            for arg_name, arg_info in func_info.get("arguments", dict()).items():
                if arg_info.get("help"):
                    raise NotImplementedError("help")
                if arg_info.get("description"):
                    code = code.add_line(":param {}: {}".format(arg_name, arg_info.get("description")), indent=2)
                pytype = utils.TYPE_CORRESPONDENCE[arg_info.get("dataType")] if arg_info.get("dataType") in utils.TYPE_CORRESPONDENCE else arg_info.get("dataType")
                code = code.add_line(":type {}: {}".format(arg_name, pytype), indent=2)
            code = code.add_line('"""', indent=2)
        if func_info.get("arguments"):
            # check type of function args in python
            for arg_name, arg_info in func_info.get("arguments").items():
                if arg_info.get("dataType") in utils.TYPE_CORRESPONDENCE:
                    check_cls = utils.TYPE_CORRESPONDENCE[arg_info.get("dataType")] if arg_info.get("dataType") in utils.TYPE_CORRESPONDENCE else arg_info.get("dataType")
                elif arg_info.get("dataType") not in all_classes_names:
                    print("arg type '{}' for function '{}.{}({})' seems unknown, no check for type will be performed".format(arg_info.get("dataType"), object_data.get("name"), func_name, arg_name))
                    continue
                else:
                    # raise NotImplementedError("arg type {} not supported for function {} of {}".format(arg_info.get("dataType"), func_name, object_data.get('name')))
                    check_cls = arg_info.get("dataType")
                code = code.add_line("""PymiereBaseObject._check_type({0}, {1}, 'arg "{0}" of function "{2}.{3}"')""".format(arg_name, check_cls, object_data.get("name"), func_name), indent=2)
        # body
        line = ""
        if func_info.get("dataType") != "undefined":
            line = "return "
            if func_info.get("dataType") not in utils.TYPE_CORRESPONDENCE:
                if func_info.get("dataType") not in all_classes_names:
                    print("Return type '{}' for function '{}.{}' seems unknown, using automatic ES class to py object".format(func_info.get("dataType"), object_data.get("name"), func_name))
                    line += "_format_object_to_py("
                else:
                    line += str(func_info.get("dataType")) + "(**"
        line += '_eval_on_global_object("{}('.format(func_name)
        if func_info.get("arguments"):
            line_args = list()
            format_args = list()
            for arg_name, arg_info in func_info.get("arguments").items():
                line_args.append("{}")
                format_args.append("_format_object_to_es({})".format(arg_name))
            line += ", ".join(line_args)
            line += ')".format({}))'.format(", ".join(format_args))
        else:
            line += ')")'
        if func_info.get("dataType") != "undefined" and func_info.get("dataType") not in utils.TYPE_CORRESPONDENCE:
            line += ")"
        code = code.add_line(line, indent=2)
        code = code.add_empty_line()
    return code


def generate_collection_class(object_data):
    """
    Same as generate_class but specifically for objects being collections
    :param object_data: (dict) object infos
    :return: (str) python code
    """
    code = utils.MyStr()
    class_name = object_data.get("name")
    # find the num property holding the length of the collection. The length property does not have the real length...
    length_property = [prop_name for prop_name in object_data.get("props").keys() if "num" in prop_name]
    if not length_property:
        raise ValueError("Couldn't find any length/number property on {}".format(object_data.get("name")))
    if len(length_property) != 1:
        raise ValueError("Found mutliple properties that could be the length of {} : {}".format(object_data.get("name"), length_property))
    length_property = length_property[0]
    # find class name of item in the collection
    if object_data.get("collectionContent"):
        item_class_name = object_data.get("collectionContent")[0]["name"]
    else:
        item_class_name = class_name.replace("Collection", "")
    # write class declaration
    code = code.add_line("class {}(PymiereBaseCollection):".format(class_name))
    code = code.add_line("def __init__(self, pymiere_id, length, {}):".format(length_property), indent=1)
    code = code.add_line('super({}, self).__init__(pymiere_id, "{}")'.format(class_name, length_property), indent=2)
    code = code.add_empty_line()
    code = code.add_line("def __getitem__(self, index):", indent=1)
    code = code.add_line("return {}(**super({}, self).__getitem__(index))".format(item_class_name, class_name), indent=2)
    code = code.add_empty_line()
    return code


if __name__ == "__main__":
    """
    Generate the global vars we can access in ES as a class
    """
    data = read_json_file(os.path.join(__file__, "..", "class_datas", "start_vars.json"))
    data["name"] = "StartVars"
    result_code = "from pymiere.core import _format_object_to_py, _format_object_to_es, _eval_script_returning_object\nfrom pymiere.autogenerated.premiere_objects import *\n\n\n"
    result_code += """def _eval_on_global_object(extend_property):
    result = _eval_script_returning_object(extend_property)
    if result == "undefined":
        return None
    # if it's an object search if class exists and return objects creation arguments
    if isinstance(result, dict) and "isObject" in result and result["isObject"] is True:
        # create key word argument list to create the object
        kwargs = result["objectValues"]
        kwargs.update(pymiere_id=result["pymiereId"])
        return kwargs
    return result\n\n"""
    import inspect
    from pymiere.autogenerated import premiere_objects
    result_code += generate_class(data, ["Array"] + [name for name, obj in inspect.getmembers(premiere_objects) if inspect.isclass(obj)])
    result_code = result_code.replace("$", "Dollar")
    with open(os.path.join(__file__, "..", "..", "autogenerated", "start_vars.py"), "w") as f:
        f.write(result_code)
