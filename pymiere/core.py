import os
import json
from time import time as current_time
import requests
from pymiere.exe_utils import exe_is_running

# ----- GLOBALS -----
PANEL_URL = "http://127.0.0.1:3000"
ALIVE_TIMEOUT = 2  # check that premiere is still alive every x seconds


# ----- FUNCTIONS -----
def check_premiere_is_alive(crash=True):
    """
    Check if premiere is running and if the pymiere CEP panel is active
    :param crash: (bool) what to do if premiere is not connected
    :return: (bool) is premiere ready to receive instruction from python
    """
    # search in globals the last time premiere was checked and if we need to chack again
    global last_alive_check_time
    if "last_alive_check_time" in globals() and current_time() - last_alive_check_time < ALIVE_TIMEOUT:
        return True
    # is premiere pro launched
    running, pid = exe_is_running("adobe premiere pro.exe")
    if not running:
        msg = "Premiere Pro is not running"
        if crash:
            raise ValueError(msg)
        print(msg)
        return False
    # is the CEP panel reachable
    try:
        response = requests.get(PANEL_URL)
    except requests.exceptions.ConnectionError:
        msg = "No connection could be established to Premiere Pro, check that the pymiere pannel is loaded"
        if crash:
            raise ConnectionError(msg)
        print(msg)
        return False
    if response.content.decode("utf-8") != "Premiere is alive":
        msg = "Found running server on '{}' but got wrong response for ping".format(PANEL_URL)
        if crash:
            raise ValueError()
        print(msg)
        return False
    last_alive_check_time = current_time()
    return True


def eval_script(code=None, filepath=None, decode_json=True):
    """
    Send some ExtendScript code to premiere and wait for the returning value
    :param code: (str) plain text ExtendScript code
    :param filepath: (str) path to a jsx file to execute
    :param decode_json: (bool) decode response using json if possible
    :return: (any) depend on the returned value
    """
    # todo voir si ca prends du temps et peut etre mettre un cache ici
    check_premiere_is_alive(crash=True)

    # arg check
    if not any([code, filepath]):
        raise ValueError("Have to supply either code as string or path to a .jsx file to eval some script")

    # load code from file
    if filepath:
        if not os.path.isfile(filepath):
            raise IOError("Specified file '{}' couldn't be found on disk".format(filepath))
        if not os.path.splitext(filepath)[-1] != "jsx":
            print("Passing a file '{}' that's not a .jsx to premiere, that's strange...".format(filepath))

        # using encoding 'utf-8-sig' to work with file saved with Adobe ExtendScript Toolkit
        with open(filepath, encoding='utf-8-sig') as f:
            code = f.read()

    # send code to premiere (adding try statement to prevent error popup message locking premiere UI)
    response = requests.post(PANEL_URL, json={"to_eval": "try{\n" + code + "\n}catch(e){e.error=true;JSON.stringify(e)}"})

    # handle response
    response_text = response.text
    if decode_json is False:
        return response_text
    try:
        response_decoded = json.loads(response_text)
    except json.decoder.JSONDecodeError as e:
        # print("No json could be decoded : {}".format(e))
        return response_text

    # handle error from extend script
    if isinstance(response_decoded, dict) and "error" in response_decoded and response_decoded["error"] is True:
        raise ExtendScriptError(response_decoded)
    return response_decoded


# ----- CLASSES -----
class ExtendScriptError(Exception):
    """
    Exception used to handle error object coming from a try statement in ES
    """
    def __init__(self, error_obj):
        msg = "\n{name} at line {line} : {message}".format(**error_obj)
        # add previous, current and next code line where the error is
        line = error_obj.get("line")
        source = error_obj.get("source").splitlines()
        if line != 1:
            msg += "\n {}\t{}".format(line-1, source[line-2])
        msg += "\n {}\t{}".format(line, source[line-1])
        if line != len(source):
            msg += "\n {}\t{}".format(line+1, source[line])
        # previous line
        super(ExtendScriptError, self).__init__(msg)


