import os
import json
import requests

# ----- FUNCTIONS -----
def _format_object_to_es(obj):
    """
    For functions args and property setter : format the given arg using quote for string, object query for object
    :param obj: (any) arg to format
    :return: (str) extend script equivalent for arg
    """
    if isinstance(obj, str):
        return "'{}'".format(obj)
    elif isinstance(obj, PymiereObject):
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
        available_subclasses = {cls.__name__: cls for cls in PymiereObject.__subclasses__()}
        available_subclasses.update({cls.__name__: cls for cls in PymiereCollection.__subclasses__()})
        if object_type in available_subclasses:
            return available_subclasses[object_type](obj.get("pymiereId"), **obj["objectValues"])
        elif "ollection" in object_type:
            raise NotImplementedError("Pymiere does not support collections as generic object...")
        else:
            return PymiereGenericObject(obj["pymiereId"], **obj["objectValues"])
    return obj

def collection_iterator(collection):
    """
    This is an iterator, we use it to redirect the use of __iter__ to __getitem__ in order to always query from
    ExtendScript. It is used by the __iter__ method of the PymiereCollection class
    :param collection: (PymiereCollection) the collection we want to iter on
    :return: yield item of the collection
    """
    for i in range(len(collection)):
        yield collection[i]


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


class Pymiere(object):
    """
    Main global class handling the communication to the node.js server in the premiere panel
    """
    def __init__(self):
        # global variables
        self.hostname = '127.0.0.1'
        self.port = 3000
        self.url = "http://{}:{}".format(self.hostname, self.port)

        # ping for connection
        try:
            response = requests.get(self.url)
        except requests.exceptions.ConnectionError:
            # todo premiere is running or not ?
            raise ConnectionError("No connection could be established to Premiere Pro, check that it is running "
                                  "and the pymiere pannel is loaded")
        if response.content.decode("utf-8") != "Premiere is alive":
            raise ValueError("No Premiere Pro instance found with server running on '{}'".format(self.url))

    def eval_script(self, code=None, filepath=None, decode_json=True):
        """
        Send some ExtendScript to premiere and wait for the returning value
        :param code: (str) plain text ExtendScript code
        :param filepath: (str) path to a jsx file to execute
        :param decode_json: (bool) decode response using json if possible
        :return: (any) depend on the returned value
        """
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
        response = requests.post(self.url, json={"to_eval": "try{\n" + code + "\n}catch(e){e.error=true;JSON.stringify(e)}"})

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


