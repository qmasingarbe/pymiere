"""
AWSOM* is a collection of automation tools originally developed by Peter Fison
(https://github.com/PFython) for use at South West London TV Ltd as part of
their Adobe Creative Cloud video production workflow.

This demo file contains script examples which use the superb Pymiere library by Quentin Masingarbe (https://github.com/qmasingarbe/pymiere) and are offered under the same GNU license as Pymiere itself.  Feel free to use and
enjoy, and perhaps support the project by sharing your own creations (and
tests, please) by forking Pymiere on Github and creating a Pull Request?

(*) AWSOM stands for "Amazing Ways to Search and Organise Media".  If you're interested in exploring the rest of the AWSOM toolkit, they'll be made
available via a snazzy new web app very soon hopefully - mostly free, but some
on a pay per use basis where we utilise third party services like professional
quality Automatic Speech Recognition.

In the meantime though, please follow us on Twitter and strike up a conversation!

https://twitter.com/AppAwsom
"""

import pymiere
from pymiere import wrappers
from pymiere import exe_utils
import datetime
from pathlib import Path
import win32api
import shutil
from cleverdict import CleverDict  # powerful dictionary/attribute switching
import PySimpleGUI as sg  # fast and easy GUI creation

sg.change_look_and_feel('DarkPurple4')  # Match the GUI with Premiere colours

WORK_IN_PROGRESS = Path("E:\\")  # Main working drive/folder for video editing
TEMPLATE = Path(r"D:\Pete's Data\OneDrive\SWLTV Editing Templates\SWL.TV Template v4\SWL.TV Template cc4.1.prproj")
PROJECT_TYPES = {"SWLTV - ": "Project intended for YouTube channel SWL.TV",
                 "WBC - ": "White Label project for Wandsworth Borough Council",
                 "Project - ": "Other project not intended for publishing",
                 "Pod - ": "Breakfast TV style interviews in 'The Pod'"}
ICON = "logo.ico"
DEFAULT_BIN_NAME = "Rushes (Unsorted)"
DEFAULT_RUSHES_SEQUENCE = "Rushes/Teaser"
EXCLUDE_DRIVES = "BCDEFHLPW"  # Attached drives, never a source to import media

