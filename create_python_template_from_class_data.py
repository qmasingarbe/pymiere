from pymiere import utils

TYPE_CORRESPONDENCE = {"string": "str", "boolean": "bool", "number": "float", "any": "any", "undefined": "None"}

class MyStr(str):
    """Subclass of string to add code line quicker"""
    def add_line(self, content, indent=0):
        return MyStr(self + "\n" + indent*4*" " + content)
    def add_empty_line(self):
        return MyStr(self + "\n")

# todo : merge property and function code
# todo try using https://github.com/Adobe-CEP/Samples/tree/master/PProPanel/jsx PremierePro.d.ts for docstrings

def generate_class(object_data):
    is_collection = False
    # checks
    if list(object_data.keys()) != ["name", "type", "description", "help", "props", "funcs"]:
        is_collection = True
        if list(object_data.keys()) != ["name", "type", "description", "help", "props", "funcs", "collectionContent"]:
            raise ValueError("Wrong keys found : {}".format(object_data.keys()))
    if object_data["type"] != "object":
        raise ValueError("Wrong type")

    if is_collection:
        return generate_collection_class(object_data)

    # ----- INIT CLASS ------
    code = MyStr()
    # definition
    code = code.add_line("class {}(PymiereObject):".format(object_data.get("name")))
    # docstring
    if object_data.get("help") or object_data.get("description"):
        raise NotImplementedError()
    # init
    properties = ["{}=None".format(p) for p in object_data.get("props").keys()]
    code = code.add_line("def __init__(self, pymiere_id=None, {}):".format(", ".join(properties)), indent=1)
    properties_dict = ["'{0}':{0}".format(p) for p in object_data.get("props").keys()]
    code = code.add_line("self.check_init_args({'pymiere_id':pymiere_id, "+ ", ".join(properties_dict) +"})", indent=2)
    code = code.add_line("super({}, self).__init__(pymiere_id)".format(object_data.get("name")), indent=2)
    for prop_name in object_data.get("props").keys():
        code = code.add_line("self.__{0} = {0}".format(prop_name), indent=2)

    # ----- CLASS PROPERTIES -----
    code = code.add_empty_line()
    code = code.add_line("# ----- PROPERTIES -----", indent=1)
    for prop_name, prop_info in object_data.get("props").items():
        # docstring
        if prop_info.get("help") or prop_info.get("description"):
            raise NotImplementedError()
        # getter
        code = code.add_line("@property", indent=1)
        code = code.add_line("def {}(self):".format(prop_name), indent=1)
        if prop_info.get("dataType") in TYPE_CORRESPONDENCE:
            code = code.add_line("self.__{0} = self._extend_eval('{0}')".format(prop_name), indent=2)
        elif not prop_info.get("dataType")[0].isupper():
            code = code.add_line("# TODO : this is unsupported dataType {}".format(prop_info.get("dataType")), indent=2)
            # raise ValueError("Don't know how to handle dataType {}".format(prop_info.get("dataType")))
        else:
            code = code.add_line("self.__{0} = {1}(**self._extend_eval('{0}'))".format(prop_name, prop_info.get("dataType")), indent=2)
        code = code.add_line("return self.__{}".format(prop_name), indent=2)
        # setter
        code = code.add_line("@{}.setter".format(prop_name), indent=1)
        code = code.add_line("def {0}(self, {0}):".format(prop_name), indent=1)
        if prop_info.get("type") == "readwrite":
            check_cls = TYPE_CORRESPONDENCE[prop_info.get("dataType")] if prop_info.get("dataType") in TYPE_CORRESPONDENCE else prop_info.get("dataType")
            code = code.add_line("self.check_type({0}, {1}, '{2}.{0}')".format(prop_name, check_cls, object_data.get("name")), indent=2)
            if prop_info.get("dataType") == "string":  # property is string
                line = """self._extend_eval("{0} = '{{}}'".format({0}))"""
            elif prop_info.get("dataType") in TYPE_CORRESPONDENCE:  # property is builtin tyoe
                line = """self._extend_eval("{0} = {{}}".format({0}))"""
            else:  # property is object
                line = """self._extend_eval("{0} = $._pymiere['{{}}']".format({0}._pymiere_id))"""
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
        if func_info.get("help") or func_info.get("description"):
            raise NotImplementedError()
        # definition
        args = ""
        if func_info.get("arguments"):
            args = ", ".join([""] + list(func_info.get("arguments").keys()))
        code = code.add_line("def {}(self{}):".format(func_name, args), indent=1)

        # docstring
        if func_info.get("arguments"):
            # pycharm coâtible docstring for arg types
            code = code.add_line('"""', indent=2)
            for arg_name, arg_info in func_info.get("arguments").items():
                if arg_info.get("help") or arg_info.get("description"):
                    raise NotImplementedError()
                pytype = TYPE_CORRESPONDENCE[arg_info.get("dataType")] if arg_info.get("dataType") in TYPE_CORRESPONDENCE else arg_info.get("dataType")
                code = code.add_line(":type {}: {}".format(arg_name, pytype), indent=2)
            code = code.add_line('"""', indent=2)
            # check type of function args in python
            for arg_name, arg_info in func_info.get("arguments").items():
                # TODO : support objects as input in functions
                if arg_info.get("dataType") not in TYPE_CORRESPONDENCE:
                    # raise NotImplementedError("arg type {} not supported for function {} of {}".format(arg_info.get("dataType"), func_name, object_data.get('name')))
                    check_cls = arg_info.get("dataType")
                else:
                    check_cls = TYPE_CORRESPONDENCE[arg_info.get("dataType")] if arg_info.get("dataType") in TYPE_CORRESPONDENCE else arg_info.get("dataType")
                code = code.add_line("""self.check_type({0}, {1}, 'arg "{0}" of function "{2}.{3}"')""".format(arg_name, check_cls, object_data.get("name"), func_name), indent=2)
        # body
        line = ""
        if func_info.get("dataType") != "undefined":
            line = "return "
            if func_info.get("dataType") not in TYPE_CORRESPONDENCE:
                line += str(func_info.get("dataType")) + "(**"
        line += 'self._extend_eval("{}('.format(func_name)
        if func_info.get("arguments"):
            line_args = list()
            format_args = list()
            for arg_name, arg_info in func_info.get("arguments").items():
                if arg_info.get("dataType") == "string":
                    line_args.append("'{}'")
                    format_args.append(arg_name)
                elif arg_info.get("dataType") not in TYPE_CORRESPONDENCE:
                    line_args.append("$._pymiere['{}']")
                    format_args.append("{}._pymiere_id".format(arg_name))
                else:
                    line_args.append("{}")
                    format_args.append(arg_name)
            line += ", ".join(line_args)
            line += ')".format({}))'.format(", ".join(format_args))
        else:
            line += ')")'
        if func_info.get("dataType") != "undefined" and func_info.get("dataType") not in TYPE_CORRESPONDENCE:
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
    code = MyStr()
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
    code = code.add_line("class {}(PymiereCollection):".format(class_name))
    code = code.add_line("def __init__(self, pymiere_id, {}):".format(length_property), indent=1)
    code = code.add_line('super({}, self).__init__(pymiere_id, "{}")'.format(class_name, length_property), indent=2)
    code = code.add_empty_line()
    code = code.add_line("def __getitem__(self, index):", indent=1)
    code = code.add_line("return {}(**super({}, self).__getitem__(index))".format(item_class_name, class_name), indent=2)
    code = code.add_empty_line()
    return code

