# builtin
import sys
import os
# third party
import win32gui
from PyQt5.QtWidgets import QApplication, QPushButton, QSlider, QVBoxLayout, QWidget, QGroupBox, QTextEdit, QGridLayout
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt

import pymiere
from pymiere import wrappers


def swap_focus(func):
    """
    Use this decorator for any method that does an action in premiere. Not needed for queries but for any action
    that will change something in the UI we have to give focus to Premiere
    """
    def wrapper(self, *args, **kwargs):
        win32gui.SetForegroundWindow(self.premiere_window_id)
        result = func(self, *args, **kwargs)
        win32gui.SetForegroundWindow(self.ui_id)
        return result
    return wrapper


def get_default_folder():
    """
    Default folder for open/save popup. Opened prproj folder or user's home
    :return: (str) folder
    """
    if not pymiere.objects.app.isDocumentOpen():
        return os.path.expanduser("~")  # user's home
    return os.path.dirname(pymiere.objects.app.project.path)


def simple_file_dialog(dialog_type, caption, directory=None, filter=None):
    """ Wrap QFileDialog for open or save dialog box """
    args = {
        "caption": caption.capitalize() if caption.endswith("...") else "{}...".format(caption.capitalize()),
        "directory": directory or get_default_folder(),
    }
    if filter:
        args.update(filter=filter)
    if dialog_type.lower() == "open":
        result = QFileDialog.getOpenFileName(**args)
    else:
        result = QFileDialog.getSaveFileName(**args)
    if result == ('', ''):
        # cancelled or closed dialog
        return False, None
    return True, os.path.normpath(result[0])


class HorizontalGroup(QGroupBox):
    """ UI wrapper for QGroupBox with integrated GridLayout"""
    def __init__(self, *args):
        super(HorizontalGroup, self).__init__(*args)
        self.internal_layout = QGridLayout()
        self.setLayout(self.internal_layout)

    def addWidget(self, widget, x, y):
        self.internal_layout.addWidget(widget, x, y)


