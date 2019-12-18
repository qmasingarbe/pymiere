from pymiere.core import PymiereObject, PymiereCollection

class Sequence(PymiereObject):
    def __init__(self, pymiere_id, name, id, videoTracks):
        super(Sequence, self).__init__(pymiere_id)
        self.__name = name
        self.__id = id
        self.__videoTracks = videoTracks

    # ----- PROPERTIES -----
    @property
    def name(self):
        self.__name = self._extend_eval("name")
        return self.__name
    @name.setter
    def name(self, name):
        self._extend_eval("name = '{}'".format(name))
        self.__name = name

    @property
    def videoTracks(self):
        self.__videoTracks = TrackCollection(**self._extend_eval("videoTracks"))
        return self.__videoTracks

    @property
    def id(self):
        self.__id = self._extend_eval("id")
        return self.__id
    @id.setter
    def id(self, id):
        raise AttributeError("Attribute 'id' is read-only")

    # ---- METHODS ----
    def getPlayerPosition(self):
        return Time(**self._extend_eval("getPlayerPosition()"))

    def getInPoint(self):
        return self._extend_eval("getInPoint()")

    def setPlayerPosition(self, newTimeInTicks):
        """
        :type newTimeInTicks: str
        """
        self._extend_eval("setPlayerPosition({})".format(newTimeInTicks))


class Time(PymiereObject):
    # todo : ameliorer ca dans la generation via class data
    def __init__(self, pymiere_id=None, seconds=None, ticks=None):
        super(Time, self).__init__(pymiere_id)
        self.__seconds = seconds
        self.__ticks = ticks

    # ----- PROPERTIES -----
    @property
    def seconds(self):
        self.__seconds = self._extend_eval("seconds")
        return self.__seconds
    @seconds.setter
    def seconds(self, seconds):
        self._extend_eval("seconds = {}".format(seconds))
        self.__seconds = seconds

    @property
    def ticks(self):
        self.__ticks = self._extend_eval("ticks")
        return self.__ticks
    @ticks.setter
    def ticks(self, ticks):
        raise AttributeError("Attribute 'ticks' is read-only")

class TrackCollection(PymiereCollection):
    def __init__(self, pymiere_id, numTracks):
        super(TrackCollection, self).__init__(pymiere_id, "numTracks")

    def __getitem__(self, index):
        return Track(**super(TrackCollection, self).__getitem__(index))

class Track(PymiereObject):
    def __init__(self, *args, **kwargs):
        super(Track, self).__init__(kwargs["pymiere_id"])
        self.args = args
        self.kwargs = kwargs
        self.__clips = kwargs["clips"]

    @property
    def clips(self):
        self.__clips = ClipCollection(**self._extend_eval("clips"))
        return self.__clips

class ClipCollection(PymiereCollection):
    def __init__(self, pymiere_id, numItems):
        super(ClipCollection, self).__init__(pymiere_id, "numItems")

    def __getitem__(self, index):
        return Clip(**super(ClipCollection, self).__getitem__(index))

class Clip(PymiereObject):
    def __init__(self, *args, **kwargs):
        super(Clip, self).__init__(kwargs["pymiere_id"])
        self.args = args
        self.kwargs = kwargs
        self.__end = kwargs["end"]

    @property
    def end(self):
        self.__end = Time(**self._extend_eval("end"))
        return self.__end

    @end.setter
    def end(self, end):
        # todo : wrapper ce code et l'inserer dans le build depuis la class data
        self._extend_eval("end = $._pymiere['{}']".format(end._pymiere_id))
        self.__end = end