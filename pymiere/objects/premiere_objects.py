from pymiere.core import PymiereBaseObject, PymiereBaseCollection, Array, _format_object_to_py, _format_object_to_es, ExtendScriptError


class Application(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Application, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def version(self):
        return self._eval_on_this_object('version')
    @version.setter
    def version(self, version):
        raise AttributeError("Attribute 'version' is read-only")

    @property
    def build(self):
        return self._eval_on_this_object('build')
    @build.setter
    def build(self, build):
        raise AttributeError("Attribute 'build' is read-only")

    @property
    def csxs(self):
        return _format_object_to_py(self._eval_on_this_object('csxs'))
    @csxs.setter
    def csxs(self, csxs):
        raise AttributeError("Attribute 'csxs' is read-only")

    @property
    def getPProPrefPath(self):
        return self._eval_on_this_object('getPProPrefPath')
    @getPProPrefPath.setter
    def getPProPrefPath(self, getPProPrefPath):
        raise AttributeError("Attribute 'getPProPrefPath' is read-only")

    @property
    def getPProSystemPrefPath(self):
        return self._eval_on_this_object('getPProSystemPrefPath')
    @getPProSystemPrefPath.setter
    def getPProSystemPrefPath(self, getPProSystemPrefPath):
        raise AttributeError("Attribute 'getPProSystemPrefPath' is read-only")

    """ This is the current active project. """
    @property
    def project(self):
        kwargs = self._eval_on_this_object('project')
        return Project(**kwargs) if kwargs else None
    @project.setter
    def project(self, project):
        self._check_type(project, Project, 'Application.project')
        self._eval_on_this_object("project = {}".format(_format_object_to_es(project)))

    @property
    def projects(self):
        kwargs = self._eval_on_this_object('projects')
        return ProjectCollection(**kwargs) if kwargs else None
    @projects.setter
    def projects(self, projects):
        raise AttributeError("Attribute 'projects' is read-only")

    @property
    def anywhere(self):
        kwargs = self._eval_on_this_object('anywhere')
        return Anywhere(**kwargs) if kwargs else None
    @anywhere.setter
    def anywhere(self, anywhere):
        raise AttributeError("Attribute 'anywhere' is read-only")

    @property
    def encoder(self):
        kwargs = self._eval_on_this_object('encoder')
        return Encoder(**kwargs) if kwargs else None
    @encoder.setter
    def encoder(self, encoder):
        raise AttributeError("Attribute 'encoder' is read-only")

    @property
    def properties(self):
        kwargs = self._eval_on_this_object('properties')
        return Properties(**kwargs) if kwargs else None
    @properties.setter
    def properties(self, properties):
        raise AttributeError("Attribute 'properties' is read-only")

    @property
    def sourceMonitor(self):
        kwargs = self._eval_on_this_object('sourceMonitor')
        return SourceMonitor(**kwargs) if kwargs else None
    @sourceMonitor.setter
    def sourceMonitor(self, sourceMonitor):
        raise AttributeError("Attribute 'sourceMonitor' is read-only")

    @property
    def projectManager(self):
        kwargs = self._eval_on_this_object('projectManager')
        return ProjectManager(**kwargs) if kwargs else None
    @projectManager.setter
    def projectManager(self, projectManager):
        raise AttributeError("Attribute 'projectManager' is read-only")

    @property
    def userGuid(self):
        return self._eval_on_this_object('userGuid')
    @userGuid.setter
    def userGuid(self, userGuid):
        raise AttributeError("Attribute 'userGuid' is read-only")

    @property
    def path(self):
        return self._eval_on_this_object('path')
    @path.setter
    def path(self, path):
        raise AttributeError("Attribute 'path' is read-only")

    @property
    def getAppPrefPath(self):
        return self._eval_on_this_object('getAppPrefPath')
    @getAppPrefPath.setter
    def getAppPrefPath(self, getAppPrefPath):
        raise AttributeError("Attribute 'getAppPrefPath' is read-only")

    @property
    def getAppSystemPrefPath(self):
        return self._eval_on_this_object('getAppSystemPrefPath')
    @getAppSystemPrefPath.setter
    def getAppSystemPrefPath(self, getAppSystemPrefPath):
        raise AttributeError("Attribute 'getAppSystemPrefPath' is read-only")

    @property
    def metadata(self):
        kwargs = self._eval_on_this_object('metadata')
        return Metadata(**kwargs) if kwargs else None
    @metadata.setter
    def metadata(self, metadata):
        raise AttributeError("Attribute 'metadata' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Application.bind"')
        self._check_type(function, any, 'arg "function" of function "Application.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Application.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Application.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "Application.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "Application.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def isDocumentOpen(self):
        return self._eval_on_this_object("isDocumentOpen()")

    def getWorkspaces(self):
        return Array(**self._eval_on_this_object("getWorkspaces()"))

    def setWorkspace(self, workspace):
        """
        :type workspace: str
        """
        self._check_type(workspace, str, 'arg "workspace" of function "Application.setWorkspace"')
        return self._eval_on_this_object("setWorkspace({})".format(_format_object_to_es(workspace)))

    def isDocument(self, filePath):
        """
        Checks whether file specified is a doc 
        :param filePath: This is the path to be checked
        :type filePath: str
        """
        self._check_type(filePath, str, 'arg "filePath" of function "Application.isDocument"')
        return self._eval_on_this_object("isDocument({})".format(_format_object_to_es(filePath)))

    def openDocument(self, filePath):
        self._check_type(filePath, str, 'arg "filePath" of function "Application.openDocument"')
        return self._eval_on_this_object("openDocument({})".format(_format_object_to_es(filePath)))

    def quit(self):
        self._eval_on_this_object("quit()")

    def trace(self, message):
        """
        :type message: str
        """
        self._check_type(message, str, 'arg "message" of function "Application.trace"')
        self._eval_on_this_object("trace({})".format(_format_object_to_es(message)))

    def write(self, arg1):
        """
        :type arg1: any
        """
        self._check_type(arg1, any, 'arg "arg1" of function "Application.write"')
        self._eval_on_this_object("write({})".format(_format_object_to_es(arg1)))

    def openFCPXML(self):
        return self._eval_on_this_object("openFCPXML()")

    def setSDKEventMessage(self, value, eventType):
        """
        :type value: str
        :type eventType: str
        """
        self._check_type(value, str, 'arg "value" of function "Application.setSDKEventMessage"')
        self._check_type(eventType, str, 'arg "eventType" of function "Application.setSDKEventMessage"')
        return self._eval_on_this_object("setSDKEventMessage({}, {})".format(_format_object_to_es(value), _format_object_to_es(eventType)))

    def setScratchDiskPath(self, value, type):
        """
        :type value: str
        :type type: str
        """
        self._check_type(value, str, 'arg "value" of function "Application.setScratchDiskPath"')
        self._check_type(type, str, 'arg "type" of function "Application.setScratchDiskPath"')
        self._eval_on_this_object("setScratchDiskPath({}, {})".format(_format_object_to_es(value), _format_object_to_es(type)))

    def broadcastPrefsChanged(self, preferencesThatChanged):
        """
        :type preferencesThatChanged: str
        """
        self._check_type(preferencesThatChanged, str, 'arg "preferencesThatChanged" of function "Application.broadcastPrefsChanged"')
        return self._eval_on_this_object("broadcastPrefsChanged({})".format(_format_object_to_es(preferencesThatChanged)))

    def setExtensionPersistent(self, extensionID, state):
        """
        :type extensionID: str
        :type state: float
        """
        self._check_type(extensionID, str, 'arg "extensionID" of function "Application.setExtensionPersistent"')
        self._check_type(state, float, 'arg "state" of function "Application.setExtensionPersistent"')
        self._eval_on_this_object("setExtensionPersistent({}, {})".format(_format_object_to_es(extensionID), _format_object_to_es(state)))

    def getEnableProxies(self):
        return self._eval_on_this_object("getEnableProxies()")

    def setEnableProxies(self, enable):
        """
        :type enable: float
        """
        self._check_type(enable, float, 'arg "enable" of function "Application.setEnableProxies"')
        return self._eval_on_this_object("setEnableProxies({})".format(_format_object_to_es(enable)))

    def showCursor(self, enable):
        """
        :type enable: bool
        """
        self._check_type(enable, bool, 'arg "enable" of function "Application.showCursor"')
        self._eval_on_this_object("showCursor({})".format(_format_object_to_es(enable)))

    def getProjectViewIDs(self):
        self._eval_on_this_object("getProjectViewIDs()")

    def getProjectFromViewID(self, viewID):
        """
        :type viewID: str
        """
        self._check_type(viewID, str, 'arg "viewID" of function "Application.getProjectFromViewID"')
        return Project(**self._eval_on_this_object("getProjectFromViewID({})".format(_format_object_to_es(viewID))))

    def getProjectViewSelection(self, viewID):
        """
        :type viewID: str
        """
        self._check_type(viewID, str, 'arg "viewID" of function "Application.getProjectViewSelection"')
        self._eval_on_this_object("getProjectViewSelection({})".format(_format_object_to_es(viewID)))

    def setProjectViewSelection(self, viewID):
        """
        :type viewID: str
        """
        self._check_type(viewID, str, 'arg "viewID" of function "Application.setProjectViewSelection"')
        self._eval_on_this_object("setProjectViewSelection({})".format(_format_object_to_es(viewID)))

    def getConstant(self, name):
        """
        :type name: str
        """
        self._check_type(name, str, 'arg "name" of function "Application.getConstant"')
        return self._eval_on_this_object("getConstant({})".format(_format_object_to_es(name)))

    def refresh(self):
        self._eval_on_this_object("refresh()")

    def setEnableTranscodeOnIngest(self, inEnable):
        """
        :type inEnable: bool
        """
        self._check_type(inEnable, bool, 'arg "inEnable" of function "Application.setEnableTranscodeOnIngest"')
        self._eval_on_this_object("setEnableTranscodeOnIngest({})".format(_format_object_to_es(inEnable)))

    def getCCXUserJSONData(self):
        return self._eval_on_this_object("getCCXUserJSONData()")

    def newProject(self, newFilePath):
        """
        Create a new empty project/document saved at the newFilePath location

        :param newFilePath: where to save the new project (filepath to .prproj)
        :type newFilePath: str
        :return: success
        """
        # only available from Premiere Pro 14.0 (2020)
        self._check_version("14.0", "Application.newProject", alternative_msg="Use pymiere.objects.qe.newProject(newFilePath) for older versions")
        self._check_type(newFilePath, str, 'arg "newProject" of function "Application.newProject"')
        return bool(self._eval_on_this_object("newProject({})".format(_format_object_to_es(newFilePath))))

    def enableQE(self):
        return self._eval_on_this_object("enableQE()")


class Project(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Project, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def documentID(self):
        return self._eval_on_this_object('documentID')
    @documentID.setter
    def documentID(self, documentID):
        raise AttributeError("Attribute 'documentID' is read-only")

    @property
    def name(self):
        return self._eval_on_this_object('name')
    @name.setter
    def name(self, name):
        raise AttributeError("Attribute 'name' is read-only")

    @property
    def path(self):
        return self._eval_on_this_object('path')
    @path.setter
    def path(self, path):
        raise AttributeError("Attribute 'path' is read-only")

    @property
    def rootItem(self):
        kwargs = self._eval_on_this_object('rootItem')
        return ProjectItem(**kwargs) if kwargs else None
    @rootItem.setter
    def rootItem(self, rootItem):
        raise AttributeError("Attribute 'rootItem' is read-only")

    @property
    def sequences(self):
        kwargs = self._eval_on_this_object('sequences')
        return SequenceCollection(**kwargs) if kwargs else None
    @sequences.setter
    def sequences(self, sequences):
        raise AttributeError("Attribute 'sequences' is read-only")

    """ f """
    @property
    def activeSequence(self):
        kwargs = self._eval_on_this_object('activeSequence')
        return Sequence(**kwargs) if kwargs else None
    @activeSequence.setter
    def activeSequence(self, activeSequence):
        self._check_type(activeSequence, Sequence, 'Project.activeSequence')
        self._eval_on_this_object("activeSequence = {}".format(_format_object_to_es(activeSequence)))

    @property
    def isCloudProject(self):
        return self._eval_on_this_object('isCloudProject')
    @isCloudProject.setter
    def isCloudProject(self, isCloudProject):
        raise AttributeError("Attribute 'isCloudProject' is read-only")

    @property
    def cloudProjectLocalID(self):
        return self._eval_on_this_object('cloudProjectLocalID')
    @cloudProjectLocalID.setter
    def cloudProjectLocalID(self, cloudProjectLocalID):
        raise AttributeError("Attribute 'cloudProjectLocalID' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Project.bind"')
        self._check_type(function, any, 'arg "function" of function "Project.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Project.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Project.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "Project.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "Project.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def openSequence(self, sequenceID):
        """
        :type sequenceID: str
        """
        self._check_type(sequenceID, str, 'arg "sequenceID" of function "Project.openSequence"')
        return self._eval_on_this_object("openSequence({})".format(_format_object_to_es(sequenceID)))

    def importFiles(self, arrayOfFilePathsToImport, suppressUI, targetBin, importAsNumberedStills):
        """
        Imports files into the project. 
        :param arrayOfFilePathsToImport: An array of paths to files to import
        :param suppressUI: optional; if true, suppress any warnings, translation reports, or errors.
        :param projectBin: optional; if present, the bin into which to import the new media.
        :param importAsNumberedStill: optional if present, interprets the file paths as a series of numbered stills.
        """
        self._check_type(arrayOfFilePathsToImport, list, 'arg "arrayOfFilePathsToImport" of function "Project.importFiles"')
        self._check_type(suppressUI, bool, 'arg "suppressUI" of function "Project.importFiles"')
        self._check_type(targetBin, ProjectItem, 'arg "targetBin" of function "Project.importFiles"')
        self._check_type(importAsNumberedStills, bool, 'arg "importAsNumberedStills" of function "Project.importFiles"')
        return self._eval_on_this_object("importFiles({}, {}, {}, {})".format(_format_object_to_es(arrayOfFilePathsToImport), _format_object_to_es(suppressUI), _format_object_to_es(targetBin), _format_object_to_es(importAsNumberedStills)))

    def importSequences(self, arg1):
        """
        Imports sequences from a project. 
        :param projectPath: Path to project from which to import sequences.
        :param sequences: An array of sequence IDs to import, from the project.
        :type arg1: any
        """
        self._check_type(arg1, any, 'arg "arg1" of function "Project.importSequences"')
        return self._eval_on_this_object("importSequences({})".format(_format_object_to_es(arg1)))

    def importAllAEComps(self, pathOfContainingProject, optionalTargetBin):
        """
         :type pathOfContainingProject: str
         :type optionalTargetBin: ProjectItem
         """
        self._check_type(pathOfContainingProject, str, 'arg "pathOfContainingProject" of function "Project.importAEComps"')
        self._check_type(optionalTargetBin, ProjectItem, 'arg "optionalTargetBin" of function "Project.importAEComps"')
        return self._eval_on_this_object("importAEComps({},{})".format(_format_object_to_es(pathOfContainingProject), _format_object_to_es(optionalTargetBin)))

    def importAEComps(self, pathOfContainingProject, arrayOfCompNames, optionalTargetBin):
        """
        :type pathOfContainingProject: str
        :type arrayOfCompNames: list
        :type optionalTargetBin: ProjectItem
        """
        self._check_type(pathOfContainingProject, str, 'arg "pathOfContainingProject" of function "Project.importAEComps"')
        self._check_type(arrayOfCompNames, list, 'arg "arrayOfCompNames" of function "Project.importAEComps"')
        self._check_type(optionalTargetBin, ProjectItem, 'arg "optionalTargetBin" of function "Project.importAEComps"')
        return self._eval_on_this_object("importAEComps({},{},{})".format(_format_object_to_es(pathOfContainingProject), _format_object_to_es(arrayOfCompNames), _format_object_to_es(optionalTargetBin)))

    def createNewSequence(self, sequenceName, placeholderID):
        """
        :type sequenceName: str
        :type placeholderID: str
        """
        self._check_type(sequenceName, str, 'arg "sequenceName" of function "Project.createNewSequence"')
        self._check_type(placeholderID, str, 'arg "placeholderID" of function "Project.createNewSequence"')
        self._eval_on_this_object("createNewSequence({}, {})".format(_format_object_to_es(sequenceName), _format_object_to_es(placeholderID)))

    def createNewSequenceFromClips(self, sequenceName, arrayOfProjectItems, destinationBin=None):
        """
        Creates a new Sequence object with the given name, in the specified destination bin,
        and sequentially inserts project items into it.

        :type sequenceName: str
        :type arrayOfProjectItems: list of ProjectItem
        :type destinationBin: ProjectItem
        :return: Sequence object
        """
        return Sequence(**self._eval_on_this_object("createNewSequenceFromClips({}, {}, {})".format(_format_object_to_es(sequenceName), _format_object_to_es(arrayOfProjectItems), _format_object_to_es(destinationBin))))

    def deleteSequence(self, sequence):
        """
        :type sequence: Sequence
        """
        self._check_type(sequence, Sequence, 'arg "sequence" of function "Project.deleteSequence"')
        return self._eval_on_this_object("deleteSequence({})".format(_format_object_to_es(sequence)))

    def exportFinalCutProXML(self, exportPath, suppressUI):
        """
        :type exportPath: str
        :type suppressUI: float
        """
        self._check_type(exportPath, str, 'arg "exportPath" of function "Project.exportFinalCutProXML"')
        self._check_type(suppressUI, float, 'arg "suppressUI" of function "Project.exportFinalCutProXML"')
        return self._eval_on_this_object("exportFinalCutProXML({}, {})".format(_format_object_to_es(exportPath), _format_object_to_es(suppressUI)))

    def exportTimeline(self, exportControllerName):
        """
        :type exportControllerName: str
        """
        self._check_type(exportControllerName, str, 'arg "exportControllerName" of function "Project.exportTimeline"')
        return self._eval_on_this_object("exportTimeline({})".format(_format_object_to_es(exportControllerName)))

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
        self._check_type(sequence, Sequence, 'arg "sequence" of function "Project.exportOMF"')
        self._check_type(filePath, str, 'arg "filePath" of function "Project.exportOMF"')
        self._check_type(OMFTitle, str, 'arg "OMFTitle" of function "Project.exportOMF"')
        self._check_type(sampleRate, float, 'arg "sampleRate" of function "Project.exportOMF"')
        self._check_type(bitsPerSample, float, 'arg "bitsPerSample" of function "Project.exportOMF"')
        self._check_type(audioEncapsulated, float, 'arg "audioEncapsulated" of function "Project.exportOMF"')
        self._check_type(audioFileFormat, float, 'arg "audioFileFormat" of function "Project.exportOMF"')
        self._check_type(trimAudioFiles, float, 'arg "trimAudioFiles" of function "Project.exportOMF"')
        self._check_type(handleFrames, float, 'arg "handleFrames" of function "Project.exportOMF"')
        self._check_type(includePan, float, 'arg "includePan" of function "Project.exportOMF"')
        return self._eval_on_this_object("exportOMF({}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(_format_object_to_es(sequence), _format_object_to_es(filePath), _format_object_to_es(OMFTitle), _format_object_to_es(sampleRate), _format_object_to_es(bitsPerSample), _format_object_to_es(audioEncapsulated), _format_object_to_es(audioFileFormat), _format_object_to_es(trimAudioFiles), _format_object_to_es(handleFrames), _format_object_to_es(includePan)))

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
        self._check_type(sequence, Sequence, 'arg "sequence" of function "Project.exportAAF"')
        self._check_type(filePath, str, 'arg "filePath" of function "Project.exportAAF"')
        self._check_type(mixDownVideo, float, 'arg "mixDownVideo" of function "Project.exportAAF"')
        self._check_type(explodeToMono, float, 'arg "explodeToMono" of function "Project.exportAAF"')
        self._check_type(sampleRate, float, 'arg "sampleRate" of function "Project.exportAAF"')
        self._check_type(bitsPerSample, float, 'arg "bitsPerSample" of function "Project.exportAAF"')
        self._check_type(embedAudio, float, 'arg "embedAudio" of function "Project.exportAAF"')
        self._check_type(audioFileFormat, float, 'arg "audioFileFormat" of function "Project.exportAAF"')
        self._check_type(trimSources, float, 'arg "trimSources" of function "Project.exportAAF"')
        self._check_type(handleFrames, float, 'arg "handleFrames" of function "Project.exportAAF"')
        return self._eval_on_this_object("exportAAF({}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(_format_object_to_es(sequence), _format_object_to_es(filePath), _format_object_to_es(mixDownVideo), _format_object_to_es(explodeToMono), _format_object_to_es(sampleRate), _format_object_to_es(bitsPerSample), _format_object_to_es(embedAudio), _format_object_to_es(audioFileFormat), _format_object_to_es(trimSources), _format_object_to_es(handleFrames)))

    def saveAs(self, saveAsPath):
        """
        :type saveAsPath: str
        """
        self._check_type(saveAsPath, str, 'arg "saveAsPath" of function "Project.saveAs"')
        return self._eval_on_this_object("saveAs({})".format(_format_object_to_es(saveAsPath)))

    def save(self):
        self._eval_on_this_object("save()")

    def pauseGrowing(self, pausedOrNot):
        """
        :type pausedOrNot: float
        """
        self._check_type(pausedOrNot, float, 'arg "pausedOrNot" of function "Project.pauseGrowing"')
        return self._eval_on_this_object("pauseGrowing({})".format(_format_object_to_es(pausedOrNot)))

    def closeDocument(self):
        return self._eval_on_this_object("closeDocument()")

    def placeAsset(self, arg1):
        """
        :type arg1: any
        """
        self._check_type(arg1, any, 'arg "arg1" of function "Project.placeAsset"')
        return self._eval_on_this_object("placeAsset({})".format(_format_object_to_es(arg1)))

    def addPropertyToProjectMetadataSchema(self, name, label, type):
        """
        :type name: str
        :type label: str
        :type type: float
        """
        self._check_type(name, str, 'arg "name" of function "Project.addPropertyToProjectMetadataSchema"')
        self._check_type(label, str, 'arg "label" of function "Project.addPropertyToProjectMetadataSchema"')
        self._check_type(type, float, 'arg "type" of function "Project.addPropertyToProjectMetadataSchema"')
        return self._eval_on_this_object("addPropertyToProjectMetadataSchema({}, {}, {})".format(_format_object_to_es(name), _format_object_to_es(label), _format_object_to_es(type)))

    def getInsertionBin(self):
        return ProjectItem(**self._eval_on_this_object("getInsertionBin()"))

    def getProjectPanelMetadata(self):
        self._eval_on_this_object("getProjectPanelMetadata()")

    def setProjectPanelMetadata(self):
        self._eval_on_this_object("setProjectPanelMetadata()")

    def setScratchDiskPath(self, value, type):
        """
        :type value: str
        :type type: str
        """
        self._check_type(value, str, 'arg "value" of function "Project.setScratchDiskPath"')
        self._check_type(type, str, 'arg "type" of function "Project.setScratchDiskPath"')
        self._eval_on_this_object("setScratchDiskPath({}, {})".format(_format_object_to_es(value), _format_object_to_es(type)))

    def consolidateDuplicates(self):
        self._eval_on_this_object("consolidateDuplicates()")

    def setEnableTranscodeOnIngest(self, inEnable):
        """
        :type inEnable: bool
        """
        self._check_type(inEnable, bool, 'arg "inEnable" of function "Project.setEnableTranscodeOnIngest"')
        return self._eval_on_this_object("setEnableTranscodeOnIngest({})".format(_format_object_to_es(inEnable)))


class ProjectItem(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(ProjectItem, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def children(self):
        kwargs = self._eval_on_this_object('children')
        return ProjectItemCollection(**kwargs) if kwargs else None
    @children.setter
    def children(self, children):
        raise AttributeError("Attribute 'children' is read-only")

    @property
    def name(self):
        return self._eval_on_this_object('name')
    @name.setter
    def name(self, name):
        self._eval_on_this_object("name = {}".format(_format_object_to_es(name)))

    @property
    def treePath(self):
        return self._eval_on_this_object('treePath')
    @treePath.setter
    def treePath(self, treePath):
        raise AttributeError("Attribute 'treePath' is read-only")

    @property
    def type(self):
        return self._eval_on_this_object('type')
    @type.setter
    def type(self, type):
        raise AttributeError("Attribute 'type' is read-only")

    @property
    def nodeId(self):
        return self._eval_on_this_object('nodeId')
    @nodeId.setter
    def nodeId(self, nodeId):
        raise AttributeError("Attribute 'nodeId' is read-only")

    @property
    def videoComponents(self):
        kwargs = self._eval_on_this_object('videoComponents')
        return ComponentCollection(**kwargs) if kwargs else None
    @videoComponents.setter
    def videoComponents(self, videoComponents):
        raise AttributeError("Attribute 'videoComponents' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ProjectItem.bind"')
        self._check_type(function, any, 'arg "function" of function "ProjectItem.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ProjectItem.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ProjectItem.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "ProjectItem.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "ProjectItem.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def getFootageInterpretation(self):
        return FootageInterpretation(**self._eval_on_this_object("getFootageInterpretation()"))

    def setFootageInterpretation(self, interpretFootage):
        """
        :type interpretFootage: FootageInterpretation
        """
        self._check_type(interpretFootage, FootageInterpretation, 'arg "interpretFootage" of function "ProjectItem.setFootageInterpretation"')
        return self._eval_on_this_object("setFootageInterpretation({})".format(_format_object_to_es(interpretFootage)))

    def createSmartBin(self, name, query):
        """
        :type name: str
        :type query: str
        """
        self._check_type(name, str, 'arg "name" of function "ProjectItem.createSmartBin"')
        self._check_type(query, str, 'arg "query" of function "ProjectItem.createSmartBin"')
        self._eval_on_this_object("createSmartBin({}, {})".format(_format_object_to_es(name), _format_object_to_es(query)))

    def createBin(self, name):
        """
        :type name: str
        """
        self._check_type(name, str, 'arg "name" of function "ProjectItem.createBin"')
        return ProjectItem(**self._eval_on_this_object("createBin({})".format(_format_object_to_es(name))))

    def renameBin(self, name):
        """
        :type name: str
        """
        self._check_type(name, str, 'arg "name" of function "ProjectItem.renameBin"')
        return self._eval_on_this_object("renameBin({})".format(_format_object_to_es(name)))

    def deleteBin(self):
        self._eval_on_this_object("deleteBin()")

    def moveBin(self, destination):
        """
        :type destination: ProjectItem
        """
        self._check_type(destination, ProjectItem, 'arg "destination" of function "ProjectItem.moveBin"')
        self._eval_on_this_object("moveBin({})".format(_format_object_to_es(destination)))

    def getXMPMetadata(self):
        return self._eval_on_this_object("getXMPMetadata()")

    def setXMPMetadata(self, buffer):
        """
        :type buffer: str
        """
        self._check_type(buffer, str, 'arg "buffer" of function "ProjectItem.setXMPMetadata"')
        return self._eval_on_this_object("setXMPMetadata({})".format(_format_object_to_es(buffer)))

    def getProjectMetadata(self):
        return self._eval_on_this_object("getProjectMetadata()")

    def setProjectMetadata(self, buffer):
        """
        :type buffer: str
        """
        self._check_type(buffer, str, 'arg "buffer" of function "ProjectItem.setProjectMetadata"')
        self._eval_on_this_object("setProjectMetadata({})".format(_format_object_to_es(buffer)))

    def getMarkers(self):
        return MarkerCollection(**self._eval_on_this_object("getMarkers()"))

    def refreshMedia(self):
        return self._eval_on_this_object("refreshMedia()")

    def getMediaPath(self):
        return self._eval_on_this_object("getMediaPath()")

    def canChangeMediaPath(self):
        return self._eval_on_this_object("canChangeMediaPath()")

    def changeMediaPath(self, mediaPath, overrideChecks):
        """
        :type mediaPath: str
        :type overrideChecks: bool
        """
        self._check_type(mediaPath, str, 'arg "mediaPath" of function "ProjectItem.changeMediaPath"')
        self._check_type(overrideChecks, bool, 'arg "overrideChecks" of function "ProjectItem.changeMediaPath"')
        return self._eval_on_this_object("changeMediaPath({}, {})".format(_format_object_to_es(mediaPath), _format_object_to_es(overrideChecks)))

    def select(self):
        self._eval_on_this_object("select()")

    def setOverridePixelAspectRatio(self, numerator, denominator):
        """
        :type numerator: float
        :type denominator: float
        """
        self._check_type(numerator, float, 'arg "numerator" of function "ProjectItem.setOverridePixelAspectRatio"')
        self._check_type(denominator, float, 'arg "denominator" of function "ProjectItem.setOverridePixelAspectRatio"')
        return self._eval_on_this_object("setOverridePixelAspectRatio({}, {})".format(_format_object_to_es(numerator), _format_object_to_es(denominator)))

    def setOverrideFrameRate(self, frameRate):
        """
        :type frameRate: float
        """
        self._check_type(frameRate, float, 'arg "frameRate" of function "ProjectItem.setOverrideFrameRate"')
        return self._eval_on_this_object("setOverrideFrameRate({})".format(_format_object_to_es(frameRate)))

    def setScaleToFrameSize(self):
        self._eval_on_this_object("setScaleToFrameSize()")

    def createSubClip(self, name, startTime, endTime, hasHardBoundaries, takeVideo, takeAudio):
        """
        :type name: str
        :type startTime: Object
        :type endTime: Object
        :type hasHardBoundaries: float
        :type takeVideo: float
        :type takeAudio: float
        """
        self._check_type(name, str, 'arg "name" of function "ProjectItem.createSubClip"')
        self._check_type(hasHardBoundaries, float, 'arg "hasHardBoundaries" of function "ProjectItem.createSubClip"')
        self._check_type(takeVideo, float, 'arg "takeVideo" of function "ProjectItem.createSubClip"')
        self._check_type(takeAudio, float, 'arg "takeAudio" of function "ProjectItem.createSubClip"')
        return ProjectItem(**self._eval_on_this_object("createSubClip({}, {}, {}, {}, {}, {})".format(_format_object_to_es(name), _format_object_to_es(startTime), _format_object_to_es(endTime), _format_object_to_es(hasHardBoundaries), _format_object_to_es(takeVideo), _format_object_to_es(takeAudio))))

    def findItemsMatchingMediaPath(self, matchString, ignoreSubclips):
        """
        :type matchString: str
        :type ignoreSubclips: float
        """
        self._check_type(matchString, str, 'arg "matchString" of function "ProjectItem.findItemsMatchingMediaPath"')
        self._check_type(ignoreSubclips, float, 'arg "ignoreSubclips" of function "ProjectItem.findItemsMatchingMediaPath"')
        return Array(**self._eval_on_this_object("findItemsMatchingMediaPath({}, {})".format(_format_object_to_es(matchString), _format_object_to_es(ignoreSubclips))))

    def attachProxy(self, mediaPath, isHiRes):
        """
        :type mediaPath: str
        :type isHiRes: float
        """
        self._check_type(mediaPath, str, 'arg "mediaPath" of function "ProjectItem.attachProxy"')
        self._check_type(isHiRes, float, 'arg "isHiRes" of function "ProjectItem.attachProxy"')
        return self._eval_on_this_object("attachProxy({}, {})".format(_format_object_to_es(mediaPath), _format_object_to_es(isHiRes)))

    def hasProxy(self):
        return self._eval_on_this_object("hasProxy()")

    def getProxyPath(self):
        return self._eval_on_this_object("getProxyPath()")

    def canProxy(self):
        return self._eval_on_this_object("canProxy()")

    def isSequence(self):
        """
        Returns whether the projectItem represents a sequence.@returns true, if projectItem is a sequence.
        """
        return self._eval_on_this_object("isSequence()")

    def startTime(self):
        return Time(**self._eval_on_this_object("startTime()"))

    def setStartTime(self, arg1):
        """
        :type arg1: Object
        """
        self._eval_on_this_object("setStartTime({})".format(_format_object_to_es(arg1)))

    def clearInPoint(self, mediaType):
        """
        :type mediaType: float
        """
        self._check_type(mediaType, float, 'arg "mediaType" of function "ProjectItem.clearInPoint"')
        self._eval_on_this_object("clearInPoint({})".format(_format_object_to_es(mediaType)))

    def setInPoint(self, arg1, mediaType):
        """
        :type arg1: Object
        :type mediaType: float
        """
        self._check_type(mediaType, float, 'arg "mediaType" of function "ProjectItem.setInPoint"')
        self._eval_on_this_object("setInPoint({}, {})".format(_format_object_to_es(arg1), _format_object_to_es(mediaType)))

    def getInPoint(self, mediaType):
        """
        :type mediaType: float
        """
        self._check_type(mediaType, float, 'arg "mediaType" of function "ProjectItem.getInPoint"')
        return Time(**self._eval_on_this_object("getInPoint({})".format(_format_object_to_es(mediaType))))

    def clearOutPoint(self, mediaType):
        """
        :type mediaType: float
        """
        self._check_type(mediaType, float, 'arg "mediaType" of function "ProjectItem.clearOutPoint"')
        self._eval_on_this_object("clearOutPoint({})".format(_format_object_to_es(mediaType)))

    def setOutPoint(self, arg1, mediaType):
        """
        :type arg1: Object
        :type mediaType: float
        """
        self._check_type(mediaType, float, 'arg "mediaType" of function "ProjectItem.setOutPoint"')
        self._eval_on_this_object("setOutPoint({}, {})".format(_format_object_to_es(arg1), _format_object_to_es(mediaType)))

    def getOutPoint(self, mediaType):
        """
        :type mediaType: float
        """
        self._check_type(mediaType, float, 'arg "mediaType" of function "ProjectItem.getOutPoint"')
        return Time(**self._eval_on_this_object("getOutPoint({})".format(_format_object_to_es(mediaType))))

    def setColorLabel(self, color):
        """
        :param color: color id
        :type color: int
        """
        self._eval_on_this_object("setColorLabel({})".format(_format_object_to_es(color)))

    def getColorLabel(self):
        return self._eval_on_this_object("getColorLabel()")

    def isOffline(self):
        return self._eval_on_this_object("isOffline()")

    def setOffline(self):
        return self._eval_on_this_object("setOffline()")

    def saveProjectSnapshot(self):
        return self._eval_on_this_object("saveProjectSnapshot()")

    def isAdjustmentLayer(self):
        return self._eval_on_this_object("isAdjustmentLayer()")

    def isReference(self):
        return self._eval_on_this_object("isReference()")


class ProjectItemCollection(PymiereBaseCollection):
    def __init__(self, pymiere_id):
        super(ProjectItemCollection, self).__init__(pymiere_id, "numItems")

    def __getitem__(self, index):
        return ProjectItem(**super(ProjectItemCollection, self).__getitem__(index))

    def __iter__(self):
        return iter([self.__getitem__(i) for i in range(len(self))])


class SequenceCollection(PymiereBaseCollection):
    def __init__(self, pymiere_id):
        super(SequenceCollection, self).__init__(pymiere_id, "numSequences")

    def __getitem__(self, index):
        return Sequence(**super(SequenceCollection, self).__getitem__(index))

    def __iter__(self):
        return iter([self.__getitem__(i) for i in range(len(self))])


class Sequence(PymiereBaseObject):
    """ A sequence. """
    def __init__(self, pymiere_id=None):
        super(Sequence, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    """ Sequence ID """
    @property
    def id(self):
        return self._eval_on_this_object('id')
    @id.setter
    def id(self, id):
        raise AttributeError("Attribute 'id' is read-only")

    """ Permanent ID of the sequence, within its project. """
    @property
    def sequenceID(self):
        return self._eval_on_this_object('sequenceID')
    @sequenceID.setter
    def sequenceID(self, sequenceID):
        raise AttributeError("Attribute 'sequenceID' is read-only")

    """ Name (writable). """
    @property
    def name(self):
        return self._eval_on_this_object('name')
    @name.setter
    def name(self, name):
        self._eval_on_this_object("name = {}".format(_format_object_to_es(name)))

    """ A collection of the sequence's audio tracks. """
    @property
    def audioTracks(self):
        kwargs = self._eval_on_this_object('audioTracks')
        return TrackCollection(**kwargs) if kwargs else None
    @audioTracks.setter
    def audioTracks(self, audioTracks):
        raise AttributeError("Attribute 'audioTracks' is read-only")

    @property
    def videoTracks(self):
        kwargs = self._eval_on_this_object('videoTracks')
        return TrackCollection(**kwargs) if kwargs else None
    @videoTracks.setter
    def videoTracks(self, videoTracks):
        raise AttributeError("Attribute 'videoTracks' is read-only")

    """ Width """
    @property
    def frameSizeHorizontal(self):
        return self._eval_on_this_object('frameSizeHorizontal')
    @frameSizeHorizontal.setter
    def frameSizeHorizontal(self, frameSizeHorizontal):
        raise AttributeError("Attribute 'frameSizeHorizontal' is read-only")

    """ Height """
    @property
    def frameSizeVertical(self):
        return self._eval_on_this_object('frameSizeVertical')
    @frameSizeVertical.setter
    def frameSizeVertical(self, frameSizeVertical):
        raise AttributeError("Attribute 'frameSizeVertical' is read-only")

    @property
    def timebase(self):
        return self._eval_on_this_object('timebase')
    @timebase.setter
    def timebase(self, timebase):
        raise AttributeError("Attribute 'timebase' is read-only")

    """ The starting timecode of the first frame of the sequence, as a string. """
    @property
    def zeroPoint(self):
        return self._eval_on_this_object('zeroPoint')
    @zeroPoint.setter
    def zeroPoint(self, zeroPoint):
        raise AttributeError("Attribute 'zeroPoint' is read-only")

    """ Timecode (as a string) of the end of the sequence. """
    @property
    def end(self):
        return self._eval_on_this_object('end')
    @end.setter
    def end(self, end):
        raise AttributeError("Attribute 'end' is read-only")

    """ The sequence's markers. """
    @property
    def markers(self):
        kwargs = self._eval_on_this_object('markers')
        return MarkerCollection(**kwargs) if kwargs else None
    @markers.setter
    def markers(self, markers):
        raise AttributeError("Attribute 'markers' is read-only")

    """ The `projectItem` corresponding to the sequence. """
    @property
    def projectItem(self):
        kwargs = self._eval_on_this_object('projectItem')
        return ProjectItem(**kwargs) if kwargs else None
    @projectItem.setter
    def projectItem(self, projectItem):
        raise AttributeError("Attribute 'projectItem' is read-only")

    @property
    def videoDisplayFormat(self):
        return self._eval_on_this_object('videoDisplayFormat')
    @videoDisplayFormat.setter
    def videoDisplayFormat(self, videoDisplayFormat):
        self._eval_on_this_object("videoDisplayFormat = {}".format(_format_object_to_es(videoDisplayFormat)))

    @property
    def audioDisplayFormat(self):
        return self._eval_on_this_object('audioDisplayFormat')
    @audioDisplayFormat.setter
    def audioDisplayFormat(self, audioDisplayFormat):
        self._eval_on_this_object("audioDisplayFormat = {}".format(_format_object_to_es(audioDisplayFormat)))


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Sequence.bind"')
        self._check_type(function, any, 'arg "function" of function "Sequence.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Sequence.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Sequence.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "Sequence.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "Sequence.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def getPlayerPosition(self):
        """
        Retrieves the current player position, as a `Time` object.
        """
        return Time(**self._eval_on_this_object("getPlayerPosition()"))

    def setPlayerPosition(self, pos):
        """
        Sets the current player position. 
        :param pos: The new position, in ticks
        :type pos: str
        """
        if isinstance(pos, float) or isinstance(pos, int):
            pos = str(pos)
        self._check_type(pos, str, 'arg "pos" of function "Sequence.setPlayerPosition"')
        self._eval_on_this_object("setPlayerPosition({})".format(_format_object_to_es(pos)))

    def setInPoint(self, time):
        """
        Sets the in point of the sequence. 
        :param seconds: Time of in point.
        :type time: Object
        """
        self._eval_on_this_object("setInPoint({})".format(_format_object_to_es(time)))

    def setOutPoint(self, time):
        """
        Sets the out point of the sequence. 
        :param seconds: Time of out point.
        :type time: Object
        """
        self._eval_on_this_object("setOutPoint({})".format(_format_object_to_es(time)))

    def getInPoint(self):
        """
        Retrieves the sequence's in point, as a timecode string.
        """
        return self._eval_on_this_object("getInPoint()")

    def getOutPoint(self):
        """
        Retrieves the sequence's out point, as a timecode string.
        """
        return self._eval_on_this_object("getOutPoint()")

    def getInPointAsTime(self):
        """
        Retrieves the sequence's in point, as a `Time` object.
        """
        return Time(**self._eval_on_this_object("getInPointAsTime()"))

    def getOutPointAsTime(self):
        """
        Retrieves the sequence's out point, as a `Time` object.
        """
        return Time(**self._eval_on_this_object("getOutPointAsTime()"))

    def setWorkAreaInPoint(self, time):
        """
        Specify the work area in point, in seconds. 
        :param timeInSeconds: new in point time.
        :type time: Object
        """
        self._eval_on_this_object("setWorkAreaInPoint({})".format(_format_object_to_es(time)))

    def setWorkAreaOutPoint(self, time):
        """
        Specify the work area out point, in seconds. 
        :param timeInSeconds: new out point time.
        :type time: Object
        """
        self._eval_on_this_object("setWorkAreaOutPoint({})".format(_format_object_to_es(time)))

    def getWorkAreaInPoint(self):
        """
        Returns the work area in point, in seconds.
        """
        return self._eval_on_this_object("getWorkAreaInPoint()")

    def getWorkAreaOutPoint(self):
        """
        Returns the work area out point, in seconds.
        """
        return self._eval_on_this_object("getWorkAreaOutPoint()")

    def getWorkAreaInPointAsTime(self):
        """
        Returns the work area in point, as a `Time` object.
        """
        return Time(**self._eval_on_this_object("getWorkAreaInPointAsTime()"))

    def getWorkAreaOutPointAsTime(self):
        """
        Returns the work area out point, as a `Time` object.
        """
        return Time(**self._eval_on_this_object("getWorkAreaOutPointAsTime()"))

    def setZeroPoint(self, ticks):
        """
        Sets the timecode of the first frame of the sequence. 
        :param newStartTime: The new starting time, in `ticks`.
        :type ticks: str
        """
        self._check_type(ticks, str, 'arg "ticks" of function "Sequence.setZeroPoint"')
        self._eval_on_this_object("setZeroPoint({})".format(_format_object_to_es(ticks)))

    def attachCustomProperty(self, propertyID, propertyValue):
        """
        Adds a new metadata key to the sequence, and sets its value. 
        :param propertyID: Name of new property
        :param propertyValue: Value of new property
        :type propertyID: str
        :type propertyValue: str
        """
        self._check_type(propertyID, str, 'arg "propertyID" of function "Sequence.attachCustomProperty"')
        self._check_type(propertyValue, str, 'arg "propertyValue" of function "Sequence.attachCustomProperty"')
        self._eval_on_this_object("attachCustomProperty({}, {})".format(_format_object_to_es(propertyID), _format_object_to_es(propertyValue)))

    def clone(self):
        """
        Clones a sequence. @returns the clone Sequence.
        """
        self._eval_on_this_object("clone()")

    def exportAsProject(self, exportPath):
        """
        Exports the sequence (and its constituent media) as a new PPro project. 
        :param path: Output file path, including file name.
        :type exportPath: str
        """
        self._check_type(exportPath, str, 'arg "exportPath" of function "Sequence.exportAsProject"')
        self._eval_on_this_object("exportAsProject({})".format(_format_object_to_es(exportPath)))

    def exportAsFinalCutProXML(self, exportPath, suppressUI):
        """
        Exports a new FCP XML file representing this sequence. 
        :param exportPath: The full file path (with file name) to create.
        :param suppressUI: Optional; quiets any warnings or errors encountered during export.
        :type exportPath: str
        :type suppressUI: float
        """
        self._check_type(exportPath, str, 'arg "exportPath" of function "Sequence.exportAsFinalCutProXML"')
        self._check_type(suppressUI, float, 'arg "suppressUI" of function "Sequence.exportAsFinalCutProXML"')
        return self._eval_on_this_object("exportAsFinalCutProXML({}, {})".format(_format_object_to_es(exportPath), _format_object_to_es(suppressUI)))

    def exportAsMediaDirect(self, outputFilePath, presetPath, workAreaType):
        """
        Premiere Pro exports the sequence immediately. 
        :param outputFilePath: The output file path (with name).
        :param presetPath: The .epr file to use.
        :param workAreaType: Optional work area specifier.
        :type outputFilePath: str
        :type presetPath: str
        :type workAreaType: float
        """
        self._check_type(outputFilePath, str, 'arg "outputFilePath" of function "Sequence.exportAsMediaDirect"')
        self._check_type(presetPath, str, 'arg "presetPath" of function "Sequence.exportAsMediaDirect"')
        self._check_type(workAreaType, float, 'arg "workAreaType" of function "Sequence.exportAsMediaDirect"')
        return self._eval_on_this_object("exportAsMediaDirect({}, {}, {})".format(_format_object_to_es(outputFilePath), _format_object_to_es(presetPath), _format_object_to_es(workAreaType)))

    def getExportFileExtension(self, presetFilePath):
        """
        Retrieves the file extension associated with a given output preset (.epr file). 
        :param presetFilePath: full path to .epr file
        :type presetFilePath: str
        """
        self._check_type(presetFilePath, str, 'arg "presetFilePath" of function "Sequence.getExportFileExtension"')
        return self._eval_on_this_object("getExportFileExtension({})".format(_format_object_to_es(presetFilePath)))

    def importMGT(self, path, time, videoTrackIndex, audioTrackIndex):
        """
        Imports a Motion Graphics Template (.mogrt) into the sequence 
        :param pathToMOGRT: Complete path to .mogrt
        :param timeInTicks: Time (in ticks) at which to insert
        :param videoTrackOffset: The offset from first video track to targeted track
        :param audioTrackOffset: The offset from first audio track to targeted track @returns newly-created `trackItem` representing the .mogrt
        :type path: str
        :type time: Object
        :type videoTrackIndex: float
        :type audioTrackIndex: float
        """
        self._check_type(path, str, 'arg "path" of function "Sequence.importMGT"')
        self._check_type(videoTrackIndex, float, 'arg "videoTrackIndex" of function "Sequence.importMGT"')
        self._check_type(audioTrackIndex, float, 'arg "audioTrackIndex" of function "Sequence.importMGT"')
        return TrackItem(**self._eval_on_this_object("importMGT({}, {}, {}, {})".format(_format_object_to_es(path), _format_object_to_es(time), _format_object_to_es(videoTrackIndex), _format_object_to_es(audioTrackIndex))))

    def importMGTFromLibrary(self, libraryName, mgtName, time, videoTrackIndex, audioTrackIndex):
        """
        :type libraryName: str
        :type mgtName: str
        :type time: Object
        :type videoTrackIndex: float
        :type audioTrackIndex: float
        """
        self._check_type(libraryName, str, 'arg "libraryName" of function "Sequence.importMGTFromLibrary"')
        self._check_type(mgtName, str, 'arg "mgtName" of function "Sequence.importMGTFromLibrary"')
        self._check_type(videoTrackIndex, float, 'arg "videoTrackIndex" of function "Sequence.importMGTFromLibrary"')
        self._check_type(audioTrackIndex, float, 'arg "audioTrackIndex" of function "Sequence.importMGTFromLibrary"')
        return TrackItem(**self._eval_on_this_object("importMGTFromLibrary({}, {}, {}, {}, {})".format(_format_object_to_es(libraryName), _format_object_to_es(mgtName), _format_object_to_es(time), _format_object_to_es(videoTrackIndex), _format_object_to_es(audioTrackIndex))))

    def getSettings(self):
        """
        Returns the current sequence settings. @returns SequenceSettings
        """
        return SequenceSettings(**self._eval_on_this_object("getSettings()"))

    def setSettings(self, settings):
        """
        Specifies the sequence settings to use. 
        :param newSettings: New settings
        :type settings: SequenceSettings
        """
        self._check_type(settings, SequenceSettings, 'arg "settings" of function "Sequence.setSettings"')
        self._eval_on_this_object("setSettings({})".format(_format_object_to_es(settings)))

    def getSelection(self):
        """
        Returns currently-selected clips, as an `Array` of `trackItems`
        """
        return Array(**self._eval_on_this_object("getSelection()"))

    def setSelection(self):
        self._eval_on_this_object("setSelection()")

    def linkSelection(self):
        """
        Links the currently-selected `trackItems` together, if possible. @returns `True` if successful.
        """
        return self._eval_on_this_object("linkSelection()")

    def unlinkSelection(self):
        """
        Unlinks the currently-selected `trackItems`, if possible. @returns `True` if successful.
        """
        return self._eval_on_this_object("unlinkSelection()")

    def insertClip(self, clipProjectItem, time, videoTrackIndex, audioTrackIndex):
        """
        Inserts a clip (`trackItem`) into the sequence. 
        :param projectItem: The project item to insert.
        :param time: Time at which to insert.
        :param vidTrackOffset: The offset from the first video track to targeted track
        :param audTrackOffset: The offset from the first audio track to targeted track
        :type clipProjectItem: ProjectItem
        :type time: Object
        :type videoTrackIndex: float
        :type audioTrackIndex: float
        """
        self._check_type(clipProjectItem, ProjectItem, 'arg "clipProjectItem" of function "Sequence.insertClip"')
        self._check_type(time, Time, 'arg "time" of function "Sequence.insertClip"')
        self._check_type(videoTrackIndex, float, 'arg "videoTrackIndex" of function "Sequence.insertClip"')
        self._check_type(audioTrackIndex, float, 'arg "audioTrackIndex" of function "Sequence.insertClip"')
        self._eval_on_this_object("insertClip({}, {}, {}, {})".format(_format_object_to_es(clipProjectItem), _format_object_to_es(time), _format_object_to_es(videoTrackIndex), _format_object_to_es(audioTrackIndex)))

    def overwriteClip(self, clipProjectItem, time, videoTrackIndex, audioTrackIndex):
        """
        :type clipProjectItem: ProjectItem
        :type time: Object
        :type videoTrackIndex: float
        :type audioTrackIndex: float
        """
        self._check_type(clipProjectItem, ProjectItem, 'arg "clipProjectItem" of function "Sequence.overwriteClip"')
        self._check_type(videoTrackIndex, float, 'arg "videoTrackIndex" of function "Sequence.overwriteClip"')
        self._check_type(audioTrackIndex, float, 'arg "audioTrackIndex" of function "Sequence.overwriteClip"')
        self._eval_on_this_object("overwriteClip({}, {}, {}, {})".format(_format_object_to_es(clipProjectItem), _format_object_to_es(time), _format_object_to_es(videoTrackIndex), _format_object_to_es(audioTrackIndex)))

    def close(self):
        self._eval_on_this_object("close()")

    def createSubsequence(self, ignoreTrackTargeting):
        """
        Creates a new sequence from the source sequence's in and out points. 
        :param ignoreMapping: If True the current selection, not track targeting, will determine the clips to include in the new sequence. If there is no selection, track targeting determines which clips are included in the new sequence.
        :type ignoreTrackTargeting: bool
        """
        self._check_type(ignoreTrackTargeting, bool, 'arg "ignoreTrackTargeting" of function "Sequence.createSubsequence"')
        return Sequence(**self._eval_on_this_object("createSubsequence({})".format(_format_object_to_es(ignoreTrackTargeting))))

    def isWorkAreaEnabled(self):
        """
        Returns `true` if work area is enabled.
        """
        return self._eval_on_this_object("isWorkAreaEnabled()")

    def setWorkAreaEnabled(self, specifiedState):
        """
        Sets the enabled state of the seqeuence work area. 
        :param enableState: The desired state
        :type specifiedState: float
        """
        self._check_type(specifiedState, float, 'arg "specifiedState" of function "Sequence.setWorkAreaEnabled"')
        return self._eval_on_this_object("setWorkAreaEnabled({})".format(_format_object_to_es(specifiedState)))


class TrackCollection(PymiereBaseCollection):
    def __init__(self, pymiere_id):
        super(TrackCollection, self).__init__(pymiere_id, "numTracks")

    def __getitem__(self, index):
        return Track(**super(TrackCollection, self).__getitem__(index))

    def __iter__(self):
        return iter([self.__getitem__(i) for i in range(len(self))])


class MarkerCollection(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(MarkerCollection, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def numMarkers(self):
        return self._eval_on_this_object('numMarkers')
    @numMarkers.setter
    def numMarkers(self, numMarkers):
        raise AttributeError("Attribute 'numMarkers' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "MarkerCollection.bind"')
        self._check_type(function, any, 'arg "function" of function "MarkerCollection.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "MarkerCollection.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "MarkerCollection.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "MarkerCollection.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "MarkerCollection.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def createMarker(self, time):
        """
        :type time: float
        """
        self._check_type(time, float, 'arg "time" of function "MarkerCollection.createMarker"')
        return Marker(**self._eval_on_this_object("createMarker({})".format(_format_object_to_es(time))))

    def deleteMarker(self, marker):
        """
        :type marker: Marker
        """
        self._check_type(marker, Marker, 'arg "marker" of function "MarkerCollection.deleteMarker"')
        self._eval_on_this_object("deleteMarker({})".format(_format_object_to_es(marker)))

    def getFirstMarker(self):
        return Marker(**self._eval_on_this_object("getFirstMarker()"))

    def getLastMarker(self):
        return Marker(**self._eval_on_this_object("getLastMarker()"))

    def getPrevMarker(self, marker):
        """
        :type marker: Marker
        """
        self._check_type(marker, Marker, 'arg "marker" of function "MarkerCollection.getPrevMarker"')
        return Marker(**self._eval_on_this_object("getPrevMarker({})".format(_format_object_to_es(marker))))

    def getNextMarker(self, marker):
        """
        :type marker: Marker
        """
        self._check_type(marker, Marker, 'arg "marker" of function "MarkerCollection.getNextMarker"')
        return Marker(**self._eval_on_this_object("getNextMarker({})".format(_format_object_to_es(marker))))


class ComponentCollection(PymiereBaseCollection):
    def __init__(self, pymiere_id):
        super(ComponentCollection, self).__init__(pymiere_id, "numItems")

    def __getitem__(self, index):
        return Component(**super(ComponentCollection, self).__getitem__(index))

    def __iter__(self):
        return iter([self.__getitem__(i) for i in range(len(self))])


class ProjectCollection(PymiereBaseCollection):
    def __init__(self, pymiere_id):
        super(ProjectCollection, self).__init__(pymiere_id, "numProjects")

    def __getitem__(self, index):
        return Project(**super(ProjectCollection, self).__getitem__(index))

    def __iter__(self):
        return iter([self.__getitem__(i) for i in range(len(self))])


class Anywhere(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Anywhere, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Anywhere.bind"')
        self._check_type(function, any, 'arg "function" of function "Anywhere.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Anywhere.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Anywhere.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "Anywhere.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "Anywhere.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def setAuthenticationToken(self, inAuthToken, inEmail):
        """
        :type inAuthToken: str
        :type inEmail: str
        """
        self._check_type(inAuthToken, str, 'arg "inAuthToken" of function "Anywhere.setAuthenticationToken"')
        self._check_type(inEmail, str, 'arg "inEmail" of function "Anywhere.setAuthenticationToken"')
        return self._eval_on_this_object("setAuthenticationToken({}, {})".format(_format_object_to_es(inAuthToken), _format_object_to_es(inEmail)))

    def getAuthenticationToken(self):
        return self._eval_on_this_object("getAuthenticationToken()")

    def listProductions(self):
        return _format_object_to_py(self._eval_on_this_object("listProductions()"))

    def openProduction(self, inProductionURL):
        """
        :type inProductionURL: str
        """
        self._check_type(inProductionURL, str, 'arg "inProductionURL" of function "Anywhere.openProduction"')
        return self._eval_on_this_object("openProduction({})".format(_format_object_to_es(inProductionURL)))

    def openTeamProjectSnapshot(self, inTeamProjectSnapshotPath):
        """
        :type inTeamProjectSnapshotPath: str
        """
        self._check_type(inTeamProjectSnapshotPath, str, 'arg "inTeamProjectSnapshotPath" of function "Anywhere.openTeamProjectSnapshot"')
        return self._eval_on_this_object("openTeamProjectSnapshot({})".format(_format_object_to_es(inTeamProjectSnapshotPath)))

    def isProductionOpen(self):
        return self._eval_on_this_object("isProductionOpen()")

    def getCurrentEditingSessionURL(self):
        return self._eval_on_this_object("getCurrentEditingSessionURL()")

    def getCurrentEditingSessionSelectionURL(self):
        return self._eval_on_this_object("getCurrentEditingSessionSelectionURL()")

    def getCurrentEditingSessionActiveSequenceURL(self):
        return self._eval_on_this_object("getCurrentEditingSessionActiveSequenceURL()")


class Encoder(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Encoder, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def ENCODE_ENTIRE(self):
        return self._eval_on_this_object('ENCODE_ENTIRE')
    @ENCODE_ENTIRE.setter
    def ENCODE_ENTIRE(self, ENCODE_ENTIRE):
        raise AttributeError("Attribute 'ENCODE_ENTIRE' is read-only")

    @property
    def ENCODE_IN_TO_OUT(self):
        return self._eval_on_this_object('ENCODE_IN_TO_OUT')
    @ENCODE_IN_TO_OUT.setter
    def ENCODE_IN_TO_OUT(self, ENCODE_IN_TO_OUT):
        raise AttributeError("Attribute 'ENCODE_IN_TO_OUT' is read-only")

    @property
    def ENCODE_WORKAREA(self):
        return self._eval_on_this_object('ENCODE_WORKAREA')
    @ENCODE_WORKAREA.setter
    def ENCODE_WORKAREA(self, ENCODE_WORKAREA):
        raise AttributeError("Attribute 'ENCODE_WORKAREA' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Encoder.bind"')
        self._check_type(function, any, 'arg "function" of function "Encoder.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Encoder.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Encoder.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "Encoder.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "Encoder.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def encodeSequence(self, sequence, outputFilePath, presetPath, WorkAreaType, removeOnCompletion, startQueueImmediately):
        """
        :type sequence: Sequence
        :type outputFilePath: str
        :type presetPath: str
        :type WorkAreaType: float
        :type removeOnCompletion: float
        :type startQueueImmediately: float
        """
        self._check_type(sequence, Sequence, 'arg "sequence" of function "Encoder.encodeSequence"')
        self._check_type(outputFilePath, str, 'arg "outputFilePath" of function "Encoder.encodeSequence"')
        self._check_type(presetPath, str, 'arg "presetPath" of function "Encoder.encodeSequence"')
        self._check_type(WorkAreaType, float, 'arg "WorkAreaType" of function "Encoder.encodeSequence"')
        self._check_type(removeOnCompletion, float, 'arg "removeOnCompletion" of function "Encoder.encodeSequence"')
        self._check_type(startQueueImmediately, float, 'arg "startQueueImmediately" of function "Encoder.encodeSequence"')
        return self._eval_on_this_object("encodeSequence({}, {}, {}, {}, {}, {})".format(_format_object_to_es(sequence), _format_object_to_es(outputFilePath), _format_object_to_es(presetPath), _format_object_to_es(WorkAreaType), _format_object_to_es(removeOnCompletion), _format_object_to_es(startQueueImmediately)))

    def encodeProjectItem(self, projectItem, outputFilePath, presetPath, WorkAreaType, removeOnCompletion, startQueueImmediately):
        """
        :type projectItem: ProjectItem
        :type outputFilePath: str
        :type presetPath: str
        :type WorkAreaType: float
        :type removeOnCompletion: float
        :type startQueueImmediately: float
        """
        self._check_type(projectItem, ProjectItem, 'arg "projectItem" of function "Encoder.encodeProjectItem"')
        self._check_type(outputFilePath, str, 'arg "outputFilePath" of function "Encoder.encodeProjectItem"')
        self._check_type(presetPath, str, 'arg "presetPath" of function "Encoder.encodeProjectItem"')
        self._check_type(WorkAreaType, float, 'arg "WorkAreaType" of function "Encoder.encodeProjectItem"')
        self._check_type(removeOnCompletion, float, 'arg "removeOnCompletion" of function "Encoder.encodeProjectItem"')
        self._check_type(startQueueImmediately, float, 'arg "startQueueImmediately" of function "Encoder.encodeProjectItem"')
        return self._eval_on_this_object("encodeProjectItem({}, {}, {}, {}, {}, {})".format(_format_object_to_es(projectItem), _format_object_to_es(outputFilePath), _format_object_to_es(presetPath), _format_object_to_es(WorkAreaType), _format_object_to_es(removeOnCompletion), _format_object_to_es(startQueueImmediately)))

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
        self._check_type(inputFilePath, str, 'arg "inputFilePath" of function "Encoder.encodeFile"')
        self._check_type(outputFilePath, str, 'arg "outputFilePath" of function "Encoder.encodeFile"')
        self._check_type(presetPath, str, 'arg "presetPath" of function "Encoder.encodeFile"')
        self._check_type(removeOnCompletion, float, 'arg "removeOnCompletion" of function "Encoder.encodeFile"')
        self._check_type(startQueueImmediately, float, 'arg "startQueueImmediately" of function "Encoder.encodeFile"')
        return self._eval_on_this_object("encodeFile({}, {}, {}, {}, {}, {}, {})".format(_format_object_to_es(inputFilePath), _format_object_to_es(outputFilePath), _format_object_to_es(presetPath), _format_object_to_es(removeOnCompletion), _format_object_to_es(startTime), _format_object_to_es(stopTime), _format_object_to_es(startQueueImmediately)))

    def startBatch(self):
        return self._eval_on_this_object("startBatch()")

    def launchEncoder(self):
        return self._eval_on_this_object("launchEncoder()")

    def setSidecarXMPEnabled(self, enable):
        """
        :type enable: float
        """
        self._check_type(enable, float, 'arg "enable" of function "Encoder.setSidecarXMPEnabled"')
        self._eval_on_this_object("setSidecarXMPEnabled({})".format(_format_object_to_es(enable)))

    def setEmbeddedXMPEnabled(self, enable):
        """
        :type enable: float
        """
        self._check_type(enable, float, 'arg "enable" of function "Encoder.setEmbeddedXMPEnabled"')
        self._eval_on_this_object("setEmbeddedXMPEnabled({})".format(_format_object_to_es(enable)))

    def getExporters(self):
        self._eval_on_this_object("getExporters()")


class Properties(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Properties, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Properties.bind"')
        self._check_type(function, any, 'arg "function" of function "Properties.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Properties.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Properties.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "Properties.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "Properties.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def doesPropertyExist(self, propertyKey):
        """
        :type propertyKey: str
        """
        self._check_type(propertyKey, str, 'arg "propertyKey" of function "Properties.doesPropertyExist"')
        return self._eval_on_this_object("doesPropertyExist({})".format(_format_object_to_es(propertyKey)))

    def isPropertyReadOnly(self, propertyKey):
        """
        :type propertyKey: str
        """
        self._check_type(propertyKey, str, 'arg "propertyKey" of function "Properties.isPropertyReadOnly"')
        return self._eval_on_this_object("isPropertyReadOnly({})".format(_format_object_to_es(propertyKey)))

    def clearProperty(self, propertyKey):
        """
        :type propertyKey: str
        """
        self._check_type(propertyKey, str, 'arg "propertyKey" of function "Properties.clearProperty"')
        self._eval_on_this_object("clearProperty({})".format(_format_object_to_es(propertyKey)))

    def setProperty(self, propertyKey):
        """
        :type propertyKey: str
        """
        self._check_type(propertyKey, str, 'arg "propertyKey" of function "Properties.setProperty"')
        self._eval_on_this_object("setProperty({})".format(_format_object_to_es(propertyKey)))

    def getProperty(self, propertyKey):
        """
        :type propertyKey: str
        """
        self._check_type(propertyKey, str, 'arg "propertyKey" of function "Properties.getProperty"')
        self._eval_on_this_object("getProperty({})".format(_format_object_to_es(propertyKey)))


class SourceMonitor(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(SourceMonitor, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "SourceMonitor.bind"')
        self._check_type(function, any, 'arg "function" of function "SourceMonitor.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "SourceMonitor.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "SourceMonitor.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "SourceMonitor.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "SourceMonitor.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def openFilePath(self, filePath):
        """
        :type filePath: str
        """
        self._check_type(filePath, str, 'arg "filePath" of function "SourceMonitor.openFilePath"')
        return self._eval_on_this_object("openFilePath({})".format(_format_object_to_es(filePath)))

    def openProjectItem(self, projectItem):
        """
        :type projectItem: ProjectItem
        """
        self._check_type(projectItem, ProjectItem, 'arg "projectItem" of function "SourceMonitor.openProjectItem"')
        return self._eval_on_this_object("openProjectItem({})".format(_format_object_to_es(projectItem)))

    def play(self, speed):
        """
        :type speed: float
        """
        self._check_type(speed, float, 'arg "speed" of function "SourceMonitor.play"')
        self._eval_on_this_object("play({})".format(_format_object_to_es(speed)))

    def closeClip(self):
        self._eval_on_this_object("closeClip()")

    def closeAllClips(self):
        self._eval_on_this_object("closeAllClips()")

    def getPosition(self):
        return Time(**self._eval_on_this_object("getPosition()"))

    def getProjectItem(self):
        return ProjectItem(**self._eval_on_this_object("getProjectItem()"))


class ProjectManager(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(ProjectManager, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    """ The `ProjectManagerOptions` structure. """
    @property
    def options(self):
        kwargs = self._eval_on_this_object('options')
        return ProjectManagerOptions(**kwargs) if kwargs else None
    @options.setter
    def options(self, options):
        raise AttributeError("Attribute 'options' is read-only")

    """ An array of strings describing errors encountered. """
    @property
    def errors(self):
        return self._eval_on_this_object('errors')
    @errors.setter
    def errors(self, errors):
        raise AttributeError("Attribute 'errors' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ProjectManager.bind"')
        self._check_type(function, any, 'arg "function" of function "ProjectManager.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ProjectManager.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ProjectManager.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "ProjectManager.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "ProjectManager.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def process(self, project):
        """
        Perform the consolidation and transfer. 
        :param project: the `Project` to consolidate.
        :type project: Project
        """
        self._check_type(project, Project, 'arg "project" of function "ProjectManager.process"')
        return self._eval_on_this_object("process({})".format(_format_object_to_es(project)))


class ProjectManagerOptions(PymiereBaseObject):
    """ Structure containing all available options for the `ProjectManager`. """
    def __init__(self, pymiere_id=None):
        super(ProjectManagerOptions, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    """ Which transfer option to use; will be one of these: 	`CLIP_TRANSFER_COPY`  `CLIP_TRANSFER_TRANSCODE` """
    @property
    def clipTransferOption(self):
        return self._eval_on_this_object('clipTransferOption')
    @clipTransferOption.setter
    def clipTransferOption(self, clipTransferOption):
        self._eval_on_this_object("clipTransferOption = {}".format(_format_object_to_es(clipTransferOption)))

    """ Which transcode option to use; will be one of these: 	`CLIP_TRANSCODE_MATCH_PRESET`  `CLIP_TRANSCODE_MATCH_CLIPS` 	`CLIP_TRANSCODE_MATCH_SEQUENCE` """
    @property
    def clipTranscoderOption(self):
        return self._eval_on_this_object('clipTranscoderOption')
    @clipTranscoderOption.setter
    def clipTranscoderOption(self, clipTranscoderOption):
        self._eval_on_this_object("clipTranscoderOption = {}".format(_format_object_to_es(clipTranscoderOption)))

    """ If `true`, projectItems not used in a sequence are not transferred """
    @property
    def excludeUnused(self):
        return self._eval_on_this_object('excludeUnused')
    @excludeUnused.setter
    def excludeUnused(self, excludeUnused):
        self._eval_on_this_object("excludeUnused = {}".format(_format_object_to_es(excludeUnused)))

    """ The number of 'handle' frames to provide, before and after the in/out points of clips in the sequence. """
    @property
    def handleFrameCount(self):
        return self._eval_on_this_object('handleFrameCount')
    @handleFrameCount.setter
    def handleFrameCount(self, handleFrameCount):
        self._eval_on_this_object("handleFrameCount = {}".format(_format_object_to_es(handleFrameCount)))

    """ If `true`, preview files will also be transferred. """
    @property
    def includePreviews(self):
        return self._eval_on_this_object('includePreviews')
    @includePreviews.setter
    def includePreviews(self, includePreviews):
        self._eval_on_this_object("includePreviews = {}".format(_format_object_to_es(includePreviews)))

    """ If `true`, conformed audio files will also be transferred. """
    @property
    def includeConformedAudio(self):
        return self._eval_on_this_object('includeConformedAudio')
    @includeConformedAudio.setter
    def includeConformedAudio(self, includeConformedAudio):
        self._eval_on_this_object("includeConformedAudio = {}".format(_format_object_to_es(includeConformedAudio)))

    """ If `true`, media files will be renamed to match clip names. """
    @property
    def renameMedia(self):
        return self._eval_on_this_object('renameMedia')
    @renameMedia.setter
    def renameMedia(self, renameMedia):
        self._eval_on_this_object("renameMedia = {}".format(_format_object_to_es(renameMedia)))

    """ The containing directory for the consolidation/transfer. """
    @property
    def destinationPath(self):
        return self._eval_on_this_object('destinationPath')
    @destinationPath.setter
    def destinationPath(self, destinationPath):
        self._eval_on_this_object("destinationPath = {}".format(_format_object_to_es(destinationPath)))

    """ If `true`, all sequences in the project will be transferred. """
    @property
    def includeAllSequences(self):
        return self._eval_on_this_object('includeAllSequences')
    @includeAllSequences.setter
    def includeAllSequences(self, includeAllSequences):
        self._eval_on_this_object("includeAllSequences = {}".format(_format_object_to_es(includeAllSequences)))

    """ An `Array` of all sequences affected by the transfer. """
    @property
    def affectedSequences(self):
        return self._eval_on_this_object('affectedSequences')
    @affectedSequences.setter
    def affectedSequences(self, affectedSequences):
        self._eval_on_this_object("affectedSequences = {}".format(_format_object_to_es(affectedSequences)))

    """ Path the the encoder preset (.epr file) to be used. """
    @property
    def encoderPresetFilePath(self):
        return self._eval_on_this_object('encoderPresetFilePath')
    @encoderPresetFilePath.setter
    def encoderPresetFilePath(self, encoderPresetFilePath):
        self._eval_on_this_object("encoderPresetFilePath = {}".format(_format_object_to_es(encoderPresetFilePath)))

    """ If `true`, image sequences will be transcoded. """
    @property
    def convertImageSequencesToClips(self):
        return self._eval_on_this_object('convertImageSequencesToClips')
    @convertImageSequencesToClips.setter
    def convertImageSequencesToClips(self, convertImageSequencesToClips):
        self._eval_on_this_object("convertImageSequencesToClips = {}".format(_format_object_to_es(convertImageSequencesToClips)))

    """ If `true`, synthetic importer clips will be transcoded. """
    @property
    def convertSyntheticsToClips(self):
        return self._eval_on_this_object('convertSyntheticsToClips')
    @convertSyntheticsToClips.setter
    def convertSyntheticsToClips(self, convertSyntheticsToClips):
        self._eval_on_this_object("convertSyntheticsToClips = {}".format(_format_object_to_es(convertSyntheticsToClips)))

    """ If `true`, After Effects compositions will be transcoded. """
    @property
    def convertAECompsToClips(self):
        return self._eval_on_this_object('convertAECompsToClips')
    @convertAECompsToClips.setter
    def convertAECompsToClips(self, convertAECompsToClips):
        self._eval_on_this_object("convertAECompsToClips = {}".format(_format_object_to_es(convertAECompsToClips)))

    """ If `true`, source media will be copied not transcoded, if transcoding would have resulted in loss of alpha information. """
    @property
    def copyToPreventAlphaLoss(self):
        return self._eval_on_this_object('copyToPreventAlphaLoss')
    @copyToPreventAlphaLoss.setter
    def copyToPreventAlphaLoss(self, copyToPreventAlphaLoss):
        self._eval_on_this_object("copyToPreventAlphaLoss = {}".format(_format_object_to_es(copyToPreventAlphaLoss)))

    """ Transfer mode setting: Copy source media """
    @property
    def CLIP_TRANSFER_COPY(self):
        return self._eval_on_this_object('CLIP_TRANSFER_COPY')
    @CLIP_TRANSFER_COPY.setter
    def CLIP_TRANSFER_COPY(self, CLIP_TRANSFER_COPY):
        raise AttributeError("Attribute 'CLIP_TRANSFER_COPY' is read-only")

    """ Transfer mode setting: Transcode source media """
    @property
    def CLIP_TRANSFER_TRANSCODE(self):
        return self._eval_on_this_object('CLIP_TRANSFER_TRANSCODE')
    @CLIP_TRANSFER_TRANSCODE.setter
    def CLIP_TRANSFER_TRANSCODE(self, CLIP_TRANSFER_TRANSCODE):
        raise AttributeError("Attribute 'CLIP_TRANSFER_TRANSCODE' is read-only")

    """ Transcode mode setting: Transcode source media to a specific preset """
    @property
    def CLIP_TRANSCODE_MATCH_PRESET(self):
        return self._eval_on_this_object('CLIP_TRANSCODE_MATCH_PRESET')
    @CLIP_TRANSCODE_MATCH_PRESET.setter
    def CLIP_TRANSCODE_MATCH_PRESET(self, CLIP_TRANSCODE_MATCH_PRESET):
        raise AttributeError("Attribute 'CLIP_TRANSCODE_MATCH_PRESET' is read-only")

    """ Transcode mode setting: Transcode source media to match clips """
    @property
    def CLIP_TRANSCODE_MATCH_CLIPS(self):
        return self._eval_on_this_object('CLIP_TRANSCODE_MATCH_CLIPS')
    @CLIP_TRANSCODE_MATCH_CLIPS.setter
    def CLIP_TRANSCODE_MATCH_CLIPS(self, CLIP_TRANSCODE_MATCH_CLIPS):
        raise AttributeError("Attribute 'CLIP_TRANSCODE_MATCH_CLIPS' is read-only")

    """ Transcode mode setting: Transcode source media to match sequence settings """
    @property
    def CLIP_TRANSCODE_MATCH_SEQUENCE(self):
        return self._eval_on_this_object('CLIP_TRANSCODE_MATCH_SEQUENCE')
    @CLIP_TRANSCODE_MATCH_SEQUENCE.setter
    def CLIP_TRANSCODE_MATCH_SEQUENCE(self, CLIP_TRANSCODE_MATCH_SEQUENCE):
        raise AttributeError("Attribute 'CLIP_TRANSCODE_MATCH_SEQUENCE' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ProjectManagerOptions.bind"')
        self._check_type(function, any, 'arg "function" of function "ProjectManagerOptions.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ProjectManagerOptions.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ProjectManagerOptions.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "ProjectManagerOptions.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "ProjectManagerOptions.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))


class Metadata(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Metadata, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def getMetadata(self):
        return self._eval_on_this_object('getMetadata')
    @getMetadata.setter
    def getMetadata(self, getMetadata):
        raise AttributeError("Attribute 'getMetadata' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Metadata.bind"')
        self._check_type(function, any, 'arg "function" of function "Metadata.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Metadata.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Metadata.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "Metadata.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "Metadata.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def setMetadataValue(self):
        self._eval_on_this_object("setMetadataValue()")

    def setMarkerData(self):
        self._eval_on_this_object("setMarkerData()")

    def addMarker(self):
        self._eval_on_this_object("addMarker()")

    def updateMarker(self):
        self._eval_on_this_object("updateMarker()")

    def deleteMarker(self):
        self._eval_on_this_object("deleteMarker()")


class Document(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Document, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Document.bind"')
        self._check_type(function, any, 'arg "function" of function "Document.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Document.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Document.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "Document.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "Document.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def importFiles(self, arg1):
        """
        :type arg1: any
        """
        self._check_type(arg1, any, 'arg "arg1" of function "Document.importFiles"')
        return self._eval_on_this_object("importFiles({})".format(_format_object_to_es(arg1)))

    def getFilePath(self):
        return self._eval_on_this_object("getFilePath()")


class ProjectItemType(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(ProjectItemType, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def BIN(self):
        return self._eval_on_this_object('BIN')
    @BIN.setter
    def BIN(self, BIN):
        raise AttributeError("Attribute 'BIN' is read-only")

    @property
    def CLIP(self):
        return self._eval_on_this_object('CLIP')
    @CLIP.setter
    def CLIP(self, CLIP):
        raise AttributeError("Attribute 'CLIP' is read-only")

    @property
    def FILE(self):
        return self._eval_on_this_object('FILE')
    @FILE.setter
    def FILE(self, FILE):
        raise AttributeError("Attribute 'FILE' is read-only")

    @property
    def ROOT(self):
        return self._eval_on_this_object('ROOT')
    @ROOT.setter
    def ROOT(self, ROOT):
        raise AttributeError("Attribute 'ROOT' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ProjectItemType.bind"')
        self._check_type(function, any, 'arg "function" of function "ProjectItemType.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ProjectItemType.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ProjectItemType.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "ProjectItemType.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "ProjectItemType.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))


class ScratchDiskType(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(ScratchDiskType, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def FirstVideoCaptureFolder(self):
        return self._eval_on_this_object('FirstVideoCaptureFolder')
    @FirstVideoCaptureFolder.setter
    def FirstVideoCaptureFolder(self, FirstVideoCaptureFolder):
        raise AttributeError("Attribute 'FirstVideoCaptureFolder' is read-only")

    @property
    def FirstAudioCaptureFolder(self):
        return self._eval_on_this_object('FirstAudioCaptureFolder')
    @FirstAudioCaptureFolder.setter
    def FirstAudioCaptureFolder(self, FirstAudioCaptureFolder):
        raise AttributeError("Attribute 'FirstAudioCaptureFolder' is read-only")

    @property
    def FirstVideoPreviewFolder(self):
        return self._eval_on_this_object('FirstVideoPreviewFolder')
    @FirstVideoPreviewFolder.setter
    def FirstVideoPreviewFolder(self, FirstVideoPreviewFolder):
        raise AttributeError("Attribute 'FirstVideoPreviewFolder' is read-only")

    @property
    def FirstAudioPreviewFolder(self):
        return self._eval_on_this_object('FirstAudioPreviewFolder')
    @FirstAudioPreviewFolder.setter
    def FirstAudioPreviewFolder(self, FirstAudioPreviewFolder):
        raise AttributeError("Attribute 'FirstAudioPreviewFolder' is read-only")

    @property
    def FirstAutoSaveFolder(self):
        return self._eval_on_this_object('FirstAutoSaveFolder')
    @FirstAutoSaveFolder.setter
    def FirstAutoSaveFolder(self, FirstAutoSaveFolder):
        raise AttributeError("Attribute 'FirstAutoSaveFolder' is read-only")

    @property
    def FirstCClibrariesFolder(self):
        return self._eval_on_this_object('FirstCClibrariesFolder')
    @FirstCClibrariesFolder.setter
    def FirstCClibrariesFolder(self, FirstCClibrariesFolder):
        raise AttributeError("Attribute 'FirstCClibrariesFolder' is read-only")

    @property
    def FirstCapsuleMediaFolder(self):
        return self._eval_on_this_object('FirstCapsuleMediaFolder')
    @FirstCapsuleMediaFolder.setter
    def FirstCapsuleMediaFolder(self, FirstCapsuleMediaFolder):
        raise AttributeError("Attribute 'FirstCapsuleMediaFolder' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ScratchDiskType.bind"')
        self._check_type(function, any, 'arg "function" of function "ScratchDiskType.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ScratchDiskType.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ScratchDiskType.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "ScratchDiskType.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "ScratchDiskType.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))


class RegisteredDirectories(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(RegisteredDirectories, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "RegisteredDirectories.bind"')
        self._check_type(function, any, 'arg "function" of function "RegisteredDirectories.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "RegisteredDirectories.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "RegisteredDirectories.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "RegisteredDirectories.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "RegisteredDirectories.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))


class UtilityFunctions(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(UtilityFunctions, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "UtilityFunctions.bind"')
        self._check_type(function, any, 'arg "function" of function "UtilityFunctions.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "UtilityFunctions.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "UtilityFunctions.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "UtilityFunctions.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "UtilityFunctions.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))


class Math(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Math, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def E(self):
        return self._eval_on_this_object('E')
    @E.setter
    def E(self, E):
        raise AttributeError("Attribute 'E' is read-only")

    @property
    def LN10(self):
        return self._eval_on_this_object('LN10')
    @LN10.setter
    def LN10(self, LN10):
        raise AttributeError("Attribute 'LN10' is read-only")

    @property
    def LN2(self):
        return self._eval_on_this_object('LN2')
    @LN2.setter
    def LN2(self, LN2):
        raise AttributeError("Attribute 'LN2' is read-only")

    @property
    def LOG2E(self):
        return self._eval_on_this_object('LOG2E')
    @LOG2E.setter
    def LOG2E(self, LOG2E):
        raise AttributeError("Attribute 'LOG2E' is read-only")

    @property
    def LOG10E(self):
        return self._eval_on_this_object('LOG10E')
    @LOG10E.setter
    def LOG10E(self, LOG10E):
        raise AttributeError("Attribute 'LOG10E' is read-only")

    @property
    def PI(self):
        return self._eval_on_this_object('PI')
    @PI.setter
    def PI(self, PI):
        raise AttributeError("Attribute 'PI' is read-only")

    @property
    def SQRT1_2(self):
        return self._eval_on_this_object('SQRT1_2')
    @SQRT1_2.setter
    def SQRT1_2(self, SQRT1_2):
        raise AttributeError("Attribute 'SQRT1_2' is read-only")

    @property
    def SQRT2(self):
        return self._eval_on_this_object('SQRT2')
    @SQRT2.setter
    def SQRT2(self, SQRT2):
        raise AttributeError("Attribute 'SQRT2' is read-only")


    # ----- FUNCTIONS -----
    def abs(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Math.abs"')
        return self._eval_on_this_object("abs({})".format(_format_object_to_es(n)))

    def acos(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Math.acos"')
        return self._eval_on_this_object("acos({})".format(_format_object_to_es(n)))

    def asin(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Math.asin"')
        return self._eval_on_this_object("asin({})".format(_format_object_to_es(n)))

    def atan(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Math.atan"')
        return self._eval_on_this_object("atan({})".format(_format_object_to_es(n)))

    def atan2(self, y, x):
        """
        :type y: float
        :type x: float
        """
        self._check_type(y, float, 'arg "y" of function "Math.atan2"')
        self._check_type(x, float, 'arg "x" of function "Math.atan2"')
        return self._eval_on_this_object("atan2({}, {})".format(_format_object_to_es(y), _format_object_to_es(x)))

    def ceil(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Math.ceil"')
        return self._eval_on_this_object("ceil({})".format(_format_object_to_es(n)))

    def cos(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Math.cos"')
        return self._eval_on_this_object("cos({})".format(_format_object_to_es(n)))

    def exp(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Math.exp"')
        return self._eval_on_this_object("exp({})".format(_format_object_to_es(n)))

    def floor(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Math.floor"')
        return self._eval_on_this_object("floor({})".format(_format_object_to_es(n)))

    def log(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Math.log"')
        return self._eval_on_this_object("log({})".format(_format_object_to_es(n)))

    def max(self, a, b):
        """
        :type a: float
        :type b: float
        """
        self._check_type(a, float, 'arg "a" of function "Math.max"')
        self._check_type(b, float, 'arg "b" of function "Math.max"')
        return self._eval_on_this_object("max({}, {})".format(_format_object_to_es(a), _format_object_to_es(b)))

    def min(self, y, x):
        """
        :type y: float
        :type x: float
        """
        self._check_type(y, float, 'arg "y" of function "Math.min"')
        self._check_type(x, float, 'arg "x" of function "Math.min"')
        return self._eval_on_this_object("min({}, {})".format(_format_object_to_es(y), _format_object_to_es(x)))

    def pow(self, x, y):
        """
        :type x: float
        :type y: float
        """
        self._check_type(x, float, 'arg "x" of function "Math.pow"')
        self._check_type(y, float, 'arg "y" of function "Math.pow"')
        return self._eval_on_this_object("pow({}, {})".format(_format_object_to_es(x), _format_object_to_es(y)))

    def random(self):
        return self._eval_on_this_object("random()")

    def round(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Math.round"')
        return self._eval_on_this_object("round({})".format(_format_object_to_es(n)))

    def sin(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Math.sin"')
        return self._eval_on_this_object("sin({})".format(_format_object_to_es(n)))

    def sqrt(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Math.sqrt"')
        return self._eval_on_this_object("sqrt({})".format(_format_object_to_es(n)))

    def tan(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Math.tan"')
        return self._eval_on_this_object("tan({})".format(_format_object_to_es(n)))


class File(PymiereBaseObject):
    """ Represents a file in the local file system in a platform-independent manner. """
    def __init__(self, pymiere_id=None):
        super(File, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    """ If true, the object refers to a file system alias or shortcut. """
    @property
    def alias(self):
        return self._eval_on_this_object('alias')
    @alias.setter
    def alias(self, alias):
        raise AttributeError("Attribute 'alias' is read-only")

    """ The creation date of the referenced file, or null if the object does not refer to a file on disk. """
    @property
    def created(self):
        kwargs = self._eval_on_this_object('created')
        return Date(**kwargs) if kwargs else None
    @created.setter
    def created(self, created):
        raise AttributeError("Attribute 'created' is read-only")

    """ A string containing a message describing the most recent file system error. Typically set by the file system, but a script can set it. Setting this value clears any error message and resets the error bit for opened files. Contains the empty string if there is no error. """
    @property
    def error(self):
        return self._eval_on_this_object('error')
    @error.setter
    def error(self, error):
        self._eval_on_this_object("error = {}".format(_format_object_to_es(error)))

    """ If true, this object refers to a file or file-system alias that actually exists in the file system. """
    @property
    def exists(self):
        return self._eval_on_this_object('exists')
    @exists.setter
    def exists(self, exists):
        raise AttributeError("Attribute 'exists' is read-only")

    """ The platform-specific full path name for the referenced file. """
    @property
    def fsName(self):
        return self._eval_on_this_object('fsName')
    @fsName.setter
    def fsName(self, fsName):
        raise AttributeError("Attribute 'fsName' is read-only")

    """ The full path name for the referenced file in URI notation. """
    @property
    def fullName(self):
        return self._eval_on_this_object('fullName')
    @fullName.setter
    def fullName(self, fullName):
        raise AttributeError("Attribute 'fullName' is read-only")

    """ The full path name for the referenced file in URI notation. """
    @property
    def absoluteURI(self):
        return self._eval_on_this_object('absoluteURI')
    @absoluteURI.setter
    def absoluteURI(self, absoluteURI):
        raise AttributeError("Attribute 'absoluteURI' is read-only")

    """ The path name for the object in URI notation, relative to the current folder. """
    @property
    def relativeURI(self):
        return self._eval_on_this_object('relativeURI')
    @relativeURI.setter
    def relativeURI(self, relativeURI):
        raise AttributeError("Attribute 'relativeURI' is read-only")

    """ The date of the referenced file's last modification, or null if the object does not refer to a file on the disk. """
    @property
    def modified(self):
        kwargs = self._eval_on_this_object('modified')
        return Date(**kwargs) if kwargs else None
    @modified.setter
    def modified(self, modified):
        raise AttributeError("Attribute 'modified' is read-only")

    """ The file name portion of the absolute URI for the referenced file, without the path specification. """
    @property
    def name(self):
        return self._eval_on_this_object('name')
    @name.setter
    def name(self, name):
        raise AttributeError("Attribute 'name' is read-only")

    """ The localized name of the referenced file, without the path specification. """
    @property
    def displayName(self):
        return self._eval_on_this_object('displayName')
    @displayName.setter
    def displayName(self, displayName):
        raise AttributeError("Attribute 'displayName' is read-only")

    """ The path portion of the absolute URI for the referenced file, without the file name. """
    @property
    def path(self):
        return self._eval_on_this_object('path')
    @path.setter
    def path(self, path):
        raise AttributeError("Attribute 'path' is read-only")

    """ The Folder object for the folder that contains this file. """
    @property
    def parent(self):
        kwargs = self._eval_on_this_object('parent')
        return Folder(**kwargs) if kwargs else None
    @parent.setter
    def parent(self, parent):
        raise AttributeError("Attribute 'parent' is read-only")

    """ The file type as a four-character string. In Mac OS, the Mac OS file type. In Windows, "appl" for .EXE files, "shlb" for .DLL files and "TEXT" for any other file. """
    @property
    def type(self):
        return self._eval_on_this_object('type')
    @type.setter
    def type(self, type):
        raise AttributeError("Attribute 'type' is read-only")

    """ In Mac OS, the file creator as a four-character string. In Windows or UNIX, value is "????". """
    @property
    def creator(self):
        return self._eval_on_this_object('creator')
    @creator.setter
    def creator(self, creator):
        raise AttributeError("Attribute 'creator' is read-only")

    """ When true, the file is not shown in the platform-specific file browser. If the object references a file-system alias or shortcut, the flag is altered on the alias, not on the original file. """
    @property
    def hidden(self):
        return self._eval_on_this_object('hidden')
    @hidden.setter
    def hidden(self, hidden):
        self._eval_on_this_object("hidden = {}".format(_format_object_to_es(hidden)))

    """ When true, prevents the file from being altered or deleted. If the referenced file is a file-system alias or shortcut, the flag is altered on the alias, not on the original file. """
    @property
    def readonly(self):
        return self._eval_on_this_object('readonly')
    @readonly.setter
    def readonly(self, readonly):
        self._eval_on_this_object("readonly = {}".format(_format_object_to_es(readonly)))

    """ How line feed characters are written in the file system. One of the values "Windows", "Macintosh", or "Unix". """
    @property
    def lineFeed(self):
        return self._eval_on_this_object('lineFeed')
    @lineFeed.setter
    def lineFeed(self, lineFeed):
        self._eval_on_this_object("lineFeed = {}".format(_format_object_to_es(lineFeed)))

    """ The size of the file in bytes. Can be set only for a file that is not open, in which case it truncates or pads the file with 0-bytes to the new length. """
    @property
    def length(self):
        return self._eval_on_this_object('length')
    @length.setter
    def length(self, length):
        self._eval_on_this_object("length = {}".format(_format_object_to_es(length)))

    """ Gets or sets the encoding for subsequent read/write operations. One of the encoding constants listed in the JavaScript Tools Guide. If the value is not recognized, uses the system default encoding.A special encoder, BINARY, is used to read binary files. It stores each byte of the file as one Unicode character regardless of any encoding. When writing, the lower byte of each Unicode character is treated as a single byte to write. """
    @property
    def encoding(self):
        return self._eval_on_this_object('encoding')
    @encoding.setter
    def encoding(self, encoding):
        self._eval_on_this_object("encoding = {}".format(_format_object_to_es(encoding)))

    """ When true, a read attempt caused the current position to be at the end of the file, or the file is not open. """
    @property
    def eof(self):
        return self._eval_on_this_object('eof')
    @eof.setter
    def eof(self, eof):
        raise AttributeError("Attribute 'eof' is read-only")


    # ----- FUNCTIONS -----
    def resolve(self):
        """
        Attempts to resolve the file-system alias or shortcut that this object refers to. If successful, creates and returns a new File object that points to the resolved file system element. Returns null if this object does not refer to an alias, or if the alias could not be resolved.
        """
        return _format_object_to_py(self._eval_on_this_object("resolve()"))

    def rename(self, name):
        """
        Renames the associated file. Does not resolve aliases, but renames the referenced alias or shortcut file itself. Returns true if the file was successfully renamed. 
        :param newName: The new file name, with no path information.
        :type name: str
        """
        self._check_type(name, str, 'arg "name" of function "File.rename"')
        return self._eval_on_this_object("rename({})".format(_format_object_to_es(name)))

    def remove(self):
        """
        Deletes the file associated with this object from disk immediately, without moving it to the system trash. Does not resolve aliases; instead, deletes the referenced alias or shortcut file itself. Returns true if the file was successfully removed. IMPORTANT: Cannot be undone. It is recommended that you prompt the user for permission before deleting.
        """
        return self._eval_on_this_object("remove()")

    def changePath(self, path):
        """
        Changes the path specification of the referenced file. 
        :param path: A string containing the new path, absolute or relative to the current folder.
        :type path: str
        """
        self._check_type(path, str, 'arg "path" of function "File.changePath"')
        return self._eval_on_this_object("changePath({})".format(_format_object_to_es(path)))

    def getRelativeURI(self, baseURI):
        """
        Retrieves and returns the path for this file, relative to the specified base path, in URI notation. If no base path is supplied, the URI is relative to the path of the current folder.Returns a string containing the relative URI. 
        :param basePath: A base path in URI notation.
        :type baseURI: str
        """
        self._check_type(baseURI, str, 'arg "baseURI" of function "File.getRelativeURI"')
        return self._eval_on_this_object("getRelativeURI({})".format(_format_object_to_es(baseURI)))

    def execute(self):
        """
        Executes or opens this file using the appropriate application, as if it had been double-clicked in a file browser. You can use this method to run scripts, launch applications, and so on.Returns true immediately if the application launch was successful.
        """
        return self._eval_on_this_object("execute()")

    def openDlg(self, prompt):
        """
        Opens the built-in platform-specific file-browsing dialog, in which the user can select an existing file or files, and creates new File objects to represent the selected files. Differs from the class method openDialog() in that it presets the current folder to this File object's parent folder and the current file to this object's associated file. If the user clicks OK, returns a File or Folder object for the selected file or folder, or an array of objects. If the user cancels, returns null. 
        :param prompt: A string containing the prompt text, if the dialog allows a prompt.
        :param filter: A filter that limits the types of files displayed in the dialog. In Windows,a filter expression such as "Javascript files:.jsx;All files:.". In Mac OS, a filter function that takes a File instance and returns true if the file should be included in the display, false if it should not.
        :param multiSelect: When true, the user can select multiple files and the return value is an array.
        :type prompt: str
        """
        self._check_type(prompt, str, 'arg "prompt" of function "File.openDlg"')
        return _format_object_to_py(self._eval_on_this_object("openDlg({})".format(_format_object_to_es(prompt))))

    def saveDlg(self, prompt):
        """
        Opens the built-in platform-specific file-browsing dialog, in which the user can select an existing file location to which to save information, and creates a new File object to represent the selected file. Differs from the class method saveDialog() in that it presets the current folder to this File object's parent folder and the file to this object's associated file. If the user clicks OK, returns a File object for the selected file. If the user cancels, returns null. 
        :param prompt: A string containing the prompt text, if the dialog allows a prompt.
        :param filter: In Windows only, a filter that limits the types of files displayed in the dialog. In Windows only,a filter expression such as "Javascript files:.jsx;All files:.". Not used In Mac OS.
        :type prompt: str
        """
        self._check_type(prompt, str, 'arg "prompt" of function "File.saveDlg"')
        return _format_object_to_py(self._eval_on_this_object("saveDlg({})".format(_format_object_to_es(prompt))))

    def toString(self):
        """
        Converts this object to a string.
        """
        return self._eval_on_this_object("toString()")

    def toSource(self):
        """
        Creates and returns a serialized string representation of this object. Pass the resulting string to eval() to recreate the object.
        """
        return self._eval_on_this_object("toSource()")

    def createAlias(self, path):
        """
        Makes this file a file-system alias or shortcut to the specified file. The referenced file for this object must not yet exist on disk. Returns true if the operation was successful. 
        :param path: A string containing the path of the target file.
        :type path: str
        """
        self._check_type(path, str, 'arg "path" of function "File.createAlias"')
        return self._eval_on_this_object("createAlias({})".format(_format_object_to_es(path)))

    def open(self, mode):
        """
        Opens the referenced file for subsequent read/write operations. The method resolves any aliases to find the file. Returns true if the file was opened successfully.The method attempts to detect the encoding of the open file. It reads a few bytes at the current location and tries to detect the Byte Order Mark character 0xFFFE. If found, the current position is advanced behind the detected character and the encoding property is set to one of the strings UCS-2BE, UCS-2LE, UCS4-BE, UCS-4LE, or UTF-8. If the marker character is not found, it checks for zero bytes at the current location and makes an assumption about one of the above formats (except UTF-8). If everything fails, the encoding property is set to the system encoding. IMPORTANT: Be careful about opening a file more than once. The operating system usually permits you to do so, but if you start writing to the file using two different File objects, you can destroy your data. 
        :param mode: The read-write mode, a single-character string. One of these characters: r (read) Opens for reading. If the file does not exist or cannot be found, the call fails. w (write) Opens a file for writing. If the file exists, its contents are destroyed. If the file does not exist, creates a new, empty file. e (edit) Opens an existing file for reading and writing. a (append) Opens an existing file for reading and writing, and moves the current position to the end of the file.
        :param type: In Mac OS, the type of a newly created file, a 4-character string. Ignored in Windows and UNIX.
        :param creator: In Mac OS, the creator of a newly created file, a 4-character string. Ignored in Windows and UNIX.
        :type mode: str
        """
        self._check_type(mode, str, 'arg "mode" of function "File.open"')
        return self._eval_on_this_object("open({})".format(_format_object_to_es(mode)))

    def close(self):
        """
        Closes this open file. Returns true if the file was closed successfully, false if an I/O error occurred.
        """
        return self._eval_on_this_object("close()")

    def read(self, count):
        """
        Reads the contents of the file, starting at the current position. Returns a string that contains up to the specified number of characters. If a number of characters is not supplied, reads from the current position to the end of the file. If the file is encoded, multiple bytes might be read to create single Unicode characters. 
        :param chars: An integer specifying the number of characters to read.
        :type count: float
        """
        self._check_type(count, float, 'arg "count" of function "File.read"')
        return self._eval_on_this_object("read({})".format(_format_object_to_es(count)))

    def readch(self):
        """
        Reads a single text character from the file at the current position. Line feeds are recognized as CR, LF, CRLF or LFCR pairs.If the file is encoded, multiple bytes might be read to create a single Unicode character. Returns a string that contains the character.
        """
        return self._eval_on_this_object("readch()")

    def readln(self):
        """
        Reads a single line of text from the file at the current position. Line feeds are recognized as CR, LF, CRLF or LFCR pairs.. If the file is encoded, multiple bytes might be read to create single Unicode characters. Returns a string that contains the text.
        """
        return self._eval_on_this_object("readln()")

    def write(self, text):
        """
        Writes the specified text to the file at the current position. You can supply multiple text values; the strings are concatenated to form a single string.For encoded files, writing a single Unicode character may write multiple bytes. Returns true if the write was successful.IMPORTANT: Be careful not to write to a file that is open in another application or object, as this can overwrite existing data. 
        :param text: A text string to be written.
        :type text: str
        """
        self._check_type(text, str, 'arg "text" of function "File.write"')
        return self._eval_on_this_object("write({})".format(_format_object_to_es(text)))

    def writeln(self, text):
        """
        Writes a string to the file at the current position and appends a line-feed sequence. You can supply multiple text values. The strings are concatenated into a single string, which is written in the file followed by one line-feed sequence, of the style specified by this object's linefeed property.For encoded files, writing a single Unicode character may write multiple bytes.Returns true if the write was successful.IMPORTANT: Be careful not to write to a file that is open in another application or object, as this can overwrite existing data. 
        :param text: A text string to be written.
        :type text: str
        """
        self._check_type(text, str, 'arg "text" of function "File.writeln"')
        return self._eval_on_this_object("writeln({})".format(_format_object_to_es(text)))

    def seek(self, pos):
        """
        Seeks to a given position in the file. The new position cannot be less than 0 or greater than the current file size. Returns true if the position was changed. 
        :param pos: The new current position in the file as an offset in bytes from the start, current position, or end, depending on the mode.
        :param mode: The seek mode. One of: 0: Seek to absolute position, where pos=0 is the first byte of the file. This is the default. 1: Seek relative to the current position. 2. Seek backward from the end of the file.
        :type pos: float
        """
        self._check_type(pos, float, 'arg "pos" of function "File.seek"')
        return self._eval_on_this_object("seek({})".format(_format_object_to_es(pos)))

    def tell(self):
        """
        Retrieves the current position as a byte offset from the start of the file. Returns a number, the position index.
        """
        return self._eval_on_this_object("tell()")

    def copy(self, where):
        """
        Copies this object's referenced file to the specified target location. Resolves any aliases to find the source file. If a file exists at the target location, it is overwritten. Returns true if the copy was successful. 
        :param target: A string with the URI path to the target location, or a File object that references the target location.
        :type where: str
        """
        self._check_type(where, str, 'arg "where" of function "File.copy"')
        return self._eval_on_this_object("copy({})".format(_format_object_to_es(where)))


class Date(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Date, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def getDate(self):
        return self._eval_on_this_object("getDate()")

    def getDay(self):
        return self._eval_on_this_object("getDay()")

    def getYear(self):
        return self._eval_on_this_object("getYear()")

    def getFullYear(self):
        return self._eval_on_this_object("getFullYear()")

    def getHours(self):
        return self._eval_on_this_object("getHours()")

    def getMilliseconds(self):
        return self._eval_on_this_object("getMilliseconds()")

    def getMinutes(self):
        return self._eval_on_this_object("getMinutes()")

    def getMonth(self):
        return self._eval_on_this_object("getMonth()")

    def getSeconds(self):
        return self._eval_on_this_object("getSeconds()")

    def getTime(self):
        return self._eval_on_this_object("getTime()")

    def getTimezoneOffset(self):
        return self._eval_on_this_object("getTimezoneOffset()")

    def getUTCDate(self):
        return self._eval_on_this_object("getUTCDate()")

    def getUTCDay(self):
        return self._eval_on_this_object("getUTCDay()")

    def getUTCFullYear(self):
        return self._eval_on_this_object("getUTCFullYear()")

    def getUTCHours(self):
        return self._eval_on_this_object("getUTCHours()")

    def getUTCMilliseconds(self):
        return self._eval_on_this_object("getUTCMilliseconds()")

    def getUTCMinutes(self):
        return self._eval_on_this_object("getUTCMinutes()")

    def getUTCMonth(self):
        return self._eval_on_this_object("getUTCMonth()")

    def getUTCSeconds(self):
        return self._eval_on_this_object("getUTCSeconds()")

    def setDate(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Date.setDate"')
        return self._eval_on_this_object("setDate({})".format(_format_object_to_es(n)))

    def setFullYear(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Date.setFullYear"')
        return self._eval_on_this_object("setFullYear({})".format(_format_object_to_es(n)))

    def setHours(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Date.setHours"')
        return self._eval_on_this_object("setHours({})".format(_format_object_to_es(n)))

    def setMilliseconds(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Date.setMilliseconds"')
        return self._eval_on_this_object("setMilliseconds({})".format(_format_object_to_es(n)))

    def setMinutes(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Date.setMinutes"')
        return self._eval_on_this_object("setMinutes({})".format(_format_object_to_es(n)))

    def setSeconds(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Date.setSeconds"')
        return self._eval_on_this_object("setSeconds({})".format(_format_object_to_es(n)))

    def setMonth(self, n, arg2):
        """
        :type n: float
        :type arg2: unknown
        """
        self._check_type(n, float, 'arg "n" of function "Date.setMonth"')
        return self._eval_on_this_object("setMonth({}, {})".format(_format_object_to_es(n), _format_object_to_es(arg2)))

    def setUTCDate(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Date.setUTCDate"')
        return self._eval_on_this_object("setUTCDate({})".format(_format_object_to_es(n)))

    def setUTCFullYear(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Date.setUTCFullYear"')
        return self._eval_on_this_object("setUTCFullYear({})".format(_format_object_to_es(n)))

    def setUTCHours(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Date.setUTCHours"')
        return self._eval_on_this_object("setUTCHours({})".format(_format_object_to_es(n)))

    def setUTCMilliseconds(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Date.setUTCMilliseconds"')
        return self._eval_on_this_object("setUTCMilliseconds({})".format(_format_object_to_es(n)))

    def setUTCMinutes(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Date.setUTCMinutes"')
        return self._eval_on_this_object("setUTCMinutes({})".format(_format_object_to_es(n)))

    def setUTCSeconds(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Date.setUTCSeconds"')
        return self._eval_on_this_object("setUTCSeconds({})".format(_format_object_to_es(n)))

    def setUTCMonth(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Date.setUTCMonth"')
        return self._eval_on_this_object("setUTCMonth({})".format(_format_object_to_es(n)))

    def setTime(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Date.setTime"')
        return self._eval_on_this_object("setTime({})".format(_format_object_to_es(n)))

    def setYear(self, n):
        """
        :type n: float
        """
        self._check_type(n, float, 'arg "n" of function "Date.setYear"')
        return self._eval_on_this_object("setYear({})".format(_format_object_to_es(n)))

    def toDateString(self):
        return self._eval_on_this_object("toDateString()")

    def toTimeString(self):
        return self._eval_on_this_object("toTimeString()")

    def toLocaleString(self):
        return self._eval_on_this_object("toLocaleString()")

    def toLocaleDateString(self):
        return self._eval_on_this_object("toLocaleDateString()")

    def toLocaleTimeString(self):
        return self._eval_on_this_object("toLocaleTimeString()")

    def toGMTString(self):
        return self._eval_on_this_object("toGMTString()")

    def toUTCString(self):
        return self._eval_on_this_object("toUTCString()")

    def toString(self):
        return self._eval_on_this_object("toString()")

    def valueOf(self):
        return self._eval_on_this_object("valueOf()")

    def toSource(self):
        return self._eval_on_this_object("toSource()")

    def toJSON(self):
        return self._eval_on_this_object("toJSON()")


class Folder(PymiereBaseObject):
    """ Represents a file-system folder or directory in a platform-independent manner. """
    def __init__(self, pymiere_id=None):
        super(Folder, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    """ When true, the object refers to a file system alias or shortcut. """
    @property
    def alias(self):
        return self._eval_on_this_object('alias')
    @alias.setter
    def alias(self, alias):
        raise AttributeError("Attribute 'alias' is read-only")

    """ The creation date of the referenced folder, or null if the object does not refer to a folder on disk. """
    @property
    def created(self):
        kwargs = self._eval_on_this_object('created')
        return Date(**kwargs) if kwargs else None
    @created.setter
    def created(self, created):
        raise AttributeError("Attribute 'created' is read-only")

    """ A message describing the most recent file system error. Typically set by the file system, but a script can set it. Setting this value clears any error message and resets the error bit for opened files. Contains the empty string if there is no error. """
    @property
    def error(self):
        return self._eval_on_this_object('error')
    @error.setter
    def error(self, error):
        self._eval_on_this_object("error = {}".format(_format_object_to_es(error)))

    """ When true, this object refers to a folder that currently exists in the file system. """
    @property
    def exists(self):
        return self._eval_on_this_object('exists')
    @exists.setter
    def exists(self, exists):
        raise AttributeError("Attribute 'exists' is read-only")

    """ The platform-specific name of the referenced folder as a full path name. """
    @property
    def fsName(self):
        return self._eval_on_this_object('fsName')
    @fsName.setter
    def fsName(self, fsName):
        raise AttributeError("Attribute 'fsName' is read-only")

    """ The full path name for the referenced folder in URI notation. . """
    @property
    def fullName(self):
        return self._eval_on_this_object('fullName')
    @fullName.setter
    def fullName(self, fullName):
        raise AttributeError("Attribute 'fullName' is read-only")

    """ The full path name for the referenced folder in URI notation. """
    @property
    def absoluteURI(self):
        return self._eval_on_this_object('absoluteURI')
    @absoluteURI.setter
    def absoluteURI(self, absoluteURI):
        raise AttributeError("Attribute 'absoluteURI' is read-only")

    """ The path name for the referenced folder in URI notation, relative to the current folder. """
    @property
    def relativeURI(self):
        return self._eval_on_this_object('relativeURI')
    @relativeURI.setter
    def relativeURI(self, relativeURI):
        raise AttributeError("Attribute 'relativeURI' is read-only")

    """ The date of the referenced folder's last modification, or null if the object does not refer to a folder on disk. """
    @property
    def modified(self):
        kwargs = self._eval_on_this_object('modified')
        return Date(**kwargs) if kwargs else None
    @modified.setter
    def modified(self, modified):
        raise AttributeError("Attribute 'modified' is read-only")

    """ The folder name portion of the absolute URI for the referenced file, without the path specification. """
    @property
    def name(self):
        return self._eval_on_this_object('name')
    @name.setter
    def name(self, name):
        raise AttributeError("Attribute 'name' is read-only")

    """ The localized name portion of the absolute URI for the referenced folder, without the path specification. """
    @property
    def displayName(self):
        return self._eval_on_this_object('displayName')
    @displayName.setter
    def displayName(self, displayName):
        raise AttributeError("Attribute 'displayName' is read-only")

    """ The path portion of the object absolute URI for the referenced file, without the folder name. """
    @property
    def path(self):
        return self._eval_on_this_object('path')
    @path.setter
    def path(self, path):
        raise AttributeError("Attribute 'path' is read-only")

    """ TThe Folder object for the folder that contains this folder, or null if this object refers to the root folder of a volume. """
    @property
    def parent(self):
        kwargs = self._eval_on_this_object('parent')
        return Folder(**kwargs) if kwargs else None
    @parent.setter
    def parent(self, parent):
        raise AttributeError("Attribute 'parent' is read-only")


    # ----- FUNCTIONS -----
    def resolve(self):
        """
        Attempts to resolve the file-system alias or shortcut that this object refers to. If successful, creates and returns a new Folder object that points to the resolved file system element. Returns null if this object does not refer to an alias, or if the alias could not be resolved.
        """
        return _format_object_to_py(self._eval_on_this_object("resolve()"))

    def rename(self, name):
        """
        Renames the associated folder. Does not resolve aliases, but renames the referenced alias or shortcut file itself. Returns true if the folder was successfully renamed. 
        :param newName: The new folder name, with no path information.
        :type name: str
        """
        self._check_type(name, str, 'arg "name" of function "Folder.rename"')
        return self._eval_on_this_object("rename({})".format(_format_object_to_es(name)))

    def remove(self):
        """
        Deletes the folder associated with this object from disk immediately, without moving it to the system trash. Folders must be empty before they can be deleted. Does not resolve aliases; instead, deletes the referenced alias or shortcut file itself. Returns true if the file was successfully removed. IMPORTANT: Cannot be undone. It is recommended that you prompt the user for permission before deleting.
        """
        return self._eval_on_this_object("remove()")

    def changePath(self, path):
        """
        Changes the path specification of the referenced folder. 
        :param path: A string containing the new path, absolute or relative to the current folder.
        :type path: str
        """
        self._check_type(path, str, 'arg "path" of function "Folder.changePath"')
        return self._eval_on_this_object("changePath({})".format(_format_object_to_es(path)))

    def getRelativeURI(self, baseURI):
        """
        Retrieves and returns the path for this file, relative to the specified base path, in URI notation. If no base path is supplied, the URI is relative to the path of the current folder.Returns a string containing the relative URI. 
        :param basePath: A base path in URI notation.
        :type baseURI: str
        """
        self._check_type(baseURI, str, 'arg "baseURI" of function "Folder.getRelativeURI"')
        return self._eval_on_this_object("getRelativeURI({})".format(_format_object_to_es(baseURI)))

    def execute(self):
        """
        Opens this folder in the platform-specific file browser (as if it had been double-clicked in the file browser). Returns true immediately if the folder was opened successfully.
        """
        return self._eval_on_this_object("execute()")

    def openDlg(self, prompt):
        """
        :type prompt: str
        """
        self._check_type(prompt, str, 'arg "prompt" of function "Folder.openDlg"')
        return _format_object_to_py(self._eval_on_this_object("openDlg({})".format(_format_object_to_es(prompt))))

    def saveDlg(self, prompt):
        """
        :type prompt: str
        """
        self._check_type(prompt, str, 'arg "prompt" of function "Folder.saveDlg"')
        return _format_object_to_py(self._eval_on_this_object("saveDlg({})".format(_format_object_to_es(prompt))))

    def toString(self):
        """
        Converts this object to a string.
        """
        return self._eval_on_this_object("toString()")

    def toSource(self):
        """
        Creates and returns a serialized string representation of this object. Pass the resulting string to eval() to recreate the object.
        """
        return self._eval_on_this_object("toSource()")

    def selectDlg(self, prompt):
        """
        Opens the built-in platform-specific file-browsing dialog, and creates a new File or Folder object for the selected file or folder. Differs from the class method selectDialog() in that it preselects this folder. If the user clicks OK, returns a File or Folder object for the selected file or folder. If the user cancels, returns null. 
        :param prompt: The prompt text, if the dialog allows a prompt.
        :type prompt: str
        """
        self._check_type(prompt, str, 'arg "prompt" of function "Folder.selectDlg"')
        return _format_object_to_py(self._eval_on_this_object("selectDlg({})".format(_format_object_to_es(prompt))))

    def getFiles(self, pattern):
        """
        Retrieves the contents of this folder, filtered by the supplied mask. Returns an array of File and Folder objects, or null if this object's referenced folder does not exist. 
        :param mask: A search mask for file names, specified as a string or a function. A mask string can contain question mark (?) and asterisk () wild cards. Default is "", which matches all file names. Can also be the name of a function that takes a File or Folder object as its argument. It is called for each file or folder found in the search; if it returns true, the object is added to the return array. NOTE: In Windows, all aliases end with the extension .lnk. ExtendScript strips this from the file name when found, in order to preserve compatibility with other operating systems. You can search for all aliases by supplying the search mask ".lnk", but note that such code is not portable.
        :type pattern: str
        """
        self._check_type(pattern, str, 'arg "pattern" of function "Folder.getFiles"')
        return Array(**self._eval_on_this_object("getFiles({})".format(_format_object_to_es(pattern))))

    def create(self):
        """
        Creates a folder at the location given by this object's path property. Returns true if the folder was created.
        """
        return self._eval_on_this_object("create()")


class FootageInterpretation(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(FootageInterpretation, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def frameRate(self):
        return self._eval_on_this_object('frameRate')
    @frameRate.setter
    def frameRate(self, frameRate):
        self._eval_on_this_object("frameRate = {}".format(_format_object_to_es(frameRate)))

    @property
    def pixelAspectRatio(self):
        return self._eval_on_this_object('pixelAspectRatio')
    @pixelAspectRatio.setter
    def pixelAspectRatio(self, pixelAspectRatio):
        self._eval_on_this_object("pixelAspectRatio = {}".format(_format_object_to_es(pixelAspectRatio)))

    @property
    def fieldType(self):
        return self._eval_on_this_object('fieldType')
    @fieldType.setter
    def fieldType(self, fieldType):
        self._eval_on_this_object("fieldType = {}".format(_format_object_to_es(fieldType)))

    @property
    def removePulldown(self):
        return self._eval_on_this_object('removePulldown')
    @removePulldown.setter
    def removePulldown(self, removePulldown):
        self._eval_on_this_object("removePulldown = {}".format(_format_object_to_es(removePulldown)))

    @property
    def alphaUsage(self):
        return self._eval_on_this_object('alphaUsage')
    @alphaUsage.setter
    def alphaUsage(self, alphaUsage):
        self._eval_on_this_object("alphaUsage = {}".format(_format_object_to_es(alphaUsage)))

    @property
    def ignoreAlpha(self):
        return self._eval_on_this_object('ignoreAlpha')
    @ignoreAlpha.setter
    def ignoreAlpha(self, ignoreAlpha):
        self._eval_on_this_object("ignoreAlpha = {}".format(_format_object_to_es(ignoreAlpha)))

    @property
    def invertAlpha(self):
        return self._eval_on_this_object('invertAlpha')
    @invertAlpha.setter
    def invertAlpha(self, invertAlpha):
        self._eval_on_this_object("invertAlpha = {}".format(_format_object_to_es(invertAlpha)))

    @property
    def vrConformProjectionType(self):
        return self._eval_on_this_object('vrConformProjectionType')
    @vrConformProjectionType.setter
    def vrConformProjectionType(self, vrConformProjectionType):
        self._eval_on_this_object("vrConformProjectionType = {}".format(_format_object_to_es(vrConformProjectionType)))

    @property
    def vrLayoutType(self):
        return self._eval_on_this_object('vrLayoutType')
    @vrLayoutType.setter
    def vrLayoutType(self, vrLayoutType):
        self._eval_on_this_object("vrLayoutType = {}".format(_format_object_to_es(vrLayoutType)))

    @property
    def vrHorizontalView(self):
        return self._eval_on_this_object('vrHorizontalView')
    @vrHorizontalView.setter
    def vrHorizontalView(self, vrHorizontalView):
        self._eval_on_this_object("vrHorizontalView = {}".format(_format_object_to_es(vrHorizontalView)))

    @property
    def vrVerticalView(self):
        return self._eval_on_this_object('vrVerticalView')
    @vrVerticalView.setter
    def vrVerticalView(self, vrVerticalView):
        self._eval_on_this_object("vrVerticalView = {}".format(_format_object_to_es(vrVerticalView)))

    @property
    def ALPHACHANNEL_NONE(self):
        return self._eval_on_this_object('ALPHACHANNEL_NONE')
    @ALPHACHANNEL_NONE.setter
    def ALPHACHANNEL_NONE(self, ALPHACHANNEL_NONE):
        raise AttributeError("Attribute 'ALPHACHANNEL_NONE' is read-only")

    @property
    def ALPHACHANNEL_STRAIGHT(self):
        return self._eval_on_this_object('ALPHACHANNEL_STRAIGHT')
    @ALPHACHANNEL_STRAIGHT.setter
    def ALPHACHANNEL_STRAIGHT(self, ALPHACHANNEL_STRAIGHT):
        raise AttributeError("Attribute 'ALPHACHANNEL_STRAIGHT' is read-only")

    @property
    def ALPHACHANNEL_PREMULTIPLIED(self):
        return self._eval_on_this_object('ALPHACHANNEL_PREMULTIPLIED')
    @ALPHACHANNEL_PREMULTIPLIED.setter
    def ALPHACHANNEL_PREMULTIPLIED(self, ALPHACHANNEL_PREMULTIPLIED):
        raise AttributeError("Attribute 'ALPHACHANNEL_PREMULTIPLIED' is read-only")

    @property
    def ALPHACHANNEL_IGNORE(self):
        return self._eval_on_this_object('ALPHACHANNEL_IGNORE')
    @ALPHACHANNEL_IGNORE.setter
    def ALPHACHANNEL_IGNORE(self, ALPHACHANNEL_IGNORE):
        raise AttributeError("Attribute 'ALPHACHANNEL_IGNORE' is read-only")

    @property
    def FIELD_TYPE_DEFAULT(self):
        return self._eval_on_this_object('FIELD_TYPE_DEFAULT')
    @FIELD_TYPE_DEFAULT.setter
    def FIELD_TYPE_DEFAULT(self, FIELD_TYPE_DEFAULT):
        raise AttributeError("Attribute 'FIELD_TYPE_DEFAULT' is read-only")

    @property
    def FIELD_TYPE_PROGRESSIVE(self):
        return self._eval_on_this_object('FIELD_TYPE_PROGRESSIVE')
    @FIELD_TYPE_PROGRESSIVE.setter
    def FIELD_TYPE_PROGRESSIVE(self, FIELD_TYPE_PROGRESSIVE):
        raise AttributeError("Attribute 'FIELD_TYPE_PROGRESSIVE' is read-only")

    @property
    def FIELD_TYPE_UPPERFIRST(self):
        return self._eval_on_this_object('FIELD_TYPE_UPPERFIRST')
    @FIELD_TYPE_UPPERFIRST.setter
    def FIELD_TYPE_UPPERFIRST(self, FIELD_TYPE_UPPERFIRST):
        raise AttributeError("Attribute 'FIELD_TYPE_UPPERFIRST' is read-only")

    @property
    def FIELD_TYPE_LOWERFIRST(self):
        return self._eval_on_this_object('FIELD_TYPE_LOWERFIRST')
    @FIELD_TYPE_LOWERFIRST.setter
    def FIELD_TYPE_LOWERFIRST(self, FIELD_TYPE_LOWERFIRST):
        raise AttributeError("Attribute 'FIELD_TYPE_LOWERFIRST' is read-only")

    @property
    def VR_CONFORM_PROJECTION_NONE(self):
        return self._eval_on_this_object('VR_CONFORM_PROJECTION_NONE')
    @VR_CONFORM_PROJECTION_NONE.setter
    def VR_CONFORM_PROJECTION_NONE(self, VR_CONFORM_PROJECTION_NONE):
        raise AttributeError("Attribute 'VR_CONFORM_PROJECTION_NONE' is read-only")

    @property
    def VR_CONFORM_PROJECTION_EQUIRECTANGULAR(self):
        return self._eval_on_this_object('VR_CONFORM_PROJECTION_EQUIRECTANGULAR')
    @VR_CONFORM_PROJECTION_EQUIRECTANGULAR.setter
    def VR_CONFORM_PROJECTION_EQUIRECTANGULAR(self, VR_CONFORM_PROJECTION_EQUIRECTANGULAR):
        raise AttributeError("Attribute 'VR_CONFORM_PROJECTION_EQUIRECTANGULAR' is read-only")

    @property
    def VR_LAYOUT_MONOSCOPIC(self):
        return self._eval_on_this_object('VR_LAYOUT_MONOSCOPIC')
    @VR_LAYOUT_MONOSCOPIC.setter
    def VR_LAYOUT_MONOSCOPIC(self, VR_LAYOUT_MONOSCOPIC):
        raise AttributeError("Attribute 'VR_LAYOUT_MONOSCOPIC' is read-only")

    @property
    def VR_LAYOUT_STEREO_OVER_UNDER(self):
        return self._eval_on_this_object('VR_LAYOUT_STEREO_OVER_UNDER')
    @VR_LAYOUT_STEREO_OVER_UNDER.setter
    def VR_LAYOUT_STEREO_OVER_UNDER(self, VR_LAYOUT_STEREO_OVER_UNDER):
        raise AttributeError("Attribute 'VR_LAYOUT_STEREO_OVER_UNDER' is read-only")

    @property
    def VR_LAYOUT_STEREO_SIDE_BY_SIDE(self):
        return self._eval_on_this_object('VR_LAYOUT_STEREO_SIDE_BY_SIDE')
    @VR_LAYOUT_STEREO_SIDE_BY_SIDE.setter
    def VR_LAYOUT_STEREO_SIDE_BY_SIDE(self, VR_LAYOUT_STEREO_SIDE_BY_SIDE):
        raise AttributeError("Attribute 'VR_LAYOUT_STEREO_SIDE_BY_SIDE' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "FootageInterpretation.bind"')
        self._check_type(function, any, 'arg "function" of function "FootageInterpretation.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "FootageInterpretation.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "FootageInterpretation.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "FootageInterpretation.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "FootageInterpretation.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))


class Time(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Time, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def seconds(self):
        return self._eval_on_this_object('seconds')
    @seconds.setter
    def seconds(self, seconds):
        self._eval_on_this_object("seconds = {}".format(_format_object_to_es(seconds)))

    @property
    def ticks(self):
        return self._eval_on_this_object('ticks')
    @ticks.setter
    def ticks(self, ticks):
        self._eval_on_this_object("ticks = {}".format(_format_object_to_es(ticks)))


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Time.bind"')
        self._check_type(function, any, 'arg "function" of function "Time.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Time.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Time.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "Time.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "Time.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def setSecondsAsFraction(self, numerator, denominator):
        """
        :type numerator: float
        :type denominator: float
        """
        self._check_type(numerator, float, 'arg "numerator" of function "Time.setSecondsAsFraction"')
        self._check_type(denominator, float, 'arg "denominator" of function "Time.setSecondsAsFraction"')
        self._eval_on_this_object("setSecondsAsFraction({}, {})".format(_format_object_to_es(numerator), _format_object_to_es(denominator)))

    def getFormatted(self, time, timeDisplay):
        """
        :type time: Object
        :type timeDisplay: float
        """
        self._check_type(timeDisplay, float, 'arg "timeDisplay" of function "Time.getFormatted"')
        return self._eval_on_this_object("getFormatted({}, {})".format(_format_object_to_es(time), _format_object_to_es(timeDisplay)))


class Track(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Track, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def id(self):
        return self._eval_on_this_object('id')
    @id.setter
    def id(self, id):
        raise AttributeError("Attribute 'id' is read-only")

    @property
    def name(self):
        return self._eval_on_this_object('name')
    @name.setter
    def name(self, name):
        self._eval_on_this_object("name = {}".format(_format_object_to_es(name)))

    @property
    def mediaType(self):
        return self._eval_on_this_object('mediaType')
    @mediaType.setter
    def mediaType(self, mediaType):
        raise AttributeError("Attribute 'mediaType' is read-only")

    @property
    def clips(self):
        kwargs = self._eval_on_this_object('clips')
        return TrackItemCollection(**kwargs) if kwargs else None
    @clips.setter
    def clips(self, clips):
        raise AttributeError("Attribute 'clips' is read-only")

    @property
    def transitions(self):
        kwargs = self._eval_on_this_object('transitions')
        return TrackItemCollection(**kwargs) if kwargs else None
    @transitions.setter
    def transitions(self, transitions):
        raise AttributeError("Attribute 'transitions' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Track.bind"')
        self._check_type(function, any, 'arg "function" of function "Track.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Track.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Track.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "Track.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "Track.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def isMuted(self):
        return self._eval_on_this_object("isMuted()")

    def setMute(self, arg1):
        """
        :type arg1: float
        """
        self._check_type(arg1, float, 'arg "arg1" of function "Track.setMute"')
        self._eval_on_this_object("setMute({})".format(_format_object_to_es(arg1)))

    def isLocked(self):
        return self._eval_on_this_object("isLocked()")

    def setLocked(self, arg1):
        """
        :type arg1: float
        """
        self._check_type(arg1, float, 'arg "arg1" of function "Track.setLocked"')
        self._eval_on_this_object("setLocked({})".format(_format_object_to_es(arg1)))

    def isTargeted(self):
        return self._eval_on_this_object("isTargeted()")

    def setTargeted(self, isTargeted, shouldBroadcast):
        """
        :type isTargeted: bool
        :type shouldBroadcast: bool
        """
        self._check_type(isTargeted, bool, 'arg "isTargeted" of function "Track.setTargeted"')
        self._check_type(shouldBroadcast, bool, 'arg "shouldBroadcast" of function "Track.setTargeted"')
        self._eval_on_this_object("setTargeted({}, {})".format(_format_object_to_es(isTargeted), _format_object_to_es(shouldBroadcast)))

    def insertClip(self, clipProjectItem, time):
        """
        :type clipProjectItem: ProjectItem
        :type time: Object
        """
        self._check_type(clipProjectItem, ProjectItem, 'arg "clipProjectItem" of function "Track.insertClip"')
        self._eval_on_this_object("insertClip({}, {})".format(_format_object_to_es(clipProjectItem), _format_object_to_es(time)))

    def overwriteClip(self, clipProjectItem, time):
        """
        :type clipProjectItem: ProjectItem
        :type time: Object
        """
        self._check_type(clipProjectItem, ProjectItem, 'arg "clipProjectItem" of function "Track.overwriteClip"')
        self._eval_on_this_object("overwriteClip({}, {})".format(_format_object_to_es(clipProjectItem), _format_object_to_es(time)))


class TrackItemCollection(PymiereBaseCollection):
    def __init__(self, pymiere_id):
        super(TrackItemCollection, self).__init__(pymiere_id, "numItems")

    def __getitem__(self, index):
        return TrackItem(**super(TrackItemCollection, self).__getitem__(index))

    def __iter__(self):
        return iter([self.__getitem__(i) for i in range(len(self))])


class TrackItem(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(TrackItem, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def duration(self):
        kwargs = self._eval_on_this_object('duration')
        return Time(**kwargs) if kwargs else None
    @duration.setter
    def duration(self, duration):
        raise AttributeError("Attribute 'duration' is read-only")

    @property
    def start(self):
        kwargs = self._eval_on_this_object('start')
        return Time(**kwargs) if kwargs else None
    @start.setter
    def start(self, start):
        self._check_type(start, any, 'TrackItem.start')
        try:
            self._eval_on_this_object("start = {}".format(_format_object_to_es(start)))
        except ExtendScriptError as e:
            # in PremierePro 2020 this will raise a specific error although it actually worked...
            # see https://community.adobe.com/t5/premiere-pro/extend-script-crash-when-setting-start-end-on-trackitem/td-p/11338656?page=1
            if e.message != "Cannot set property start":
                raise e

    @property
    def end(self):
        kwargs = self._eval_on_this_object('end')
        return Time(**kwargs) if kwargs else None
    @end.setter
    def end(self, end):
        self._check_type(end, Time, 'TrackItem.end')
        try:
            self._eval_on_this_object("end = {}".format(_format_object_to_es(end)))
        except ExtendScriptError as e:
            # in PremierePro 2020 this will raise a specific error although it actually worked...
            # see https://community.adobe.com/t5/premiere-pro/extend-script-crash-when-setting-start-end-on-trackitem/td-p/11338656?page=1
            if e.message != "Cannot set property end":
                raise e

    @property
    def inPoint(self):
        kwargs = self._eval_on_this_object('inPoint')
        return Time(**kwargs) if kwargs else None
    @inPoint.setter
    def inPoint(self, inPoint):
        self._check_type(inPoint, Time, 'TrackItem.inPoint')
        try:
            self._eval_on_this_object("inPoint = {}".format(_format_object_to_es(inPoint)))
        except ExtendScriptError as e:
            # in PremierePro 2020 this will raise a specific error although it actually worked...
            # see https://community.adobe.com/t5/premiere-pro/extend-script-crash-when-setting-start-end-on-trackitem/td-p/11338656?page=1
            if e.message != "Cannot set property inPoint":
                raise e

    @property
    def outPoint(self):
        kwargs = self._eval_on_this_object('outPoint')
        return Time(**kwargs) if kwargs else None
    @outPoint.setter
    def outPoint(self, outPoint):
        self._check_type(outPoint, Time, 'TrackItem.outPoint')
        try:
            self._eval_on_this_object("outPoint = {}".format(_format_object_to_es(outPoint)))
        except ExtendScriptError as e:
            # in PremierePro 2020 this will raise a specific error although it actually worked...
            # see https://community.adobe.com/t5/premiere-pro/extend-script-crash-when-setting-start-end-on-trackitem/td-p/11338656?page=1
            if e.message != "Cannot set property outPoint":
                raise e

    @property
    def type(self):
        return self._eval_on_this_object('type')
    @type.setter
    def type(self, type):
        raise AttributeError("Attribute 'type' is read-only")

    @property
    def mediaType(self):
        return self._eval_on_this_object('mediaType')
    @mediaType.setter
    def mediaType(self, mediaType):
        raise AttributeError("Attribute 'mediaType' is read-only")

    @property
    def projectItem(self):
        kwargs = self._eval_on_this_object('projectItem')
        return ProjectItem(**kwargs) if kwargs else None
    @projectItem.setter
    def projectItem(self, projectItem):
        self._check_type(projectItem, ProjectItem, 'TrackItem.projectItem')
        self._eval_on_this_object("projectItem = {}".format(_format_object_to_es(projectItem)))

    @property
    def name(self):
        return self._eval_on_this_object('name')
    @name.setter
    def name(self, name):
        self._eval_on_this_object("name = {}".format(_format_object_to_es(name)))

    @property
    def matchName(self):
        return self._eval_on_this_object('matchName')
    @matchName.setter
    def matchName(self, matchName):
        raise AttributeError("Attribute 'matchName' is read-only")

    @property
    def nodeId(self):
        return self._eval_on_this_object('nodeId')
    @nodeId.setter
    def nodeId(self, nodeId):
        raise AttributeError("Attribute 'nodeId' is read-only")

    @property
    def components(self):
        kwargs = self._eval_on_this_object('components')
        return ComponentCollection(**kwargs) if kwargs else None
    @components.setter
    def components(self, components):
        raise AttributeError("Attribute 'components' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "TrackItem.bind"')
        self._check_type(function, any, 'arg "function" of function "TrackItem.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "TrackItem.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "TrackItem.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "TrackItem.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "TrackItem.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def isSelected(self):
        return self._eval_on_this_object("isSelected()")

    def setSelected(self, isSelected, updateUI):
        """
        :type isSelected: float
        :type updateUI: float
        """
        self._check_type(isSelected, float, 'arg "isSelected" of function "TrackItem.setSelected"')
        self._check_type(updateUI, float, 'arg "updateUI" of function "TrackItem.setSelected"')
        self._eval_on_this_object("setSelected({}, {})".format(_format_object_to_es(isSelected), _format_object_to_es(updateUI)))

    def getLinkedItems(self):
        return TrackItemCollection(**self._eval_on_this_object("getLinkedItems()"))

    def isMGT(self):
        return self._eval_on_this_object("isMGT()")

    def getMGTComponent(self):
        return Component(**self._eval_on_this_object("getMGTComponent()"))

    def isAdjustmentLayer(self):
        return self._eval_on_this_object("isAdjustmentLayer()")

    def getSpeed(self):
        return self._eval_on_this_object("getSpeed()")

    def isSpeedReversed(self):
        return self._eval_on_this_object("isSpeedReversed()")

    def getMatchName(self):
        return self._eval_on_this_object("getMatchName()")

    def remove(self, inRipple, inAlignToVideo):
        """
        :type inRipple: bool
        :type inAlignToVideo: bool
        """
        self._check_type(inRipple, bool, 'arg "inRipple" of function "TrackItem.remove"')
        self._check_type(inAlignToVideo, bool, 'arg "inAlignToVideo" of function "TrackItem.remove"')
        return self._eval_on_this_object("remove({}, {})".format(_format_object_to_es(inRipple), _format_object_to_es(inAlignToVideo)))


class SequenceSettings(PymiereBaseObject):
    """ Structure containing sequence settings. """
    def __init__(self, pymiere_id=None):
        super(SequenceSettings, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def editingMode(self):
        return self._eval_on_this_object('editingMode')
    @editingMode.setter
    def editingMode(self, editingMode):
        self._eval_on_this_object("editingMode = {}".format(_format_object_to_es(editingMode)))

    @property
    def videoFrameRate(self):
        kwargs = self._eval_on_this_object('videoFrameRate')
        return Time(**kwargs) if kwargs else None
    @videoFrameRate.setter
    def videoFrameRate(self, videoFrameRate):
        self._check_type(videoFrameRate, Time, 'SequenceSettings.videoFrameRate')
        self._eval_on_this_object("videoFrameRate = {}".format(_format_object_to_es(videoFrameRate)))

    @property
    def videoFrameWidth(self):
        return self._eval_on_this_object('videoFrameWidth')
    @videoFrameWidth.setter
    def videoFrameWidth(self, videoFrameWidth):
        self._eval_on_this_object("videoFrameWidth = {}".format(_format_object_to_es(videoFrameWidth)))

    @property
    def videoFrameHeight(self):
        return self._eval_on_this_object('videoFrameHeight')
    @videoFrameHeight.setter
    def videoFrameHeight(self, videoFrameHeight):
        self._eval_on_this_object("videoFrameHeight = {}".format(_format_object_to_es(videoFrameHeight)))

    @property
    def videoPixelAspectRatio(self):
        return self._eval_on_this_object('videoPixelAspectRatio')
    @videoPixelAspectRatio.setter
    def videoPixelAspectRatio(self, videoPixelAspectRatio):
        self._eval_on_this_object("videoPixelAspectRatio = {}".format(_format_object_to_es(videoPixelAspectRatio)))

    @property
    def videoFieldType(self):
        return self._eval_on_this_object('videoFieldType')
    @videoFieldType.setter
    def videoFieldType(self, videoFieldType):
        self._eval_on_this_object("videoFieldType = {}".format(_format_object_to_es(videoFieldType)))

    @property
    def videoDisplayFormat(self):
        return self._eval_on_this_object('videoDisplayFormat')
    @videoDisplayFormat.setter
    def videoDisplayFormat(self, videoDisplayFormat):
        self._eval_on_this_object("videoDisplayFormat = {}".format(_format_object_to_es(videoDisplayFormat)))

    @property
    def audioChannelType(self):
        return self._eval_on_this_object('audioChannelType')
    @audioChannelType.setter
    def audioChannelType(self, audioChannelType):
        self._eval_on_this_object("audioChannelType = {}".format(_format_object_to_es(audioChannelType)))

    @property
    def audioChannelCount(self):
        return self._eval_on_this_object('audioChannelCount')
    @audioChannelCount.setter
    def audioChannelCount(self, audioChannelCount):
        self._eval_on_this_object("audioChannelCount = {}".format(_format_object_to_es(audioChannelCount)))

    @property
    def audioSampleRate(self):
        kwargs = self._eval_on_this_object('audioSampleRate')
        return Time(**kwargs) if kwargs else None
    @audioSampleRate.setter
    def audioSampleRate(self, audioSampleRate):
        self._check_type(audioSampleRate, Time, 'SequenceSettings.audioSampleRate')
        self._eval_on_this_object("audioSampleRate = {}".format(_format_object_to_es(audioSampleRate)))

    @property
    def audioDisplayFormat(self):
        return self._eval_on_this_object('audioDisplayFormat')
    @audioDisplayFormat.setter
    def audioDisplayFormat(self, audioDisplayFormat):
        self._eval_on_this_object("audioDisplayFormat = {}".format(_format_object_to_es(audioDisplayFormat)))

    @property
    def previewFileFormat(self):
        return self._eval_on_this_object('previewFileFormat')
    @previewFileFormat.setter
    def previewFileFormat(self, previewFileFormat):
        self._eval_on_this_object("previewFileFormat = {}".format(_format_object_to_es(previewFileFormat)))

    @property
    def previewCodec(self):
        return self._eval_on_this_object('previewCodec')
    @previewCodec.setter
    def previewCodec(self, previewCodec):
        self._eval_on_this_object("previewCodec = {}".format(_format_object_to_es(previewCodec)))

    @property
    def previewFrameWidth(self):
        return self._eval_on_this_object('previewFrameWidth')
    @previewFrameWidth.setter
    def previewFrameWidth(self, previewFrameWidth):
        self._eval_on_this_object("previewFrameWidth = {}".format(_format_object_to_es(previewFrameWidth)))

    @property
    def previewFrameHeight(self):
        return self._eval_on_this_object('previewFrameHeight')
    @previewFrameHeight.setter
    def previewFrameHeight(self, previewFrameHeight):
        self._eval_on_this_object("previewFrameHeight = {}".format(_format_object_to_es(previewFrameHeight)))

    @property
    def maximumBitDepth(self):
        return self._eval_on_this_object('maximumBitDepth')
    @maximumBitDepth.setter
    def maximumBitDepth(self, maximumBitDepth):
        self._eval_on_this_object("maximumBitDepth = {}".format(_format_object_to_es(maximumBitDepth)))

    @property
    def maximumRenderQuality(self):
        return self._eval_on_this_object('maximumRenderQuality')
    @maximumRenderQuality.setter
    def maximumRenderQuality(self, maximumRenderQuality):
        self._eval_on_this_object("maximumRenderQuality = {}".format(_format_object_to_es(maximumRenderQuality)))

    @property
    def compositeLinearColor(self):
        return self._eval_on_this_object('compositeLinearColor')
    @compositeLinearColor.setter
    def compositeLinearColor(self, compositeLinearColor):
        self._eval_on_this_object("compositeLinearColor = {}".format(_format_object_to_es(compositeLinearColor)))

    @property
    def vrProjection(self):
        return self._eval_on_this_object('vrProjection')
    @vrProjection.setter
    def vrProjection(self, vrProjection):
        self._eval_on_this_object("vrProjection = {}".format(_format_object_to_es(vrProjection)))

    @property
    def vrLayout(self):
        return self._eval_on_this_object('vrLayout')
    @vrLayout.setter
    def vrLayout(self, vrLayout):
        self._eval_on_this_object("vrLayout = {}".format(_format_object_to_es(vrLayout)))

    @property
    def vrHorzCapturedView(self):
        return self._eval_on_this_object('vrHorzCapturedView')
    @vrHorzCapturedView.setter
    def vrHorzCapturedView(self, vrHorzCapturedView):
        self._eval_on_this_object("vrHorzCapturedView = {}".format(_format_object_to_es(vrHorzCapturedView)))

    @property
    def vrVertCapturedView(self):
        return self._eval_on_this_object('vrVertCapturedView')
    @vrVertCapturedView.setter
    def vrVertCapturedView(self, vrVertCapturedView):
        self._eval_on_this_object("vrVertCapturedView = {}".format(_format_object_to_es(vrVertCapturedView)))


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "SequenceSettings.bind"')
        self._check_type(function, any, 'arg "function" of function "SequenceSettings.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "SequenceSettings.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "SequenceSettings.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "SequenceSettings.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "SequenceSettings.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))


class Marker(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Marker, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def start(self):
        kwargs = self._eval_on_this_object('start')
        return Time(**kwargs) if kwargs else None
    @start.setter
    def start(self, start):
        self._check_type(start, Time, 'Marker.start')
        self._eval_on_this_object("start = {}".format(_format_object_to_es(start)))

    @property
    def end(self):
        kwargs = self._eval_on_this_object('end')
        return Time(**kwargs) if kwargs else None
    @end.setter
    def end(self, end):
        self._check_type(end, Time, 'Marker.end')
        self._eval_on_this_object("end = {}".format(_format_object_to_es(end)))

    @property
    def type(self):
        return self._eval_on_this_object('type')
    @type.setter
    def type(self, type):
        self._eval_on_this_object("type = {}".format(_format_object_to_es(type)))

    @property
    def name(self):
        return self._eval_on_this_object('name')
    @name.setter
    def name(self, name):
        self._eval_on_this_object("name = {}".format(_format_object_to_es(name)))

    @property
    def comments(self):
        return self._eval_on_this_object('comments')
    @comments.setter
    def comments(self, comments):
        self._eval_on_this_object("comments = {}".format(_format_object_to_es(comments)))

    @property
    def guid(self):
        return self._eval_on_this_object('guid')
    @guid.setter
    def guid(self, guid):
        raise AttributeError("Attribute 'guid' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Marker.bind"')
        self._check_type(function, any, 'arg "function" of function "Marker.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Marker.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Marker.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "Marker.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "Marker.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def setTypeAsComment(self):
        self._eval_on_this_object("setTypeAsComment()")

    def setTypeAsChapter(self):
        self._eval_on_this_object("setTypeAsChapter()")

    def setTypeAsSegmentation(self):
        self._eval_on_this_object("setTypeAsSegmentation()")

    def setTypeAsWebLink(self, url, frameTarget):
        """
        :type url: str
        :type frameTarget: str
        """
        self._check_type(url, str, 'arg "url" of function "Marker.setTypeAsWebLink"')
        self._check_type(frameTarget, str, 'arg "frameTarget" of function "Marker.setTypeAsWebLink"')
        self._eval_on_this_object("setTypeAsWebLink({}, {})".format(_format_object_to_es(url), _format_object_to_es(frameTarget)))

    def getWebLinkURL(self):
        return self._eval_on_this_object("getWebLinkURL()")

    def getWebLinkFrameTarget(self):
        return self._eval_on_this_object("getWebLinkFrameTarget()")

    def setColorByIndex(self, arg1):
        """
        :type arg1: float
        """
        self._check_type(arg1, float, 'arg "arg1" of function "Marker.setColorByIndex"')
        self._eval_on_this_object("setColorByIndex({})".format(_format_object_to_es(arg1)))

    def getColorByIndex(self):
        return self._eval_on_this_object("getColorByIndex()")


class Component(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Component, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def displayName(self):
        return self._eval_on_this_object('displayName')
    @displayName.setter
    def displayName(self, displayName):
        raise AttributeError("Attribute 'displayName' is read-only")

    @property
    def matchName(self):
        return self._eval_on_this_object('matchName')
    @matchName.setter
    def matchName(self, matchName):
        raise AttributeError("Attribute 'matchName' is read-only")

    @property
    def properties(self):
        kwargs = self._eval_on_this_object('properties')
        return ComponentParamCollection(**kwargs) if kwargs else None
    @properties.setter
    def properties(self, properties):
        raise AttributeError("Attribute 'properties' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Component.bind"')
        self._check_type(function, any, 'arg "function" of function "Component.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Component.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Component.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "Component.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "Component.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))


class ComponentParamCollection(PymiereBaseCollection):
    def __init__(self, pymiere_id):
        super(ComponentParamCollection, self).__init__(pymiere_id, "numItems")

    def __getitem__(self, index):
        return ComponentParam(**super(ComponentParamCollection, self).__getitem__(index))

    def __iter__(self):
        return iter([self.__getitem__(i) for i in range(len(self))])


class Dollar(PymiereBaseObject):
    """ The $ object provides a number of debugging facilities and informational methods. """
    def __init__(self, pymiere_id=None):
        super(Dollar, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    """ The most recent run-time error information. Assigning error text to this property generates a run-time error; however, the preferred way to generate a run-time error is to throw an Error object. """
    @property
    def error(self):
        """The current runtime error"""
        kwargs = self._eval_on_this_object('error')
        return Error(**kwargs) if kwargs else None
    @error.setter
    def error(self, error):
        self._check_type(error, Error, '$.error')
        self._eval_on_this_object("error = {}".format(_format_object_to_es(error)))

    """ The version number of the ExtendScript engine. Formatted as a three-part number and description; for example: "3.92.95 (debug)". """
    @property
    def version(self):
        """The ExtendScript version"""
        return self._eval_on_this_object('version')
    @version.setter
    def version(self, version):
        raise AttributeError("Attribute 'version' is read-only")

    """ The ExtendScript build information. """
    @property
    def build(self):
        """The ExtendScript build number"""
        return self._eval_on_this_object('build')
    @build.setter
    def build(self, build):
        raise AttributeError("Attribute 'build' is read-only")

    """ The ExtendScript build date. """
    @property
    def buildDate(self):
        """The ExtendScript build date"""
        kwargs = self._eval_on_this_object('buildDate')
        return Date(**kwargs) if kwargs else None
    @buildDate.setter
    def buildDate(self, buildDate):
        raise AttributeError("Attribute 'buildDate' is read-only")

    """ The current stack trace. """
    @property
    def stack(self):
        """The current stack trace"""
        return self._eval_on_this_object('stack')
    @stack.setter
    def stack(self, stack):
        raise AttributeError("Attribute 'stack' is read-only")

    """ The current debugging level, which enables or disables the JavaScript debugger. One of 0 (no debugging), 1 (break on runtime errors), or 2 (full debug mode). """
    @property
    def level(self):
        """The debugging level"""
        return self._eval_on_this_object('level')
    @level.setter
    def level(self, level):
        self._eval_on_this_object("level = {}".format(_format_object_to_es(level)))

    """ Gets or sets low-level debug output flags. A logical AND of bit flag values: 0x0002 (2): Displays each line with its line number as it is executed. 0x0040 (64): Enables excessive garbage collection. Usually, garbage collection starts when the number of objects has increased by a certain amount since the last garbage collection. This flag causes ExtendScript to garbage collect after almost every statement. This impairs performance severely, but is useful when you suspect that an object gets released too soon. 0x0080 (128): Displays all calls with their arguments and the return value. 0x0100 (256): Enables extended error handling (see strict). 0x0200 (512): Enables the localization feature of the toString method. Equivalent to the localize property. """
    @property
    def flags(self):
        """Debugging flags"""
        return self._eval_on_this_object('flags')
    @flags.setter
    def flags(self, flags):
        self._eval_on_this_object("flags = {}".format(_format_object_to_es(flags)))

    """ Sets or clears strict mode for object modification. When true, any attempt to write to a read-only property causes a runtime error. Some objects do not permit the creation of new properties when true. """
    @property
    def strict(self):
        """Set to true to enforce strict mode"""
        return self._eval_on_this_object('strict')
    @strict.setter
    def strict(self, strict):
        self._eval_on_this_object("strict = {}".format(_format_object_to_es(strict)))

    """ Gets or sets the current locale. The string contains five characters in the form LL_RR, where LL is an ISO 639 language specifier, and RR is an ISO 3166 region specifier.Initially, this is the value that the application or the platform returns for the current user. You can set it to temporarily change the locale for testing. To return to the application or platform setting, set to undefined, null, or the empty string. """
    @property
    def locale(self):
        """The current locale"""
        return self._eval_on_this_object('locale')
    @locale.setter
    def locale(self, locale):
        self._eval_on_this_object("locale = {}".format(_format_object_to_es(locale)))

    """ Set to true to enable the extended localization features of the built-in toString() method. """
    @property
    def localize(self):
        """Set to true to enable auto-localization"""
        return self._eval_on_this_object('localize')
    @localize.setter
    def localize(self, localize):
        self._eval_on_this_object("localize = {}".format(_format_object_to_es(localize)))

    """ The character used as the decimal point character in formatted numeric output. """
    @property
    def decimalPoint(self):
        """The decimal point separator"""
        return self._eval_on_this_object('decimalPoint')
    @decimalPoint.setter
    def decimalPoint(self, decimalPoint):
        raise AttributeError("Attribute 'decimalPoint' is read-only")

    """ The ExtendScript memory cache size, in bytes. """
    @property
    def memCache(self):
        """The memory cache size"""
        return self._eval_on_this_object('memCache')
    @memCache.setter
    def memCache(self, memCache):
        self._eval_on_this_object("memCache = {}".format(_format_object_to_es(memCache)))

    @property
    def appEncoding(self):
        """The default application encoding"""
        return self._eval_on_this_object('appEncoding')
    @appEncoding.setter
    def appEncoding(self, appEncoding):
        self._eval_on_this_object("appEncoding = {}".format(_format_object_to_es(appEncoding)))

    """ An array of objects containing information about the display screens attached to your computer. Each object has the properties left, top, right, bottom, which contain the four corners of each screen in global coordinates.A property primary is true if that object describes the primary display. """
    @property
    def screens(self):
        """An array of rectangles"""
        return _format_object_to_py(self._eval_on_this_object('screens'))
    @screens.setter
    def screens(self, screens):
        raise AttributeError("Attribute 'screens' is read-only")

    """ The current operating system version information. """
    @property
    def os(self):
        """The operating system"""
        return self._eval_on_this_object('os')
    @os.setter
    def os(self, os):
        raise AttributeError("Attribute 'os' is read-only")

    """ The file name of the current script. """
    @property
    def fileName(self):
        """The file name of the current script"""
        return self._eval_on_this_object('fileName')
    @fileName.setter
    def fileName(self, fileName):
        raise AttributeError("Attribute 'fileName' is read-only")

    """ The current line number of the currently executing script. """
    @property
    def line(self):
        """The current line number of the current script"""
        return self._eval_on_this_object('line')
    @line.setter
    def line(self, line):
        raise AttributeError("Attribute 'line' is read-only")

    """ A high-resolution timer, measuring the time in microseconds. The timer starts when ExtendScript is initialized during the application startup sequence. Every read access resets the timer to Zero. """
    @property
    def hiresTimer(self):
        """The elapsed time in microseconds since the last access"""
        return self._eval_on_this_object('hiresTimer')
    @hiresTimer.setter
    def hiresTimer(self, hiresTimer):
        raise AttributeError("Attribute 'hiresTimer' is read-only")

    @property
    def dictionary(self):
        """The application's main dictionary"""
        kwargs = self._eval_on_this_object('dictionary')
        return Dictionary(**kwargs) if kwargs else None
    @dictionary.setter
    def dictionary(self, dictionary):
        raise AttributeError("Attribute 'dictionary' is read-only")

    """ The name of the current ExtendScript engine, if set. """
    @property
    def engineName(self):
        """The name of the current engine if set"""
        return self._eval_on_this_object('engineName')
    @engineName.setter
    def engineName(self, engineName):
        raise AttributeError("Attribute 'engineName' is read-only")

    """ The path for include files for the current script. """
    @property
    def includePath(self):
        """The path for include files"""
        return self._eval_on_this_object('includePath')
    @includePath.setter
    def includePath(self, includePath):
        raise AttributeError("Attribute 'includePath' is read-only")


    # ----- FUNCTIONS -----
    def about(self):
        """
        An About box
        Shows an About box for the ExtendScript component, and returns the text for the box.
        """
        return self._eval_on_this_object("about()")

    def toString(self):
        """
        Converts this object to a string
        Converts this object to a string.
        """
        return self._eval_on_this_object("toString()")

    def write(self):
        """
        Prints text
        Prints text to the Console. 
        :param text: The text to print. All arguments are concatenated.
        """
        self._eval_on_this_object("write()")

    def writeln(self, text):
        """
        Prints text
        Prints text to the Console, and adds a newline character. 
        :param text: The text to print. All arguments are concatenated.
        """
        self._eval_on_this_object("writeln({})".format(_format_object_to_es(text)))

    def bp(self):
        """
        Breaks execution
        Breaks execution at the current position. 
        :param condition: A string containing a JavaScript statement to be used as a condition. If the statement evaluates to true or nonzero when this point is reached, execution stops.
        """
        self._eval_on_this_object("bp()")

    def getenv(self, name):
        """
        Returns an environment variable
        Retrieves the value of an environment variable. 
        :param name: The name of the variable.
        :param name: The name of the variable
        :type name: str
        """
        self._check_type(name, str, 'arg "name" of function "$.getenv"')
        return self._eval_on_this_object("getenv({})".format(_format_object_to_es(name)))

    def setenv(self, key, value):
        """
        Sets the value of an environment variable. 
        :param name: The name of the variable.
        :param value: The value of the variable.
        :type key: str
        :param value: Sets an environment variable
        :type value: str
        """
        self._check_type(key, str, 'arg "key" of function "$.setenv"')
        self._check_type(value, str, 'arg "value" of function "$.setenv"')
        return self._eval_on_this_object("setenv({}, {})".format(_format_object_to_es(key), _format_object_to_es(value)))

    def sleep(self, msecs):
        """
        Sleep
        Suspends the calling thread for a number of milliseconds. During a sleep period, checks at 100 millisecond intervals to see whether the sleep should be terminated. This can happen if there is a break request, or if the script timeout has expired. 
        :param msecs: Number of milliseconds to sleep.
        :param msecs: Number of milliseconds to sleep
        :type msecs: float
        """
        self._check_type(msecs, float, 'arg "msecs" of function "$.sleep"')
        self._eval_on_this_object("sleep({})".format(_format_object_to_es(msecs)))

    def colorPicker(self, color):
        """
        Invokes the platform-specific color selection dialog, and returns the selected color. 
        :param color: The color to be preselected in the dialog, as 0xRRGGBB, or -1 for the platform default.
        :param color: Picks a color; the argument is the color or -1.
        :type color: float
        """
        self._check_type(color, float, 'arg "color" of function "$.colorPicker"')
        return self._eval_on_this_object("colorPicker({})".format(_format_object_to_es(color)))

    def evalFile(self, file):
        """
        Loads and evaluates a file
        Loads and evaluates a file. 
        :param file: The file to load.
        :param timeout: An optional timeout in milliseconds.
        :param file: The file to load
        :type file: File
        """
        self._check_type(file, File, 'arg "file" of function "$.evalFile"')
        return self._eval_on_this_object("evalFile({})".format(_format_object_to_es(file)))

    def list(self, arg1):
        """
        :type arg1: any
        """
        self._check_type(arg1, any, 'arg "arg1" of function "$.list"')
        return _format_object_to_py(self._eval_on_this_object("list({})".format(_format_object_to_es(arg1))))

    def listLO(self, arg1):
        """
        :type arg1: any
        """
        self._check_type(arg1, any, 'arg "arg1" of function "$.listLO"')
        return _format_object_to_py(self._eval_on_this_object("listLO({})".format(_format_object_to_es(arg1))))

    def summary(self):
        return _format_object_to_py(self._eval_on_this_object("summary()"))

    def gc(self):
        """
        Runs the garbage collector
        Initiates garbage collection in the ExtendScript engine.
        """
        self._eval_on_this_object("gc()")


class Error(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Error, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def number(self):
        return self._eval_on_this_object('number')
    @number.setter
    def number(self, number):
        self._eval_on_this_object("number = {}".format(_format_object_to_es(number)))

    @property
    def fileName(self):
        return self._eval_on_this_object('fileName')
    @fileName.setter
    def fileName(self, fileName):
        self._eval_on_this_object("fileName = {}".format(_format_object_to_es(fileName)))

    @property
    def line(self):
        return self._eval_on_this_object('line')
    @line.setter
    def line(self, line):
        self._eval_on_this_object("line = {}".format(_format_object_to_es(line)))

    @property
    def source(self):
        return self._eval_on_this_object('source')
    @source.setter
    def source(self, source):
        self._eval_on_this_object("source = {}".format(_format_object_to_es(source)))

    @property
    def start(self):
        return self._eval_on_this_object('start')
    @start.setter
    def start(self, start):
        self._eval_on_this_object("start = {}".format(_format_object_to_es(start)))

    @property
    def end(self):
        return self._eval_on_this_object('end')
    @end.setter
    def end(self, end):
        self._eval_on_this_object("end = {}".format(_format_object_to_es(end)))

    @property
    def message(self):
        return self._eval_on_this_object('message')
    @message.setter
    def message(self, message):
        self._eval_on_this_object("message = {}".format(_format_object_to_es(message)))

    @property
    def name(self):
        return self._eval_on_this_object('name')
    @name.setter
    def name(self, name):
        self._eval_on_this_object("name = {}".format(_format_object_to_es(name)))

    @property
    def description(self):
        return self._eval_on_this_object('description')
    @description.setter
    def description(self, description):
        self._eval_on_this_object("description = {}".format(_format_object_to_es(description)))


    # ----- FUNCTIONS -----
    def toString(self):
        return self._eval_on_this_object("toString()")

    def toSource(self):
        return self._eval_on_this_object("toSource()")


class Dictionary(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Dictionary, self).__init__(pymiere_id)

    # ----- PROPERTIES -----

    # ----- FUNCTIONS -----
    def getGroups(self):
        """
        Gets the list of groups.
        """
        return Array(**self._eval_on_this_object("getGroups()"))

    def getClasses(self):
        """
        Gets a list of classes by group.
        """
        return Array(**self._eval_on_this_object("getClasses()"))

    def getClass(self):
        """
        Gets a class description.
        """
        return _format_object_to_py(self._eval_on_this_object("getClass()"))

    def toXML(self, prefix):
        """
        Converts a Dictionary instance to XML.
        :param prefix: The href prefix.
        :type prefix: str
        """
        self._check_type(prefix, str, 'arg "prefix" of function "Dictionary.toXML"')
        return _format_object_to_py(self._eval_on_this_object("toXML({})".format(_format_object_to_es(prefix))))


class ComponentParam(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(ComponentParam, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def displayName(self):
        return self._eval_on_this_object('displayName')
    @displayName.setter
    def displayName(self, displayName):
        raise AttributeError("Attribute 'displayName' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ComponentParam.bind"')
        self._check_type(function, any, 'arg "function" of function "ComponentParam.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ComponentParam.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "ComponentParam.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "ComponentParam.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "ComponentParam.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def areKeyframesSupported(self):
        return self._eval_on_this_object("areKeyframesSupported()")

    def isEmpty(self):
        return self._eval_on_this_object("isEmpty()")

    def isTimeVarying(self):
        return self._eval_on_this_object("isTimeVarying()")

    def setTimeVarying(self, isTimeVarying):
        """
        :type isTimeVarying: bool
        """
        self._check_type(isTimeVarying, bool, 'arg "isTimeVarying" of function "ComponentParam.setTimeVarying"')
        self._eval_on_this_object("setTimeVarying({})".format(_format_object_to_es(isTimeVarying)))

    def findNearestKey(self, time, threshold):
        """
        :type time: float
        :type threshold: float
        """
        self._check_type(time, float, 'arg "time" of function "ComponentParam.findNearestKey"')
        self._check_type(threshold, float, 'arg "threshold" of function "ComponentParam.findNearestKey"')
        return Time(**self._eval_on_this_object("findNearestKey({}, {})".format(_format_object_to_es(time), _format_object_to_es(threshold))))

    def findPreviousKey(self, time):
        """
        :type time: float
        """
        self._check_type(time, float, 'arg "time" of function "ComponentParam.findPreviousKey"')
        return Time(**self._eval_on_this_object("findPreviousKey({})".format(_format_object_to_es(time))))

    def findNextKey(self, time):
        """
        :type time: float
        """
        self._check_type(time, float, 'arg "time" of function "ComponentParam.findNextKey"')
        return Time(**self._eval_on_this_object("findNextKey({})".format(_format_object_to_es(time))))

    def getKeys(self):
        return self._eval_on_this_object("getKeys()")

    def addKey(self, time):
        """
        :type time: float
        """
        self._check_type(time, float, 'arg "time" of function "ComponentParam.addKey"')
        self._eval_on_this_object("addKey({})".format(_format_object_to_es(time)))

    def removeKey(self, time):
        """
        :type time: float
        """
        self._check_type(time, float, 'arg "time" of function "ComponentParam.removeKey"')
        self._eval_on_this_object("removeKey({})".format(_format_object_to_es(time)))

    def removeKeyRange(self, startTime, stopTime, updateUI):
        """
        :type startTime: float
        :type stopTime: float
        :type updateUI: bool
        """
        self._check_type(startTime, float, 'arg "startTime" of function "ComponentParam.removeKeyRange"')
        self._check_type(stopTime, float, 'arg "stopTime" of function "ComponentParam.removeKeyRange"')
        self._check_type(updateUI, bool, 'arg "updateUI" of function "ComponentParam.removeKeyRange"')
        self._eval_on_this_object("removeKeyRange({}, {}, {})".format(_format_object_to_es(startTime), _format_object_to_es(stopTime), _format_object_to_es(updateUI)))

    def keyExistsAtTime(self, time):
        """
        :type time: float
        """
        self._check_type(time, float, 'arg "time" of function "ComponentParam.keyExistsAtTime"')
        return self._eval_on_this_object("keyExistsAtTime({})".format(_format_object_to_es(time)))

    def getValue(self):
        return self._eval_on_this_object("getValue()")

    def setValue(self, value, updateUI):
        self._check_type(updateUI, bool, 'arg "updateUI" of function "ComponentParam.setValue"')
        return self._eval_on_this_object("setValue({}, {})".format(_format_object_to_es(value), _format_object_to_es(updateUI)))

    def getColorValue(self):
        """
        Get the value of a color property on an effect

        :return: (Array) containing in order alpha, red, green and blue color channel (0-255 int)
        """
        return Array(**self._eval_on_this_object("getColorValue()"))

    def setColorValue(self, alpha, red, green, blue, updateUI):
        """
        :type alpha: int
        :type red: int
        :type green: int
        :type blue: int
        :type updateUI: bool
        """
        self._check_type(alpha, int, 'arg "alpha" of function "ComponentParam.setColorValue"')
        self._check_type(red, int, 'arg "red" of function "ComponentParam.setColorValue"')
        self._check_type(green, int, 'arg "green" of function "ComponentParam.setColorValue"')
        self._check_type(blue, int, 'arg "blue" of function "ComponentParam.setColorValue"')
        self._check_type(updateUI, bool, 'arg "updateUI" of function "ComponentParam.setColorValue"')
        return self._eval_on_this_object("setColorValue({}, {}, {}, {}, {})".format(
            _format_object_to_es(alpha), _format_object_to_es(red), _format_object_to_es(green),
            _format_object_to_es(blue), _format_object_to_es(updateUI)
        ))

    def getValueAtKey(self, time):
        """
        :type time: Object
        """
        return self._eval_on_this_object("getValueAtKey({})".format(_format_object_to_es(time)))

    def setValueAtKey(self, time, value, updateUI):
        """
        :type time: Object
        :type value: float
        :type updateUI: bool
        """
        return self._eval_on_this_object("setValueAtKey({}, {}, {})".format(_format_object_to_es(time), _format_object_to_es(value), _format_object_to_es(updateUI)))

    def getValueAtTime(self, time):
        """
        :type time: Object
        """
        return self._eval_on_this_object("getValueAtTime({})".format(_format_object_to_es(time)))

    def setInterpolationTypeAtKey(self, time):
        """
        :type time: Object
        """
        return self._eval_on_this_object("setInterpolationTypeAtKey({})".format(_format_object_to_es(time)))


class Exporter(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(Exporter, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def name(self):
        return self._eval_on_this_object('name')
    @name.setter
    def name(self, name):
        raise AttributeError("Attribute 'name' is read-only")

    @property
    def classID(self):
        return self._eval_on_this_object('classID')
    @classID.setter
    def classID(self, classID):
        raise AttributeError("Attribute 'classID' is read-only")

    @property
    def fileType(self):
        return self._eval_on_this_object('fileType')
    @fileType.setter
    def fileType(self, fileType):
        raise AttributeError("Attribute 'fileType' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Exporter.bind"')
        self._check_type(function, any, 'arg "function" of function "Exporter.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Exporter.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "Exporter.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "Exporter.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "Exporter.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def getPresets(self):
        self._eval_on_this_object("getPresets()")


class EncoderPreset(PymiereBaseObject):
    def __init__(self, pymiere_id=None):
        super(EncoderPreset, self).__init__(pymiere_id)

    # ----- PROPERTIES -----
    @property
    def name(self):
        return self._eval_on_this_object('name')
    @name.setter
    def name(self, name):
        raise AttributeError("Attribute 'name' is read-only")

    @property
    def matchName(self):
        return self._eval_on_this_object('matchName')
    @matchName.setter
    def matchName(self, matchName):
        raise AttributeError("Attribute 'matchName' is read-only")


    # ----- FUNCTIONS -----
    def bind(self, eventName, function):
        """
        :type eventName: str
        :type function: any
        """
        self._check_type(eventName, str, 'arg "eventName" of function "EncoderPreset.bind"')
        self._check_type(function, any, 'arg "function" of function "EncoderPreset.bind"')
        self._eval_on_this_object("bind({}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function)))

    def unbind(self, eventName):
        """
        :type eventName: str
        """
        self._check_type(eventName, str, 'arg "eventName" of function "EncoderPreset.unbind"')
        self._eval_on_this_object("unbind({})".format(_format_object_to_es(eventName)))

    def setTimeout(self, eventName, function, milliseconds):
        """
        :type eventName: str
        :type function: any
        :type milliseconds: float
        """
        self._check_type(eventName, str, 'arg "eventName" of function "EncoderPreset.setTimeout"')
        self._check_type(function, any, 'arg "function" of function "EncoderPreset.setTimeout"')
        self._check_type(milliseconds, float, 'arg "milliseconds" of function "EncoderPreset.setTimeout"')
        self._eval_on_this_object("setTimeout({}, {}, {})".format(_format_object_to_es(eventName), _format_object_to_es(function), _format_object_to_es(milliseconds)))

    def writeToFile(self, outputFilePath):
        """
        :type outputFilePath: str
        """
        self._check_type(outputFilePath, str, 'arg "outputFilePath" of function "EncoderPreset.writeToFile"')
        return self._eval_on_this_object("writeToFile({})".format(_format_object_to_es(outputFilePath)))