class PymiereControl(QWidget):
    """ main window """
    def __init__(self):
        super(PymiereControl, self).__init__()

        # get UI ids for swapping focus
        self.premiere_window_id = win32gui.FindWindow("Premiere Pro", None)
        self.ui_id = self.winId()

        # create UI
        layout = QVBoxLayout()

        # player
        player = HorizontalGroup("Playback")
        play = QPushButton("Play/Pause")
        forward = QPushButton("Forward 10 frames")
        backward = QPushButton("Backward 10 frames")
        play.clicked.connect(self.play_func)
        forward.clicked.connect(self.forward_func)
        backward.clicked.connect(self.backward_func)
        player.addWidget(play, 0, 0)
        player.addWidget(backward, 0, 1)
        player.addWidget(forward, 0, 2)

        # selection
        selection = HorizontalGroup("Selection")
        refresh_selection = QPushButton("Refresh")
        refresh_selection.clicked.connect(self.refresh_selection_func)
        self.selection_info = QTextEdit()
        change_path = QPushButton("Change media path")
        change_path.clicked.connect(self.change_path_func)
        move_clips = QPushButton("Move selected by : ")
        move_clips.clicked.connect(self.move_selected_func)
        self.move_seconds = QSlider(Qt.Horizontal)
        self.move_seconds.setTickInterval(1)
        self.move_seconds.setMinimum(-5)
        self.move_seconds.setMaximum(5)
        self.move_seconds.setTickPosition(QSlider.TicksBelow)
        selection.addWidget(refresh_selection, 0, 0)
        selection.addWidget(self.selection_info, 0, 1)
        selection.addWidget(change_path, 1, 0)
        selection.addWidget(move_clips, 2, 0)
        selection.addWidget(self.move_seconds, 2, 1)


        # import/export
        io = HorizontalGroup("I/O")
        import_file = QPushButton("Import")
        import_file.clicked.connect(self.import_func)
        import_insert_file = QPushButton("Import + insert")
        import_insert_file.clicked.connect(self.import_insert_func)
        export_frame = QPushButton("Export current frame as PNG")
        export_frame.clicked.connect(self.export_frame_func)
        export_encoder = QPushButton("Export region of sequence")
        export_encoder.clicked.connect(self.export_encoder_func)
        open = QPushButton("Open project")
        open.clicked.connect(self.open_func)
        save = QPushButton("Save project")
        save.clicked.connect(self.save_func)
        saveas = QPushButton("Save project as")
        saveas.clicked.connect(self.saveas_func)
        close = QPushButton("Close project")
        close.clicked.connect(self.close_func)
        io.addWidget(import_file, 0, 0)
        io.addWidget(import_insert_file, 0, 1)
        io.addWidget(export_frame, 1, 0)
        io.addWidget(export_encoder, 1, 1)
        io.addWidget(open, 2, 0)
        io.addWidget(close, 2, 1)
        io.addWidget(save, 3, 0)
        io.addWidget(saveas, 3, 1)

        # miscelanious
        miscellaneous = HorizontalGroup("Miscellaneous")
        add_effect = QPushButton("Add effect on clip")
        add_effect.clicked.connect(self.add_effect_func)
        miscellaneous.addWidget(add_effect, 1, 0)

        layout.addWidget(player)
        layout.addWidget(selection)
        layout.addWidget(io)
        layout.addWidget(miscellaneous)

        self.setLayout(layout)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # avoid doing the query for active sequence in each method
        self.__active_sequence = pymiere.objects.app.project.activeSequence if wrappers.check_active_sequence(crash=False) else None

    @property
    def active_sequence(self):
        if self.__active_sequence is None:
            wrappers.check_active_sequence()
            self.__active_sequence = pymiere.objects.app.project.activeSequence
        return self.__active_sequence

    @swap_focus
    def play_func(self, *args):
        """ Press play/pause button for main player (program monitor) """
        pymiere.objects.qe.startPlayback()

    @swap_focus
    def forward_func(self, *args, frames=10):
        """ Put the timeline cursor x frame later """
        current_time = self.active_sequence.getPlayerPosition()
        current_time.seconds += 1 / 25 * frames
        self.active_sequence.setPlayerPosition(current_time.ticks)

    def backward_func(self, *args, frames=10):
        """ Put the timeline cursor x frame before """
        current_time = self.active_sequence.getPlayerPosition()
        current_time.seconds -= 1 / 25 * frames
        self.active_sequence.setPlayerPosition(current_time.ticks)

    def refresh_selection_func(self, *args):
        """ Refresh list of selected clip in UI, should be triggered by event in the future """
        clips = self.active_sequence.getSelection()
        result = list(set([clip.name for clip in clips]))
        self.selection_info.setText("\n".join(result))

    @swap_focus
    def change_path_func(self, *args):
        """ Change the path of selected clips to this new media """
        clips = self.active_sequence.getSelection()
        success, new_path = simple_file_dialog("open", "choose a new media")
        if not success:
            return
        for clip in clips:
            if clip.isMGT():
                continue  # no media path for Motion Graphics Templates
            item = clip.projectItem  # clips are linked to a project item
            current_path = item.getMediaPath()
            if new_path == current_path:
                continue  # already using the new path...
            if not item.canChangeMediaPath():
                continue
            item.changeMediaPath(new_path, overrideChecks=True)

    @swap_focus
    def move_selected_func(self, *args):
        clips = self.active_sequence.getSelection()
        seconds = self.move_seconds.value()
        for clip in clips:
            wrappers.move_clip(clip, seconds)

    @swap_focus
    def add_effect_func(self, *args):
        """ add a swirl effect and change parameteres """
        qe_project = pymiere.objects.qe.project
        first_track = qe_project.getActiveSequence().getVideoTrackAt(0)
        index = 0
        clip = None
        while clip is None or clip.type == "Empty":
            clip = first_track.getItemAt(index)
            index += 1
        clip.addVideoEffect(qe_project.getVideoEffectByName("Twirl"))
        twirl = self.active_sequence.videoTracks[0].clips[0].components[2]
        for property in twirl.properties:
            if property.displayName == "Angle":
                property.setValue(50, True)

    @swap_focus
    def import_func(self, *args):
        success, file_to_import = simple_file_dialog("open", "choose a file to import")
        if not success:
            return
        root_bin = pymiere.objects.app.project.getInsertionBin()
        pymiere.objects.app.project.importFiles([file_to_import], True, root_bin, True)
        result = root_bin.findItemsMatchingMediaPath(file_to_import, True)
        if len(result) == 0:
            raise ImportError("Failed to find the imported items")
        if len(result) != 1:
            raise ValueError("Import sucessfull but there are more than one clips matching path {} in the root bin".format(file_to_import))
        return result[0]

    @swap_focus
    def import_insert_func(self, *args):
        item = self.import_func()
        self.insert_func(project_item=item)

    def insert_func(self, *args, project_item):
        current_time = self.active_sequence.getPlayerPosition()
        self.active_sequence.insertClip(project_item, current_time, 0, 0)

    @swap_focus
    def export_frame_func(self, *args):
        active_sequence_qe = pymiere.objects.qe.project.getActiveSequence()
        time = active_sequence_qe.CTI.timecode
        success, filename = simple_file_dialog("save", "export png frame there", filter="Image (*.png)")
        if not success:
            return
        if os.path.isfile(filename):
            os.remove(filename)
        active_sequence_qe.exportFramePNG(time, filename)

    @swap_focus
    def export_encoder_func(self, *args):
        # # export via MediaEncoder => no because I do not have not Adobe Media Encoder installed...
        # encoder = pymiere.objects.app.encoder
        # encoder.launchEncoder()

        # export directly via Premiere
        default_encoding_preset_path = os.path.join(pymiere.objects.app.path, "MediaIO", "systempresets")
        success, encoding_preset = simple_file_dialog("open", "choose an encoding preset",
                                                      filter="Encoding preset (*.epr)",
                                                      directory=default_encoding_preset_path)
        if not success:
            return
        success, output_path = simple_file_dialog("save", "export region")
        if not success:
            return
        self.active_sequence.exportAsMediaDirect(output_path, encoding_preset, 1)

    def close_func(self, *args):
        self.__active_sequence = None
        pymiere.objects.app.project.closeDocument()

    def open_func(self, *args):
        self.__active_sequence = None
        success, filepath = simple_file_dialog("open", "choose a project to open",
                                               filter="Premiere project (*.prproj)")
        if not success:
            return
        pymiere.objects.app.openDocument(filepath)

    def save_func(self, *args):
        pymiere.objects.app.project.save()

    def saveas_func(self, *args):
        success, filepath = simple_file_dialog("open", "choose new location to save project",
                                               filter="Premiere project (*.prproj)")
        if not success:
            return
        if os.path.isfile(filepath):
            os.remove(filepath)
        pymiere.objects.app.project.saveAs(filepath)


if __name__ == "__main__":
    # handle pyqt silent exceptions
    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook

    app = QApplication([])
    pymiere_ui = PymiereControl()
    pymiere_ui.show()
    app.exec_()
