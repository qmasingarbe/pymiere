from pymiere.core import PymiereObject, PymiereCollection

class Marker(PymiereObject):
    def __init__(self, pymiere_id=None, start=None, end=None, type=None, name=None, comments=None, guid=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'start':start, 'end':end, 'type':type, 'name':name, 'comments':comments, 'guid':guid})
        super(Marker, self).__init__(pymiere_id)
        self.__start = start
        self.__end = end
        self.__type = type
        self.__name = name
        self.__comments = comments
        self.__guid = guid

    # ----- PROPERTIES -----
    @property
    def start(self):
        self.__start = Time(**self._extend_eval('start'))
        return self.__start
    @start.setter
    def start(self, start):
        self.check_type(start, Time, 'Marker.start')
        self._extend_eval("start = $._pymiere['{}']".format(start._pymiere_id))
        self.__start = start

    @property
    def end(self):
        self.__end = Time(**self._extend_eval('end'))
        return self.__end
    @end.setter
    def end(self, end):
        self.check_type(end, Time, 'Marker.end')
        self._extend_eval("end = $._pymiere['{}']".format(end._pymiere_id))
        self.__end = end

    @property
    def type(self):
        self.__type = self._extend_eval('type')
        return self.__type
    @type.setter
    def type(self, type):
        self.check_type(type, str, 'Marker.type')
        self._extend_eval("type = '{}'".format(type))
        self.__type = type

    @property
    def name(self):
        self.__name = self._extend_eval('name')
        return self.__name
    @name.setter
    def name(self, name):
        self.check_type(name, str, 'Marker.name')
        self._extend_eval("name = '{}'".format(name))
        self.__name = name

    @property
    def comments(self):
        self.__comments = self._extend_eval('comments')
        return self.__comments
    @comments.setter
    def comments(self, comments):
        self.check_type(comments, str, 'Marker.comments')
        self._extend_eval("comments = '{}'".format(comments))
        self.__comments = comments

    @property
    def guid(self):
        self.__guid = self._extend_eval('guid')
        return self.__guid
    @guid.setter
    def guid(self, guid):
        self.check_type(guid, str, 'Marker.guid')
        raise AttributeError("Attribute 'guid' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Marker.bind"')
        self.check_type(function, any, 'arg "function" of function "Marker.bind"')
        self._extend_eval("bind('{}', {})".format(eventName, function))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Marker.unbind"')
        self._extend_eval("unbind('{}')".format(eventName))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Marker.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "Marker.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "Marker.setTimeout"')
        self._extend_eval("setTimeout('{}', {}, {})".format(eventName, function, milliseconds))

    def setTypeAsComment(self):
        self._extend_eval("setTypeAsComment()")

    def setTypeAsChapter(self):
        self._extend_eval("setTypeAsChapter()")

    def setTypeAsSegmentation(self):
        self._extend_eval("setTypeAsSegmentation()")

    def setTypeAsWebLink(self, url, frameTarget):
        """
        :type url: str
        :type frameTarget: str
        """
        self.check_type(url, str, 'arg "url" of function "Marker.setTypeAsWebLink"')
        self.check_type(frameTarget, str, 'arg "frameTarget" of function "Marker.setTypeAsWebLink"')
        self._extend_eval("setTypeAsWebLink('{}', '{}')".format(url, frameTarget))

    def getWebLinkURL(self):
        return self._extend_eval("getWebLinkURL()")

    def getWebLinkFrameTarget(self):
        return self._extend_eval("getWebLinkFrameTarget()")