class PymiereBaseObject(object):
    """
    base object for every mirror object from ES
    """
    def __init__(self, pymiere_id):
        """
        Init pymiere connection global
        :param pymiere_id: (str) Id of the object we are about to create in extend script, every object is stored in
        $._pymiere var to be accessed easily from python
        """
        # if the id is None, the user created this object in python, we want to create it in ExtendScript
        if pymiere_id is None:
            # I don't think we need to create new objects with creation args... Put back if needed
            """# python args to string (object as creation arguments of other object is not supported by pymiere yet)
            str_args = ["'{}'".format(a) if isinstance(a, str) else str(a) for a in args]
            str_args += ["{}='{}'".format(k, v) if isinstance(v, str) else "{}={}".format(k, v) for k, v in kwargs]"""
            # create code line with 'new' statement and sending it to premiere
            line = "new {}()".format(self.__class__.__name__)
            result = _eval_script_returning_object(line)
            pymiere_id = result["pymiereId"]

        # store id
        self._pymiere_id = pymiere_id

    def _eval_on_this_object(self, extend_property, dot_notation=True):
        """
        Do something on the current object in extendscript, could be to query or set a property or exec a function
        :param extend_property: (str) code part after object needed to be execute (ex: get property name second => 'second',
        set property index => 'index = 12', execute a method 'getColor()'
        :param dot_notation: (bool) by default the dot is includin between the object query and the property, if we
        want to for example use the bracket notation for a collection we don't want the point in between
        :return: (any) could be None if got undefined from js, could be simple type like boolean, int or could be
        a dict of kwargs if the result was an object
        """
        # act on current object using id
        line = "$._pymiere['{}']{}{};".format(self._pymiere_id, "." if dot_notation else "", extend_property)
        result = _eval_script_returning_object(line)

        if result == "undefined":
            return None

        # if it's an object search if class exists and return objects creation arguments
        if isinstance(result, dict) and "isObject" in result and result["isObject"] is True:
            # search subclass of PymiereObject
            available_subclasses = {cls.__name__: cls for cls in PymiereBaseObject.__subclasses__()}
            available_subclasses.update({cls.__name__: cls for cls in PymiereBaseCollection.__subclasses__()})
            # todo : put back this check ? I don't think because we handle unknown objects with PymiereGenericObject
            # if result["objectType"] not in available_subclasses:
            #     raise ValueError("Received object of type '{}' that is not implemented in API...".format(result["objectType"]))
            # create key word argument list to create the object
            kwargs = result["objectValues"]
            kwargs.update(pymiere_id=result["pymiereId"])
            return kwargs
        return result

    @staticmethod
    def _check_init_args(kwargs):
        """
        Check that we either get all init args (when object comes from ES) or no args (when we want to create an empty object)
        :param kwargs: (dict) keyword arguments at object creation
        """
        if not kwargs.get("created_by_user", False):
            return
        kwargs = {k: v is not None for k, v in kwargs.items()}
        if all(kwargs.values()) is True:  # all args are given
            return
        if any(kwargs.values()) is False:  # no args given
            return
        arg_with_value = list()
        arg_without_value = list()
        for k, v in kwargs.items():
            if v:
                arg_with_value.append(k)
            else:
                arg_without_value.append(k)
        raise ValueError("Creation of object with keywords args doesn't work. Got keywords {} and not {}".format(arg_with_value, arg_without_value))

    @staticmethod
    def _check_type(obj, cls, name):
        """
        Check that the object is an instances of the right type
        :param obj: (any) object to check
        :param cls: (type) class the object should be
        :param name: (str) name of the object being check to print in the error if check fails
        """
        if cls == any or cls == "any":
            return
        if not isinstance(obj, cls):
            raise ValueError("{} shoud be of type {} but got '{}' (type {})".format(name, cls, obj, type(obj)))


