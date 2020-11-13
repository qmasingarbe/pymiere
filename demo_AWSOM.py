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

import os
import pymiere
from pymiere import exe_utils
import requests
import datetime
from pathlib import Path
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


def from_device_to_storage(project):
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
    return

def get_new_path(path, index, rule = "SWL.TV #1"):
    """
    Returns a new filepath based on the preferred formatting rule
    """
    if rule == "SWL.TV #1":
        new_name = project.title + " " +str(index+1).zfill(4) + path.suffix
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
    project.get_format()
    if project.format == "XDCAM":
        project.clip_path = project.path / "XDROOT/Clip"
        project.thumbnail_path = project.path / "XDROOT/Thmbnl"
        project.metadata_path = project.path / "XDROOT/MEDIAPRO.XML"
    file_lists = [list(project.clip_path.glob("*.mxf"))]
    file_lists += [list(project.clip_path.glob("*.xml"))]
    thumbnails = list(project.thumbnail_path.glob("*.jpg"))
    # Only rename thumbnails corresponding to selected clips, not all
    stems = [x.stem for x in file_lists[0]]
    thumbnails = [x for x in thumbnails if x.stem.split("T01")[0] in stems]
    file_lists += [thumbnails]
    with open(project.metadata_path, "r") as file:
        metadata = file.read()
    with open(project.metadata_path, "w") as file:
        for file_list in file_lists:
            for index, path in enumerate(file_list):
                new_path = get_new_path(path, index)
                new_end = "/".join(path.rename(new_path).parts[-2:])
                print(path,"->", "…/" + new_end)
                metadata = metadata.replace("/".join(path.parts[-2:]), new_end)
        file.write(metadata)
    project.media_renamed_on = datetime.datetime.now()


def ingest():
    """
    A typical workflow to speed up the ingest process, from copying new media
    from a connected device to a working storage area, all the way through to
    having Premiere Pro open and ready for actual editing.
    """
    project = Project()
    from_device_to_storage(project)
    rename_media(project)
    create_pproj_from_template(project)
    import_clips_to_bin(project)
    create_rushes_sequence(project)
    # import_subtitles_to_bin(project)
    # add_subtitles_to_rushes(project)
    # send_rushes_to_media_encoder(project)
    save_and_close(project)
