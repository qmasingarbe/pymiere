from pymiere.core import _format_object_to_py, _format_object_to_es, _eval_script_returning_object
from pymiere.objects.premiere_objects import *


def _eval_on_global_object(extend_property):
    result = _eval_script_returning_object(extend_property)
    if result == "undefined":
        return None
    # if it's an object search if class exists and return objects creation arguments
    if isinstance(result, dict) and "isObject" in result and result["isObject"] is True:
        # create key word argument list to create the object
        kwargs = dict(pymiere_id=result["pymiereId"])
        return kwargs
    return result


class StartVars(object):
    def __init__(self):
        super(StartVars, self).__init__()

    # ----- PROPERTIES -----
    @property
    def NaN(self):
        return _eval_on_global_object('NaN')
    @NaN.setter
    def NaN(self, NaN):
        PymiereBaseObject._check_type(NaN, float, 'StartVars.NaN')
        _eval_on_global_object("NaN = {}".format(_format_object_to_es(NaN)))

    @property
    def Infinity(self):
        return _eval_on_global_object('Infinity')
    @Infinity.setter
    def Infinity(self, Infinity):
        PymiereBaseObject._check_type(Infinity, float, 'StartVars.Infinity')
        _eval_on_global_object("Infinity = {}".format(_format_object_to_es(Infinity)))

    @property
    def undefined(self):
        return _eval_on_global_object('undefined')
    @undefined.setter
    def undefined(self, undefined):
        PymiereBaseObject._check_type(undefined, None, 'StartVars.undefined')
        _eval_on_global_object("undefined = {}".format(_format_object_to_es(undefined)))

    @property
    def qe(self):
        return _format_object_to_py(_eval_script_returning_object('qe'))
    @qe.setter
    def qe(self, qe):
        raise AttributeError("Attribute 'qe' is read-only")

    """ The application object """
    @property
    def app(self):
        return Application(**_eval_script_returning_object('app', as_kwargs=True))
    @app.setter
    def app(self, app):
        raise AttributeError("Attribute 'app' is read-only")

    @property
    def document(self):
        return Document(**_eval_script_returning_object('document', as_kwargs=True))
    @document.setter
    def document(self, document):
        raise AttributeError("Attribute 'document' is read-only")

    @property
    def ProjectItemType(self):
        return ProjectItemType(**_eval_script_returning_object('ProjectItemType', as_kwargs=True))
    @ProjectItemType.setter
    def ProjectItemType(self, ProjectItemType):
        raise AttributeError("Attribute 'ProjectItemType' is read-only")

    @property
    def ScratchDiskType(self):
        return ScratchDiskType(**_eval_script_returning_object('ScratchDiskType', as_kwargs=True))
    @ScratchDiskType.setter
    def ScratchDiskType(self, ScratchDiskType):
        raise AttributeError("Attribute 'ScratchDiskType' is read-only")

    @property
    def RegisteredDirectories(self):
        return RegisteredDirectories(**_eval_script_returning_object('RegisteredDirectories', as_kwargs=True))
    @RegisteredDirectories.setter
    def RegisteredDirectories(self, RegisteredDirectories):
        raise AttributeError("Attribute 'RegisteredDirectories' is read-only")

    @property
    def UtilityFunctions(self):
        return UtilityFunctions(**_eval_script_returning_object('UtilityFunctions', as_kwargs=True))
    @UtilityFunctions.setter
    def UtilityFunctions(self, UtilityFunctions):
        raise AttributeError("Attribute 'UtilityFunctions' is read-only")

    @property
    def Dollar(self):
        return Dollar(**_eval_script_returning_object('$', as_kwargs=True))
    @Dollar.setter
    def Dollar(self, Dollar):
        raise AttributeError("Attribute 'Dollar' is read-only")

    @property
    def Math(self):
        return Math(**_eval_script_returning_object('Math', as_kwargs=True))
    @Math.setter
    def Math(self, Math):
        raise AttributeError("Attribute 'Math' is read-only")

    @property
    def premierepro13(self):
        return _format_object_to_py(_eval_script_returning_object('premierepro13'))
    @premierepro13.setter
    def premierepro13(self, premierepro13):
        _eval_on_global_object("premierepro13 = {}".format(_format_object_to_es(premierepro13)))

    @property
    def AEFTBridge(self):
        return _format_object_to_py(_eval_script_returning_object('AEFTBridge'))
    @AEFTBridge.setter
    def AEFTBridge(self, AEFTBridge):
        _eval_on_global_object("AEFTBridge = {}".format(_format_object_to_es(AEFTBridge)))

    @property
    def PHXSBridge(self):
        return _format_object_to_py(_eval_script_returning_object('PHXSBridge'))
    @PHXSBridge.setter
    def PHXSBridge(self, PHXSBridge):
        _eval_on_global_object("PHXSBridge = {}".format(_format_object_to_es(PHXSBridge)))

    @property
    def CCXHostBridge(self):
        return _format_object_to_py(_eval_script_returning_object('CCXHostBridge'))
    @CCXHostBridge.setter
    def CCXHostBridge(self, CCXHostBridge):
        _eval_on_global_object("CCXHostBridge = {}".format(_format_object_to_es(CCXHostBridge)))

    @property
    def f(self):
        return File(**_eval_script_returning_object('f', as_kwargs=True))
    @f.setter
    def f(self, f):
        PymiereBaseObject._check_type(f, File, 'StartVars.f')
        _eval_on_global_object("f = {}".format(_format_object_to_es(f)))

    @property
    def JSON(self):
        return _format_object_to_py(_eval_script_returning_object('JSON'))
    @JSON.setter
    def JSON(self, JSON):
        _eval_on_global_object("JSON = {}".format(_format_object_to_es(JSON)))


    # ----- FUNCTIONS -----
    def encodeURI(self, text):
        """
        Encodes a string after RFC2396. Create an UTF-8 ASCII encoded version of this string. The string is converted into UTF-8. Every non-alphanumeric character is encoded as a percent escape character of the form %xx, where xx is the hex value of the character. After the conversion to UTF-8 encoding and escaping, it is guaranteed that the string does not contain characters codes greater than 127. The list of characters not to be encoded is -_.!~'();/?:@&=+Dollar,#. The method returns false on errors. 
        :param text: The text to encode.
        :type text: str
        """
        PymiereBaseObject._check_type(text, str, 'arg "text" of function "StartVars.encodeURI"')
        return _eval_on_global_object("encodeURI({})".format(_format_object_to_es(text)))

    def encodeURIComponent(self, text):
        """
        Encodes a string after RFC2396. Create an UTF-8 ASCII encoded version of this string. The string is converted into UTF-8. Every non-alphanumeric character is encoded as a percent escape character of the form %xx, where xx is the hex value of the character. After the conversion to UTF-8 encoding and escaping, it is guaranteed that the string does not contain characters codes greater than 127. The list of characters not to be encoded is -_.!~'(). The method returns false on errors. 
        :param text: The text to encode.
        :type text: str
        """
        PymiereBaseObject._check_type(text, str, 'arg "text" of function "StartVars.encodeURIComponent"')
        return _eval_on_global_object("encodeURIComponent({})".format(_format_object_to_es(text)))

    def decodeURI(self, uri):
        """
        Decodes a string created with encodeURI(). 
        :param uri: The text to decode.
        :type uri: str
        """
        PymiereBaseObject._check_type(uri, str, 'arg "uri" of function "StartVars.decodeURI"')
        return _eval_on_global_object("decodeURI({})".format(_format_object_to_es(uri)))

    def decodeURIComponent(self, uri):
        """
        Decodes a string created with encodeURIComponent(). 
        :param uri: The text to decode.
        :type uri: str
        """
        PymiereBaseObject._check_type(uri, str, 'arg "uri" of function "StartVars.decodeURIComponent"')
        return _eval_on_global_object("decodeURIComponent({})".format(_format_object_to_es(uri)))

    def escape(self, text):
        """
        Creates a URL-encoded string from aString. In the new string, characters of aString that require URL encoding are replaced with the format %xx, where xx is the hexadecimal value of the character code in the Unicode character set.This format is used to transmit information appended to a URL during, for example, execution of the GET method.Use the unescape() global function to translate the string back into its original format. Returns a string which is aString URL-encoded. 
        :param aString: The string to be encoded.
        :type text: str
        """
        PymiereBaseObject._check_type(text, str, 'arg "text" of function "StartVars.escape"')
        return _eval_on_global_object("escape({})".format(_format_object_to_es(text)))

    def eval(self, source):
        """
        Evaluates its argument as a JavaScript script, and returns the result of evaluation. You can pass the result of an object's toSource() method to reconstruct that object. 
        :param stringExpression: The string to evaluate.
        :type source: str
        """
        PymiereBaseObject._check_type(source, str, 'arg "source" of function "StartVars.eval"')
        return _eval_on_global_object("eval({})".format(_format_object_to_es(source)))

    def uneval(self, what):
        """
        Creates a source code representation of the supplied argument, and returns it as a string. 
        :param what: The object to uneval.
        :type what: any
        """
        PymiereBaseObject._check_type(what, any, 'arg "what" of function "StartVars.uneval"')
        return _eval_on_global_object("uneval({})".format(_format_object_to_es(what)))

    def isFinite(self, what):
        """
        Evaluates an expression and reports whether the result is a finite number. Returns true if the expression is a finite number, false otherwise. False if the value is infinity or negative infinity. 
        :param expression: Any valid JavaScript expression.
        :type what: float
        """
        PymiereBaseObject._check_type(what, float, 'arg "what" of function "StartVars.isFinite"')
        return _eval_on_global_object("isFinite({})".format(_format_object_to_es(what)))

    def isNaN(self, what):
        """
        Evaluates an expression and reports whether the result is "Not-a-Number" (NaN). Returns true if the result of evaluation is not a number (NaN), false if the value is a number. 
        :param expression: Any valid JavaScript expression.
        :type what: float
        """
        PymiereBaseObject._check_type(what, float, 'arg "what" of function "StartVars.isNaN"')
        return _eval_on_global_object("isNaN({})".format(_format_object_to_es(what)))

    def parseInt(self, text, base):
        """
        Extracts an integer from a string. Parses a string to find the first set of characters, in a specified base, that can be converted to an integer, and returns that integer, or NaN if it does not encounter characters that it can convert to a number. 
        :param text: The string from which to extract an integer.
        :param base: The base of the string to parse (from base 2 to base 36). If not supplied, base is determined by the format of string.
        :type text: str
        :type base: float
        """
        PymiereBaseObject._check_type(text, str, 'arg "text" of function "StartVars.parseInt"')
        PymiereBaseObject._check_type(base, float, 'arg "base" of function "StartVars.parseInt"')
        return _eval_on_global_object("parseInt({}, {})".format(_format_object_to_es(text), _format_object_to_es(base)))

    def parseFloat(self, txt):
        """
        Extracts a floating-point number from a string. Parses a string to find the first set of characters that can be converted to a floating point number, and returns that number, or NaN if it does not encounter characters that it can converted to a number.The function supports exponential notation. 
        :param text: The string from which to extract a floating point number.
        :type txt: str
        """
        PymiereBaseObject._check_type(txt, str, 'arg "txt" of function "StartVars.parseFloat"')
        return _eval_on_global_object("parseFloat({})".format(_format_object_to_es(txt)))

    def unescape(self, uri):
        """
        Translates URL-encoded string into a regular string, and returns that string. Use the escape() global function to URL-encode strings. 
        :param stringExpression: The URL-encoded string to convert.
        :type uri: str
        """
        PymiereBaseObject._check_type(uri, str, 'arg "uri" of function "StartVars.unescape"')
        return _eval_on_global_object("unescape({})".format(_format_object_to_es(uri)))

    def localize(self, what):
        """
        Localizes a ZString-encoded string and merges additional arguments into the string. 
        :param what: The string to localize. A ZString-encoded string that can contain placeholder for additional arguments in the form %1 to %n.
        :param arguments: Optional argument(s) to be merged into the string. There may be more than one argument.
        :type what: any
        """
        PymiereBaseObject._check_type(what, any, 'arg "what" of function "StartVars.localize"')
        return _eval_on_global_object("localize({})".format(_format_object_to_es(what)))

    def isXMLName(self, name):
        """
        Returns true if the supplied string is a valid XML name. 
        :param name: The XML name to test.
        :type name: str
        """
        PymiereBaseObject._check_type(name, str, 'arg "name" of function "StartVars.isXMLName"')
        return _eval_on_global_object("isXMLName({})".format(_format_object_to_es(name)))

    def setDefaultXMLNamespace(self, ns):
        """
        Defines the default XML namespace. This is a replacement function for the standard JavaScript statement set default xml namespace. 
        :param namespace: The namespace to use. Omit this parameter to return to the empty namespace. This is either a Namespace object or a string.
        :type ns: Namespace
        """
        return _eval_on_global_object("setDefaultXMLNamespace({})".format(_format_object_to_es(ns)))

    def alert(self, prompt):
        """
        Displays an alert box 
        :param message: The text to display
        :param title: The title of the alert; ignored on the Macintosh
        :param errorIcon: Display an Error icon; ignored on the Macintosh
        :type prompt: str
        """
        PymiereBaseObject._check_type(prompt, str, 'arg "prompt" of function "StartVars.alert"')
        _eval_on_global_object("alert({})".format(_format_object_to_es(prompt)))

    def confirm(self, prompt):
        """
        Displays an alert box with Yes and No buttons; returns true for Yes 
        :param message: The text to display
        :param noAsDefault: Set to true to set the No button as the default button
        :param title: The title of the alert; ignored on the Macintosh
        :type prompt: str
        """
        PymiereBaseObject._check_type(prompt, str, 'arg "prompt" of function "StartVars.confirm"')
        return _eval_on_global_object("confirm({})".format(_format_object_to_es(prompt)))

    def prompt(self, prompt):
        """
        Displays a dialog allowing the user to enter text Returns null if the user cancelled the dialog, the text otherwise 
        :param prompt: The text to display
        :param default_: The default text to preset the edit field with
        :param title: The title of the dialog;
        :type prompt: str
        """
        PymiereBaseObject._check_type(prompt, str, 'arg "prompt" of function "StartVars.prompt"')
        return _eval_on_global_object("prompt({})".format(_format_object_to_es(prompt)))