class PymiereBaseCollection(PymiereBaseObject):
    def __init__(self, pymiere_id, len_property):
        """
        These is the base class for all collections, interfacing between premiere Collection objects and python builtin
        iteration tools
        :param pymiere_id: (str) Id of the object we are about to create in extend script, every object is stored in
        $._pymiere var to be accessed easily from python
        :param len_property: (str) name of the property, on the ExtendScript collection object, holding the number of items
        """
        if pymiere_id is None:
            raise ValueError("Creating a collection from scratch is not supported")
        self.len_property = len_property
        super(PymiereBaseCollection, self).__init__(pymiere_id)

    def __getitem__(self, index):
        """
        Builtin method for getting the value at the specific index, redirect to ExtendScript similar query
        :param index: (int) index of item we are searching in the collection
        :return: (dict) dict of kwargs to create the object. The object creation itself append in the subclass for
        code inspection/autocomplete purposes
        """
        return self._eval_on_this_object("[{}]".format(index), dot_notation=False)

    def __len__(self):
        """
        Builtin method for length, we ask premiere using the 'num...' property of the object
        :return: (int) length of the collection
        """
        return self._eval_on_this_object(self.len_property)

    def __iter__(self):
        """
        Builtin method for iteration, we return our custom iterator to redirect to the __getitem__ method
        This is actually overriden on all super class using a list to keep code type hint in IDE
        :return: (generator)
        """
        return _collection_iterator(self)


class PymiereGenericObject(PymiereBaseObject):
    """
    For all extend scrip objects that are not a specific class, works like the others but does not support code completion
    """
    def __init__(self, pymiere_id, *args, **kwargs):
        super(PymiereGenericObject, self).__init__(pymiere_id)

    def __setattr__(self, key, value):
        """
        Cqlled when we set a property value
        :param key: (str) name of the property
        :param value: (any) new value for the property
        """
        # pymiere id is a special prop
        if "pymiere_id" in key:
            return super(PymiereGenericObject, self).__setattr__(key, value)

        # check prop is available in extend script
        available_props = eval_script("$._pymiere['{}'].reflect.properties".format(self._pymiere_id), decode_json=False).split(",")
        if key not in available_props:
            raise ValueError("Cannot set property '{}' of object '{}' because it does not exists".format(key, self))
        # check prop is writable
        prop_type = eval_script("$._pymiere['{}'].reflect.properties[{}].type".format(self._pymiere_id, available_props.index(key)), decode_json=False)
        if prop_type != "readwrite":
            raise ValueError("Cannot write to property '{}' of '{}' because it is {}".format(key, self, prop_type))

        # write prop
        self._extend_eval("{} = {}".format(key, _format_object_to_es(value)))

    def __getattr__(self, item):
        """
        Called when we query a prop or execute a function : search in ES if func or prop + return value or function
        :param item: (str) name of function or the property
        :return: (any or func) value of the property or function to be executed
        """
        # pymiere id is a special property
        if "pymiere_id" in item:
            return super(PymiereGenericObject, self).__getattribute__(item)

        # search this item in methods and properties of extend script object
        available_props = eval_script("$._pymiere['{}'].reflect.properties".format(self._pymiere_id), decode_json=False).split(",")
        available_funcs = eval_script("$._pymiere['{}'].reflect.methods".format(self._pymiere_id), decode_json=False).split(",")
        if item not in available_props and item not in available_funcs:
            raise ValueError("Cannot get function/property '{}' because it does not exist on object '{}'".format(item, self))

        # getting a property value
        if item in available_props:
            line = "$._pymiere['{}'].{};".format(self._pymiere_id, item)
            result = _eval_script_returning_object(line)
            return _format_object_to_py(result)

        # using a function
        def generic_method(*args, **kwargs):
            args_line = list()
            for arg in args:
                args_line.append(_format_object_to_es(arg))
            for arg_name, arg in kwargs.items():
                args_line.append("{}={}".format(arg_name, _format_object_to_es(arg)))
            # build extend script line
            line = "$._pymiere['{}'].{}({});".format(self._pymiere_id, item, ",".join(args_line))

            # execute function
            result = _eval_script_returning_object(line)
            return _format_object_to_py(result)
        return generic_method
    
    def inspect(self):
        """
        Print functions and properties available on this object, can't be autocompleted
        """
        # start printing debug infos
        object_name = eval_script("$._pymiere['{}'].reflect.name".format(self._pymiere_id), decode_json=False)
        print("Inspection of object '{}' found :".format(object_name))
        # print available props
        available_props = eval_script("$._pymiere['{}'].reflect.properties".format(self._pymiere_id), decode_json=False).split(",")
        available_props = [p for p in available_props if not p.startswith("__") and p not in ["reflect"]]
        print(" {} properties :".format(len(available_props)))
        for prop in sorted(available_props):
            print("  - {} = {}".format(prop, self.__getattr__(prop)))
        # print available methods
        available_methods = eval_script("$._pymiere['{}'].reflect.methods".format(self._pymiere_id), decode_json=False).split(",")
        available_methods = [m for m in available_methods if m not in ["hasOwnProperty", "propertyIsEnumerable", "isPrototypeOf", "toSource", "watch", "unwatch"]]
        print(" {} methods".format(len(available_methods)))
        for i, method in enumerate(sorted(available_methods)):
            print("  - {}({})".format(method, eval_script("$._pymiere['{}'].reflect.methods[{}].arguments".format(self._pymiere_id, i))))

