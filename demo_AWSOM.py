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
from pymiere import exe_utils
import requests
import datetime
from pathlib import Path
from cleverdict import CleverDict  # powerful dictionary/attribute switching
import PySimpleGUI as sg  # fast and easy GUI creation

sg.change_look_and_feel('DarkPurple4')  # Match the GUI with Premiere colours

WORK_IN_PROGRESS = Path("E:\\")  # Main working drive/folder for video editing
PROJECT_TYPES = {"SWLTV - ": "Project intended for YouTube channel SWL.TV",
                 "WBC - ": "White Label project for Wandsworth Borough Council",
                 "Project - ": "Other project not intended for publishing"}

class Project(CleverDict):
    """
    Objects of this class encapsulate metadata required internally for passing
    them around the various functions in this script.

    Each media Project will usually have its own storage folder containing
    source files, media, metadata and subfolders, as well as at least one
    master .prproj file for Premiere Pro.

    Each new Project instance will prompt for a title if none is supplied, and
    will be added to a class list: Project.index for batch processing where more
    than one Project is involved.

    This class inherits from the CleverDict data type in order to flexibly
    switch between Python dictionary {key: value} notation and object.attribute
    notation.  For more information about CleverDict type help(CleverDict) or have a look at the online README: https://pypi.org/project/cleverdict/
    """
    index = []
    def __init__(self, title = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if title is None:
            title = sg.popup_get_text("Please enter a project title",title="New AWSOM Project", icon="logo.ico", )
        self.title = title.replace('"',"_") or "None"  # validate filename
        self.created_on = datetime.datetime.now()
        self.get_project_type()  # creates .folder_prefix and .type
        self.path = WORK_IN_PROGRESS / (self.folder_prefix + self.title)
        print(self.info(as_str=True).replace("CleverDict:", "Project Created:"))
        Project.index += [self]

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
        choices = [[sg.Button(button_text=k, size=(width,1)), sg.Text(text=v)]
                   for k,v in PROJECT_TYPES.items()]
        event, _  = sg.Window('Confirm Project Type', choices).read(close=True)
        self.folder_prefix = event
        self.type = PROJECT_TYPES[event]



def from_device_to_storage():
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
    return

def rename_clips():
    """
    Renames individual clips according to rules e.g.

    - Prepend Project Name
    - XDCAM: Clip00xx.mxf -> 022.mxf
    """

def from_device_to_timeline():
    """
    A typical workflow to speed up the ingest process, from copying new media
    from a connected device to a working storage area, all the way through to
    having Premiere Pro open and ready for actual editing.
    """
    create_project()
    rename_clips()
    from_device_to_storage()
