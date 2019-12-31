from pymiere.core import PymiereObject, PymiereCollection, Array, _format_object_to_py, _format_object_to_es

class Application(PymiereObject):
    def __init__(self, pymiere_id=None, version=None, build=None, getPProPrefPath=None, getPProSystemPrefPath=None, project=None, projects=None, anywhere=None, encoder=None, properties=None, sourceMonitor=None, projectManager=None, userGuid=None, path=None, getAppPrefPath=None, getAppSystemPrefPath=None, metadata=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'version':version, 'build':build, 'getPProPrefPath':getPProPrefPath, 'getPProSystemPrefPath':getPProSystemPrefPath, 'project':project, 'projects':projects, 'anywhere':anywhere, 'encoder':encoder, 'properties':properties, 'sourceMonitor':sourceMonitor, 'projectManager':projectManager, 'userGuid':userGuid, 'path':path, 'getAppPrefPath':getAppPrefPath, 'getAppSystemPrefPath':getAppSystemPrefPath, 'metadata':metadata})
        super(Application, self).__init__(pymiere_id)
        self.__version = version
        self.__build = build
        self.__getPProPrefPath = getPProPrefPath
        self.__getPProSystemPrefPath = getPProSystemPrefPath
        self.__project = project
        self.__projects = projects
        self.__anywhere = anywhere
        self.__encoder = encoder
        self.__properties = properties
        self.__sourceMonitor = sourceMonitor
        self.__projectManager = projectManager
        self.__userGuid = userGuid
        self.__path = path
        self.__getAppPrefPath = getAppPrefPath
        self.__getAppSystemPrefPath = getAppSystemPrefPath
        self.__metadata = metadata

    # ----- PROPERTIES -----
    @property
    def version(self):
        self.__version = self._extend_eval('version')
        return self.__version
    @version.setter
    def version(self, version):
        raise AttributeError("Attribute 'version' is read-only")

    @property
    def build(self):
        self.__build = self._extend_eval('build')
        return self.__build
    @build.setter
    def build(self, build):
        raise AttributeError("Attribute 'build' is read-only")

    @property
    def getPProPrefPath(self):
        self.__getPProPrefPath = self._extend_eval('getPProPrefPath')
        return self.__getPProPrefPath
    @getPProPrefPath.setter
    def getPProPrefPath(self, getPProPrefPath):
        raise AttributeError("Attribute 'getPProPrefPath' is read-only")

    @property
    def getPProSystemPrefPath(self):
        self.__getPProSystemPrefPath = self._extend_eval('getPProSystemPrefPath')
        return self.__getPProSystemPrefPath
    @getPProSystemPrefPath.setter
    def getPProSystemPrefPath(self, getPProSystemPrefPath):
        raise AttributeError("Attribute 'getPProSystemPrefPath' is read-only")

    @property
    def project(self):
        self.__project = Project(**self._extend_eval('project'))
        return self.__project
    @project.setter
    def project(self, project):
        self.check_type(project, Project, 'Application.project')
        self._extend_eval("project = {}".format(_format_object_to_es(project)))
        self.__project = project

    @property
    def projects(self):
        self.__projects = ProjectCollection(**self._extend_eval('projects'))
        return self.__projects
    @projects.setter
    def projects(self, projects):
        raise AttributeError("Attribute 'projects' is read-only")

    @property
    def anywhere(self):
        self.__anywhere = Anywhere(**self._extend_eval('anywhere'))
        return self.__anywhere
    @anywhere.setter
    def anywhere(self, anywhere):
        raise AttributeError("Attribute 'anywhere' is read-only")

    @property
    def encoder(self):
        self.__encoder = Encoder(**self._extend_eval('encoder'))
        return self.__encoder
    @encoder.setter
    def encoder(self, encoder):
        raise AttributeError("Attribute 'encoder' is read-only")

    @property
    def properties(self):
        self.__properties = Properties(**self._extend_eval('properties'))
        return self.__properties
    @properties.setter
    def properties(self, properties):
        raise AttributeError("Attribute 'properties' is read-only")

    @property
    def sourceMonitor(self):
        self.__sourceMonitor = SourceMonitor(**self._extend_eval('sourceMonitor'))
        return self.__sourceMonitor
    @sourceMonitor.setter
    def sourceMonitor(self, sourceMonitor):
        raise AttributeError("Attribute 'sourceMonitor' is read-only")

    @property
    def projectManager(self):
        self.__projectManager = ProjectManager(**self._extend_eval('projectManager'))
        return self.__projectManager
    @projectManager.setter
    def projectManager(self, projectManager):
        raise AttributeError("Attribute 'projectManager' is read-only")

    @property
    def userGuid(self):
        self.__userGuid = self._extend_eval('userGuid')
        return self.__userGuid
    @userGuid.setter
    def userGuid(self, userGuid):
        raise AttributeError("Attribute 'userGuid' is read-only")

    @property
    def path(self):
        self.__path = self._extend_eval('path')
        return self.__path
    @path.setter
    def path(self, path):
        raise AttributeError("Attribute 'path' is read-only")

    @property
    def getAppPrefPath(self):
        self.__getAppPrefPath = self._extend_eval('getAppPrefPath')
        return self.__getAppPrefPath
    @getAppPrefPath.setter
    def getAppPrefPath(self, getAppPrefPath):
        raise AttributeError("Attribute 'getAppPrefPath' is read-only")

    @property
    def getAppSystemPrefPath(self):
        self.__getAppSystemPrefPath = self._extend_eval('getAppSystemPrefPath')
        return self.__getAppSystemPrefPath
    @getAppSystemPrefPath.setter
    def getAppSystemPrefPath(self, getAppSystemPrefPath):
        raise AttributeError("Attribute 'getAppSystemPrefPath' is read-only")

    @property
    def metadata(self):
        self.__metadata = Metadata(**self._extend_eval('metadata'))
        return self.__metadata
    @metadata.setter
    def metadata(self, metadata):
        raise AttributeError("Attribute 'metadata' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Application.bind"')
        self.check_type(function, any, 'arg "function" of function "Application.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Application.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Application.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "Application.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "Application.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def isDocumentOpen(self):
        return self._extend_eval("isDocumentOpen()")

    def getWorkspaces(self):
        self._extend_eval("getWorkspaces()")

    def setWorkspace(self, workspace):
        """
        :type workspace: str
        """
        self.check_type(workspace, str, 'arg "workspace" of function "Application.setWorkspace"')
        return self._extend_eval("setWorkspace({})".format(_format_object_to_es(workspace)))

    def isDocument(self, filePath):
        """
        :type filePath: str
        """
        self.check_type(filePath, str, 'arg "filePath" of function "Application.isDocument"')
        return self._extend_eval("isDocument({})".format(_format_object_to_es(filePath)))

    def openDocument(self):
        return self._extend_eval("openDocument()")

    def quit(self):
        self._extend_eval("quit()")

    def trace(self, message):
        """
        :type message: str
        """
        self.check_type(message, str, 'arg "message" of function "Application.trace"')
        self._extend_eval("trace({})".format(_format_object_to_es(message)))

    def write(self, arg1):
        """
        :type arg1: any
        """
        self.check_type(arg1, any, 'arg "arg1" of function "Application.write"')
        self._extend_eval("write({})".format(_format_object_to_es(arg1)))

    def openFCPXML(self):
        return self._extend_eval("openFCPXML()")

    def setSDKEventMessage(self, value, eventType):
        """
        :type value: str
        :type eventType: str
        """
        self.check_type(value, str, 'arg "value" of function "Application.setSDKEventMessage"')
        self.check_type(eventType, str, 'arg "eventType" of function "Application.setSDKEventMessage"')
        return self._extend_eval("setSDKEventMessage({}, {})".format(_format_object_to_es(value), _format_object_to_es(eventType)))

    def setScratchDiskPath(self, value, type):
        """
        :type value: str
        :type type: str
        """
        self.check_type(value, str, 'arg "value" of function "Application.setScratchDiskPath"')
        self.check_type(type, str, 'arg "type" of function "Application.setScratchDiskPath"')
        self._extend_eval("setScratchDiskPath({}, {})".format(_format_object_to_es(value), _format_object_to_es(type)))

    def broadcastPrefsChanged(self, preferencesThatChanged):
        """
        :type preferencesThatChanged: str
        """
        self.check_type(preferencesThatChanged, str, 'arg "preferencesThatChanged" of function "Application.broadcastPrefsChanged"')
        return self._extend_eval("broadcastPrefsChanged({})".format(_format_object_to_es(preferencesThatChanged)))

    def setExtensionPersistent(self, extensionID, state):
        """
        :type extensionID: str
        :type state: float
        """
        self.check_type(extensionID, str, 'arg "extensionID" of function "Application.setExtensionPersistent"')
        self.check_type(state, float, 'arg "state" of function "Application.setExtensionPersistent"')
        self._extend_eval("setExtensionPersistent({}, {})".format(_format_object_to_es(extensionID), _format_object_to_es(state)))

    def getEnableProxies(self):
        return self._extend_eval("getEnableProxies()")

    def setEnableProxies(self, enable):
        """
        :type enable: float
        """
        self.check_type(enable, float, 'arg "enable" of function "Application.setEnableProxies"')
        return self._extend_eval("setEnableProxies({})".format(_format_object_to_es(enable)))

    def showCursor(self, enable):
        """
        :type enable: bool
        """
        self.check_type(enable, bool, 'arg "enable" of function "Application.showCursor"')
        self._extend_eval("showCursor({})".format(_format_object_to_es(enable)))

    def getProjectViewIDs(self):
        self._extend_eval("getProjectViewIDs()")

    def getProjectFromViewID(self, viewID):
        """
        :type viewID: str
        """
        self.check_type(viewID, str, 'arg "viewID" of function "Application.getProjectFromViewID"')
        return Project(**self._extend_eval("getProjectFromViewID({})".format(_format_object_to_es(viewID))))

    def getProjectViewSelection(self, viewID):
        """
        :type viewID: str
        """
        self.check_type(viewID, str, 'arg "viewID" of function "Application.getProjectViewSelection"')
        self._extend_eval("getProjectViewSelection({})".format(_format_object_to_es(viewID)))

    def setProjectViewSelection(self, viewID):
        """
        :type viewID: str
        """
        self.check_type(viewID, str, 'arg "viewID" of function "Application.setProjectViewSelection"')
        self._extend_eval("setProjectViewSelection({})".format(_format_object_to_es(viewID)))

    def getConstant(self, name):
        """
        :type name: str
        """
        self.check_type(name, str, 'arg "name" of function "Application.getConstant"')
        return self._extend_eval("getConstant({})".format(_format_object_to_es(name)))

    def refresh(self):
        self._extend_eval("refresh()")

    def setEnableTranscodeOnIngest(self, inEnable):
        """
        :type inEnable: bool
        """
        self.check_type(inEnable, bool, 'arg "inEnable" of function "Application.setEnableTranscodeOnIngest"')
        self._extend_eval("setEnableTranscodeOnIngest({})".format(_format_object_to_es(inEnable)))

    def getCCXUserJSONData(self):
        return self._extend_eval("getCCXUserJSONData()")

    def enableQE(self):
        return self._extend_eval("enableQE()")

class Project(PymiereObject):
    def __init__(self, pymiere_id=None, documentID=None, name=None, path=None, rootItem=None, sequences=None, activeSequence=None, isCloudProject=None, cloudProjectLocalID=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'documentID':documentID, 'name':name, 'path':path, 'rootItem':rootItem, 'sequences':sequences, 'activeSequence':activeSequence, 'isCloudProject':isCloudProject, 'cloudProjectLocalID':cloudProjectLocalID})
        super(Project, self).__init__(pymiere_id)
        self.__documentID = documentID
        self.__name = name
        self.__path = path
        self.__rootItem = rootItem
        self.__sequences = sequences
        self.__activeSequence = activeSequence
        self.__isCloudProject = isCloudProject
        self.__cloudProjectLocalID = cloudProjectLocalID

    # ----- PROPERTIES -----
    @property
    def documentID(self):
        self.__documentID = self._extend_eval('documentID')
        return self.__documentID
    @documentID.setter
    def documentID(self, documentID):
        raise AttributeError("Attribute 'documentID' is read-only")

    @property
    def name(self):
        self.__name = self._extend_eval('name')
        return self.__name
    @name.setter
    def name(self, name):
        raise AttributeError("Attribute 'name' is read-only")

    @property
    def path(self):
        self.__path = self._extend_eval('path')
        return self.__path
    @path.setter
    def path(self, path):
        raise AttributeError("Attribute 'path' is read-only")

    @property
    def rootItem(self):
        self.__rootItem = ProjectItem(**self._extend_eval('rootItem'))
        return self.__rootItem
    @rootItem.setter
    def rootItem(self, rootItem):
        raise AttributeError("Attribute 'rootItem' is read-only")

    @property
    def sequences(self):
        self.__sequences = SequenceCollection(**self._extend_eval('sequences'))
        return self.__sequences
    @sequences.setter
    def sequences(self, sequences):
        raise AttributeError("Attribute 'sequences' is read-only")

    @property
    def activeSequence(self):
        self.__activeSequence = Sequence(**self._extend_eval('activeSequence'))
        return self.__activeSequence
    @activeSequence.setter
    def activeSequence(self, activeSequence):
        self.check_type(activeSequence, Sequence, 'Project.activeSequence')
        self._extend_eval("activeSequence = {}".format(_format_object_to_es(activeSequence)))
        self.__activeSequence = activeSequence

    @property
    def isCloudProject(self):
        self.__isCloudProject = self._extend_eval('isCloudProject')
        return self.__isCloudProject
    @isCloudProject.setter
    def isCloudProject(self, isCloudProject):
        raise AttributeError("Attribute 'isCloudProject' is read-only")

    @property
    def cloudProjectLocalID(self):
        self.__cloudProjectLocalID = self._extend_eval('cloudProjectLocalID')
        return self.__cloudProjectLocalID
    @cloudProjectLocalID.setter
    def cloudProjectLocalID(self, cloudProjectLocalID):
        raise AttributeError("Attribute 'cloudProjectLocalID' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Project.bind"')
        self.check_type(function, any, 'arg "function" of function "Project.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Project.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Project.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "Project.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "Project.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def openSequence(self, sequenceID):
        """
        :type sequenceID: str
        """
        self.check_type(sequenceID, str, 'arg "sequenceID" of function "Project.openSequence"')
        return self._extend_eval("openSequence({})".format(_format_object_to_es(sequenceID)))

    def importFiles(self, arg1):
        """
        :type arg1: any
        """
        self.check_type(arg1, any, 'arg "arg1" of function "Project.importFiles"')
        return self._extend_eval("importFiles({})".format(_format_object_to_es(arg1)))

    def importSequences(self, arg1):
        """
        :type arg1: any
        """
        self.check_type(arg1, any, 'arg "arg1" of function "Project.importSequences"')
        return self._extend_eval("importSequences({})".format(_format_object_to_es(arg1)))

    def importAllAEComps(self, arg1):
        """
        :type arg1: any
        """
        self.check_type(arg1, any, 'arg "arg1" of function "Project.importAllAEComps"')
        return self._extend_eval("importAllAEComps({})".format(_format_object_to_es(arg1)))

    def importAEComps(self, arg1):
        """
        :type arg1: any
        """
        self.check_type(arg1, any, 'arg "arg1" of function "Project.importAEComps"')
        return self._extend_eval("importAEComps({})".format(_format_object_to_es(arg1)))

    def createNewSequence(self, sequenceName, placeholderID):
        """
        :type sequenceName: str
        :type placeholderID: str
        """
        self.check_type(sequenceName, str, 'arg "sequenceName" of function "Project.createNewSequence"')
        self.check_type(placeholderID, str, 'arg "placeholderID" of function "Project.createNewSequence"')
        self._extend_eval("createNewSequence({}, {})".format(_format_object_to_es(sequenceName), _format_object_to_es(placeholderID)))

    def deleteSequence(self, sequence):
        """
        :type sequence: Sequence
        """
        self.check_type(sequence, Sequence, 'arg "sequence" of function "Project.deleteSequence"')
        return self._extend_eval("deleteSequence({})".format(_format_object_to_es(sequence)))

    def exportFinalCutProXML(self, exportPath, suppressUI):
        """
        :type exportPath: str
        :type suppressUI: float
        """
        self.check_type(exportPath, str, 'arg "exportPath" of function "Project.exportFinalCutProXML"')
        self.check_type(suppressUI, float, 'arg "suppressUI" of function "Project.exportFinalCutProXML"')
        return self._extend_eval("exportFinalCutProXML({}, {})".format(_format_object_to_es(exportPath), _format_object_to_es(suppressUI)))

    def exportTimeline(self, exportControllerName):
        """
        :type exportControllerName: str
        """
        self.check_type(exportControllerName, str, 'arg "exportControllerName" of function "Project.exportTimeline"')
        return self._extend_eval("exportTimeline({})".format(_format_object_to_es(exportControllerName)))

    def exportOMF(self, sequence, filePath, OMFTitle, sampleRate, bitsPerSample, audioEncapsulated, audioFileFormat, trimAudioFiles, handleFrames, includePan):
        """
        :type sequence: Sequence
        :type filePath: str
        :type OMFTitle: str
        :type sampleRate: float
        :type bitsPerSample: float
        :type audioEncapsulated: float
        :type audioFileFormat: float
        :type trimAudioFiles: float
        :type handleFrames: float
        :type includePan: float
        """
        self.check_type(sequence, Sequence, 'arg "sequence" of function "Project.exportOMF"')
        self.check_type(filePath, str, 'arg "filePath" of function "Project.exportOMF"')
        self.check_type(OMFTitle, str, 'arg "OMFTitle" of function "Project.exportOMF"')
        self.check_type(sampleRate, float, 'arg "sampleRate" of function "Project.exportOMF"')
        self.check_type(bitsPerSample, float, 'arg "bitsPerSample" of function "Project.exportOMF"')
        self.check_type(audioEncapsulated, float, 'arg "audioEncapsulated" of function "Project.exportOMF"')
        self.check_type(audioFileFormat, float, 'arg "audioFileFormat" of function "Project.exportOMF"')
        self.check_type(trimAudioFiles, float, 'arg "trimAudioFiles" of function "Project.exportOMF"')
        self.check_type(handleFrames, float, 'arg "handleFrames" of function "Project.exportOMF"')
        self.check_type(includePan, float, 'arg "includePan" of function "Project.exportOMF"')
        return self._extend_eval("exportOMF({}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(_format_object_to_es(sequence), _format_object_to_es(filePath), _format_object_to_es(OMFTitle), _format_object_to_es(sampleRate), _format_object_to_es(bitsPerSample), _format_object_to_es(audioEncapsulated), _format_object_to_es(audioFileFormat), _format_object_to_es(trimAudioFiles), _format_object_to_es(handleFrames), _format_object_to_es(includePan)))

    def exportAAF(self, sequence, filePath, mixDownVideo, explodeToMono, sampleRate, bitsPerSample, embedAudio, audioFileFormat, trimSources, handleFrames):
        """
        :type sequence: Sequence
        :type filePath: str
        :type mixDownVideo: float
        :type explodeToMono: float
        :type sampleRate: float
        :type bitsPerSample: float
        :type embedAudio: float
        :type audioFileFormat: float
        :type trimSources: float
        :type handleFrames: float
        """
        self.check_type(sequence, Sequence, 'arg "sequence" of function "Project.exportAAF"')
        self.check_type(filePath, str, 'arg "filePath" of function "Project.exportAAF"')
        self.check_type(mixDownVideo, float, 'arg "mixDownVideo" of function "Project.exportAAF"')
        self.check_type(explodeToMono, float, 'arg "explodeToMono" of function "Project.exportAAF"')
        self.check_type(sampleRate, float, 'arg "sampleRate" of function "Project.exportAAF"')
        self.check_type(bitsPerSample, float, 'arg "bitsPerSample" of function "Project.exportAAF"')
        self.check_type(embedAudio, float, 'arg "embedAudio" of function "Project.exportAAF"')
        self.check_type(audioFileFormat, float, 'arg "audioFileFormat" of function "Project.exportAAF"')
        self.check_type(trimSources, float, 'arg "trimSources" of function "Project.exportAAF"')
        self.check_type(handleFrames, float, 'arg "handleFrames" of function "Project.exportAAF"')
        return self._extend_eval("exportAAF({}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(_format_object_to_es(sequence), _format_object_to_es(filePath), _format_object_to_es(mixDownVideo), _format_object_to_es(explodeToMono), _format_object_to_es(sampleRate), _format_object_to_es(bitsPerSample), _format_object_to_es(embedAudio), _format_object_to_es(audioFileFormat), _format_object_to_es(trimSources), _format_object_to_es(handleFrames)))

    def saveAs(self, saveAsPath):
        """
        :type saveAsPath: str
        """
        self.check_type(saveAsPath, str, 'arg "saveAsPath" of function "Project.saveAs"')
        return self._extend_eval("saveAs({})".format(_format_object_to_es(saveAsPath)))

    def save(self):
        self._extend_eval("save()")

    def pauseGrowing(self, pausedOrNot):
        """
        :type pausedOrNot: float
        """
        self.check_type(pausedOrNot, float, 'arg "pausedOrNot" of function "Project.pauseGrowing"')
        return self._extend_eval("pauseGrowing({})".format(_format_object_to_es(pausedOrNot)))

    def closeDocument(self):
        return self._extend_eval("closeDocument()")

    def placeAsset(self, arg1):
        """
        :type arg1: any
        """
        self.check_type(arg1, any, 'arg "arg1" of function "Project.placeAsset"')
        return self._extend_eval("placeAsset({})".format(_format_object_to_es(arg1)))

    def addPropertyToProjectMetadataSchema(self, name, label, type):
        """
        :type name: str
        :type label: str
        :type type: float
        """
        self.check_type(name, str, 'arg "name" of function "Project.addPropertyToProjectMetadataSchema"')
        self.check_type(label, str, 'arg "label" of function "Project.addPropertyToProjectMetadataSchema"')
        self.check_type(type, float, 'arg "type" of function "Project.addPropertyToProjectMetadataSchema"')
        return self._extend_eval("addPropertyToProjectMetadataSchema({}, {}, {})".format(_format_object_to_es(name), _format_object_to_es(label), _format_object_to_es(type)))

    def getInsertionBin(self):
        return ProjectItem(**self._extend_eval("getInsertionBin()"))

    def getProjectPanelMetadata(self):
        self._extend_eval("getProjectPanelMetadata()")

    def setProjectPanelMetadata(self):
        self._extend_eval("setProjectPanelMetadata()")

    def setScratchDiskPath(self, value, type):
        """
        :type value: str
        :type type: str
        """
        self.check_type(value, str, 'arg "value" of function "Project.setScratchDiskPath"')
        self.check_type(type, str, 'arg "type" of function "Project.setScratchDiskPath"')
        self._extend_eval("setScratchDiskPath({}, {})".format(_format_object_to_es(value), _format_object_to_es(type)))

    def consolidateDuplicates(self):
        self._extend_eval("consolidateDuplicates()")

    def setEnableTranscodeOnIngest(self, inEnable):
        """
        :type inEnable: bool
        """
        self.check_type(inEnable, bool, 'arg "inEnable" of function "Project.setEnableTranscodeOnIngest"')
        return self._extend_eval("setEnableTranscodeOnIngest({})".format(_format_object_to_es(inEnable)))

class ProjectItem(PymiereObject):
    def __init__(self, pymiere_id=None, children=None, name=None, treePath=None, type=None, nodeId=None, videoComponents=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'children':children, 'name':name, 'treePath':treePath, 'type':type, 'nodeId':nodeId, 'videoComponents':videoComponents})
        super(ProjectItem, self).__init__(pymiere_id)
        self.__children = children
        self.__name = name
        self.__treePath = treePath
        self.__type = type
        self.__nodeId = nodeId
        self.__videoComponents = videoComponents

    # ----- PROPERTIES -----
    @property
    def children(self):
        self.__children = ProjectItemCollection(**self._extend_eval('children'))
        return self.__children
    @children.setter
    def children(self, children):
        raise AttributeError("Attribute 'children' is read-only")

    @property
    def name(self):
        self.__name = self._extend_eval('name')
        return self.__name
    @name.setter
    def name(self, name):
        self._extend_eval("name = {}".format(_format_object_to_es(name)))
        self.__name = name

    @property
    def treePath(self):
        self.__treePath = self._extend_eval('treePath')
        return self.__treePath
    @treePath.setter
    def treePath(self, treePath):
        raise AttributeError("Attribute 'treePath' is read-only")

    @property
    def type(self):
        self.__type = self._extend_eval('type')
        return self.__type
    @type.setter
    def type(self, type):
        raise AttributeError("Attribute 'type' is read-only")

    @property
    def nodeId(self):
        self.__nodeId = self._extend_eval('nodeId')
        return self.__nodeId
    @nodeId.setter
    def nodeId(self, nodeId):
        raise AttributeError("Attribute 'nodeId' is read-only")

    @property
    def videoComponents(self):
        self.__videoComponents = ComponentCollection(**self._extend_eval('videoComponents'))
        return self.__videoComponents
    @videoComponents.setter
    def videoComponents(self, videoComponents):
        raise AttributeError("Attribute 'videoComponents' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ProjectItem.bind"')
        self.check_type(function, any, 'arg "function" of function "ProjectItem.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ProjectItem.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ProjectItem.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "ProjectItem.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "ProjectItem.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def getFootageInterpretation(self):
        return FootageInterpretation(**self._extend_eval("getFootageInterpretation()"))

    def setFootageInterpretation(self, interpretFootage):
        """
        :type interpretFootage: FootageInterpretation
        """
        self.check_type(interpretFootage, FootageInterpretation, 'arg "interpretFootage" of function "ProjectItem.setFootageInterpretation"')
        return self._extend_eval("setFootageInterpretation({})".format(_format_object_to_es(interpretFootage)))

    def createSmartBin(self, name, query):
        """
        :type name: str
        :type query: str
        """
        self.check_type(name, str, 'arg "name" of function "ProjectItem.createSmartBin"')
        self.check_type(query, str, 'arg "query" of function "ProjectItem.createSmartBin"')
        self._extend_eval("createSmartBin({}, {})".format(_format_object_to_es(name), _format_object_to_es(query)))

    def createBin(self, name):
        """
        :type name: str
        """
        self.check_type(name, str, 'arg "name" of function "ProjectItem.createBin"')
        self._extend_eval("createBin({})".format(_format_object_to_es(name)))

    def renameBin(self, name):
        """
        :type name: str
        """
        self.check_type(name, str, 'arg "name" of function "ProjectItem.renameBin"')
        return self._extend_eval("renameBin({})".format(_format_object_to_es(name)))

    def deleteBin(self):
        self._extend_eval("deleteBin()")

    def moveBin(self, destination):
        """
        :type destination: ProjectItem
        """
        self.check_type(destination, ProjectItem, 'arg "destination" of function "ProjectItem.moveBin"')
        self._extend_eval("moveBin({})".format(_format_object_to_es(destination)))

    def getXMPMetadata(self):
        return self._extend_eval("getXMPMetadata()")

    def setXMPMetadata(self, buffer):
        """
        :type buffer: str
        """
        self.check_type(buffer, str, 'arg "buffer" of function "ProjectItem.setXMPMetadata"')
        return self._extend_eval("setXMPMetadata({})".format(_format_object_to_es(buffer)))

    def getProjectMetadata(self):
        return self._extend_eval("getProjectMetadata()")

    def setProjectMetadata(self, buffer):
        """
        :type buffer: str
        """
        self.check_type(buffer, str, 'arg "buffer" of function "ProjectItem.setProjectMetadata"')
        self._extend_eval("setProjectMetadata({})".format(_format_object_to_es(buffer)))

    def getMarkers(self):
        return MarkerCollection(**self._extend_eval("getMarkers()"))

    def refreshMedia(self):
        return self._extend_eval("refreshMedia()")

    def getMediaPath(self):
        return self._extend_eval("getMediaPath()")

    def canChangeMediaPath(self):
        return self._extend_eval("canChangeMediaPath()")

    def changeMediaPath(self, mediaPath, overrideChecks):
        """
        :type mediaPath: str
        :type overrideChecks: bool
        """
        self.check_type(mediaPath, str, 'arg "mediaPath" of function "ProjectItem.changeMediaPath"')
        self.check_type(overrideChecks, bool, 'arg "overrideChecks" of function "ProjectItem.changeMediaPath"')
        return self._extend_eval("changeMediaPath({}, {})".format(_format_object_to_es(mediaPath), _format_object_to_es(overrideChecks)))

    def select(self):
        self._extend_eval("select()")

    def setOverridePixelAspectRatio(self, numerator, denominator):
        """
        :type numerator: float
        :type denominator: float
        """
        self.check_type(numerator, float, 'arg "numerator" of function "ProjectItem.setOverridePixelAspectRatio"')
        self.check_type(denominator, float, 'arg "denominator" of function "ProjectItem.setOverridePixelAspectRatio"')
        return self._extend_eval("setOverridePixelAspectRatio({}, {})".format(_format_object_to_es(numerator), _format_object_to_es(denominator)))

    def setOverrideFrameRate(self, frameRate):
        """
        :type frameRate: float
        """
        self.check_type(frameRate, float, 'arg "frameRate" of function "ProjectItem.setOverrideFrameRate"')
        return self._extend_eval("setOverrideFrameRate({})".format(_format_object_to_es(frameRate)))

    def setScaleToFrameSize(self):
        self._extend_eval("setScaleToFrameSize()")

    def createSubClip(self, name, startTime, endTime, hasHardBoundaries, takeVideo, takeAudio):
        """
        :type name: str
        :type startTime: Object
        :type endTime: Object
        :type hasHardBoundaries: float
        :type takeVideo: float
        :type takeAudio: float
        """
        self.check_type(name, str, 'arg "name" of function "ProjectItem.createSubClip"')
        self.check_type(hasHardBoundaries, float, 'arg "hasHardBoundaries" of function "ProjectItem.createSubClip"')
        self.check_type(takeVideo, float, 'arg "takeVideo" of function "ProjectItem.createSubClip"')
        self.check_type(takeAudio, float, 'arg "takeAudio" of function "ProjectItem.createSubClip"')
        return ProjectItem(**self._extend_eval("createSubClip({}, {}, {}, {}, {}, {})".format(_format_object_to_es(name), _format_object_to_es(startTime), _format_object_to_es(endTime), _format_object_to_es(hasHardBoundaries), _format_object_to_es(takeVideo), _format_object_to_es(takeAudio))))

    def findItemsMatchingMediaPath(self, matchString, ignoreSubclips):
        """
        :type matchString: str
        :type ignoreSubclips: float
        """
        self.check_type(matchString, str, 'arg "matchString" of function "ProjectItem.findItemsMatchingMediaPath"')
        self.check_type(ignoreSubclips, float, 'arg "ignoreSubclips" of function "ProjectItem.findItemsMatchingMediaPath"')
        self._extend_eval("findItemsMatchingMediaPath({}, {})".format(_format_object_to_es(matchString), _format_object_to_es(ignoreSubclips)))

    def attachProxy(self, mediaPath, isHiRes):
        """
        :type mediaPath: str
        :type isHiRes: float
        """
        self.check_type(mediaPath, str, 'arg "mediaPath" of function "ProjectItem.attachProxy"')
        self.check_type(isHiRes, float, 'arg "isHiRes" of function "ProjectItem.attachProxy"')
        return self._extend_eval("attachProxy({}, {})".format(_format_object_to_es(mediaPath), _format_object_to_es(isHiRes)))

    def hasProxy(self):
        return self._extend_eval("hasProxy()")

    def getProxyPath(self):
        return self._extend_eval("getProxyPath()")

    def canProxy(self):
        return self._extend_eval("canProxy()")

    def isSequence(self):
        return self._extend_eval("isSequence()")

    def startTime(self):
        return Time(**self._extend_eval("startTime()"))

    def setStartTime(self, arg1):
        """
        :type arg1: Object
        """
        self._extend_eval("setStartTime({})".format(_format_object_to_es(arg1)))

    def clearInPoint(self, mediaType):
        """
        :type mediaType: float
        """
        self.check_type(mediaType, float, 'arg "mediaType" of function "ProjectItem.clearInPoint"')
        self._extend_eval("clearInPoint({})".format(_format_object_to_es(mediaType)))

    def setInPoint(self, arg1, mediaType):
        """
        :type arg1: Object
        :type mediaType: float
        """
        self.check_type(mediaType, float, 'arg "mediaType" of function "ProjectItem.setInPoint"')
        self._extend_eval("setInPoint({}, {})".format(_format_object_to_es(arg1), _format_object_to_es(mediaType)))

    def getInPoint(self, mediaType):
        """
        :type mediaType: float
        """
        self.check_type(mediaType, float, 'arg "mediaType" of function "ProjectItem.getInPoint"')
        return Time(**self._extend_eval("getInPoint({})".format(_format_object_to_es(mediaType))))

    def clearOutPoint(self, mediaType):
        """
        :type mediaType: float
        """
        self.check_type(mediaType, float, 'arg "mediaType" of function "ProjectItem.clearOutPoint"')
        self._extend_eval("clearOutPoint({})".format(_format_object_to_es(mediaType)))

    def setOutPoint(self, arg1, mediaType):
        """
        :type arg1: Object
        :type mediaType: float
        """
        self.check_type(mediaType, float, 'arg "mediaType" of function "ProjectItem.setOutPoint"')
        self._extend_eval("setOutPoint({}, {})".format(_format_object_to_es(arg1), _format_object_to_es(mediaType)))

    def getOutPoint(self, mediaType):
        """
        :type mediaType: float
        """
        self.check_type(mediaType, float, 'arg "mediaType" of function "ProjectItem.getOutPoint"')
        return Time(**self._extend_eval("getOutPoint({})".format(_format_object_to_es(mediaType))))

    def setColorLabel(self):
        self._extend_eval("setColorLabel()")

    def getColorLabel(self):
        return self._extend_eval("getColorLabel()")

    def isOffline(self):
        return self._extend_eval("isOffline()")

    def setOffline(self):
        return self._extend_eval("setOffline()")

    def saveProjectSnapshot(self):
        return self._extend_eval("saveProjectSnapshot()")

    def isAdjustmentLayer(self):
        return self._extend_eval("isAdjustmentLayer()")

    def isReference(self):
        return self._extend_eval("isReference()")

class ProjectItemCollection(PymiereCollection):
    def __init__(self, pymiere_id, numItems):
        super(ProjectItemCollection, self).__init__(pymiere_id, "numItems")

    def __getitem__(self, index):
        return ProjectItem(**super(ProjectItemCollection, self).__getitem__(index))

class SequenceCollection(PymiereCollection):
    def __init__(self, pymiere_id, numSequences):
        super(SequenceCollection, self).__init__(pymiere_id, "numSequences")

    def __getitem__(self, index):
        return Sequence(**super(SequenceCollection, self).__getitem__(index))

class Sequence(PymiereObject):
    def __init__(self, pymiere_id=None, id=None, sequenceID=None, name=None, audioTracks=None, videoTracks=None, frameSizeHorizontal=None, frameSizeVertical=None, timebase=None, zeroPoint=None, end=None, markers=None, projectItem=None, videoDisplayFormat=None, audioDisplayFormat=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'id':id, 'sequenceID':sequenceID, 'name':name, 'audioTracks':audioTracks, 'videoTracks':videoTracks, 'frameSizeHorizontal':frameSizeHorizontal, 'frameSizeVertical':frameSizeVertical, 'timebase':timebase, 'zeroPoint':zeroPoint, 'end':end, 'markers':markers, 'projectItem':projectItem, 'videoDisplayFormat':videoDisplayFormat, 'audioDisplayFormat':audioDisplayFormat})
        super(Sequence, self).__init__(pymiere_id)
        self.__id = id
        self.__sequenceID = sequenceID
        self.__name = name
        self.__audioTracks = audioTracks
        self.__videoTracks = videoTracks
        self.__frameSizeHorizontal = frameSizeHorizontal
        self.__frameSizeVertical = frameSizeVertical
        self.__timebase = timebase
        self.__zeroPoint = zeroPoint
        self.__end = end
        self.__markers = markers
        self.__projectItem = projectItem
        self.__videoDisplayFormat = videoDisplayFormat
        self.__audioDisplayFormat = audioDisplayFormat

    # ----- PROPERTIES -----
    @property
    def id(self):
        self.__id = self._extend_eval('id')
        return self.__id
    @id.setter
    def id(self, id):
        raise AttributeError("Attribute 'id' is read-only")

    @property
    def sequenceID(self):
        self.__sequenceID = self._extend_eval('sequenceID')
        return self.__sequenceID
    @sequenceID.setter
    def sequenceID(self, sequenceID):
        raise AttributeError("Attribute 'sequenceID' is read-only")

    @property
    def name(self):
        self.__name = self._extend_eval('name')
        return self.__name
    @name.setter
    def name(self, name):
        self._extend_eval("name = {}".format(_format_object_to_es(name)))
        self.__name = name

    @property
    def audioTracks(self):
        self.__audioTracks = TrackCollection(**self._extend_eval('audioTracks'))
        return self.__audioTracks
    @audioTracks.setter
    def audioTracks(self, audioTracks):
        raise AttributeError("Attribute 'audioTracks' is read-only")

    @property
    def videoTracks(self):
        self.__videoTracks = TrackCollection(**self._extend_eval('videoTracks'))
        return self.__videoTracks
    @videoTracks.setter
    def videoTracks(self, videoTracks):
        raise AttributeError("Attribute 'videoTracks' is read-only")

    @property
    def frameSizeHorizontal(self):
        self.__frameSizeHorizontal = self._extend_eval('frameSizeHorizontal')
        return self.__frameSizeHorizontal
    @frameSizeHorizontal.setter
    def frameSizeHorizontal(self, frameSizeHorizontal):
        raise AttributeError("Attribute 'frameSizeHorizontal' is read-only")

    @property
    def frameSizeVertical(self):
        self.__frameSizeVertical = self._extend_eval('frameSizeVertical')
        return self.__frameSizeVertical
    @frameSizeVertical.setter
    def frameSizeVertical(self, frameSizeVertical):
        raise AttributeError("Attribute 'frameSizeVertical' is read-only")

    @property
    def timebase(self):
        self.__timebase = self._extend_eval('timebase')
        return self.__timebase
    @timebase.setter
    def timebase(self, timebase):
        raise AttributeError("Attribute 'timebase' is read-only")

    @property
    def zeroPoint(self):
        self.__zeroPoint = self._extend_eval('zeroPoint')
        return self.__zeroPoint
    @zeroPoint.setter
    def zeroPoint(self, zeroPoint):
        raise AttributeError("Attribute 'zeroPoint' is read-only")

    @property
    def end(self):
        self.__end = self._extend_eval('end')
        return self.__end
    @end.setter
    def end(self, end):
        raise AttributeError("Attribute 'end' is read-only")

    @property
    def markers(self):
        self.__markers = MarkerCollection(**self._extend_eval('markers'))
        return self.__markers
    @markers.setter
    def markers(self, markers):
        raise AttributeError("Attribute 'markers' is read-only")

    @property
    def projectItem(self):
        self.__projectItem = ProjectItem(**self._extend_eval('projectItem'))
        return self.__projectItem
    @projectItem.setter
    def projectItem(self, projectItem):
        raise AttributeError("Attribute 'projectItem' is read-only")

    @property
    def videoDisplayFormat(self):
        self.__videoDisplayFormat = self._extend_eval('videoDisplayFormat')
        return self.__videoDisplayFormat
    @videoDisplayFormat.setter
    def videoDisplayFormat(self, videoDisplayFormat):
        self._extend_eval("videoDisplayFormat = {}".format(_format_object_to_es(videoDisplayFormat)))
        self.__videoDisplayFormat = videoDisplayFormat

    @property
    def audioDisplayFormat(self):
        self.__audioDisplayFormat = self._extend_eval('audioDisplayFormat')
        return self.__audioDisplayFormat
    @audioDisplayFormat.setter
    def audioDisplayFormat(self, audioDisplayFormat):
        self._extend_eval("audioDisplayFormat = {}".format(_format_object_to_es(audioDisplayFormat)))
        self.__audioDisplayFormat = audioDisplayFormat


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Sequence.bind"')
        self.check_type(function, any, 'arg "function" of function "Sequence.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Sequence.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Sequence.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "Sequence.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "Sequence.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def getPlayerPosition(self):
        return Time(**self._extend_eval("getPlayerPosition()"))

    def setPlayerPosition(self, pos):
        """
        :type pos: str
        """
        self.check_type(pos, str, 'arg "pos" of function "Sequence.setPlayerPosition"')
        self._extend_eval("setPlayerPosition({})".format(_format_object_to_es(pos)))

    def setInPoint(self, time):
        """
        :type time: Object
        """
        self._extend_eval("setInPoint({})".format(_format_object_to_es(time)))

    def setOutPoint(self, time):
        """
        :type time: Object
        """
        self._extend_eval("setOutPoint({})".format(_format_object_to_es(time)))

    def getInPoint(self):
        return self._extend_eval("getInPoint()")

    def getOutPoint(self):
        return self._extend_eval("getOutPoint()")

    def getInPointAsTime(self):
        return Time(**self._extend_eval("getInPointAsTime()"))

    def getOutPointAsTime(self):
        return Time(**self._extend_eval("getOutPointAsTime()"))

    def setWorkAreaInPoint(self, time):
        """
        :type time: Object
        """
        self._extend_eval("setWorkAreaInPoint({})".format(_format_object_to_es(time)))

    def setWorkAreaOutPoint(self, time):
        """
        :type time: Object
        """
        self._extend_eval("setWorkAreaOutPoint({})".format(_format_object_to_es(time)))

    def getWorkAreaInPoint(self):
        return self._extend_eval("getWorkAreaInPoint()")

    def getWorkAreaOutPoint(self):
        return self._extend_eval("getWorkAreaOutPoint()")

    def getWorkAreaInPointAsTime(self):
        return Time(**self._extend_eval("getWorkAreaInPointAsTime()"))

    def getWorkAreaOutPointAsTime(self):
        return Time(**self._extend_eval("getWorkAreaOutPointAsTime()"))

    def setZeroPoint(self, ticks):
        """
        :type ticks: str
        """
        self.check_type(ticks, str, 'arg "ticks" of function "Sequence.setZeroPoint"')
        self._extend_eval("setZeroPoint({})".format(_format_object_to_es(ticks)))

    def attachCustomProperty(self, propertyID, propertyValue):
        """
        :type propertyID: str
        :type propertyValue: str
        """
        self.check_type(propertyID, str, 'arg "propertyID" of function "Sequence.attachCustomProperty"')
        self.check_type(propertyValue, str, 'arg "propertyValue" of function "Sequence.attachCustomProperty"')
        self._extend_eval("attachCustomProperty({}, {})".format(_format_object_to_es(propertyID), _format_object_to_es(propertyValue)))

    def clone(self):
        self._extend_eval("clone()")

    def exportAsProject(self, exportPath):
        """
        :type exportPath: str
        """
        self.check_type(exportPath, str, 'arg "exportPath" of function "Sequence.exportAsProject"')
        self._extend_eval("exportAsProject({})".format(_format_object_to_es(exportPath)))

    def exportAsFinalCutProXML(self, exportPath, suppressUI):
        """
        :type exportPath: str
        :type suppressUI: float
        """
        self.check_type(exportPath, str, 'arg "exportPath" of function "Sequence.exportAsFinalCutProXML"')
        self.check_type(suppressUI, float, 'arg "suppressUI" of function "Sequence.exportAsFinalCutProXML"')
        return self._extend_eval("exportAsFinalCutProXML({}, {})".format(_format_object_to_es(exportPath), _format_object_to_es(suppressUI)))

    def exportAsMediaDirect(self, outputFilePath, presetPath, workAreaType):
        """
        :type outputFilePath: str
        :type presetPath: str
        :type workAreaType: float
        """
        self.check_type(outputFilePath, str, 'arg "outputFilePath" of function "Sequence.exportAsMediaDirect"')
        self.check_type(presetPath, str, 'arg "presetPath" of function "Sequence.exportAsMediaDirect"')
        self.check_type(workAreaType, float, 'arg "workAreaType" of function "Sequence.exportAsMediaDirect"')
        return self._extend_eval("exportAsMediaDirect({}, {}, {})".format(_format_object_to_es(outputFilePath), _format_object_to_es(presetPath), _format_object_to_es(workAreaType)))

    def getExportFileExtension(self, presetFilePath):
        """
        :type presetFilePath: str
        """
        self.check_type(presetFilePath, str, 'arg "presetFilePath" of function "Sequence.getExportFileExtension"')
        return self._extend_eval("getExportFileExtension({})".format(_format_object_to_es(presetFilePath)))

    def importMGT(self, path, time, videoTrackIndex, audioTrackIndex):
        """
        :type path: str
        :type time: Object
        :type videoTrackIndex: float
        :type audioTrackIndex: float
        """
        self.check_type(path, str, 'arg "path" of function "Sequence.importMGT"')
        self.check_type(videoTrackIndex, float, 'arg "videoTrackIndex" of function "Sequence.importMGT"')
        self.check_type(audioTrackIndex, float, 'arg "audioTrackIndex" of function "Sequence.importMGT"')
        return TrackItem(**self._extend_eval("importMGT({}, {}, {}, {})".format(_format_object_to_es(path), _format_object_to_es(time), _format_object_to_es(videoTrackIndex), _format_object_to_es(audioTrackIndex))))

    def importMGTFromLibrary(self, libraryName, mgtName, time, videoTrackIndex, audioTrackIndex):
        """
        :type libraryName: str
        :type mgtName: str
        :type time: Object
        :type videoTrackIndex: float
        :type audioTrackIndex: float
        """
        self.check_type(libraryName, str, 'arg "libraryName" of function "Sequence.importMGTFromLibrary"')
        self.check_type(mgtName, str, 'arg "mgtName" of function "Sequence.importMGTFromLibrary"')
        self.check_type(videoTrackIndex, float, 'arg "videoTrackIndex" of function "Sequence.importMGTFromLibrary"')
        self.check_type(audioTrackIndex, float, 'arg "audioTrackIndex" of function "Sequence.importMGTFromLibrary"')
        return TrackItem(**self._extend_eval("importMGTFromLibrary({}, {}, {}, {}, {})".format(_format_object_to_es(libraryName), _format_object_to_es(mgtName), _format_object_to_es(time), _format_object_to_es(videoTrackIndex), _format_object_to_es(audioTrackIndex))))

    def getSettings(self):
        return SequenceSettings(**self._extend_eval("getSettings()"))

    def setSettings(self, settings):
        """
        :type settings: SequenceSettings
        """
        self.check_type(settings, SequenceSettings, 'arg "settings" of function "Sequence.setSettings"')
        self._extend_eval("setSettings({})".format(_format_object_to_es(settings)))

    def getSelection(self):
        self._extend_eval("getSelection()")

    def setSelection(self):
        self._extend_eval("setSelection()")

    def linkSelection(self):
        return self._extend_eval("linkSelection()")

    def unlinkSelection(self):
        return self._extend_eval("unlinkSelection()")

    def insertClip(self, clipProjectItem, time, videoTrackIndex, audioTrackIndex):
        """
        :type clipProjectItem: ProjectItem
        :type time: Object
        :type videoTrackIndex: float
        :type audioTrackIndex: float
        """
        self.check_type(clipProjectItem, ProjectItem, 'arg "clipProjectItem" of function "Sequence.insertClip"')
        self.check_type(videoTrackIndex, float, 'arg "videoTrackIndex" of function "Sequence.insertClip"')
        self.check_type(audioTrackIndex, float, 'arg "audioTrackIndex" of function "Sequence.insertClip"')
        self._extend_eval("insertClip({}, {}, {}, {})".format(_format_object_to_es(clipProjectItem), _format_object_to_es(time), _format_object_to_es(videoTrackIndex), _format_object_to_es(audioTrackIndex)))

    def overwriteClip(self, clipProjectItem, time, videoTrackIndex, audioTrackIndex):
        """
        :type clipProjectItem: ProjectItem
        :type time: Object
        :type videoTrackIndex: float
        :type audioTrackIndex: float
        """
        self.check_type(clipProjectItem, ProjectItem, 'arg "clipProjectItem" of function "Sequence.overwriteClip"')
        self.check_type(videoTrackIndex, float, 'arg "videoTrackIndex" of function "Sequence.overwriteClip"')
        self.check_type(audioTrackIndex, float, 'arg "audioTrackIndex" of function "Sequence.overwriteClip"')
        self._extend_eval("overwriteClip({}, {}, {}, {})".format(_format_object_to_es(clipProjectItem), _format_object_to_es(time), _format_object_to_es(videoTrackIndex), _format_object_to_es(audioTrackIndex)))

    def close(self):
        self._extend_eval("close()")

    def createSubsequence(self, ignoreTrackTargeting):
        """
        :type ignoreTrackTargeting: bool
        """
        self.check_type(ignoreTrackTargeting, bool, 'arg "ignoreTrackTargeting" of function "Sequence.createSubsequence"')
        return Sequence(**self._extend_eval("createSubsequence({})".format(_format_object_to_es(ignoreTrackTargeting))))

    def isWorkAreaEnabled(self):
        return self._extend_eval("isWorkAreaEnabled()")

    def setWorkAreaEnabled(self, specifiedState):
        """
        :type specifiedState: float
        """
        self.check_type(specifiedState, float, 'arg "specifiedState" of function "Sequence.setWorkAreaEnabled"')
        return self._extend_eval("setWorkAreaEnabled({})".format(_format_object_to_es(specifiedState)))

class TrackCollection(PymiereCollection):
    def __init__(self, pymiere_id, numTracks):
        super(TrackCollection, self).__init__(pymiere_id, "numTracks")

    def __getitem__(self, index):
        return Track(**super(TrackCollection, self).__getitem__(index))

class MarkerCollection(PymiereObject):
    def __init__(self, pymiere_id=None, numMarkers=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'numMarkers':numMarkers})
        super(MarkerCollection, self).__init__(pymiere_id)
        self.__numMarkers = numMarkers

    # ----- PROPERTIES -----
    @property
    def numMarkers(self):
        self.__numMarkers = self._extend_eval('numMarkers')
        return self.__numMarkers
    @numMarkers.setter
    def numMarkers(self, numMarkers):
        raise AttributeError("Attribute 'numMarkers' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "MarkerCollection.bind"')
        self.check_type(function, any, 'arg "function" of function "MarkerCollection.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "MarkerCollection.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "MarkerCollection.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "MarkerCollection.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "MarkerCollection.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def createMarker(self, time):
        """
        :type time: float
        """
        self.check_type(time, float, 'arg "time" of function "MarkerCollection.createMarker"')
        return Marker(**self._extend_eval("createMarker({})".format(_format_object_to_es(time))))

    def deleteMarker(self, marker):
        """
        :type marker: Marker
        """
        self.check_type(marker, Marker, 'arg "marker" of function "MarkerCollection.deleteMarker"')
        self._extend_eval("deleteMarker({})".format(_format_object_to_es(marker)))

    def getFirstMarker(self):
        return Marker(**self._extend_eval("getFirstMarker()"))

    def getLastMarker(self):
        return Marker(**self._extend_eval("getLastMarker()"))

    def getPrevMarker(self, marker):
        """
        :type marker: Marker
        """
        self.check_type(marker, Marker, 'arg "marker" of function "MarkerCollection.getPrevMarker"')
        return Marker(**self._extend_eval("getPrevMarker({})".format(_format_object_to_es(marker))))

    def getNextMarker(self, marker):
        """
        :type marker: Marker
        """
        self.check_type(marker, Marker, 'arg "marker" of function "MarkerCollection.getNextMarker"')
        return Marker(**self._extend_eval("getNextMarker({})".format(_format_object_to_es(marker))))

class ComponentCollection(PymiereCollection):
    def __init__(self, pymiere_id, numItems):
        super(ComponentCollection, self).__init__(pymiere_id, "numItems")

    def __getitem__(self, index):
        return Component(**super(ComponentCollection, self).__getitem__(index))

class ProjectCollection(PymiereCollection):
    def __init__(self, pymiere_id, numProjects):
        super(ProjectCollection, self).__init__(pymiere_id, "numProjects")

    def __getitem__(self, index):
        return Project(**super(ProjectCollection, self).__getitem__(index))

class Anywhere(PymiereObject):
    def __init__(self, pymiere_id=None, ):
        self.check_init_args({'pymiere_id':pymiere_id, })
        super(Anywhere, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Anywhere.bind"')
        self.check_type(function, any, 'arg "function" of function "Anywhere.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Anywhere.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Anywhere.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "Anywhere.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "Anywhere.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def setAuthenticationToken(self, inAuthToken, inEmail):
        """
        :type inAuthToken: str
        :type inEmail: str
        """
        self.check_type(inAuthToken, str, 'arg "inAuthToken" of function "Anywhere.setAuthenticationToken"')
        self.check_type(inEmail, str, 'arg "inEmail" of function "Anywhere.setAuthenticationToken"')
        return self._extend_eval("setAuthenticationToken({}, {})".format(_format_object_to_es(inAuthToken), _format_object_to_es(inEmail)))

    def getAuthenticationToken(self):
        return self._extend_eval("getAuthenticationToken()")

    def listProductions(self):
        return _format_object_to_py(self._extend_eval("listProductions()"))

    def openProduction(self, inProductionURL):
        """
        :type inProductionURL: str
        """
        self.check_type(inProductionURL, str, 'arg "inProductionURL" of function "Anywhere.openProduction"')
        return self._extend_eval("openProduction({})".format(_format_object_to_es(inProductionURL)))

    def openTeamProjectSnapshot(self, inTeamProjectSnapshotPath):
        """
        :type inTeamProjectSnapshotPath: str
        """
        self.check_type(inTeamProjectSnapshotPath, str, 'arg "inTeamProjectSnapshotPath" of function "Anywhere.openTeamProjectSnapshot"')
        return self._extend_eval("openTeamProjectSnapshot({})".format(_format_object_to_es(inTeamProjectSnapshotPath)))

    def isProductionOpen(self):
        return self._extend_eval("isProductionOpen()")

    def getCurrentEditingSessionURL(self):
        return self._extend_eval("getCurrentEditingSessionURL()")

    def getCurrentEditingSessionSelectionURL(self):
        return self._extend_eval("getCurrentEditingSessionSelectionURL()")

    def getCurrentEditingSessionActiveSequenceURL(self):
        return self._extend_eval("getCurrentEditingSessionActiveSequenceURL()")

class Encoder(PymiereObject):
    def __init__(self, pymiere_id=None, ENCODE_ENTIRE=None, ENCODE_IN_TO_OUT=None, ENCODE_WORKAREA=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'ENCODE_ENTIRE':ENCODE_ENTIRE, 'ENCODE_IN_TO_OUT':ENCODE_IN_TO_OUT, 'ENCODE_WORKAREA':ENCODE_WORKAREA})
        super(Encoder, self).__init__(pymiere_id)
        self.__ENCODE_ENTIRE = ENCODE_ENTIRE
        self.__ENCODE_IN_TO_OUT = ENCODE_IN_TO_OUT
        self.__ENCODE_WORKAREA = ENCODE_WORKAREA

    # ----- PROPERTIES -----
    @property
    def ENCODE_ENTIRE(self):
        self.__ENCODE_ENTIRE = self._extend_eval('ENCODE_ENTIRE')
        return self.__ENCODE_ENTIRE
    @ENCODE_ENTIRE.setter
    def ENCODE_ENTIRE(self, ENCODE_ENTIRE):
        raise AttributeError("Attribute 'ENCODE_ENTIRE' is read-only")

    @property
    def ENCODE_IN_TO_OUT(self):
        self.__ENCODE_IN_TO_OUT = self._extend_eval('ENCODE_IN_TO_OUT')
        return self.__ENCODE_IN_TO_OUT
    @ENCODE_IN_TO_OUT.setter
    def ENCODE_IN_TO_OUT(self, ENCODE_IN_TO_OUT):
        raise AttributeError("Attribute 'ENCODE_IN_TO_OUT' is read-only")

    @property
    def ENCODE_WORKAREA(self):
        self.__ENCODE_WORKAREA = self._extend_eval('ENCODE_WORKAREA')
        return self.__ENCODE_WORKAREA
    @ENCODE_WORKAREA.setter
    def ENCODE_WORKAREA(self, ENCODE_WORKAREA):
        raise AttributeError("Attribute 'ENCODE_WORKAREA' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Encoder.bind"')
        self.check_type(function, any, 'arg "function" of function "Encoder.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Encoder.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Encoder.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "Encoder.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "Encoder.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def encodeSequence(self, sequence, outputFilePath, presetPath, WorkAreaType, removeOnCompletion, startQueueImmediately):
        """
        :type sequence: Sequence
        :type outputFilePath: str
        :type presetPath: str
        :type WorkAreaType: float
        :type removeOnCompletion: float
        :type startQueueImmediately: float
        """
        self.check_type(sequence, Sequence, 'arg "sequence" of function "Encoder.encodeSequence"')
        self.check_type(outputFilePath, str, 'arg "outputFilePath" of function "Encoder.encodeSequence"')
        self.check_type(presetPath, str, 'arg "presetPath" of function "Encoder.encodeSequence"')
        self.check_type(WorkAreaType, float, 'arg "WorkAreaType" of function "Encoder.encodeSequence"')
        self.check_type(removeOnCompletion, float, 'arg "removeOnCompletion" of function "Encoder.encodeSequence"')
        self.check_type(startQueueImmediately, float, 'arg "startQueueImmediately" of function "Encoder.encodeSequence"')
        return self._extend_eval("encodeSequence({}, {}, {}, {}, {}, {})".format(_format_object_to_es(sequence), _format_object_to_es(outputFilePath), _format_object_to_es(presetPath), _format_object_to_es(WorkAreaType), _format_object_to_es(removeOnCompletion), _format_object_to_es(startQueueImmediately)))

    def encodeProjectItem(self, projectItem, outputFilePath, presetPath, WorkAreaType, removeOnCompletion, startQueueImmediately):
        """
        :type projectItem: ProjectItem
        :type outputFilePath: str
        :type presetPath: str
        :type WorkAreaType: float
        :type removeOnCompletion: float
        :type startQueueImmediately: float
        """
        self.check_type(projectItem, ProjectItem, 'arg "projectItem" of function "Encoder.encodeProjectItem"')
        self.check_type(outputFilePath, str, 'arg "outputFilePath" of function "Encoder.encodeProjectItem"')
        self.check_type(presetPath, str, 'arg "presetPath" of function "Encoder.encodeProjectItem"')
        self.check_type(WorkAreaType, float, 'arg "WorkAreaType" of function "Encoder.encodeProjectItem"')
        self.check_type(removeOnCompletion, float, 'arg "removeOnCompletion" of function "Encoder.encodeProjectItem"')
        self.check_type(startQueueImmediately, float, 'arg "startQueueImmediately" of function "Encoder.encodeProjectItem"')
        return self._extend_eval("encodeProjectItem({}, {}, {}, {}, {}, {})".format(_format_object_to_es(projectItem), _format_object_to_es(outputFilePath), _format_object_to_es(presetPath), _format_object_to_es(WorkAreaType), _format_object_to_es(removeOnCompletion), _format_object_to_es(startQueueImmediately)))

    def encodeFile(self, inputFilePath, outputFilePath, presetPath, removeOnCompletion, startTime, stopTime, startQueueImmediately):
        """
        :type inputFilePath: str
        :type outputFilePath: str
        :type presetPath: str
        :type removeOnCompletion: float
        :type startTime: Object
        :type stopTime: Object
        :type startQueueImmediately: float
        """
        self.check_type(inputFilePath, str, 'arg "inputFilePath" of function "Encoder.encodeFile"')
        self.check_type(outputFilePath, str, 'arg "outputFilePath" of function "Encoder.encodeFile"')
        self.check_type(presetPath, str, 'arg "presetPath" of function "Encoder.encodeFile"')
        self.check_type(removeOnCompletion, float, 'arg "removeOnCompletion" of function "Encoder.encodeFile"')
        self.check_type(startQueueImmediately, float, 'arg "startQueueImmediately" of function "Encoder.encodeFile"')
        return self._extend_eval("encodeFile({}, {}, {}, {}, {}, {}, {})".format(_format_object_to_es(inputFilePath), _format_object_to_es(outputFilePath), _format_object_to_es(presetPath), _format_object_to_es(removeOnCompletion), _format_object_to_es(startTime), _format_object_to_es(stopTime), _format_object_to_es(startQueueImmediately)))

    def startBatch(self):
        return self._extend_eval("startBatch()")

    def launchEncoder(self):
        return self._extend_eval("launchEncoder()")

    def setSidecarXMPEnabled(self, enable):
        """
        :type enable: float
        """
        self.check_type(enable, float, 'arg "enable" of function "Encoder.setSidecarXMPEnabled"')
        self._extend_eval("setSidecarXMPEnabled({})".format(_format_object_to_es(enable)))

    def setEmbeddedXMPEnabled(self, enable):
        """
        :type enable: float
        """
        self.check_type(enable, float, 'arg "enable" of function "Encoder.setEmbeddedXMPEnabled"')
        self._extend_eval("setEmbeddedXMPEnabled({})".format(_format_object_to_es(enable)))

    def getExporters(self):
        self._extend_eval("getExporters()")

class Properties(PymiereObject):
    def __init__(self, pymiere_id=None, ):
        self.check_init_args({'pymiere_id':pymiere_id, })
        super(Properties, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Properties.bind"')
        self.check_type(function, any, 'arg "function" of function "Properties.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Properties.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Properties.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "Properties.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "Properties.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def doesPropertyExist(self, propertyKey):
        """
        :type propertyKey: str
        """
        self.check_type(propertyKey, str, 'arg "propertyKey" of function "Properties.doesPropertyExist"')
        return self._extend_eval("doesPropertyExist({})".format(_format_object_to_es(propertyKey)))

    def isPropertyReadOnly(self, propertyKey):
        """
        :type propertyKey: str
        """
        self.check_type(propertyKey, str, 'arg "propertyKey" of function "Properties.isPropertyReadOnly"')
        return self._extend_eval("isPropertyReadOnly({})".format(_format_object_to_es(propertyKey)))

    def clearProperty(self, propertyKey):
        """
        :type propertyKey: str
        """
        self.check_type(propertyKey, str, 'arg "propertyKey" of function "Properties.clearProperty"')
        self._extend_eval("clearProperty({})".format(_format_object_to_es(propertyKey)))

    def setProperty(self, propertyKey):
        """
        :type propertyKey: str
        """
        self.check_type(propertyKey, str, 'arg "propertyKey" of function "Properties.setProperty"')
        self._extend_eval("setProperty({})".format(_format_object_to_es(propertyKey)))

    def getProperty(self, propertyKey):
        """
        :type propertyKey: str
        """
        self.check_type(propertyKey, str, 'arg "propertyKey" of function "Properties.getProperty"')
        self._extend_eval("getProperty({})".format(_format_object_to_es(propertyKey)))

class SourceMonitor(PymiereObject):
    def __init__(self, pymiere_id=None, ):
        self.check_init_args({'pymiere_id':pymiere_id, })
        super(SourceMonitor, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "SourceMonitor.bind"')
        self.check_type(function, any, 'arg "function" of function "SourceMonitor.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "SourceMonitor.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "SourceMonitor.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "SourceMonitor.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "SourceMonitor.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def openFilePath(self, filePath):
        """
        :type filePath: str
        """
        self.check_type(filePath, str, 'arg "filePath" of function "SourceMonitor.openFilePath"')
        return self._extend_eval("openFilePath({})".format(_format_object_to_es(filePath)))

    def openProjectItem(self, projectItem):
        """
        :type projectItem: ProjectItem
        """
        self.check_type(projectItem, ProjectItem, 'arg "projectItem" of function "SourceMonitor.openProjectItem"')
        return self._extend_eval("openProjectItem({})".format(_format_object_to_es(projectItem)))

    def play(self, speed):
        """
        :type speed: float
        """
        self.check_type(speed, float, 'arg "speed" of function "SourceMonitor.play"')
        self._extend_eval("play({})".format(_format_object_to_es(speed)))

    def closeClip(self):
        self._extend_eval("closeClip()")

    def closeAllClips(self):
        self._extend_eval("closeAllClips()")

    def getPosition(self):
        return Time(**self._extend_eval("getPosition()"))

    def getProjectItem(self):
        return ProjectItem(**self._extend_eval("getProjectItem()"))

class ProjectManager(PymiereObject):
    def __init__(self, pymiere_id=None, options=None, errors=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'options':options, 'errors':errors})
        super(ProjectManager, self).__init__(pymiere_id)
        self.__options = options
        self.__errors = errors

    # ----- PROPERTIES -----
    @property
    def options(self):
        self.__options = ProjectManagerOptions(**self._extend_eval('options'))
        return self.__options
    @options.setter
    def options(self, options):
        raise AttributeError("Attribute 'options' is read-only")

    @property
    def errors(self):
        self.__errors = self._extend_eval('errors')
        return self.__errors
    @errors.setter
    def errors(self, errors):
        raise AttributeError("Attribute 'errors' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ProjectManager.bind"')
        self.check_type(function, any, 'arg "function" of function "ProjectManager.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ProjectManager.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ProjectManager.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "ProjectManager.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "ProjectManager.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def process(self, project):
        """
        :type project: Project
        """
        self.check_type(project, Project, 'arg "project" of function "ProjectManager.process"')
        return self._extend_eval("process({})".format(_format_object_to_es(project)))

class ProjectManagerOptions(PymiereObject):
    def __init__(self, pymiere_id=None, clipTransferOption=None, clipTranscoderOption=None, excludeUnused=None, handleFrameCount=None, includePreviews=None, includeConformedAudio=None, renameMedia=None, destinationPath=None, includeAllSequences=None, affectedSequences=None, encoderPresetFilePath=None, convertImageSequencesToClips=None, convertSyntheticsToClips=None, convertAECompsToClips=None, copyToPreventAlphaLoss=None, CLIP_TRANSFER_COPY=None, CLIP_TRANSFER_TRANSCODE=None, CLIP_TRANSCODE_MATCH_PRESET=None, CLIP_TRANSCODE_MATCH_CLIPS=None, CLIP_TRANSCODE_MATCH_SEQUENCE=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'clipTransferOption':clipTransferOption, 'clipTranscoderOption':clipTranscoderOption, 'excludeUnused':excludeUnused, 'handleFrameCount':handleFrameCount, 'includePreviews':includePreviews, 'includeConformedAudio':includeConformedAudio, 'renameMedia':renameMedia, 'destinationPath':destinationPath, 'includeAllSequences':includeAllSequences, 'affectedSequences':affectedSequences, 'encoderPresetFilePath':encoderPresetFilePath, 'convertImageSequencesToClips':convertImageSequencesToClips, 'convertSyntheticsToClips':convertSyntheticsToClips, 'convertAECompsToClips':convertAECompsToClips, 'copyToPreventAlphaLoss':copyToPreventAlphaLoss, 'CLIP_TRANSFER_COPY':CLIP_TRANSFER_COPY, 'CLIP_TRANSFER_TRANSCODE':CLIP_TRANSFER_TRANSCODE, 'CLIP_TRANSCODE_MATCH_PRESET':CLIP_TRANSCODE_MATCH_PRESET, 'CLIP_TRANSCODE_MATCH_CLIPS':CLIP_TRANSCODE_MATCH_CLIPS, 'CLIP_TRANSCODE_MATCH_SEQUENCE':CLIP_TRANSCODE_MATCH_SEQUENCE})
        super(ProjectManagerOptions, self).__init__(pymiere_id)
        self.__clipTransferOption = clipTransferOption
        self.__clipTranscoderOption = clipTranscoderOption
        self.__excludeUnused = excludeUnused
        self.__handleFrameCount = handleFrameCount
        self.__includePreviews = includePreviews
        self.__includeConformedAudio = includeConformedAudio
        self.__renameMedia = renameMedia
        self.__destinationPath = destinationPath
        self.__includeAllSequences = includeAllSequences
        self.__affectedSequences = affectedSequences
        self.__encoderPresetFilePath = encoderPresetFilePath
        self.__convertImageSequencesToClips = convertImageSequencesToClips
        self.__convertSyntheticsToClips = convertSyntheticsToClips
        self.__convertAECompsToClips = convertAECompsToClips
        self.__copyToPreventAlphaLoss = copyToPreventAlphaLoss
        self.__CLIP_TRANSFER_COPY = CLIP_TRANSFER_COPY
        self.__CLIP_TRANSFER_TRANSCODE = CLIP_TRANSFER_TRANSCODE
        self.__CLIP_TRANSCODE_MATCH_PRESET = CLIP_TRANSCODE_MATCH_PRESET
        self.__CLIP_TRANSCODE_MATCH_CLIPS = CLIP_TRANSCODE_MATCH_CLIPS
        self.__CLIP_TRANSCODE_MATCH_SEQUENCE = CLIP_TRANSCODE_MATCH_SEQUENCE

    # ----- PROPERTIES -----
    @property
    def clipTransferOption(self):
        self.__clipTransferOption = self._extend_eval('clipTransferOption')
        return self.__clipTransferOption
    @clipTransferOption.setter
    def clipTransferOption(self, clipTransferOption):
        self._extend_eval("clipTransferOption = {}".format(_format_object_to_es(clipTransferOption)))
        self.__clipTransferOption = clipTransferOption

    @property
    def clipTranscoderOption(self):
        self.__clipTranscoderOption = self._extend_eval('clipTranscoderOption')
        return self.__clipTranscoderOption
    @clipTranscoderOption.setter
    def clipTranscoderOption(self, clipTranscoderOption):
        self._extend_eval("clipTranscoderOption = {}".format(_format_object_to_es(clipTranscoderOption)))
        self.__clipTranscoderOption = clipTranscoderOption

    @property
    def excludeUnused(self):
        self.__excludeUnused = self._extend_eval('excludeUnused')
        return self.__excludeUnused
    @excludeUnused.setter
    def excludeUnused(self, excludeUnused):
        self._extend_eval("excludeUnused = {}".format(_format_object_to_es(excludeUnused)))
        self.__excludeUnused = excludeUnused

    @property
    def handleFrameCount(self):
        self.__handleFrameCount = self._extend_eval('handleFrameCount')
        return self.__handleFrameCount
    @handleFrameCount.setter
    def handleFrameCount(self, handleFrameCount):
        self._extend_eval("handleFrameCount = {}".format(_format_object_to_es(handleFrameCount)))
        self.__handleFrameCount = handleFrameCount

    @property
    def includePreviews(self):
        self.__includePreviews = self._extend_eval('includePreviews')
        return self.__includePreviews
    @includePreviews.setter
    def includePreviews(self, includePreviews):
        self._extend_eval("includePreviews = {}".format(_format_object_to_es(includePreviews)))
        self.__includePreviews = includePreviews

    @property
    def includeConformedAudio(self):
        self.__includeConformedAudio = self._extend_eval('includeConformedAudio')
        return self.__includeConformedAudio
    @includeConformedAudio.setter
    def includeConformedAudio(self, includeConformedAudio):
        self._extend_eval("includeConformedAudio = {}".format(_format_object_to_es(includeConformedAudio)))
        self.__includeConformedAudio = includeConformedAudio

    @property
    def renameMedia(self):
        self.__renameMedia = self._extend_eval('renameMedia')
        return self.__renameMedia
    @renameMedia.setter
    def renameMedia(self, renameMedia):
        self._extend_eval("renameMedia = {}".format(_format_object_to_es(renameMedia)))
        self.__renameMedia = renameMedia

    @property
    def destinationPath(self):
        self.__destinationPath = self._extend_eval('destinationPath')
        return self.__destinationPath
    @destinationPath.setter
    def destinationPath(self, destinationPath):
        self._extend_eval("destinationPath = {}".format(_format_object_to_es(destinationPath)))
        self.__destinationPath = destinationPath

    @property
    def includeAllSequences(self):
        self.__includeAllSequences = self._extend_eval('includeAllSequences')
        return self.__includeAllSequences
    @includeAllSequences.setter
    def includeAllSequences(self, includeAllSequences):
        self._extend_eval("includeAllSequences = {}".format(_format_object_to_es(includeAllSequences)))
        self.__includeAllSequences = includeAllSequences

    @property
    def affectedSequences(self):
        self.__affectedSequences = self._extend_eval('affectedSequences')
        return self.__affectedSequences
    @affectedSequences.setter
    def affectedSequences(self, affectedSequences):
        self._extend_eval("affectedSequences = {}".format(_format_object_to_es(affectedSequences)))
        self.__affectedSequences = affectedSequences

    @property
    def encoderPresetFilePath(self):
        self.__encoderPresetFilePath = self._extend_eval('encoderPresetFilePath')
        return self.__encoderPresetFilePath
    @encoderPresetFilePath.setter
    def encoderPresetFilePath(self, encoderPresetFilePath):
        self._extend_eval("encoderPresetFilePath = {}".format(_format_object_to_es(encoderPresetFilePath)))
        self.__encoderPresetFilePath = encoderPresetFilePath

    @property
    def convertImageSequencesToClips(self):
        self.__convertImageSequencesToClips = self._extend_eval('convertImageSequencesToClips')
        return self.__convertImageSequencesToClips
    @convertImageSequencesToClips.setter
    def convertImageSequencesToClips(self, convertImageSequencesToClips):
        self._extend_eval("convertImageSequencesToClips = {}".format(_format_object_to_es(convertImageSequencesToClips)))
        self.__convertImageSequencesToClips = convertImageSequencesToClips

    @property
    def convertSyntheticsToClips(self):
        self.__convertSyntheticsToClips = self._extend_eval('convertSyntheticsToClips')
        return self.__convertSyntheticsToClips
    @convertSyntheticsToClips.setter
    def convertSyntheticsToClips(self, convertSyntheticsToClips):
        self._extend_eval("convertSyntheticsToClips = {}".format(_format_object_to_es(convertSyntheticsToClips)))
        self.__convertSyntheticsToClips = convertSyntheticsToClips

    @property
    def convertAECompsToClips(self):
        self.__convertAECompsToClips = self._extend_eval('convertAECompsToClips')
        return self.__convertAECompsToClips
    @convertAECompsToClips.setter
    def convertAECompsToClips(self, convertAECompsToClips):
        self._extend_eval("convertAECompsToClips = {}".format(_format_object_to_es(convertAECompsToClips)))
        self.__convertAECompsToClips = convertAECompsToClips

    @property
    def copyToPreventAlphaLoss(self):
        self.__copyToPreventAlphaLoss = self._extend_eval('copyToPreventAlphaLoss')
        return self.__copyToPreventAlphaLoss
    @copyToPreventAlphaLoss.setter
    def copyToPreventAlphaLoss(self, copyToPreventAlphaLoss):
        self._extend_eval("copyToPreventAlphaLoss = {}".format(_format_object_to_es(copyToPreventAlphaLoss)))
        self.__copyToPreventAlphaLoss = copyToPreventAlphaLoss

    @property
    def CLIP_TRANSFER_COPY(self):
        self.__CLIP_TRANSFER_COPY = self._extend_eval('CLIP_TRANSFER_COPY')
        return self.__CLIP_TRANSFER_COPY
    @CLIP_TRANSFER_COPY.setter
    def CLIP_TRANSFER_COPY(self, CLIP_TRANSFER_COPY):
        raise AttributeError("Attribute 'CLIP_TRANSFER_COPY' is read-only")

    @property
    def CLIP_TRANSFER_TRANSCODE(self):
        self.__CLIP_TRANSFER_TRANSCODE = self._extend_eval('CLIP_TRANSFER_TRANSCODE')
        return self.__CLIP_TRANSFER_TRANSCODE
    @CLIP_TRANSFER_TRANSCODE.setter
    def CLIP_TRANSFER_TRANSCODE(self, CLIP_TRANSFER_TRANSCODE):
        raise AttributeError("Attribute 'CLIP_TRANSFER_TRANSCODE' is read-only")

    @property
    def CLIP_TRANSCODE_MATCH_PRESET(self):
        self.__CLIP_TRANSCODE_MATCH_PRESET = self._extend_eval('CLIP_TRANSCODE_MATCH_PRESET')
        return self.__CLIP_TRANSCODE_MATCH_PRESET
    @CLIP_TRANSCODE_MATCH_PRESET.setter
    def CLIP_TRANSCODE_MATCH_PRESET(self, CLIP_TRANSCODE_MATCH_PRESET):
        raise AttributeError("Attribute 'CLIP_TRANSCODE_MATCH_PRESET' is read-only")

    @property
    def CLIP_TRANSCODE_MATCH_CLIPS(self):
        self.__CLIP_TRANSCODE_MATCH_CLIPS = self._extend_eval('CLIP_TRANSCODE_MATCH_CLIPS')
        return self.__CLIP_TRANSCODE_MATCH_CLIPS
    @CLIP_TRANSCODE_MATCH_CLIPS.setter
    def CLIP_TRANSCODE_MATCH_CLIPS(self, CLIP_TRANSCODE_MATCH_CLIPS):
        raise AttributeError("Attribute 'CLIP_TRANSCODE_MATCH_CLIPS' is read-only")

    @property
    def CLIP_TRANSCODE_MATCH_SEQUENCE(self):
        self.__CLIP_TRANSCODE_MATCH_SEQUENCE = self._extend_eval('CLIP_TRANSCODE_MATCH_SEQUENCE')
        return self.__CLIP_TRANSCODE_MATCH_SEQUENCE
    @CLIP_TRANSCODE_MATCH_SEQUENCE.setter
    def CLIP_TRANSCODE_MATCH_SEQUENCE(self, CLIP_TRANSCODE_MATCH_SEQUENCE):
        raise AttributeError("Attribute 'CLIP_TRANSCODE_MATCH_SEQUENCE' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ProjectManagerOptions.bind"')
        self.check_type(function, any, 'arg "function" of function "ProjectManagerOptions.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ProjectManagerOptions.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ProjectManagerOptions.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "ProjectManagerOptions.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "ProjectManagerOptions.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

class Metadata(PymiereObject):
    def __init__(self, pymiere_id=None, getMetadata=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'getMetadata':getMetadata})
        super(Metadata, self).__init__(pymiere_id)
        self.__getMetadata = getMetadata

    # ----- PROPERTIES -----
    @property
    def getMetadata(self):
        self.__getMetadata = self._extend_eval('getMetadata')
        return self.__getMetadata
    @getMetadata.setter
    def getMetadata(self, getMetadata):
        raise AttributeError("Attribute 'getMetadata' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Metadata.bind"')
        self.check_type(function, any, 'arg "function" of function "Metadata.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Metadata.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Metadata.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "Metadata.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "Metadata.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def setMetadataValue(self):
        self._extend_eval("setMetadataValue()")

    def setMarkerData(self):
        self._extend_eval("setMarkerData()")

    def addMarker(self):
        self._extend_eval("addMarker()")

    def updateMarker(self):
        self._extend_eval("updateMarker()")

    def deleteMarker(self):
        self._extend_eval("deleteMarker()")

class Document(PymiereObject):
    def __init__(self, pymiere_id=None, ):
        self.check_init_args({'pymiere_id':pymiere_id, })
        super(Document, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Document.bind"')
        self.check_type(function, any, 'arg "function" of function "Document.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Document.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Document.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "Document.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "Document.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def importFiles(self, arg1):
        """
        :type arg1: any
        """
        self.check_type(arg1, any, 'arg "arg1" of function "Document.importFiles"')
        return self._extend_eval("importFiles({})".format(_format_object_to_es(arg1)))

    def getFilePath(self):
        return self._extend_eval("getFilePath()")

class ProjectItemType(PymiereObject):
    def __init__(self, pymiere_id=None, BIN=None, CLIP=None, FILE=None, ROOT=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'BIN':BIN, 'CLIP':CLIP, 'FILE':FILE, 'ROOT':ROOT})
        super(ProjectItemType, self).__init__(pymiere_id)
        self.__BIN = BIN
        self.__CLIP = CLIP
        self.__FILE = FILE
        self.__ROOT = ROOT

    # ----- PROPERTIES -----
    @property
    def BIN(self):
        self.__BIN = self._extend_eval('BIN')
        return self.__BIN
    @BIN.setter
    def BIN(self, BIN):
        raise AttributeError("Attribute 'BIN' is read-only")

    @property
    def CLIP(self):
        self.__CLIP = self._extend_eval('CLIP')
        return self.__CLIP
    @CLIP.setter
    def CLIP(self, CLIP):
        raise AttributeError("Attribute 'CLIP' is read-only")

    @property
    def FILE(self):
        self.__FILE = self._extend_eval('FILE')
        return self.__FILE
    @FILE.setter
    def FILE(self, FILE):
        raise AttributeError("Attribute 'FILE' is read-only")

    @property
    def ROOT(self):
        self.__ROOT = self._extend_eval('ROOT')
        return self.__ROOT
    @ROOT.setter
    def ROOT(self, ROOT):
        raise AttributeError("Attribute 'ROOT' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ProjectItemType.bind"')
        self.check_type(function, any, 'arg "function" of function "ProjectItemType.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ProjectItemType.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ProjectItemType.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "ProjectItemType.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "ProjectItemType.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

class ScratchDiskType(PymiereObject):
    def __init__(self, pymiere_id=None, FirstVideoCaptureFolder=None, FirstAudioCaptureFolder=None, FirstVideoPreviewFolder=None, FirstAudioPreviewFolder=None, FirstAutoSaveFolder=None, FirstCClibrariesFolder=None, FirstCapsuleMediaFolder=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'FirstVideoCaptureFolder':FirstVideoCaptureFolder, 'FirstAudioCaptureFolder':FirstAudioCaptureFolder, 'FirstVideoPreviewFolder':FirstVideoPreviewFolder, 'FirstAudioPreviewFolder':FirstAudioPreviewFolder, 'FirstAutoSaveFolder':FirstAutoSaveFolder, 'FirstCClibrariesFolder':FirstCClibrariesFolder, 'FirstCapsuleMediaFolder':FirstCapsuleMediaFolder})
        super(ScratchDiskType, self).__init__(pymiere_id)
        self.__FirstVideoCaptureFolder = FirstVideoCaptureFolder
        self.__FirstAudioCaptureFolder = FirstAudioCaptureFolder
        self.__FirstVideoPreviewFolder = FirstVideoPreviewFolder
        self.__FirstAudioPreviewFolder = FirstAudioPreviewFolder
        self.__FirstAutoSaveFolder = FirstAutoSaveFolder
        self.__FirstCClibrariesFolder = FirstCClibrariesFolder
        self.__FirstCapsuleMediaFolder = FirstCapsuleMediaFolder

    # ----- PROPERTIES -----
    @property
    def FirstVideoCaptureFolder(self):
        self.__FirstVideoCaptureFolder = self._extend_eval('FirstVideoCaptureFolder')
        return self.__FirstVideoCaptureFolder
    @FirstVideoCaptureFolder.setter
    def FirstVideoCaptureFolder(self, FirstVideoCaptureFolder):
        raise AttributeError("Attribute 'FirstVideoCaptureFolder' is read-only")

    @property
    def FirstAudioCaptureFolder(self):
        self.__FirstAudioCaptureFolder = self._extend_eval('FirstAudioCaptureFolder')
        return self.__FirstAudioCaptureFolder
    @FirstAudioCaptureFolder.setter
    def FirstAudioCaptureFolder(self, FirstAudioCaptureFolder):
        raise AttributeError("Attribute 'FirstAudioCaptureFolder' is read-only")

    @property
    def FirstVideoPreviewFolder(self):
        self.__FirstVideoPreviewFolder = self._extend_eval('FirstVideoPreviewFolder')
        return self.__FirstVideoPreviewFolder
    @FirstVideoPreviewFolder.setter
    def FirstVideoPreviewFolder(self, FirstVideoPreviewFolder):
        raise AttributeError("Attribute 'FirstVideoPreviewFolder' is read-only")

    @property
    def FirstAudioPreviewFolder(self):
        self.__FirstAudioPreviewFolder = self._extend_eval('FirstAudioPreviewFolder')
        return self.__FirstAudioPreviewFolder
    @FirstAudioPreviewFolder.setter
    def FirstAudioPreviewFolder(self, FirstAudioPreviewFolder):
        raise AttributeError("Attribute 'FirstAudioPreviewFolder' is read-only")

    @property
    def FirstAutoSaveFolder(self):
        self.__FirstAutoSaveFolder = self._extend_eval('FirstAutoSaveFolder')
        return self.__FirstAutoSaveFolder
    @FirstAutoSaveFolder.setter
    def FirstAutoSaveFolder(self, FirstAutoSaveFolder):
        raise AttributeError("Attribute 'FirstAutoSaveFolder' is read-only")

    @property
    def FirstCClibrariesFolder(self):
        self.__FirstCClibrariesFolder = self._extend_eval('FirstCClibrariesFolder')
        return self.__FirstCClibrariesFolder
    @FirstCClibrariesFolder.setter
    def FirstCClibrariesFolder(self, FirstCClibrariesFolder):
        raise AttributeError("Attribute 'FirstCClibrariesFolder' is read-only")

    @property
    def FirstCapsuleMediaFolder(self):
        self.__FirstCapsuleMediaFolder = self._extend_eval('FirstCapsuleMediaFolder')
        return self.__FirstCapsuleMediaFolder
    @FirstCapsuleMediaFolder.setter
    def FirstCapsuleMediaFolder(self, FirstCapsuleMediaFolder):
        raise AttributeError("Attribute 'FirstCapsuleMediaFolder' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ScratchDiskType.bind"')
        self.check_type(function, any, 'arg "function" of function "ScratchDiskType.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ScratchDiskType.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ScratchDiskType.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "ScratchDiskType.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "ScratchDiskType.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

class RegisteredDirectories(PymiereObject):
    def __init__(self, pymiere_id=None, ):
        self.check_init_args({'pymiere_id':pymiere_id, })
        super(RegisteredDirectories, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "RegisteredDirectories.bind"')
        self.check_type(function, any, 'arg "function" of function "RegisteredDirectories.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "RegisteredDirectories.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "RegisteredDirectories.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "RegisteredDirectories.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "RegisteredDirectories.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

class UtilityFunctions(PymiereObject):
    def __init__(self, pymiere_id=None, ):
        self.check_init_args({'pymiere_id':pymiere_id, })
        super(UtilityFunctions, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "UtilityFunctions.bind"')
        self.check_type(function, any, 'arg "function" of function "UtilityFunctions.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "UtilityFunctions.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "UtilityFunctions.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "UtilityFunctions.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "UtilityFunctions.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

class Math(PymiereObject):
    def __init__(self, pymiere_id=None, E=None, LN10=None, LN2=None, LOG2E=None, LOG10E=None, PI=None, SQRT1_2=None, SQRT2=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'E':E, 'LN10':LN10, 'LN2':LN2, 'LOG2E':LOG2E, 'LOG10E':LOG10E, 'PI':PI, 'SQRT1_2':SQRT1_2, 'SQRT2':SQRT2})
        super(Math, self).__init__(pymiere_id)
        self.__E = E
        self.__LN10 = LN10
        self.__LN2 = LN2
        self.__LOG2E = LOG2E
        self.__LOG10E = LOG10E
        self.__PI = PI
        self.__SQRT1_2 = SQRT1_2
        self.__SQRT2 = SQRT2

    # ----- PROPERTIES -----
    @property
    def E(self):
        self.__E = self._extend_eval('E')
        return self.__E
    @E.setter
    def E(self, E):
        raise AttributeError("Attribute 'E' is read-only")

    @property
    def LN10(self):
        self.__LN10 = self._extend_eval('LN10')
        return self.__LN10
    @LN10.setter
    def LN10(self, LN10):
        raise AttributeError("Attribute 'LN10' is read-only")

    @property
    def LN2(self):
        self.__LN2 = self._extend_eval('LN2')
        return self.__LN2
    @LN2.setter
    def LN2(self, LN2):
        raise AttributeError("Attribute 'LN2' is read-only")

    @property
    def LOG2E(self):
        self.__LOG2E = self._extend_eval('LOG2E')
        return self.__LOG2E
    @LOG2E.setter
    def LOG2E(self, LOG2E):
        raise AttributeError("Attribute 'LOG2E' is read-only")

    @property
    def LOG10E(self):
        self.__LOG10E = self._extend_eval('LOG10E')
        return self.__LOG10E
    @LOG10E.setter
    def LOG10E(self, LOG10E):
        raise AttributeError("Attribute 'LOG10E' is read-only")

    @property
    def PI(self):
        self.__PI = self._extend_eval('PI')
        return self.__PI
    @PI.setter
    def PI(self, PI):
        raise AttributeError("Attribute 'PI' is read-only")

    @property
    def SQRT1_2(self):
        self.__SQRT1_2 = self._extend_eval('SQRT1_2')
        return self.__SQRT1_2
    @SQRT1_2.setter
    def SQRT1_2(self, SQRT1_2):
        raise AttributeError("Attribute 'SQRT1_2' is read-only")

    @property
    def SQRT2(self):
        self.__SQRT2 = self._extend_eval('SQRT2')
        return self.__SQRT2
    @SQRT2.setter
    def SQRT2(self, SQRT2):
        raise AttributeError("Attribute 'SQRT2' is read-only")


    # ----- FUNCTIONS -----
    def abs(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Math.abs"')
        return self._extend_eval("abs({})".format(_format_object_to_es(n)))

    def acos(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Math.acos"')
        return self._extend_eval("acos({})".format(_format_object_to_es(n)))

    def asin(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Math.asin"')
        return self._extend_eval("asin({})".format(_format_object_to_es(n)))

    def atan(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Math.atan"')
        return self._extend_eval("atan({})".format(_format_object_to_es(n)))

    def atan2(self, y, x):
        """
        :type y: float
        :type x: float
        """
        self.check_type(y, float, 'arg "y" of function "Math.atan2"')
        self.check_type(x, float, 'arg "x" of function "Math.atan2"')
        return self._extend_eval("atan2({}, {})".format(_format_object_to_es(y), _format_object_to_es(x)))

    def ceil(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Math.ceil"')
        return self._extend_eval("ceil({})".format(_format_object_to_es(n)))

    def cos(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Math.cos"')
        return self._extend_eval("cos({})".format(_format_object_to_es(n)))

    def exp(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Math.exp"')
        return self._extend_eval("exp({})".format(_format_object_to_es(n)))

    def floor(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Math.floor"')
        return self._extend_eval("floor({})".format(_format_object_to_es(n)))

    def log(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Math.log"')
        return self._extend_eval("log({})".format(_format_object_to_es(n)))

    def max(self, a, b):
        """
        :type a: float
        :type b: float
        """
        self.check_type(a, float, 'arg "a" of function "Math.max"')
        self.check_type(b, float, 'arg "b" of function "Math.max"')
        return self._extend_eval("max({}, {})".format(_format_object_to_es(a), _format_object_to_es(b)))

    def min(self, y, x):
        """
        :type y: float
        :type x: float
        """
        self.check_type(y, float, 'arg "y" of function "Math.min"')
        self.check_type(x, float, 'arg "x" of function "Math.min"')
        return self._extend_eval("min({}, {})".format(_format_object_to_es(y), _format_object_to_es(x)))

    def pow(self, x, y):
        """
        :type x: float
        :type y: float
        """
        self.check_type(x, float, 'arg "x" of function "Math.pow"')
        self.check_type(y, float, 'arg "y" of function "Math.pow"')
        return self._extend_eval("pow({}, {})".format(_format_object_to_es(x), _format_object_to_es(y)))

    def random(self):
        return self._extend_eval("random()")

    def round(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Math.round"')
        return self._extend_eval("round({})".format(_format_object_to_es(n)))

    def sin(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Math.sin"')
        return self._extend_eval("sin({})".format(_format_object_to_es(n)))

    def sqrt(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Math.sqrt"')
        return self._extend_eval("sqrt({})".format(_format_object_to_es(n)))

    def tan(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Math.tan"')
        return self._extend_eval("tan({})".format(_format_object_to_es(n)))

class File(PymiereObject):
    def __init__(self, pymiere_id=None, alias=None, created=None, error=None, exists=None, fsName=None, fullName=None, absoluteURI=None, relativeURI=None, modified=None, name=None, displayName=None, path=None, parent=None, type=None, creator=None, hidden=None, readonly=None, lineFeed=None, length=None, encoding=None, eof=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'alias':alias, 'created':created, 'error':error, 'exists':exists, 'fsName':fsName, 'fullName':fullName, 'absoluteURI':absoluteURI, 'relativeURI':relativeURI, 'modified':modified, 'name':name, 'displayName':displayName, 'path':path, 'parent':parent, 'type':type, 'creator':creator, 'hidden':hidden, 'readonly':readonly, 'lineFeed':lineFeed, 'length':length, 'encoding':encoding, 'eof':eof})
        super(File, self).__init__(pymiere_id)
        self.__alias = alias
        self.__created = created
        self.__error = error
        self.__exists = exists
        self.__fsName = fsName
        self.__fullName = fullName
        self.__absoluteURI = absoluteURI
        self.__relativeURI = relativeURI
        self.__modified = modified
        self.__name = name
        self.__displayName = displayName
        self.__path = path
        self.__parent = parent
        self.__type = type
        self.__creator = creator
        self.__hidden = hidden
        self.__readonly = readonly
        self.__lineFeed = lineFeed
        self.__length = length
        self.__encoding = encoding
        self.__eof = eof

    # ----- PROPERTIES -----
    @property
    def alias(self):
        self.__alias = self._extend_eval('alias')
        return self.__alias
    @alias.setter
    def alias(self, alias):
        raise AttributeError("Attribute 'alias' is read-only")

    @property
    def created(self):
        self.__created = Date(**self._extend_eval('created'))
        return self.__created
    @created.setter
    def created(self, created):
        raise AttributeError("Attribute 'created' is read-only")

    @property
    def error(self):
        self.__error = self._extend_eval('error')
        return self.__error
    @error.setter
    def error(self, error):
        self._extend_eval("error = {}".format(_format_object_to_es(error)))
        self.__error = error

    @property
    def exists(self):
        self.__exists = self._extend_eval('exists')
        return self.__exists
    @exists.setter
    def exists(self, exists):
        raise AttributeError("Attribute 'exists' is read-only")

    @property
    def fsName(self):
        self.__fsName = self._extend_eval('fsName')
        return self.__fsName
    @fsName.setter
    def fsName(self, fsName):
        raise AttributeError("Attribute 'fsName' is read-only")

    @property
    def fullName(self):
        self.__fullName = self._extend_eval('fullName')
        return self.__fullName
    @fullName.setter
    def fullName(self, fullName):
        raise AttributeError("Attribute 'fullName' is read-only")

    @property
    def absoluteURI(self):
        self.__absoluteURI = self._extend_eval('absoluteURI')
        return self.__absoluteURI
    @absoluteURI.setter
    def absoluteURI(self, absoluteURI):
        raise AttributeError("Attribute 'absoluteURI' is read-only")

    @property
    def relativeURI(self):
        self.__relativeURI = self._extend_eval('relativeURI')
        return self.__relativeURI
    @relativeURI.setter
    def relativeURI(self, relativeURI):
        raise AttributeError("Attribute 'relativeURI' is read-only")

    @property
    def modified(self):
        self.__modified = Date(**self._extend_eval('modified'))
        return self.__modified
    @modified.setter
    def modified(self, modified):
        raise AttributeError("Attribute 'modified' is read-only")

    @property
    def name(self):
        self.__name = self._extend_eval('name')
        return self.__name
    @name.setter
    def name(self, name):
        raise AttributeError("Attribute 'name' is read-only")

    @property
    def displayName(self):
        self.__displayName = self._extend_eval('displayName')
        return self.__displayName
    @displayName.setter
    def displayName(self, displayName):
        raise AttributeError("Attribute 'displayName' is read-only")

    @property
    def path(self):
        self.__path = self._extend_eval('path')
        return self.__path
    @path.setter
    def path(self, path):
        raise AttributeError("Attribute 'path' is read-only")

    @property
    def parent(self):
        self.__parent = Folder(**self._extend_eval('parent'))
        return self.__parent
    @parent.setter
    def parent(self, parent):
        raise AttributeError("Attribute 'parent' is read-only")

    @property
    def type(self):
        self.__type = self._extend_eval('type')
        return self.__type
    @type.setter
    def type(self, type):
        raise AttributeError("Attribute 'type' is read-only")

    @property
    def creator(self):
        self.__creator = self._extend_eval('creator')
        return self.__creator
    @creator.setter
    def creator(self, creator):
        raise AttributeError("Attribute 'creator' is read-only")

    @property
    def hidden(self):
        self.__hidden = self._extend_eval('hidden')
        return self.__hidden
    @hidden.setter
    def hidden(self, hidden):
        self._extend_eval("hidden = {}".format(_format_object_to_es(hidden)))
        self.__hidden = hidden

    @property
    def readonly(self):
        self.__readonly = self._extend_eval('readonly')
        return self.__readonly
    @readonly.setter
    def readonly(self, readonly):
        self._extend_eval("readonly = {}".format(_format_object_to_es(readonly)))
        self.__readonly = readonly

    @property
    def lineFeed(self):
        self.__lineFeed = self._extend_eval('lineFeed')
        return self.__lineFeed
    @lineFeed.setter
    def lineFeed(self, lineFeed):
        self._extend_eval("lineFeed = {}".format(_format_object_to_es(lineFeed)))
        self.__lineFeed = lineFeed

    @property
    def length(self):
        self.__length = self._extend_eval('length')
        return self.__length
    @length.setter
    def length(self, length):
        self._extend_eval("length = {}".format(_format_object_to_es(length)))
        self.__length = length

    @property
    def encoding(self):
        self.__encoding = self._extend_eval('encoding')
        return self.__encoding
    @encoding.setter
    def encoding(self, encoding):
        self._extend_eval("encoding = {}".format(_format_object_to_es(encoding)))
        self.__encoding = encoding

    @property
    def eof(self):
        self.__eof = self._extend_eval('eof')
        return self.__eof
    @eof.setter
    def eof(self, eof):
        raise AttributeError("Attribute 'eof' is read-only")


    # ----- FUNCTIONS -----
    def resolve(self):
        return _format_object_to_py(self._extend_eval("resolve()"))

    def rename(self, name):
        """
        :type name: str
        """
        self.check_type(name, str, 'arg "name" of function "File.rename"')
        return self._extend_eval("rename({})".format(_format_object_to_es(name)))

    def remove(self):
        return self._extend_eval("remove()")

    def changePath(self, path):
        """
        :type path: str
        """
        self.check_type(path, str, 'arg "path" of function "File.changePath"')
        return self._extend_eval("changePath({})".format(_format_object_to_es(path)))

    def getRelativeURI(self, baseURI):
        """
        :type baseURI: str
        """
        self.check_type(baseURI, str, 'arg "baseURI" of function "File.getRelativeURI"')
        return self._extend_eval("getRelativeURI({})".format(_format_object_to_es(baseURI)))

    def execute(self):
        return self._extend_eval("execute()")

    def openDlg(self, prompt):
        """
        :type prompt: str
        """
        self.check_type(prompt, str, 'arg "prompt" of function "File.openDlg"')
        return _format_object_to_py(self._extend_eval("openDlg({})".format(_format_object_to_es(prompt))))

    def saveDlg(self, prompt):
        """
        :type prompt: str
        """
        self.check_type(prompt, str, 'arg "prompt" of function "File.saveDlg"')
        return _format_object_to_py(self._extend_eval("saveDlg({})".format(_format_object_to_es(prompt))))

    def toString(self):
        return self._extend_eval("toString()")

    def toSource(self):
        return self._extend_eval("toSource()")

    def createAlias(self, path):
        """
        :type path: str
        """
        self.check_type(path, str, 'arg "path" of function "File.createAlias"')
        return self._extend_eval("createAlias({})".format(_format_object_to_es(path)))

    def open(self, mode):
        """
        :type mode: str
        """
        self.check_type(mode, str, 'arg "mode" of function "File.open"')
        return self._extend_eval("open({})".format(_format_object_to_es(mode)))

    def close(self):
        return self._extend_eval("close()")

    def read(self, count):
        """
        :type count: float
        """
        self.check_type(count, float, 'arg "count" of function "File.read"')
        return self._extend_eval("read({})".format(_format_object_to_es(count)))

    def readch(self):
        return self._extend_eval("readch()")

    def readln(self):
        return self._extend_eval("readln()")

    def write(self, text):
        """
        :type text: str
        """
        self.check_type(text, str, 'arg "text" of function "File.write"')
        return self._extend_eval("write({})".format(_format_object_to_es(text)))

    def print(self, text):
        """
        :type text: str
        """
        self.check_type(text, str, 'arg "text" of function "File.print"')
        return self._extend_eval("print({})".format(_format_object_to_es(text)))

    def writeln(self, text):
        """
        :type text: str
        """
        self.check_type(text, str, 'arg "text" of function "File.writeln"')
        return self._extend_eval("writeln({})".format(_format_object_to_es(text)))

    def seek(self, pos):
        """
        :type pos: float
        """
        self.check_type(pos, float, 'arg "pos" of function "File.seek"')
        return self._extend_eval("seek({})".format(_format_object_to_es(pos)))

    def tell(self):
        return self._extend_eval("tell()")

    def copy(self, where):
        """
        :type where: str
        """
        self.check_type(where, str, 'arg "where" of function "File.copy"')
        return self._extend_eval("copy({})".format(_format_object_to_es(where)))

class Date(PymiereObject):
    def __init__(self, pymiere_id=None, ):
        self.check_init_args({'pymiere_id':pymiere_id, })
        super(Date, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def getDate(self):
        return self._extend_eval("getDate()")

    def getDay(self):
        return self._extend_eval("getDay()")

    def getYear(self):
        return self._extend_eval("getYear()")

    def getFullYear(self):
        return self._extend_eval("getFullYear()")

    def getHours(self):
        return self._extend_eval("getHours()")

    def getMilliseconds(self):
        return self._extend_eval("getMilliseconds()")

    def getMinutes(self):
        return self._extend_eval("getMinutes()")

    def getMonth(self):
        return self._extend_eval("getMonth()")

    def getSeconds(self):
        return self._extend_eval("getSeconds()")

    def getTime(self):
        return self._extend_eval("getTime()")

    def getTimezoneOffset(self):
        return self._extend_eval("getTimezoneOffset()")

    def getUTCDate(self):
        return self._extend_eval("getUTCDate()")

    def getUTCDay(self):
        return self._extend_eval("getUTCDay()")

    def getUTCFullYear(self):
        return self._extend_eval("getUTCFullYear()")

    def getUTCHours(self):
        return self._extend_eval("getUTCHours()")

    def getUTCMilliseconds(self):
        return self._extend_eval("getUTCMilliseconds()")

    def getUTCMinutes(self):
        return self._extend_eval("getUTCMinutes()")

    def getUTCMonth(self):
        return self._extend_eval("getUTCMonth()")

    def getUTCSeconds(self):
        return self._extend_eval("getUTCSeconds()")

    def setDate(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Date.setDate"')
        return self._extend_eval("setDate({})".format(_format_object_to_es(n)))

    def setFullYear(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Date.setFullYear"')
        return self._extend_eval("setFullYear({})".format(_format_object_to_es(n)))

    def setHours(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Date.setHours"')
        return self._extend_eval("setHours({})".format(_format_object_to_es(n)))

    def setMilliseconds(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Date.setMilliseconds"')
        return self._extend_eval("setMilliseconds({})".format(_format_object_to_es(n)))

    def setMinutes(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Date.setMinutes"')
        return self._extend_eval("setMinutes({})".format(_format_object_to_es(n)))

    def setSeconds(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Date.setSeconds"')
        return self._extend_eval("setSeconds({})".format(_format_object_to_es(n)))

    def setMonth(self, n, arg2):
        """
        :type n: float
        :type arg2: unknown
        """
        self.check_type(n, float, 'arg "n" of function "Date.setMonth"')
        return self._extend_eval("setMonth({}, {})".format(_format_object_to_es(n), _format_object_to_es(arg2)))

    def setUTCDate(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Date.setUTCDate"')
        return self._extend_eval("setUTCDate({})".format(_format_object_to_es(n)))

    def setUTCFullYear(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Date.setUTCFullYear"')
        return self._extend_eval("setUTCFullYear({})".format(_format_object_to_es(n)))

    def setUTCHours(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Date.setUTCHours"')
        return self._extend_eval("setUTCHours({})".format(_format_object_to_es(n)))

    def setUTCMilliseconds(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Date.setUTCMilliseconds"')
        return self._extend_eval("setUTCMilliseconds({})".format(_format_object_to_es(n)))

    def setUTCMinutes(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Date.setUTCMinutes"')
        return self._extend_eval("setUTCMinutes({})".format(_format_object_to_es(n)))

    def setUTCSeconds(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Date.setUTCSeconds"')
        return self._extend_eval("setUTCSeconds({})".format(_format_object_to_es(n)))

    def setUTCMonth(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Date.setUTCMonth"')
        return self._extend_eval("setUTCMonth({})".format(_format_object_to_es(n)))

    def setTime(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Date.setTime"')
        return self._extend_eval("setTime({})".format(_format_object_to_es(n)))

    def setYear(self, n):
        """
        :type n: float
        """
        self.check_type(n, float, 'arg "n" of function "Date.setYear"')
        return self._extend_eval("setYear({})".format(_format_object_to_es(n)))

    def toDateString(self):
        return self._extend_eval("toDateString()")

    def toTimeString(self):
        return self._extend_eval("toTimeString()")

    def toLocaleString(self):
        return self._extend_eval("toLocaleString()")

    def toLocaleDateString(self):
        return self._extend_eval("toLocaleDateString()")

    def toLocaleTimeString(self):
        return self._extend_eval("toLocaleTimeString()")

    def toGMTString(self):
        return self._extend_eval("toGMTString()")

    def toUTCString(self):
        return self._extend_eval("toUTCString()")

    def toString(self):
        return self._extend_eval("toString()")

    def valueOf(self):
        return self._extend_eval("valueOf()")

    def toSource(self):
        return self._extend_eval("toSource()")

    def toJSON(self):
        return self._extend_eval("toJSON()")

class Folder(PymiereObject):
    def __init__(self, pymiere_id=None, alias=None, created=None, error=None, exists=None, fsName=None, fullName=None, absoluteURI=None, relativeURI=None, modified=None, name=None, displayName=None, path=None, parent=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'alias':alias, 'created':created, 'error':error, 'exists':exists, 'fsName':fsName, 'fullName':fullName, 'absoluteURI':absoluteURI, 'relativeURI':relativeURI, 'modified':modified, 'name':name, 'displayName':displayName, 'path':path, 'parent':parent})
        super(Folder, self).__init__(pymiere_id)
        self.__alias = alias
        self.__created = created
        self.__error = error
        self.__exists = exists
        self.__fsName = fsName
        self.__fullName = fullName
        self.__absoluteURI = absoluteURI
        self.__relativeURI = relativeURI
        self.__modified = modified
        self.__name = name
        self.__displayName = displayName
        self.__path = path
        self.__parent = parent

    # ----- PROPERTIES -----
    @property
    def alias(self):
        self.__alias = self._extend_eval('alias')
        return self.__alias
    @alias.setter
    def alias(self, alias):
        raise AttributeError("Attribute 'alias' is read-only")

    @property
    def created(self):
        self.__created = Date(**self._extend_eval('created'))
        return self.__created
    @created.setter
    def created(self, created):
        raise AttributeError("Attribute 'created' is read-only")

    @property
    def error(self):
        self.__error = self._extend_eval('error')
        return self.__error
    @error.setter
    def error(self, error):
        self._extend_eval("error = {}".format(_format_object_to_es(error)))
        self.__error = error

    @property
    def exists(self):
        self.__exists = self._extend_eval('exists')
        return self.__exists
    @exists.setter
    def exists(self, exists):
        raise AttributeError("Attribute 'exists' is read-only")

    @property
    def fsName(self):
        self.__fsName = self._extend_eval('fsName')
        return self.__fsName
    @fsName.setter
    def fsName(self, fsName):
        raise AttributeError("Attribute 'fsName' is read-only")

    @property
    def fullName(self):
        self.__fullName = self._extend_eval('fullName')
        return self.__fullName
    @fullName.setter
    def fullName(self, fullName):
        raise AttributeError("Attribute 'fullName' is read-only")

    @property
    def absoluteURI(self):
        self.__absoluteURI = self._extend_eval('absoluteURI')
        return self.__absoluteURI
    @absoluteURI.setter
    def absoluteURI(self, absoluteURI):
        raise AttributeError("Attribute 'absoluteURI' is read-only")

    @property
    def relativeURI(self):
        self.__relativeURI = self._extend_eval('relativeURI')
        return self.__relativeURI
    @relativeURI.setter
    def relativeURI(self, relativeURI):
        raise AttributeError("Attribute 'relativeURI' is read-only")

    @property
    def modified(self):
        self.__modified = Date(**self._extend_eval('modified'))
        return self.__modified
    @modified.setter
    def modified(self, modified):
        raise AttributeError("Attribute 'modified' is read-only")

    @property
    def name(self):
        self.__name = self._extend_eval('name')
        return self.__name
    @name.setter
    def name(self, name):
        raise AttributeError("Attribute 'name' is read-only")

    @property
    def displayName(self):
        self.__displayName = self._extend_eval('displayName')
        return self.__displayName
    @displayName.setter
    def displayName(self, displayName):
        raise AttributeError("Attribute 'displayName' is read-only")

    @property
    def path(self):
        self.__path = self._extend_eval('path')
        return self.__path
    @path.setter
    def path(self, path):
        raise AttributeError("Attribute 'path' is read-only")

    @property
    def parent(self):
        self.__parent = Folder(**self._extend_eval('parent'))
        return self.__parent
    @parent.setter
    def parent(self, parent):
        raise AttributeError("Attribute 'parent' is read-only")


    # ----- FUNCTIONS -----
    def resolve(self):
        return _format_object_to_py(self._extend_eval("resolve()"))

    def rename(self, name):
        """
        :type name: str
        """
        self.check_type(name, str, 'arg "name" of function "Folder.rename"')
        return self._extend_eval("rename({})".format(_format_object_to_es(name)))

    def remove(self):
        return self._extend_eval("remove()")

    def changePath(self, path):
        """
        :type path: str
        """
        self.check_type(path, str, 'arg "path" of function "Folder.changePath"')
        return self._extend_eval("changePath({})".format(_format_object_to_es(path)))

    def getRelativeURI(self, baseURI):
        """
        :type baseURI: str
        """
        self.check_type(baseURI, str, 'arg "baseURI" of function "Folder.getRelativeURI"')
        return self._extend_eval("getRelativeURI({})".format(_format_object_to_es(baseURI)))

    def execute(self):
        return self._extend_eval("execute()")

    def openDlg(self, prompt):
        """
        :type prompt: str
        """
        self.check_type(prompt, str, 'arg "prompt" of function "Folder.openDlg"')
        return _format_object_to_py(self._extend_eval("openDlg({})".format(_format_object_to_es(prompt))))

    def saveDlg(self, prompt):
        """
        :type prompt: str
        """
        self.check_type(prompt, str, 'arg "prompt" of function "Folder.saveDlg"')
        return _format_object_to_py(self._extend_eval("saveDlg({})".format(_format_object_to_es(prompt))))

    def toString(self):
        return self._extend_eval("toString()")

    def toSource(self):
        return self._extend_eval("toSource()")

    def selectDlg(self, prompt):
        """
        :type prompt: str
        """
        self.check_type(prompt, str, 'arg "prompt" of function "Folder.selectDlg"')
        return _format_object_to_py(self._extend_eval("selectDlg({})".format(_format_object_to_es(prompt))))

    def getFiles(self, pattern):
        """
        :type pattern: str
        """
        self.check_type(pattern, str, 'arg "pattern" of function "Folder.getFiles"')
        return Array(**self._extend_eval("getFiles({})".format(_format_object_to_es(pattern))))

    def create(self):
        return self._extend_eval("create()")

class FootageInterpretation(PymiereObject):
    def __init__(self, pymiere_id=None, frameRate=None, pixelAspectRatio=None, fieldType=None, removePulldown=None, alphaUsage=None, ignoreAlpha=None, invertAlpha=None, vrConformProjectionType=None, vrLayoutType=None, vrHorizontalView=None, vrVerticalView=None, ALPHACHANNEL_NONE=None, ALPHACHANNEL_STRAIGHT=None, ALPHACHANNEL_PREMULTIPLIED=None, ALPHACHANNEL_IGNORE=None, FIELD_TYPE_DEFAULT=None, FIELD_TYPE_PROGRESSIVE=None, FIELD_TYPE_UPPERFIRST=None, FIELD_TYPE_LOWERFIRST=None, VR_CONFORM_PROJECTION_NONE=None, VR_CONFORM_PROJECTION_EQUIRECTANGULAR=None, VR_LAYOUT_MONOSCOPIC=None, VR_LAYOUT_STEREO_OVER_UNDER=None, VR_LAYOUT_STEREO_SIDE_BY_SIDE=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'frameRate':frameRate, 'pixelAspectRatio':pixelAspectRatio, 'fieldType':fieldType, 'removePulldown':removePulldown, 'alphaUsage':alphaUsage, 'ignoreAlpha':ignoreAlpha, 'invertAlpha':invertAlpha, 'vrConformProjectionType':vrConformProjectionType, 'vrLayoutType':vrLayoutType, 'vrHorizontalView':vrHorizontalView, 'vrVerticalView':vrVerticalView, 'ALPHACHANNEL_NONE':ALPHACHANNEL_NONE, 'ALPHACHANNEL_STRAIGHT':ALPHACHANNEL_STRAIGHT, 'ALPHACHANNEL_PREMULTIPLIED':ALPHACHANNEL_PREMULTIPLIED, 'ALPHACHANNEL_IGNORE':ALPHACHANNEL_IGNORE, 'FIELD_TYPE_DEFAULT':FIELD_TYPE_DEFAULT, 'FIELD_TYPE_PROGRESSIVE':FIELD_TYPE_PROGRESSIVE, 'FIELD_TYPE_UPPERFIRST':FIELD_TYPE_UPPERFIRST, 'FIELD_TYPE_LOWERFIRST':FIELD_TYPE_LOWERFIRST, 'VR_CONFORM_PROJECTION_NONE':VR_CONFORM_PROJECTION_NONE, 'VR_CONFORM_PROJECTION_EQUIRECTANGULAR':VR_CONFORM_PROJECTION_EQUIRECTANGULAR, 'VR_LAYOUT_MONOSCOPIC':VR_LAYOUT_MONOSCOPIC, 'VR_LAYOUT_STEREO_OVER_UNDER':VR_LAYOUT_STEREO_OVER_UNDER, 'VR_LAYOUT_STEREO_SIDE_BY_SIDE':VR_LAYOUT_STEREO_SIDE_BY_SIDE})
        super(FootageInterpretation, self).__init__(pymiere_id)
        self.__frameRate = frameRate
        self.__pixelAspectRatio = pixelAspectRatio
        self.__fieldType = fieldType
        self.__removePulldown = removePulldown
        self.__alphaUsage = alphaUsage
        self.__ignoreAlpha = ignoreAlpha
        self.__invertAlpha = invertAlpha
        self.__vrConformProjectionType = vrConformProjectionType
        self.__vrLayoutType = vrLayoutType
        self.__vrHorizontalView = vrHorizontalView
        self.__vrVerticalView = vrVerticalView
        self.__ALPHACHANNEL_NONE = ALPHACHANNEL_NONE
        self.__ALPHACHANNEL_STRAIGHT = ALPHACHANNEL_STRAIGHT
        self.__ALPHACHANNEL_PREMULTIPLIED = ALPHACHANNEL_PREMULTIPLIED
        self.__ALPHACHANNEL_IGNORE = ALPHACHANNEL_IGNORE
        self.__FIELD_TYPE_DEFAULT = FIELD_TYPE_DEFAULT
        self.__FIELD_TYPE_PROGRESSIVE = FIELD_TYPE_PROGRESSIVE
        self.__FIELD_TYPE_UPPERFIRST = FIELD_TYPE_UPPERFIRST
        self.__FIELD_TYPE_LOWERFIRST = FIELD_TYPE_LOWERFIRST
        self.__VR_CONFORM_PROJECTION_NONE = VR_CONFORM_PROJECTION_NONE
        self.__VR_CONFORM_PROJECTION_EQUIRECTANGULAR = VR_CONFORM_PROJECTION_EQUIRECTANGULAR
        self.__VR_LAYOUT_MONOSCOPIC = VR_LAYOUT_MONOSCOPIC
        self.__VR_LAYOUT_STEREO_OVER_UNDER = VR_LAYOUT_STEREO_OVER_UNDER
        self.__VR_LAYOUT_STEREO_SIDE_BY_SIDE = VR_LAYOUT_STEREO_SIDE_BY_SIDE

    # ----- PROPERTIES -----
    @property
    def frameRate(self):
        self.__frameRate = self._extend_eval('frameRate')
        return self.__frameRate
    @frameRate.setter
    def frameRate(self, frameRate):
        self._extend_eval("frameRate = {}".format(_format_object_to_es(frameRate)))
        self.__frameRate = frameRate

    @property
    def pixelAspectRatio(self):
        self.__pixelAspectRatio = self._extend_eval('pixelAspectRatio')
        return self.__pixelAspectRatio
    @pixelAspectRatio.setter
    def pixelAspectRatio(self, pixelAspectRatio):
        self._extend_eval("pixelAspectRatio = {}".format(_format_object_to_es(pixelAspectRatio)))
        self.__pixelAspectRatio = pixelAspectRatio

    @property
    def fieldType(self):
        self.__fieldType = self._extend_eval('fieldType')
        return self.__fieldType
    @fieldType.setter
    def fieldType(self, fieldType):
        self._extend_eval("fieldType = {}".format(_format_object_to_es(fieldType)))
        self.__fieldType = fieldType

    @property
    def removePulldown(self):
        self.__removePulldown = self._extend_eval('removePulldown')
        return self.__removePulldown
    @removePulldown.setter
    def removePulldown(self, removePulldown):
        self._extend_eval("removePulldown = {}".format(_format_object_to_es(removePulldown)))
        self.__removePulldown = removePulldown

    @property
    def alphaUsage(self):
        self.__alphaUsage = self._extend_eval('alphaUsage')
        return self.__alphaUsage
    @alphaUsage.setter
    def alphaUsage(self, alphaUsage):
        self._extend_eval("alphaUsage = {}".format(_format_object_to_es(alphaUsage)))
        self.__alphaUsage = alphaUsage

    @property
    def ignoreAlpha(self):
        self.__ignoreAlpha = self._extend_eval('ignoreAlpha')
        return self.__ignoreAlpha
    @ignoreAlpha.setter
    def ignoreAlpha(self, ignoreAlpha):
        self._extend_eval("ignoreAlpha = {}".format(_format_object_to_es(ignoreAlpha)))
        self.__ignoreAlpha = ignoreAlpha

    @property
    def invertAlpha(self):
        self.__invertAlpha = self._extend_eval('invertAlpha')
        return self.__invertAlpha
    @invertAlpha.setter
    def invertAlpha(self, invertAlpha):
        self._extend_eval("invertAlpha = {}".format(_format_object_to_es(invertAlpha)))
        self.__invertAlpha = invertAlpha

    @property
    def vrConformProjectionType(self):
        self.__vrConformProjectionType = self._extend_eval('vrConformProjectionType')
        return self.__vrConformProjectionType
    @vrConformProjectionType.setter
    def vrConformProjectionType(self, vrConformProjectionType):
        self._extend_eval("vrConformProjectionType = {}".format(_format_object_to_es(vrConformProjectionType)))
        self.__vrConformProjectionType = vrConformProjectionType

    @property
    def vrLayoutType(self):
        self.__vrLayoutType = self._extend_eval('vrLayoutType')
        return self.__vrLayoutType
    @vrLayoutType.setter
    def vrLayoutType(self, vrLayoutType):
        self._extend_eval("vrLayoutType = {}".format(_format_object_to_es(vrLayoutType)))
        self.__vrLayoutType = vrLayoutType

    @property
    def vrHorizontalView(self):
        self.__vrHorizontalView = self._extend_eval('vrHorizontalView')
        return self.__vrHorizontalView
    @vrHorizontalView.setter
    def vrHorizontalView(self, vrHorizontalView):
        self._extend_eval("vrHorizontalView = {}".format(_format_object_to_es(vrHorizontalView)))
        self.__vrHorizontalView = vrHorizontalView

    @property
    def vrVerticalView(self):
        self.__vrVerticalView = self._extend_eval('vrVerticalView')
        return self.__vrVerticalView
    @vrVerticalView.setter
    def vrVerticalView(self, vrVerticalView):
        self._extend_eval("vrVerticalView = {}".format(_format_object_to_es(vrVerticalView)))
        self.__vrVerticalView = vrVerticalView

    @property
    def ALPHACHANNEL_NONE(self):
        self.__ALPHACHANNEL_NONE = self._extend_eval('ALPHACHANNEL_NONE')
        return self.__ALPHACHANNEL_NONE
    @ALPHACHANNEL_NONE.setter
    def ALPHACHANNEL_NONE(self, ALPHACHANNEL_NONE):
        raise AttributeError("Attribute 'ALPHACHANNEL_NONE' is read-only")

    @property
    def ALPHACHANNEL_STRAIGHT(self):
        self.__ALPHACHANNEL_STRAIGHT = self._extend_eval('ALPHACHANNEL_STRAIGHT')
        return self.__ALPHACHANNEL_STRAIGHT
    @ALPHACHANNEL_STRAIGHT.setter
    def ALPHACHANNEL_STRAIGHT(self, ALPHACHANNEL_STRAIGHT):
        raise AttributeError("Attribute 'ALPHACHANNEL_STRAIGHT' is read-only")

    @property
    def ALPHACHANNEL_PREMULTIPLIED(self):
        self.__ALPHACHANNEL_PREMULTIPLIED = self._extend_eval('ALPHACHANNEL_PREMULTIPLIED')
        return self.__ALPHACHANNEL_PREMULTIPLIED
    @ALPHACHANNEL_PREMULTIPLIED.setter
    def ALPHACHANNEL_PREMULTIPLIED(self, ALPHACHANNEL_PREMULTIPLIED):
        raise AttributeError("Attribute 'ALPHACHANNEL_PREMULTIPLIED' is read-only")

    @property
    def ALPHACHANNEL_IGNORE(self):
        self.__ALPHACHANNEL_IGNORE = self._extend_eval('ALPHACHANNEL_IGNORE')
        return self.__ALPHACHANNEL_IGNORE
    @ALPHACHANNEL_IGNORE.setter
    def ALPHACHANNEL_IGNORE(self, ALPHACHANNEL_IGNORE):
        raise AttributeError("Attribute 'ALPHACHANNEL_IGNORE' is read-only")

    @property
    def FIELD_TYPE_DEFAULT(self):
        self.__FIELD_TYPE_DEFAULT = self._extend_eval('FIELD_TYPE_DEFAULT')
        return self.__FIELD_TYPE_DEFAULT
    @FIELD_TYPE_DEFAULT.setter
    def FIELD_TYPE_DEFAULT(self, FIELD_TYPE_DEFAULT):
        raise AttributeError("Attribute 'FIELD_TYPE_DEFAULT' is read-only")

    @property
    def FIELD_TYPE_PROGRESSIVE(self):
        self.__FIELD_TYPE_PROGRESSIVE = self._extend_eval('FIELD_TYPE_PROGRESSIVE')
        return self.__FIELD_TYPE_PROGRESSIVE
    @FIELD_TYPE_PROGRESSIVE.setter
    def FIELD_TYPE_PROGRESSIVE(self, FIELD_TYPE_PROGRESSIVE):
        raise AttributeError("Attribute 'FIELD_TYPE_PROGRESSIVE' is read-only")

    @property
    def FIELD_TYPE_UPPERFIRST(self):
        self.__FIELD_TYPE_UPPERFIRST = self._extend_eval('FIELD_TYPE_UPPERFIRST')
        return self.__FIELD_TYPE_UPPERFIRST
    @FIELD_TYPE_UPPERFIRST.setter
    def FIELD_TYPE_UPPERFIRST(self, FIELD_TYPE_UPPERFIRST):
        raise AttributeError("Attribute 'FIELD_TYPE_UPPERFIRST' is read-only")

    @property
    def FIELD_TYPE_LOWERFIRST(self):
        self.__FIELD_TYPE_LOWERFIRST = self._extend_eval('FIELD_TYPE_LOWERFIRST')
        return self.__FIELD_TYPE_LOWERFIRST
    @FIELD_TYPE_LOWERFIRST.setter
    def FIELD_TYPE_LOWERFIRST(self, FIELD_TYPE_LOWERFIRST):
        raise AttributeError("Attribute 'FIELD_TYPE_LOWERFIRST' is read-only")

    @property
    def VR_CONFORM_PROJECTION_NONE(self):
        self.__VR_CONFORM_PROJECTION_NONE = self._extend_eval('VR_CONFORM_PROJECTION_NONE')
        return self.__VR_CONFORM_PROJECTION_NONE
    @VR_CONFORM_PROJECTION_NONE.setter
    def VR_CONFORM_PROJECTION_NONE(self, VR_CONFORM_PROJECTION_NONE):
        raise AttributeError("Attribute 'VR_CONFORM_PROJECTION_NONE' is read-only")

    @property
    def VR_CONFORM_PROJECTION_EQUIRECTANGULAR(self):
        self.__VR_CONFORM_PROJECTION_EQUIRECTANGULAR = self._extend_eval('VR_CONFORM_PROJECTION_EQUIRECTANGULAR')
        return self.__VR_CONFORM_PROJECTION_EQUIRECTANGULAR
    @VR_CONFORM_PROJECTION_EQUIRECTANGULAR.setter
    def VR_CONFORM_PROJECTION_EQUIRECTANGULAR(self, VR_CONFORM_PROJECTION_EQUIRECTANGULAR):
        raise AttributeError("Attribute 'VR_CONFORM_PROJECTION_EQUIRECTANGULAR' is read-only")

    @property
    def VR_LAYOUT_MONOSCOPIC(self):
        self.__VR_LAYOUT_MONOSCOPIC = self._extend_eval('VR_LAYOUT_MONOSCOPIC')
        return self.__VR_LAYOUT_MONOSCOPIC
    @VR_LAYOUT_MONOSCOPIC.setter
    def VR_LAYOUT_MONOSCOPIC(self, VR_LAYOUT_MONOSCOPIC):
        raise AttributeError("Attribute 'VR_LAYOUT_MONOSCOPIC' is read-only")

    @property
    def VR_LAYOUT_STEREO_OVER_UNDER(self):
        self.__VR_LAYOUT_STEREO_OVER_UNDER = self._extend_eval('VR_LAYOUT_STEREO_OVER_UNDER')
        return self.__VR_LAYOUT_STEREO_OVER_UNDER
    @VR_LAYOUT_STEREO_OVER_UNDER.setter
    def VR_LAYOUT_STEREO_OVER_UNDER(self, VR_LAYOUT_STEREO_OVER_UNDER):
        raise AttributeError("Attribute 'VR_LAYOUT_STEREO_OVER_UNDER' is read-only")

    @property
    def VR_LAYOUT_STEREO_SIDE_BY_SIDE(self):
        self.__VR_LAYOUT_STEREO_SIDE_BY_SIDE = self._extend_eval('VR_LAYOUT_STEREO_SIDE_BY_SIDE')
        return self.__VR_LAYOUT_STEREO_SIDE_BY_SIDE
    @VR_LAYOUT_STEREO_SIDE_BY_SIDE.setter
    def VR_LAYOUT_STEREO_SIDE_BY_SIDE(self, VR_LAYOUT_STEREO_SIDE_BY_SIDE):
        raise AttributeError("Attribute 'VR_LAYOUT_STEREO_SIDE_BY_SIDE' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "FootageInterpretation.bind"')
        self.check_type(function, any, 'arg "function" of function "FootageInterpretation.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "FootageInterpretation.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "FootageInterpretation.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "FootageInterpretation.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "FootageInterpretation.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

class Time(PymiereObject):
    def __init__(self, pymiere_id=None, seconds=None, ticks=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'seconds':seconds, 'ticks':ticks})
        super(Time, self).__init__(pymiere_id)
        self.__seconds = seconds
        self.__ticks = ticks

    # ----- PROPERTIES -----
    @property
    def seconds(self):
        self.__seconds = self._extend_eval('seconds')
        return self.__seconds
    @seconds.setter
    def seconds(self, seconds):
        self._extend_eval("seconds = {}".format(_format_object_to_es(seconds)))
        self.__seconds = seconds

    @property
    def ticks(self):
        self.__ticks = self._extend_eval('ticks')
        return self.__ticks
    @ticks.setter
    def ticks(self, ticks):
        self._extend_eval("ticks = {}".format(_format_object_to_es(ticks)))
        self.__ticks = ticks


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Time.bind"')
        self.check_type(function, any, 'arg "function" of function "Time.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Time.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Time.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "Time.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "Time.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def setSecondsAsFraction(self, numerator, denominator):
        """
        :type numerator: float
        :type denominator: float
        """
        self.check_type(numerator, float, 'arg "numerator" of function "Time.setSecondsAsFraction"')
        self.check_type(denominator, float, 'arg "denominator" of function "Time.setSecondsAsFraction"')
        self._extend_eval("setSecondsAsFraction({}, {})".format(_format_object_to_es(numerator), _format_object_to_es(denominator)))

    def getFormatted(self, time, timeDisplay):
        """
        :type time: Object
        :type timeDisplay: float
        """
        self.check_type(timeDisplay, float, 'arg "timeDisplay" of function "Time.getFormatted"')
        return self._extend_eval("getFormatted({}, {})".format(_format_object_to_es(time), _format_object_to_es(timeDisplay)))

class Track(PymiereObject):
    def __init__(self, pymiere_id=None, id=None, name=None, mediaType=None, clips=None, transitions=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'id':id, 'name':name, 'mediaType':mediaType, 'clips':clips, 'transitions':transitions})
        super(Track, self).__init__(pymiere_id)
        self.__id = id
        self.__name = name
        self.__mediaType = mediaType
        self.__clips = clips
        self.__transitions = transitions

    # ----- PROPERTIES -----
    @property
    def id(self):
        self.__id = self._extend_eval('id')
        return self.__id
    @id.setter
    def id(self, id):
        raise AttributeError("Attribute 'id' is read-only")

    @property
    def name(self):
        self.__name = self._extend_eval('name')
        return self.__name
    @name.setter
    def name(self, name):
        self._extend_eval("name = {}".format(_format_object_to_es(name)))
        self.__name = name

    @property
    def mediaType(self):
        self.__mediaType = self._extend_eval('mediaType')
        return self.__mediaType
    @mediaType.setter
    def mediaType(self, mediaType):
        raise AttributeError("Attribute 'mediaType' is read-only")

    @property
    def clips(self):
        self.__clips = TrackItemCollection(**self._extend_eval('clips'))
        return self.__clips
    @clips.setter
    def clips(self, clips):
        raise AttributeError("Attribute 'clips' is read-only")

    @property
    def transitions(self):
        self.__transitions = TrackItemCollection(**self._extend_eval('transitions'))
        return self.__transitions
    @transitions.setter
    def transitions(self, transitions):
        raise AttributeError("Attribute 'transitions' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Track.bind"')
        self.check_type(function, any, 'arg "function" of function "Track.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Track.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Track.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "Track.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "Track.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def isMuted(self):
        return self._extend_eval("isMuted()")

    def setMute(self, arg1):
        """
        :type arg1: float
        """
        self.check_type(arg1, float, 'arg "arg1" of function "Track.setMute"')
        self._extend_eval("setMute({})".format(_format_object_to_es(arg1)))

    def isLocked(self):
        return self._extend_eval("isLocked()")

    def setLocked(self, arg1):
        """
        :type arg1: float
        """
        self.check_type(arg1, float, 'arg "arg1" of function "Track.setLocked"')
        self._extend_eval("setLocked({})".format(_format_object_to_es(arg1)))

    def isTargeted(self):
        return self._extend_eval("isTargeted()")

    def setTargeted(self, isTargeted, shouldBroadcast):
        """
        :type isTargeted: bool
        :type shouldBroadcast: bool
        """
        self.check_type(isTargeted, bool, 'arg "isTargeted" of function "Track.setTargeted"')
        self.check_type(shouldBroadcast, bool, 'arg "shouldBroadcast" of function "Track.setTargeted"')
        self._extend_eval("setTargeted({}, {})".format(_format_object_to_es(isTargeted), _format_object_to_es(shouldBroadcast)))

    def insertClip(self, clipProjectItem, time):
        """
        :type clipProjectItem: ProjectItem
        :type time: Object
        """
        self.check_type(clipProjectItem, ProjectItem, 'arg "clipProjectItem" of function "Track.insertClip"')
        self._extend_eval("insertClip({}, {})".format(_format_object_to_es(clipProjectItem), _format_object_to_es(time)))

    def overwriteClip(self, clipProjectItem, time):
        """
        :type clipProjectItem: ProjectItem
        :type time: Object
        """
        self.check_type(clipProjectItem, ProjectItem, 'arg "clipProjectItem" of function "Track.overwriteClip"')
        self._extend_eval("overwriteClip({}, {})".format(_format_object_to_es(clipProjectItem), _format_object_to_es(time)))

class TrackItemCollection(PymiereCollection):
    def __init__(self, pymiere_id, numItems):
        super(TrackItemCollection, self).__init__(pymiere_id, "numItems")

    def __getitem__(self, index):
        return TrackItem(**super(TrackItemCollection, self).__getitem__(index))

class TrackItem(PymiereObject):
    def __init__(self, pymiere_id=None, duration=None, start=None, end=None, inPoint=None, outPoint=None, type=None, mediaType=None, projectItem=None, name=None, matchName=None, nodeId=None, components=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'duration':duration, 'start':start, 'end':end, 'inPoint':inPoint, 'outPoint':outPoint, 'type':type, 'mediaType':mediaType, 'projectItem':projectItem, 'name':name, 'matchName':matchName, 'nodeId':nodeId, 'components':components})
        super(TrackItem, self).__init__(pymiere_id)
        self.__duration = duration
        self.__start = start
        self.__end = end
        self.__inPoint = inPoint
        self.__outPoint = outPoint
        self.__type = type
        self.__mediaType = mediaType
        self.__projectItem = projectItem
        self.__name = name
        self.__matchName = matchName
        self.__nodeId = nodeId
        self.__components = components

    # ----- PROPERTIES -----
    @property
    def duration(self):
        self.__duration = Time(**self._extend_eval('duration'))
        return self.__duration
    @duration.setter
    def duration(self, duration):
        raise AttributeError("Attribute 'duration' is read-only")

    @property
    def start(self):
        self.__start = Time(**self._extend_eval('start'))
        return self.__start
    @start.setter
    def start(self, start):
        self.check_type(start, Time, 'TrackItem.start')
        self._extend_eval("start = {}".format(_format_object_to_es(start)))
        self.__start = start

    @property
    def end(self):
        self.__end = Time(**self._extend_eval('end'))
        return self.__end
    @end.setter
    def end(self, end):
        self.check_type(end, Time, 'TrackItem.end')
        self._extend_eval("end = {}".format(_format_object_to_es(end)))
        self.__end = end

    @property
    def inPoint(self):
        self.__inPoint = Time(**self._extend_eval('inPoint'))
        return self.__inPoint
    @inPoint.setter
    def inPoint(self, inPoint):
        self.check_type(inPoint, Time, 'TrackItem.inPoint')
        self._extend_eval("inPoint = {}".format(_format_object_to_es(inPoint)))
        self.__inPoint = inPoint

    @property
    def outPoint(self):
        self.__outPoint = Time(**self._extend_eval('outPoint'))
        return self.__outPoint
    @outPoint.setter
    def outPoint(self, outPoint):
        self.check_type(outPoint, Time, 'TrackItem.outPoint')
        self._extend_eval("outPoint = {}".format(_format_object_to_es(outPoint)))
        self.__outPoint = outPoint

    @property
    def type(self):
        self.__type = self._extend_eval('type')
        return self.__type
    @type.setter
    def type(self, type):
        raise AttributeError("Attribute 'type' is read-only")

    @property
    def mediaType(self):
        self.__mediaType = self._extend_eval('mediaType')
        return self.__mediaType
    @mediaType.setter
    def mediaType(self, mediaType):
        raise AttributeError("Attribute 'mediaType' is read-only")

    @property
    def projectItem(self):
        self.__projectItem = ProjectItem(**self._extend_eval('projectItem'))
        return self.__projectItem
    @projectItem.setter
    def projectItem(self, projectItem):
        self.check_type(projectItem, ProjectItem, 'TrackItem.projectItem')
        self._extend_eval("projectItem = {}".format(_format_object_to_es(projectItem)))
        self.__projectItem = projectItem

    @property
    def name(self):
        self.__name = self._extend_eval('name')
        return self.__name
    @name.setter
    def name(self, name):
        self._extend_eval("name = {}".format(_format_object_to_es(name)))
        self.__name = name

    @property
    def matchName(self):
        self.__matchName = self._extend_eval('matchName')
        return self.__matchName
    @matchName.setter
    def matchName(self, matchName):
        raise AttributeError("Attribute 'matchName' is read-only")

    @property
    def nodeId(self):
        self.__nodeId = self._extend_eval('nodeId')
        return self.__nodeId
    @nodeId.setter
    def nodeId(self, nodeId):
        raise AttributeError("Attribute 'nodeId' is read-only")

    @property
    def components(self):
        self.__components = ComponentCollection(**self._extend_eval('components'))
        return self.__components
    @components.setter
    def components(self, components):
        raise AttributeError("Attribute 'components' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "TrackItem.bind"')
        self.check_type(function, any, 'arg "function" of function "TrackItem.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "TrackItem.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "TrackItem.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "TrackItem.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "TrackItem.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def isSelected(self):
        return self._extend_eval("isSelected()")

    def setSelected(self, isSelected, updateUI):
        """
        :type isSelected: float
        :type updateUI: float
        """
        self.check_type(isSelected, float, 'arg "isSelected" of function "TrackItem.setSelected"')
        self.check_type(updateUI, float, 'arg "updateUI" of function "TrackItem.setSelected"')
        self._extend_eval("setSelected({}, {})".format(_format_object_to_es(isSelected), _format_object_to_es(updateUI)))

    def getLinkedItems(self):
        return TrackItemCollection(**self._extend_eval("getLinkedItems()"))

    def isMGT(self):
        return self._extend_eval("isMGT()")

    def getMGTComponent(self):
        return Component(**self._extend_eval("getMGTComponent()"))

    def isAdjustmentLayer(self):
        return self._extend_eval("isAdjustmentLayer()")

    def getSpeed(self):
        return self._extend_eval("getSpeed()")

    def isSpeedReversed(self):
        return self._extend_eval("isSpeedReversed()")

    def getMatchName(self):
        return self._extend_eval("getMatchName()")

    def remove(self, inRipple, inAlignToVideo):
        """
        :type inRipple: bool
        :type inAlignToVideo: bool
        """
        self.check_type(inRipple, bool, 'arg "inRipple" of function "TrackItem.remove"')
        self.check_type(inAlignToVideo, bool, 'arg "inAlignToVideo" of function "TrackItem.remove"')
        return self._extend_eval("remove({}, {})".format(_format_object_to_es(inRipple), _format_object_to_es(inAlignToVideo)))

class SequenceSettings(PymiereObject):
    def __init__(self, pymiere_id=None, editingMode=None, videoFrameRate=None, videoFrameWidth=None, videoFrameHeight=None, videoPixelAspectRatio=None, videoFieldType=None, videoDisplayFormat=None, audioChannelType=None, audioChannelCount=None, audioSampleRate=None, audioDisplayFormat=None, previewFileFormat=None, previewCodec=None, previewFrameWidth=None, previewFrameHeight=None, maximumBitDepth=None, maximumRenderQuality=None, compositeLinearColor=None, vrProjection=None, vrLayout=None, vrHorzCapturedView=None, vrVertCapturedView=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'editingMode':editingMode, 'videoFrameRate':videoFrameRate, 'videoFrameWidth':videoFrameWidth, 'videoFrameHeight':videoFrameHeight, 'videoPixelAspectRatio':videoPixelAspectRatio, 'videoFieldType':videoFieldType, 'videoDisplayFormat':videoDisplayFormat, 'audioChannelType':audioChannelType, 'audioChannelCount':audioChannelCount, 'audioSampleRate':audioSampleRate, 'audioDisplayFormat':audioDisplayFormat, 'previewFileFormat':previewFileFormat, 'previewCodec':previewCodec, 'previewFrameWidth':previewFrameWidth, 'previewFrameHeight':previewFrameHeight, 'maximumBitDepth':maximumBitDepth, 'maximumRenderQuality':maximumRenderQuality, 'compositeLinearColor':compositeLinearColor, 'vrProjection':vrProjection, 'vrLayout':vrLayout, 'vrHorzCapturedView':vrHorzCapturedView, 'vrVertCapturedView':vrVertCapturedView})
        super(SequenceSettings, self).__init__(pymiere_id)
        self.__editingMode = editingMode
        self.__videoFrameRate = videoFrameRate
        self.__videoFrameWidth = videoFrameWidth
        self.__videoFrameHeight = videoFrameHeight
        self.__videoPixelAspectRatio = videoPixelAspectRatio
        self.__videoFieldType = videoFieldType
        self.__videoDisplayFormat = videoDisplayFormat
        self.__audioChannelType = audioChannelType
        self.__audioChannelCount = audioChannelCount
        self.__audioSampleRate = audioSampleRate
        self.__audioDisplayFormat = audioDisplayFormat
        self.__previewFileFormat = previewFileFormat
        self.__previewCodec = previewCodec
        self.__previewFrameWidth = previewFrameWidth
        self.__previewFrameHeight = previewFrameHeight
        self.__maximumBitDepth = maximumBitDepth
        self.__maximumRenderQuality = maximumRenderQuality
        self.__compositeLinearColor = compositeLinearColor
        self.__vrProjection = vrProjection
        self.__vrLayout = vrLayout
        self.__vrHorzCapturedView = vrHorzCapturedView
        self.__vrVertCapturedView = vrVertCapturedView

    # ----- PROPERTIES -----
    @property
    def editingMode(self):
        self.__editingMode = self._extend_eval('editingMode')
        return self.__editingMode
    @editingMode.setter
    def editingMode(self, editingMode):
        self._extend_eval("editingMode = {}".format(_format_object_to_es(editingMode)))
        self.__editingMode = editingMode

    @property
    def videoFrameRate(self):
        self.__videoFrameRate = Time(**self._extend_eval('videoFrameRate'))
        return self.__videoFrameRate
    @videoFrameRate.setter
    def videoFrameRate(self, videoFrameRate):
        self.check_type(videoFrameRate, Time, 'SequenceSettings.videoFrameRate')
        self._extend_eval("videoFrameRate = {}".format(_format_object_to_es(videoFrameRate)))
        self.__videoFrameRate = videoFrameRate

    @property
    def videoFrameWidth(self):
        self.__videoFrameWidth = self._extend_eval('videoFrameWidth')
        return self.__videoFrameWidth
    @videoFrameWidth.setter
    def videoFrameWidth(self, videoFrameWidth):
        self._extend_eval("videoFrameWidth = {}".format(_format_object_to_es(videoFrameWidth)))
        self.__videoFrameWidth = videoFrameWidth

    @property
    def videoFrameHeight(self):
        self.__videoFrameHeight = self._extend_eval('videoFrameHeight')
        return self.__videoFrameHeight
    @videoFrameHeight.setter
    def videoFrameHeight(self, videoFrameHeight):
        self._extend_eval("videoFrameHeight = {}".format(_format_object_to_es(videoFrameHeight)))
        self.__videoFrameHeight = videoFrameHeight

    @property
    def videoPixelAspectRatio(self):
        self.__videoPixelAspectRatio = self._extend_eval('videoPixelAspectRatio')
        return self.__videoPixelAspectRatio
    @videoPixelAspectRatio.setter
    def videoPixelAspectRatio(self, videoPixelAspectRatio):
        self._extend_eval("videoPixelAspectRatio = {}".format(_format_object_to_es(videoPixelAspectRatio)))
        self.__videoPixelAspectRatio = videoPixelAspectRatio

    @property
    def videoFieldType(self):
        self.__videoFieldType = self._extend_eval('videoFieldType')
        return self.__videoFieldType
    @videoFieldType.setter
    def videoFieldType(self, videoFieldType):
        self._extend_eval("videoFieldType = {}".format(_format_object_to_es(videoFieldType)))
        self.__videoFieldType = videoFieldType

    @property
    def videoDisplayFormat(self):
        self.__videoDisplayFormat = self._extend_eval('videoDisplayFormat')
        return self.__videoDisplayFormat
    @videoDisplayFormat.setter
    def videoDisplayFormat(self, videoDisplayFormat):
        self._extend_eval("videoDisplayFormat = {}".format(_format_object_to_es(videoDisplayFormat)))
        self.__videoDisplayFormat = videoDisplayFormat

    @property
    def audioChannelType(self):
        self.__audioChannelType = self._extend_eval('audioChannelType')
        return self.__audioChannelType
    @audioChannelType.setter
    def audioChannelType(self, audioChannelType):
        self._extend_eval("audioChannelType = {}".format(_format_object_to_es(audioChannelType)))
        self.__audioChannelType = audioChannelType

    @property
    def audioChannelCount(self):
        self.__audioChannelCount = self._extend_eval('audioChannelCount')
        return self.__audioChannelCount
    @audioChannelCount.setter
    def audioChannelCount(self, audioChannelCount):
        self._extend_eval("audioChannelCount = {}".format(_format_object_to_es(audioChannelCount)))
        self.__audioChannelCount = audioChannelCount

    @property
    def audioSampleRate(self):
        self.__audioSampleRate = Time(**self._extend_eval('audioSampleRate'))
        return self.__audioSampleRate
    @audioSampleRate.setter
    def audioSampleRate(self, audioSampleRate):
        self.check_type(audioSampleRate, Time, 'SequenceSettings.audioSampleRate')
        self._extend_eval("audioSampleRate = {}".format(_format_object_to_es(audioSampleRate)))
        self.__audioSampleRate = audioSampleRate

    @property
    def audioDisplayFormat(self):
        self.__audioDisplayFormat = self._extend_eval('audioDisplayFormat')
        return self.__audioDisplayFormat
    @audioDisplayFormat.setter
    def audioDisplayFormat(self, audioDisplayFormat):
        self._extend_eval("audioDisplayFormat = {}".format(_format_object_to_es(audioDisplayFormat)))
        self.__audioDisplayFormat = audioDisplayFormat

    @property
    def previewFileFormat(self):
        self.__previewFileFormat = self._extend_eval('previewFileFormat')
        return self.__previewFileFormat
    @previewFileFormat.setter
    def previewFileFormat(self, previewFileFormat):
        self._extend_eval("previewFileFormat = {}".format(_format_object_to_es(previewFileFormat)))
        self.__previewFileFormat = previewFileFormat

    @property
    def previewCodec(self):
        self.__previewCodec = self._extend_eval('previewCodec')
        return self.__previewCodec
    @previewCodec.setter
    def previewCodec(self, previewCodec):
        self._extend_eval("previewCodec = {}".format(_format_object_to_es(previewCodec)))
        self.__previewCodec = previewCodec

    @property
    def previewFrameWidth(self):
        self.__previewFrameWidth = self._extend_eval('previewFrameWidth')
        return self.__previewFrameWidth
    @previewFrameWidth.setter
    def previewFrameWidth(self, previewFrameWidth):
        self._extend_eval("previewFrameWidth = {}".format(_format_object_to_es(previewFrameWidth)))
        self.__previewFrameWidth = previewFrameWidth

    @property
    def previewFrameHeight(self):
        self.__previewFrameHeight = self._extend_eval('previewFrameHeight')
        return self.__previewFrameHeight
    @previewFrameHeight.setter
    def previewFrameHeight(self, previewFrameHeight):
        self._extend_eval("previewFrameHeight = {}".format(_format_object_to_es(previewFrameHeight)))
        self.__previewFrameHeight = previewFrameHeight

    @property
    def maximumBitDepth(self):
        self.__maximumBitDepth = self._extend_eval('maximumBitDepth')
        return self.__maximumBitDepth
    @maximumBitDepth.setter
    def maximumBitDepth(self, maximumBitDepth):
        self._extend_eval("maximumBitDepth = {}".format(_format_object_to_es(maximumBitDepth)))
        self.__maximumBitDepth = maximumBitDepth

    @property
    def maximumRenderQuality(self):
        self.__maximumRenderQuality = self._extend_eval('maximumRenderQuality')
        return self.__maximumRenderQuality
    @maximumRenderQuality.setter
    def maximumRenderQuality(self, maximumRenderQuality):
        self._extend_eval("maximumRenderQuality = {}".format(_format_object_to_es(maximumRenderQuality)))
        self.__maximumRenderQuality = maximumRenderQuality

    @property
    def compositeLinearColor(self):
        self.__compositeLinearColor = self._extend_eval('compositeLinearColor')
        return self.__compositeLinearColor
    @compositeLinearColor.setter
    def compositeLinearColor(self, compositeLinearColor):
        self._extend_eval("compositeLinearColor = {}".format(_format_object_to_es(compositeLinearColor)))
        self.__compositeLinearColor = compositeLinearColor

    @property
    def vrProjection(self):
        self.__vrProjection = self._extend_eval('vrProjection')
        return self.__vrProjection
    @vrProjection.setter
    def vrProjection(self, vrProjection):
        self._extend_eval("vrProjection = {}".format(_format_object_to_es(vrProjection)))
        self.__vrProjection = vrProjection

    @property
    def vrLayout(self):
        self.__vrLayout = self._extend_eval('vrLayout')
        return self.__vrLayout
    @vrLayout.setter
    def vrLayout(self, vrLayout):
        self._extend_eval("vrLayout = {}".format(_format_object_to_es(vrLayout)))
        self.__vrLayout = vrLayout

    @property
    def vrHorzCapturedView(self):
        self.__vrHorzCapturedView = self._extend_eval('vrHorzCapturedView')
        return self.__vrHorzCapturedView
    @vrHorzCapturedView.setter
    def vrHorzCapturedView(self, vrHorzCapturedView):
        self._extend_eval("vrHorzCapturedView = {}".format(_format_object_to_es(vrHorzCapturedView)))
        self.__vrHorzCapturedView = vrHorzCapturedView

    @property
    def vrVertCapturedView(self):
        self.__vrVertCapturedView = self._extend_eval('vrVertCapturedView')
        return self.__vrVertCapturedView
    @vrVertCapturedView.setter
    def vrVertCapturedView(self, vrVertCapturedView):
        self._extend_eval("vrVertCapturedView = {}".format(_format_object_to_es(vrVertCapturedView)))
        self.__vrVertCapturedView = vrVertCapturedView


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "SequenceSettings.bind"')
        self.check_type(function, any, 'arg "function" of function "SequenceSettings.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "SequenceSettings.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "SequenceSettings.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "SequenceSettings.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "SequenceSettings.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

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
        self._extend_eval("start = {}".format(_format_object_to_es(start)))
        self.__start = start

    @property
    def end(self):
        self.__end = Time(**self._extend_eval('end'))
        return self.__end
    @end.setter
    def end(self, end):
        self.check_type(end, Time, 'Marker.end')
        self._extend_eval("end = {}".format(_format_object_to_es(end)))
        self.__end = end

    @property
    def type(self):
        self.__type = self._extend_eval('type')
        return self.__type
    @type.setter
    def type(self, type):
        self._extend_eval("type = {}".format(_format_object_to_es(type)))
        self.__type = type

    @property
    def name(self):
        self.__name = self._extend_eval('name')
        return self.__name
    @name.setter
    def name(self, name):
        self._extend_eval("name = {}".format(_format_object_to_es(name)))
        self.__name = name

    @property
    def comments(self):
        self.__comments = self._extend_eval('comments')
        return self.__comments
    @comments.setter
    def comments(self, comments):
        self._extend_eval("comments = {}".format(_format_object_to_es(comments)))
        self.__comments = comments

    @property
    def guid(self):
        self.__guid = self._extend_eval('guid')
        return self.__guid
    @guid.setter
    def guid(self, guid):
        raise AttributeError("Attribute 'guid' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Marker.bind"')
        self.check_type(function, any, 'arg "function" of function "Marker.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Marker.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Marker.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "Marker.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "Marker.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

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
        self._extend_eval("setTypeAsWebLink({}, {})".format(_format_object_to_es(url), _format_object_to_es(frameTarget)))

    def getWebLinkURL(self):
        return self._extend_eval("getWebLinkURL()")

    def getWebLinkFrameTarget(self):
        return self._extend_eval("getWebLinkFrameTarget()")

    def setColorByIndex(self, arg1):
        """
        :type arg1: float
        """
        self.check_type(arg1, float, 'arg "arg1" of function "Marker.setColorByIndex"')
        self._extend_eval("setColorByIndex({})".format(_format_object_to_es(arg1)))

    def getColorByIndex(self):
        return self._extend_eval("getColorByIndex()")

class Component(PymiereObject):
    def __init__(self, pymiere_id=None, displayName=None, matchName=None, properties=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'displayName':displayName, 'matchName':matchName, 'properties':properties})
        super(Component, self).__init__(pymiere_id)
        self.__displayName = displayName
        self.__matchName = matchName
        self.__properties = properties

    # ----- PROPERTIES -----
    @property
    def displayName(self):
        self.__displayName = self._extend_eval('displayName')
        return self.__displayName
    @displayName.setter
    def displayName(self, displayName):
        raise AttributeError("Attribute 'displayName' is read-only")

    @property
    def matchName(self):
        self.__matchName = self._extend_eval('matchName')
        return self.__matchName
    @matchName.setter
    def matchName(self, matchName):
        raise AttributeError("Attribute 'matchName' is read-only")

    @property
    def properties(self):
        self.__properties = ComponentParamCollection(**self._extend_eval('properties'))
        return self.__properties
    @properties.setter
    def properties(self, properties):
        raise AttributeError("Attribute 'properties' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Component.bind"')
        self.check_type(function, any, 'arg "function" of function "Component.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Component.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Component.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "Component.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "Component.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

class ComponentParamCollection(PymiereCollection):
    def __init__(self, pymiere_id, numItems):
        super(ComponentParamCollection, self).__init__(pymiere_id, "numItems")

    def __getitem__(self, index):
        return ComponentParam(**super(ComponentParamCollection, self).__getitem__(index))

class Dollar(PymiereObject):
    def __init__(self, pymiere_id=None, error=None, version=None, build=None, buildDate=None, stack=None, level=None, flags=None, strict=None, locale=None, localize=None, decimalPoint=None, memCache=None, appEncoding=None, screens=None, os=None, fileName=None, line=None, hiresTimer=None, dictionary=None, engineName=None, includePath=None, _pymiere=None, _jsxFunctions=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'error':error, 'version':version, 'build':build, 'buildDate':buildDate, 'stack':stack, 'level':level, 'flags':flags, 'strict':strict, 'locale':locale, 'localize':localize, 'decimalPoint':decimalPoint, 'memCache':memCache, 'appEncoding':appEncoding, 'screens':screens, 'os':os, 'fileName':fileName, 'line':line, 'hiresTimer':hiresTimer, 'dictionary':dictionary, 'engineName':engineName, 'includePath':includePath, '_pymiere':_pymiere, '_jsxFunctions':_jsxFunctions})
        super(Dollar, self).__init__(pymiere_id)
        self.__error = error
        self.__version = version
        self.__build = build
        self.__buildDate = buildDate
        self.__stack = stack
        self.__level = level
        self.__flags = flags
        self.__strict = strict
        self.__locale = locale
        self.__localize = localize
        self.__decimalPoint = decimalPoint
        self.__memCache = memCache
        self.__appEncoding = appEncoding
        self.__screens = screens
        self.__os = os
        self.__fileName = fileName
        self.__line = line
        self.__hiresTimer = hiresTimer
        self.__dictionary = dictionary
        self.__engineName = engineName
        self.__includePath = includePath
        self.___pymiere = _pymiere
        self.___jsxFunctions = _jsxFunctions

    # ----- PROPERTIES -----
    @property
    def error(self):
        """The current runtime error"""
        self.__error = Error(**self._extend_eval('error'))
        return self.__error
    @error.setter
    def error(self, error):
        self.check_type(error, Error, '$.error')
        self._extend_eval("error = {}".format(_format_object_to_es(error)))
        self.__error = error

    @property
    def version(self):
        """The ExtendScript version"""
        self.__version = self._extend_eval('version')
        return self.__version
    @version.setter
    def version(self, version):
        raise AttributeError("Attribute 'version' is read-only")

    @property
    def build(self):
        """The ExtendScript build number"""
        self.__build = self._extend_eval('build')
        return self.__build
    @build.setter
    def build(self, build):
        raise AttributeError("Attribute 'build' is read-only")

    @property
    def buildDate(self):
        """The ExtendScript build date"""
        self.__buildDate = Date(**self._extend_eval('buildDate'))
        return self.__buildDate
    @buildDate.setter
    def buildDate(self, buildDate):
        raise AttributeError("Attribute 'buildDate' is read-only")

    @property
    def stack(self):
        """The current stack trace"""
        self.__stack = self._extend_eval('stack')
        return self.__stack
    @stack.setter
    def stack(self, stack):
        raise AttributeError("Attribute 'stack' is read-only")

    @property
    def level(self):
        """The debugging level"""
        self.__level = self._extend_eval('level')
        return self.__level
    @level.setter
    def level(self, level):
        self._extend_eval("level = {}".format(_format_object_to_es(level)))
        self.__level = level

    @property
    def flags(self):
        """Debugging flags"""
        self.__flags = self._extend_eval('flags')
        return self.__flags
    @flags.setter
    def flags(self, flags):
        self._extend_eval("flags = {}".format(_format_object_to_es(flags)))
        self.__flags = flags

    @property
    def strict(self):
        """Set to true to enforce strict mode"""
        self.__strict = self._extend_eval('strict')
        return self.__strict
    @strict.setter
    def strict(self, strict):
        self._extend_eval("strict = {}".format(_format_object_to_es(strict)))
        self.__strict = strict

    @property
    def locale(self):
        """The current locale"""
        self.__locale = self._extend_eval('locale')
        return self.__locale
    @locale.setter
    def locale(self, locale):
        self._extend_eval("locale = {}".format(_format_object_to_es(locale)))
        self.__locale = locale

    @property
    def localize(self):
        """Set to true to enable auto-localization"""
        self.__localize = self._extend_eval('localize')
        return self.__localize
    @localize.setter
    def localize(self, localize):
        self._extend_eval("localize = {}".format(_format_object_to_es(localize)))
        self.__localize = localize

    @property
    def decimalPoint(self):
        """The decimal point separator"""
        self.__decimalPoint = self._extend_eval('decimalPoint')
        return self.__decimalPoint
    @decimalPoint.setter
    def decimalPoint(self, decimalPoint):
        raise AttributeError("Attribute 'decimalPoint' is read-only")

    @property
    def memCache(self):
        """The memory cache size"""
        self.__memCache = self._extend_eval('memCache')
        return self.__memCache
    @memCache.setter
    def memCache(self, memCache):
        self._extend_eval("memCache = {}".format(_format_object_to_es(memCache)))
        self.__memCache = memCache

    @property
    def appEncoding(self):
        """The default application encoding"""
        self.__appEncoding = self._extend_eval('appEncoding')
        return self.__appEncoding
    @appEncoding.setter
    def appEncoding(self, appEncoding):
        self._extend_eval("appEncoding = {}".format(_format_object_to_es(appEncoding)))
        self.__appEncoding = appEncoding

    @property
    def screens(self):
        """An array of rectangles"""
        self.__screens = _format_object_to_py(self._extend_eval('screens'))
        return self.__screens
    @screens.setter
    def screens(self, screens):
        raise AttributeError("Attribute 'screens' is read-only")

    @property
    def os(self):
        """The operating system"""
        self.__os = self._extend_eval('os')
        return self.__os
    @os.setter
    def os(self, os):
        raise AttributeError("Attribute 'os' is read-only")

    @property
    def fileName(self):
        """The file name of the current script"""
        self.__fileName = self._extend_eval('fileName')
        return self.__fileName
    @fileName.setter
    def fileName(self, fileName):
        raise AttributeError("Attribute 'fileName' is read-only")

    @property
    def line(self):
        """The current line number of the current script"""
        self.__line = self._extend_eval('line')
        return self.__line
    @line.setter
    def line(self, line):
        raise AttributeError("Attribute 'line' is read-only")

    @property
    def hiresTimer(self):
        """The elapsed time in microseconds since the last access"""
        self.__hiresTimer = self._extend_eval('hiresTimer')
        return self.__hiresTimer
    @hiresTimer.setter
    def hiresTimer(self, hiresTimer):
        raise AttributeError("Attribute 'hiresTimer' is read-only")

    @property
    def dictionary(self):
        """The application's main dictionary"""
        self.__dictionary = Dictionary(**self._extend_eval('dictionary'))
        return self.__dictionary
    @dictionary.setter
    def dictionary(self, dictionary):
        raise AttributeError("Attribute 'dictionary' is read-only")

    @property
    def engineName(self):
        """The name of the current engine if set"""
        self.__engineName = self._extend_eval('engineName')
        return self.__engineName
    @engineName.setter
    def engineName(self, engineName):
        raise AttributeError("Attribute 'engineName' is read-only")

    @property
    def includePath(self):
        """The path for include files"""
        self.__includePath = self._extend_eval('includePath')
        return self.__includePath
    @includePath.setter
    def includePath(self, includePath):
        raise AttributeError("Attribute 'includePath' is read-only")

    @property
    def _pymiere(self):
        self.___pymiere = _format_object_to_py(self._extend_eval('_pymiere'))
        return self.___pymiere
    @_pymiere.setter
    def _pymiere(self, _pymiere):
        self._extend_eval("_pymiere = {}".format(_format_object_to_es(_pymiere)))
        self.___pymiere = _pymiere

    @property
    def _jsxFunctions(self):
        self.___jsxFunctions = _format_object_to_py(self._extend_eval('_jsxFunctions'))
        return self.___jsxFunctions
    @_jsxFunctions.setter
    def _jsxFunctions(self, _jsxFunctions):
        self._extend_eval("_jsxFunctions = {}".format(_format_object_to_es(_jsxFunctions)))
        self.___jsxFunctions = _jsxFunctions


    # ----- FUNCTIONS -----
    def about(self):
        """
        An About box
        """
        return self._extend_eval("about()")

    def toString(self):
        """
        Converts this object to a string
        """
        return self._extend_eval("toString()")

    def write(self):
        """
        Prints text
        """
        self._extend_eval("write()")

    def writeln(self):
        """
        Prints text
        """
        self._extend_eval("writeln()")

    def bp(self):
        """
        Breaks execution
        """
        self._extend_eval("bp()")

    def getenv(self, name):
        """
        Returns an environment variable
        :param name: The name of the variable
        :type name: str
        """
        self.check_type(name, str, 'arg "name" of function "$.getenv"')
        return self._extend_eval("getenv({})".format(_format_object_to_es(name)))

    def setenv(self, key, value):
        """
        :type key: str
        :param value: Sets an environment variable
        :type value: str
        """
        self.check_type(key, str, 'arg "key" of function "$.setenv"')
        self.check_type(value, str, 'arg "value" of function "$.setenv"')
        return self._extend_eval("setenv({}, {})".format(_format_object_to_es(key), _format_object_to_es(value)))

    def sleep(self, msecs):
        """
        Sleep
        :param msecs: Number of milliseconds to sleep
        :type msecs: float
        """
        self.check_type(msecs, float, 'arg "msecs" of function "$.sleep"')
        self._extend_eval("sleep({})".format(_format_object_to_es(msecs)))

    def colorPicker(self, color):
        """
        :param color: Picks a color; the argument is the color or -1.
        :type color: float
        """
        self.check_type(color, float, 'arg "color" of function "$.colorPicker"')
        return self._extend_eval("colorPicker({})".format(_format_object_to_es(color)))

    def evalFile(self, file):
        """
        Loads and evaluates a file
        :param file: The file to load
        :type file: File
        """
        self.check_type(file, File, 'arg "file" of function "$.evalFile"')
        return self._extend_eval("evalFile({})".format(_format_object_to_es(file)))

    def list(self, arg1):
        """
        :type arg1: any
        """
        self.check_type(arg1, any, 'arg "arg1" of function "$.list"')
        return _format_object_to_py(self._extend_eval("list({})".format(_format_object_to_es(arg1))))

    def listLO(self, arg1):
        """
        :type arg1: any
        """
        self.check_type(arg1, any, 'arg "arg1" of function "$.listLO"')
        return _format_object_to_py(self._extend_eval("listLO({})".format(_format_object_to_es(arg1))))

    def summary(self):
        return _format_object_to_py(self._extend_eval("summary()"))

    def gc(self):
        """
        Runs the garbage collector
        """
        self._extend_eval("gc()")

class Error(PymiereObject):
    def __init__(self, pymiere_id=None, number=None, fileName=None, line=None, source=None, start=None, end=None, message=None, name=None, description=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'number':number, 'fileName':fileName, 'line':line, 'source':source, 'start':start, 'end':end, 'message':message, 'name':name, 'description':description})
        super(Error, self).__init__(pymiere_id)
        self.__number = number
        self.__fileName = fileName
        self.__line = line
        self.__source = source
        self.__start = start
        self.__end = end
        self.__message = message
        self.__name = name
        self.__description = description

    # ----- PROPERTIES -----
    @property
    def number(self):
        self.__number = self._extend_eval('number')
        return self.__number
    @number.setter
    def number(self, number):
        self._extend_eval("number = {}".format(_format_object_to_es(number)))
        self.__number = number

    @property
    def fileName(self):
        self.__fileName = self._extend_eval('fileName')
        return self.__fileName
    @fileName.setter
    def fileName(self, fileName):
        self._extend_eval("fileName = {}".format(_format_object_to_es(fileName)))
        self.__fileName = fileName

    @property
    def line(self):
        self.__line = self._extend_eval('line')
        return self.__line
    @line.setter
    def line(self, line):
        self._extend_eval("line = {}".format(_format_object_to_es(line)))
        self.__line = line

    @property
    def source(self):
        self.__source = self._extend_eval('source')
        return self.__source
    @source.setter
    def source(self, source):
        self._extend_eval("source = {}".format(_format_object_to_es(source)))
        self.__source = source

    @property
    def start(self):
        self.__start = self._extend_eval('start')
        return self.__start
    @start.setter
    def start(self, start):
        self._extend_eval("start = {}".format(_format_object_to_es(start)))
        self.__start = start

    @property
    def end(self):
        self.__end = self._extend_eval('end')
        return self.__end
    @end.setter
    def end(self, end):
        self._extend_eval("end = {}".format(_format_object_to_es(end)))
        self.__end = end

    @property
    def message(self):
        self.__message = self._extend_eval('message')
        return self.__message
    @message.setter
    def message(self, message):
        self._extend_eval("message = {}".format(_format_object_to_es(message)))
        self.__message = message

    @property
    def name(self):
        self.__name = self._extend_eval('name')
        return self.__name
    @name.setter
    def name(self, name):
        self._extend_eval("name = {}".format(_format_object_to_es(name)))
        self.__name = name

    @property
    def description(self):
        self.__description = self._extend_eval('description')
        return self.__description
    @description.setter
    def description(self, description):
        self._extend_eval("description = {}".format(_format_object_to_es(description)))
        self.__description = description


    # ----- FUNCTIONS -----
    def toString(self):
        return self._extend_eval("toString()")

    def toSource(self):
        return self._extend_eval("toSource()")

class Dictionary(PymiereObject):
    def __init__(self, pymiere_id=None, ):
        self.check_init_args({'pymiere_id':pymiere_id, })
        super(Dictionary, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def getGroups(self):
        """
        Gets the list of groups.
        """
        return Array(**self._extend_eval("getGroups()"))

    def getClasses(self):
        """
        Gets a list of classes by group.
        """
        return Array(**self._extend_eval("getClasses()"))

    def getClass(self):
        """
        Gets a class description.
        """
        return _format_object_to_py(self._extend_eval("getClass()"))

    def toXML(self, prefix):
        """
        Converts a Dictionary instance to XML.
        :param prefix: The href prefix.
        :type prefix: str
        """
        self.check_type(prefix, str, 'arg "prefix" of function "Dictionary.toXML"')
        return _format_object_to_py(self._extend_eval("toXML({})".format(_format_object_to_es(prefix))))

class ComponentParam(PymiereObject):
    def __init__(self, pymiere_id=None, displayName=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'displayName':displayName})
        super(ComponentParam, self).__init__(pymiere_id)
        self.__displayName = displayName

    # ----- PROPERTIES -----
    @property
    def displayName(self):
        self.__displayName = self._extend_eval('displayName')
        return self.__displayName
    @displayName.setter
    def displayName(self, displayName):
        raise AttributeError("Attribute 'displayName' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ComponentParam.bind"')
        self.check_type(function, any, 'arg "function" of function "ComponentParam.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ComponentParam.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "ComponentParam.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "ComponentParam.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "ComponentParam.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def areKeyframesSupported(self):
        return self._extend_eval("areKeyframesSupported()")

    def isEmpty(self):
        return self._extend_eval("isEmpty()")

    def isTimeVarying(self):
        return self._extend_eval("isTimeVarying()")

    def setTimeVarying(self, isTimeVarying):
        """
        :type isTimeVarying: bool
        """
        self.check_type(isTimeVarying, bool, 'arg "isTimeVarying" of function "ComponentParam.setTimeVarying"')
        self._extend_eval("setTimeVarying({})".format(_format_object_to_es(isTimeVarying)))

    def findNearestKey(self, time, threshold):
        """
        :type time: Object
        :type threshold: Object
        """
        return Time(**self._extend_eval("findNearestKey({}, {})".format(_format_object_to_es(time), _format_object_to_es(threshold))))

    def findPreviousKey(self, time):
        """
        :type time: Object
        """
        return Time(**self._extend_eval("findPreviousKey({})".format(_format_object_to_es(time))))

    def findNextKey(self, time):
        """
        :type time: Object
        """
        return Time(**self._extend_eval("findNextKey({})".format(_format_object_to_es(time))))

    def getKeys(self):
        self._extend_eval("getKeys()")

    def addKey(self, time):
        """
        :type time: Object
        """
        self._extend_eval("addKey({})".format(_format_object_to_es(time)))

    def removeKey(self, time):
        """
        :type time: Object
        """
        self._extend_eval("removeKey({})".format(_format_object_to_es(time)))

    def removeKeyRange(self, startTime, stopTime):
        """
        :type startTime: Object
        :type stopTime: Object
        """
        self._extend_eval("removeKeyRange({}, {})".format(_format_object_to_es(startTime), _format_object_to_es(stopTime)))

    def keyExistsAtTime(self, time):
        """
        :type time: Object
        """
        return self._extend_eval("keyExistsAtTime({})".format(_format_object_to_es(time)))

    def getValue(self):
        self._extend_eval("getValue()")

    def setValue(self):
        return self._extend_eval("setValue()")

    def getColorValue(self):
        self._extend_eval("getColorValue()")

    def setColorValue(self, arg1):
        """
        :type arg1: any
        """
        self.check_type(arg1, any, 'arg "arg1" of function "ComponentParam.setColorValue"')
        return self._extend_eval("setColorValue({})".format(_format_object_to_es(arg1)))

    def getValueAtKey(self, time):
        """
        :type time: Object
        """
        self._extend_eval("getValueAtKey({})".format(_format_object_to_es(time)))

    def setValueAtKey(self, time):
        """
        :type time: Object
        """
        return self._extend_eval("setValueAtKey({})".format(_format_object_to_es(time)))

    def getValueAtTime(self, time):
        """
        :type time: Object
        """
        self._extend_eval("getValueAtTime({})".format(_format_object_to_es(time)))

    def setInterpolationTypeAtKey(self, time):
        """
        :type time: Object
        """
        return self._extend_eval("setInterpolationTypeAtKey({})".format(_format_object_to_es(time)))

class Exporter(PymiereObject):
    def __init__(self, pymiere_id=None, name=None, classID=None, fileType=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'name':name, 'classID':classID, 'fileType':fileType})
        super(Exporter, self).__init__(pymiere_id)
        self.__name = name
        self.__classID = classID
        self.__fileType = fileType

    # ----- PROPERTIES -----
    @property
    def name(self):
        self.__name = self._extend_eval('name')
        return self.__name
    @name.setter
    def name(self, name):
        raise AttributeError("Attribute 'name' is read-only")

    @property
    def classID(self):
        self.__classID = self._extend_eval('classID')
        return self.__classID
    @classID.setter
    def classID(self, classID):
        raise AttributeError("Attribute 'classID' is read-only")

    @property
    def fileType(self):
        self.__fileType = self._extend_eval('fileType')
        return self.__fileType
    @fileType.setter
    def fileType(self, fileType):
        raise AttributeError("Attribute 'fileType' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Exporter.bind"')
        self.check_type(function, any, 'arg "function" of function "Exporter.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Exporter.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "Exporter.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "Exporter.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "Exporter.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def getPresets(self):
        self._extend_eval("getPresets()")

class EncoderPreset(PymiereObject):
    def __init__(self, pymiere_id=None, name=None, matchName=None):
        self.check_init_args({'pymiere_id':pymiere_id, 'name':name, 'matchName':matchName})
        super(EncoderPreset, self).__init__(pymiere_id)
        self.__name = name
        self.__matchName = matchName

    # ----- PROPERTIES -----
    @property
    def name(self):
        self.__name = self._extend_eval('name')
        return self.__name
    @name.setter
    def name(self, name):
        raise AttributeError("Attribute 'name' is read-only")

    @property
    def matchName(self):
        self.__matchName = self._extend_eval('matchName')
        return self.__matchName
    @matchName.setter
    def matchName(self, matchName):
        raise AttributeError("Attribute 'matchName' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self.check_type(eventName, str, 'arg "eventName" of function "EncoderPreset.bind"')
        self.check_type(function, any, 'arg "function" of function "EncoderPreset.bind"')
        self._extend_eval("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self.check_type(eventName, str, 'arg "eventName" of function "EncoderPreset.unbind"')
        self._extend_eval("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self.check_type(eventName, str, 'arg "eventName" of function "EncoderPreset.setTimeout"')
        self.check_type(function, any, 'arg "function" of function "EncoderPreset.setTimeout"')
        self.check_type(milliseconds, float, 'arg "milliseconds" of function "EncoderPreset.setTimeout"')
        self._extend_eval("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def writeToFile(self, outputFilePath):
        """
        :type outputFilePath: str
        """
        self.check_type(outputFilePath, str, 'arg "outputFilePath" of function "EncoderPreset.writeToFile"')
        return self._extend_eval("writeToFile({})".format(_format_object_to_es(outputFilePath)))