class Array(PymiereBaseCollection):
    def __init__(self, pymiere_id, length):
        super(Array, self).__init__(pymiere_id, "length")

    def __getitem__(self, index):
        return _format_object_to_py(super(Array, self).__getitem__(index))


# ----- PRIVATE FUNCTIONS ----
def _format_object_to_es(obj):
    """
    For functions args and property setter : format the given arg using quote for string, object query for object
    :param obj: (any) arg to format
    :return: (str) extend script equivalent for arg
    """
    if isinstance(obj, str):
        return "'{}'".format(obj)
    elif isinstance(obj, PymiereBaseObject):
        return "$._pymiere['{}']".format(obj._pymiere_id)
    else:
        return str(obj)


def _format_object_to_py(obj):
    """
    when getting a value from extend script, create object if it is one or return value for builtin
    :param obj: (any) value from ES decoded via json, could be an object repr
    :return: (any) python value
    """
    if isinstance(obj, dict) and obj.get("isObject") is True:
        object_type = obj.get("objectType")
        available_subclasses = {cls.__name__: cls for cls in PymiereBaseObject.__subclasses__()}
        available_subclasses.update({cls.__name__: cls for cls in PymiereBaseCollection.__subclasses__()})
        if object_type in available_subclasses:
            return available_subclasses[object_type](obj.get("pymiereId"), **obj["objectValues"])
        elif "ollection" in object_type:
            raise NotImplementedError("Pymiere does not support collections as generic object...")
        elif object_type == "$":
            return available_subclasses["Dollar"](obj.get("pymiereId"), **obj["objectValues"])
        else:
            return PymiereGenericObject(obj["pymiereId"], **obj["objectValues"])
    return obj


def _eval_script_returning_object(line, as_kwargs=False):
    """
    Eval the line as ExtendScript code, if the code return an object, it will be properly stored with an id for
    pymiere to handle it and returned as a representation with the id
    :param line: (str) line of code to execute in ES
    :param as_kwargs: (bool) if object return only kwargs+pymiere_id to directly pass it to class init
    :return: (dict) object repr
    """
    if not line.endswith(";"):
        line += ";"
    script = "var tmp = {}".format(line)
    script += """\nif(typeof tmp === 'object'){
            var newPymiereId = $._pymiere.generateId();
            $._pymiere[newPymiereId] = tmp;
            tmp = JSON.stringify({"isObject": true, "objectType": tmp.reflect.name, "objectValues": tmp, "pymiereId": newPymiereId}, internal_variables_replacer, 0, 1);
        }
        tmp"""
    result = eval_script(script, decode_json=True)
    if as_kwargs and isinstance(result, dict) and result.get("isObject"):
        kwargs = result.get("objectValues", dict())
        kwargs.update(pymiere_id=result["pymiereId"])
        return kwargs
    return result


def _collection_iterator(collection):
    """
    This is an iterator, we use it to redirect the use of __iter__ to __getitem__ in order to always query from
    ExtendScript. It is used by the __iter__ method of the PymiereBaseCollection class
    :param collection: (PymiereBaseCollection) the collection we want to iter on
    :return: yield item of the collection
    """
    for i in range(len(collection)):
        yield collection[i]