class PymiereObject(object):
    """
    base object for every mirror object from ES
    """
    def __init__(self, pymiere_id):
        """
        Init pymiere connection global
        :param pymiere_id: (str) Id of the object we are about to create in extend script, every object is stored in
        $._pymiere var to be accessed easily from python
        """
        # connect to premiere
        global PYMIERE
        if 'PYMIERE' not in globals():
            PYMIERE = Pymiere()

        # if the id is None, the user created this object in python, we want to create it in ExtendScript
        if pymiere_id is None:
            # I don't think we need to create new objects with creation args... Put back if needed
            """# python args to string (object as creation arguments of other object is not supported by pymiere yet)
            str_args = ["'{}'".format(a) if isinstance(a, str) else str(a) for a in args]
            str_args += ["{}='{}'".format(k, v) if isinstance(v, str) else "{}={}".format(k, v) for k, v in kwargs]"""
            # create code line with 'new' statement and sending it to premiere
            line = "new {}()".format(self.__class__.__name__)
            result = self._eval_line_returning_object(line)
            pymiere_id = result["pymiereId"]

        # store id
        self._pymiere_id = pymiere_id

    @staticmethod
    def _eval_line_returning_object(line):
        """
        Eval the line as ExtendScript code, if the code return an object, it will be properly stored with an id for
        pymiere to handle it and returned as a representation with the id
        :param line: (str) line of code to execute in ES
        :return: (dict) object repr
        """
        if not line.endswith(";"):
            line += ";"
        script = "var tmp = {}".format(line)
        script += """\nif(typeof tmp === 'object'){
            var newPymiereId = $._pymiere.generateId();
            $._pymiere[newPymiereId] = tmp;
            tmp = JSON.stringify({"isObject": true, "objectType": tmp.reflect.name, "objectValues": tmp, "pymiereId": newPymiereId});
        }
        tmp"""
        return PYMIERE.eval_script(script, decode_json=True)

    def _extend_eval(self, extend_property, dot_notation=True):
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
        result = self._eval_line_returning_object(line)

        if result == "undefined":
            return None

        # if it's an object search if class exists and return objects creation arguments
        if isinstance(result, dict) and "isObject" in result and result["isObject"] is True:
            # search subclass of PymiereObject
            available_subclasses = {cls.__name__: cls for cls in PymiereObject.__subclasses__()}
            available_subclasses.update({cls.__name__: cls for cls in PymiereCollection.__subclasses__()})
            # todo : remettre le check quand tout a bien ete genere
            # if result["objectType"] not in available_subclasses:
            #     raise ValueError("Received object of type '{}' that is not implemented in API...".format(result["objectType"]))
            # create key word argument list to create the object
            kwargs = result["objectValues"]
            kwargs.update(pymiere_id=result["pymiereId"])
            return kwargs
        return result

    @staticmethod
    def check_init_args(kwargs):
        """
        Check that we either get all init args (object comes from ES) or no args (we want to create an empty object)
        :param kwargs: (dict) keyword arguments at object creation
        """
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
    def check_type(obj, cls, name):
        if cls == any or cls == "any":
            return
        if not isinstance(obj, cls):
            raise ValueError("{} shoud be of type {} but got '{}' (type {})".format(name, cls, obj, type(obj)))


class PymiereCollection(PymiereObject):
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
        super(PymiereCollection, self).__init__(pymiere_id)

    def __getitem__(self, index):
        """
        Builtin method for getting the value at the specific index, redirect to ExtendScript similar query
        :param index: (int) index of item we are searching in the collection
        :return: (dict) dict of kwargs to create the object. The object creation itself append in the subclass for
        code inspection/autocomplete purposes
        """
        return self._extend_eval("[{}]".format(index), dot_notation=False)

    def __len__(self):
        """
        Builtin method for length, we ask premiere using the 'num...' property of the object
        :return: (int) length of the collection
        """
        return self._extend_eval(self.len_property)

    def __iter__(self):
        """
        Builtin method for iteration, we return our custom iterator to redirect to the __getitem__ method
        :return: (generator)
        """
        return collection_iterator(self)


class PymiereGenericObject(PymiereObject):
    """
    For all extend scrip object that are not a specific class, works like the others but does not support code completion
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
        available_props = PYMIERE.eval_script("$._pymiere['{}'].reflect.properties".format(self._pymiere_id), decode_json=False).split(",")
        if key not in available_props:
            raise ValueError("Cannot set property '{}' of object '{}' because it does not exists".format(key, self))
        # check prop is writable
        prop_type = PYMIERE.eval_script("$._pymiere['{}'].reflect.properties[{}].type".format(self._pymiere_id, available_props.index(key)), decode_json=False)
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
        available_props = PYMIERE.eval_script("$._pymiere['{}'].reflect.properties".format(self._pymiere_id), decode_json=False).split(",")
        available_funcs = PYMIERE.eval_script("$._pymiere['{}'].reflect.methods".format(self._pymiere_id), decode_json=False).split(",")
        if item not in available_props and item not in available_funcs:
            raise ValueError("Cannot get function/property '{}' because it does not exist on object '{}'".format(item, self))

        # getting a property value
        if item in available_props:
            line = "$._pymiere['{}'].{};".format(self._pymiere_id, item)
            result = self._eval_line_returning_object(line)
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
            result = self._eval_line_returning_object(line)
            return _format_object_to_py(result)
        return generic_method