class Project(CleverDict):
    """
    Each Project is conceptually a video production, typically comprising a
    single folder on a workstation or Network Attaches Storage, containing
    source files, media, metadata and subfolders, as well as at least one
    Premiere Pro (.prproj) file and one or more final rendered videos.

    Creating a new Project instance will prompt for a title if none is supplied as an argument, and the Project will be added to Project.index for batch processing where more than one Project is involved.

    This class inherits from the CleverDict custom data type in order to
    flexibly switch between Python dictionary {key: value} notation and
    object.attribute notation.  For more information about CleverDict see:
    https://pypi.org/project/cleverdict/
    """
    index = []
    def __init__(self, title = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if title is None:
            title = sg.popup_get_text("Please enter a project title",title="New AWSOM Project", icon=ICON, )
        self.title = title.replace('"',"_") or "None"  # validate filename
        self.created_on = datetime.datetime.now()
        self.get_project_type()  # creates .folder_prefix and .type
        self.path = WORK_IN_PROGRESS / (self.folder_prefix + self.title)
        print(self)
        Project.index += [self]

    def __str__(self):
        output = self.info(as_str=True)
        return output.replace("CleverDict", type(self).__name__, 1)

    def get_project_type(self):
        """
        Confirms what category/type a project falls in, and assigns a standard
        prefix to be used for folder names.  This helps keep the directory
        structure organised... by Client, Topic, Location etc.

        For example the author uses "SWLTV - " for all productions which will appear on their main YouTube channel, but other prefixes are used for
        regular "White Label" work for specific clients.

        Creates attributes: .folder_prefix and .type in-place.
        """
        width = max([len(x) for x in PROJECT_TYPES])
        choices = [[sg.Text(text="Please confirm the folder prefix and project type:\n", text_color = "white")]]
        choices += [[sg.Button(button_text=k, size=(width,1)), sg.Text(text=v)]
                   for k,v in PROJECT_TYPES.items()]
        choices += [[sg.Text(text="\n")]]
        event, _  = sg.Window(self.title, choices, icon=ICON).read(close=True)
        self.folder_prefix = event
        self.type = PROJECT_TYPES[event]

    def get_format(self):
        """
        Scans self.path for media files (TODO) and sets best-guess format.
        Creates .format in-place.
        """
        if hasattr(self, "format"):
            return
        self.format = "XDCAM"
        project.clip_path = project.path / "XDROOT/Clip"
        project.thumbnail_path = project.path / "XDROOT/Thmbnl"
        project.metadata_path = project.path / "XDROOT/MEDIAPRO.XML"

def search_for_XDCAM_media(project):
    """
    Searches for connected devices with XDCAM media.
    Creates list project.sources with any drives found.
    """
    drives = win32api.GetLogicalDriveStrings()
    drives = [x for x in drives if x.isalpha() and x not in EXCLUDE_DRIVES]
    project.sources = []
    for drive in drives:
        dirs = [x for x in Path(drive+":\\").rglob("*") if x.is_dir()]
        # Check for XDCAM structure
        possible_source = [x for x in dirs if "\\XDROOT\\Clip" in str(x)]
        if possible_source:
            if len(list(possible_source[0].glob("*.mxf"))):
                project.sources += possible_source

def copy_media_from_device(project):
    """
    TODO:
    Intelligently* copies media from a connected device (usually a video camera or memory card).

    (*) For example for Sony XDCAM media, looks for the XDROOT folder to copy.

    Optionally: only copy media created before/since a specific date
    (default=today) which is helpful when you've recorded multiple productions to the same device but only want the first/last collection.

    Optionally: browse media to select a particular clip and import all other
    clips recorded before/since that clip.

    Optionally: automatically look for "breaks" over a specified duration and assume these breaks mark the start/end of a project.  Create a new project and a separate project folder on storage for each collection of clips.

    Optionally: group clips by date and create a new project and a separate
    project folder on storage for each day of filming.

    Optionally: trigger bulk Automatic Speech Recognition for each clip and
    create sidecare .srt (subtitles) files and overall Summary transcript.
    """
    project.get_format()  # Premature/redundant?
    search_for_XDCAM_media(project)
    for source in project.sources:
        print(f"Copying media from {source.parent} to {project.clip_path.parent}")
        files = list(source.parent.rglob("*.*"))
        print(len(files), "files, ending with", files[-1].name)
        print("Please be patient...")
        shutil.copytree(source.parent, project.clip_path.parent)



def get_new_path(path, index, title, rule = "SWL.TV #1"):
    """
    Returns a new filepath based on the preferred formatting rule
    """
    if rule == "SWL.TV #1":
        new_name = title + " " +str(index+1).zfill(4) + path.suffix
        return path.with_name(new_name)
    # If all else fails, return original path
    return path

def rename_media(project):
    """
    Renames individual clips according to rules e.g.

    - Prepend Project Name
    - XDCAM: Clip00xx.mxf -> 022.mxf

    Also renames thumbnail images and updates any Metadata XML (XDCAM)
    """
    if project.format == "XDCAM":
        file_lists = [list(project.clip_path.glob("*.mxf"))]
        file_lists += [list(project.clip_path.glob("*.xml"))]
        thumbnails = list(project.thumbnail_path.glob("*.jpg"))
        # Only rename thumbnails corresponding to selected clips, not all
        stems = [x.stem for x in file_lists[0]]
        thumbnails = [x for x in thumbnails if x.stem.split("T01")[0] in stems]
        file_lists += [thumbnails]
    try:
        with open(project.metadata_path, "r") as file:
            metadata = file.read()
    except FileNotFoundError:
        metadata = ""
    with open(project.metadata_path, "w") as file:
        for file_list in file_lists:
            for index, path in enumerate(file_list):
                new_path = get_new_path(path, index, project.title)
                new_end = "/".join(path.rename(new_path).parts[-2:])
                print(path,"->", "…/" + new_end)
                metadata = metadata.replace("/".join(path.parts[-2:]), new_end)
        if metadata:
            file.write(metadata)
    project.media_renamed_on = datetime.datetime.now()


def create_global_shortcuts():
    """
    Creates shortcuts for common Pymiere objects for developer convenience.
    """
    global app, ProjectItem
    app = pymiere.objects.app
    ProjectItem = pymiere.ProjectItem

def create_prproj_from_template(project):
    """
    Launches Premiere Pro if not already running;
    Prompts to open a template .prpoj file;
    Saves the .prproj file with a path based on .title and .path
    """
    # Start Premiere Pro and open the selected project
    if not exe_utils.exe_is_running("adobe premiere pro.exe")[0]:
        exe_utils.start_premiere()
    create_global_shortcuts()
    if project.prproj_path.is_file():
        app.openDocument(str(project.prproj_path))
    else:
        app.openDocument(str(project.template_path))
        app.project.saveAs(str(project.prproj_path))

def import_clips_to_bin(project):
    """
    Imports Clips from .clip_path to a new bin named as DEFAULT_BIN_NAME
    """
    project.clips = list(project.clip_path.glob("*.mxf"))
    root = app.project.rootItem
    ProjectItem.createBin(root, DEFAULT_BIN_NAME)
    project.default_bin = [x for x in root.children if x.type == 2 and x.name == DEFAULT_BIN_NAME][0]
    # Type 1: "Sequence" object
    # Type 2: "Bin" object
    files = [str(x) for x in project.clips]
    # for file in files:
    print(f"Importing {len(files)} files, from {project.clips[0].name} to {project.clips[-1].name}")
    app.project.importFiles(files, True, project.default_bin, False)

def create_rushes_sequence(project):
    """
    Create DEFAULT_RUSHES_SEQUENCE or make it active if it already exists
    """
    sequences = app.project.sequences
    sequence = [x for x in sequences if x.name == DEFAULT_RUSHES_SEQUENCE]
    if not sequence:
        app.project.createNewSequence(DEFAULT_RUSHES_SEQUENCE,"Rushes Sequence")
        # Auto-selects new Sequence on creation
    else:
        app.project.activeSequence = sequence[0]

def insert_clips_in_rushes_sequence(project):
    """
    Insert all Clips from DEFAULT_BIN_NAME into Sequence DEFAULT_RUSHES_SEQUENCE
    """
    for clip in reversed(project.clips):
        media = project.default_bin.findItemsMatchingMediaPath(str(clip), True)
        current_time = app.project.activeSequence.getPlayerPosition()
        app.project.activeSequence.insertClip(media[0], current_time, 0, 0)

def get_all_input_for_ingest():
    """
    Use PySimpleGUI popups to get all user input up front, thereby allowing
    automation to proceed without later steps pausing for user input.
    """
    project = Project()
    project.template_path = Path(sg.popup_get_file("Please select a Premiere Pro project to open", default_path=TEMPLATE, icon=ICON, file_types=(("Premiere Pro", "*.prproj"),)))
    project.prproj_path = project.path / (project.title + ".prproj")
    return project

def ingest():
    """
    A typical workflow to speed up the ingest process, from copying new media
    from a connected device, right up to having Premiere Pro open and ready for
    actual editing to start.
    """
    project = get_all_input_for_ingest()
    copy_media_from_device(project)
    project.get_format()
    rename_media(project)
    create_prproj_from_template(project)
    import_clips_to_bin(project)
    create_rushes_sequence(project)
    insert_clips_in_rushes_sequence(project)
    # import_subtitles_to_bin(project)
    # add_subtitles_to_rushes(project)
    # send_rushes_to_media_encoder(project)
    app.project.save()