def build_python_from_data(datas, save_path):
    result_code = "from pymiere.core import PymiereObject, PymiereCollection\n"
    for data in datas:
        result_code += generate_class(data)
    with open(save_path, "w") as f:
        f.write(result_code)

def decrypt_object(d):
    objects = dict()
    if d is None:
        return objects
    if d.get("name") in ["Object", "object"]:
        # print("Simple object detected :", d.get("name"))
        return objects
    if d.get("type") in TYPE_CORRESPONDENCE:
        # print("Type is not object : ", d.get("type"))
        return objects
    if d.get("name") not in objects:
        objects.update({d.get("name"): d})
    for prop_name, prop_value in d.get("props").items():
        if prop_value.get("value") is None:
            continue
        if not isinstance(prop_value.get("value"), dict):
            # print("Type is not object : ", d.get("dataType"))
            continue
        if prop_value.get("value").get("name") in ["Object", "object"]:
            # print("Simple object detected :", prop_name)
            continue
        objects.update(decrypt_object(prop_value.get("value")))
    return objects



if __name__ == "__main__":
    data = utils.read_json_file(r"D:\code\prpro\classData_globals.json")
    unique_objects = decrypt_object(data)
    build_python_from_data(unique_objects.values(), r"D:\code\prpro\pymiere\autogenerated\globals_auto.py")