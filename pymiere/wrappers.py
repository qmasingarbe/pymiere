"""
Collection of higher level functions using low level pymiere code
"""
import os
import platform
import pymiere
from pymiere.core import get_premiere_version

# premiere uses ticks as its base time unit, this is used to convert from ticks to seconds
TICKS_PER_SECONDS = 254016000000


def check_active_sequence(crash=True):
    """
    Check if a project is opened and if a sequence is active

    :param crash: (bool) crash or return status as bool
    :return: (bool), (bool) project is opened, sequence is active
    """
    # is there a project opened ?
    if not pymiere.objects.app.isDocumentOpen():
        msg = "No project is opened"
        if crash:
            raise IOError(msg)
        print(msg)
        return False, False
    # is there a sequence opened ?
    if not pymiere.objects.app.project.activeSequence:
        msg = "No sequence is currently opened in the UI"
        if crash:
            raise AttributeError(msg)
        print(msg)
        return True, False
    return True, True


def get_item_recursive(item, add_root=False, filter_function=lambda i: True):
    """
    Recursively browse the project items returning a list of item with associated filepaths

    :param item: (ProjectItem) start item to browse from
    :param add_root: (bool) add the root (first given item) to the list and to the path
    :param filter_function: (None or func) function applied on all item, should return a bool adding or dismissing it
    :return: (list of ProjectItem)
    """
    all_children = [item] if filter_function(item) and add_root else list()
    # no children under item
    if item.children is None:
        return all_children
    # iter over children
    for c in item.children:
        all_children.extend(get_item_recursive(c, add_root=True, filter_function=filter_function))
    return all_children


def list_sequences():
    """
    List available sequences in the opened project, print infos and return objects

    :return: (list of Sequence) all sequences available in the project
    """
    sequences = pymiere.objects.app.project.sequences
    print("Found {} sequences in project '{}'\n".format(len(sequences), pymiere.objects.app.project.name))
    for sequence in sequences:
        print("Name : '{}'\nPath : '{}'".format(sequence.name, sequence.projectItem.treePath))
        print("Sequence setting :")
        settings = sequence.getSettings()
        for setting in ["videoFrameRate", "videoFrameWidth", "videoFrameHeight", "videoPixelAspectRatio", "audioSampleRate"]:
            value = settings.__getattribute__(setting)
            if isinstance(value, pymiere.Time):
                value = 1/value.seconds
            print("\t{} : {}".format(setting, value))
        print("\n")
    return sequences


def list_video(sequence):
    """
    List all video clips on all tracks on this sequence

    :param sequence: (Sequence)
    :return: (list of Clip)
    """
    video_clips = list()
    tracks = sequence.videoTracks
    for track in tracks:
        print("Track :", track.name or track.id)  # Premiere 2017 doesn't have 'name' property on tracks
        clips = track.clips
        for clip in clips:
            print("\tName: {}".format(clip.name))  # Premiere 2017 doesn't have 'name' property on clips
            print("\t- {:.<12}{}".format("Path", clip.projectItem.getMediaPath() if not clip.isMGT() else "[No path, this is a Motion Graphics template]"))
            print("\t- {:.<12}{}".format("Start", clip.start.seconds))
            print("\t- {:.<12}{}".format("End", clip.end.seconds))
            print("\t- {:.<12}{}".format("In", clip.inPoint.seconds))
            print("\t- {:.<12}{}".format("Out", clip.outPoint.seconds))
            print("\t- {:.<12}{}".format("Duration", clip.duration.seconds))
            print("")
            video_clips.append(clip)
        print("")
    return video_clips


def edit_clip(clip, start_on_timeline, end_on_timeline, in_point_on_clip, out_point_on_clip, fps=None):
    """
    Trim or move clip. This in not available in ppro 2017, use insertClip or overwriteClip

    :param clip: (Clip)
    :param start_on_timeline: (int) Frame at which the clip should start in the sequence timeline
    :param end_on_timeline: (int) Frame at which the clip should end in the sequence timeline
    :param in_point_on_clip: (int) First frame we will see of the clip (in the clip own timeline)
    :param out_point_on_clip: (int) Last frame we will see of the clip (in the clip own timeline)
    """
    # get clip fps if no fps given
    if fps is None:
        fps = clip.projectItem.getFootageInterpretation().frameRate  # not available in ppro 2017, use sequence.timebase
    # check length match
    if end_on_timeline - start_on_timeline != out_point_on_clip - in_point_on_clip:
        raise ValueError("Duration in timeline ({} frames) doesn't match duration of clip ({} frames)".format(end_on_timeline - start_on_timeline, out_point_on_clip - in_point_on_clip))
    # set actual properties
    clip.end = time_from_seconds(end_on_timeline / fps)
    clip.start = time_from_seconds(start_on_timeline / fps)
    clip.inPoint = time_from_seconds(in_point_on_clip / fps)
    clip.outPoint = time_from_seconds(out_point_on_clip / fps)


def move_clip(clip, seconds):
    """
    Move a clip by the number of seconds. Negative values will move the clip left (before the original position),
    positive values move the clip right (after the original position)
    :param clip: (Clip) clip object we want to move
    :param seconds: (float) how many seconds we want to move the clip by, negative value will move left, positive right
    """
    params = ["end", "start"] if seconds > 0 else ["start", "end"]
    for param in params:
        time_object = getattr(clip, param)
        time_object.seconds = time_object.seconds + seconds
        setattr(clip, param, time_object)


def animate_effect_using_function(clip, effect_name, property_name, anim_func, overwrite=True, keyframe_per_seconds=1/25):
    """
    Reproduce the animation of the given function on an effect property
    :param clip: (Clip) clip object on which we want to change animate the effect
    :param effect_name: (str) name of the effect (ex: 'twirl')
    :param property_name: (str) name of the property on the effect (ex: 'angle')
    :param anim_func: (function) function that take a float number as input (seconds) and return the value for the effect at this time as float
    (ex: lambda s: math.cos(s*2)*10 for a sine wave, lambda s: int(s % 2)*10 for a blinking effect, ...)
    :param overwrite: (bool) if True, clear existing keys else only add keys
    :param keyframe_per_seconds: (float) number of keyframes to place each seconds
    """
    # filter effect by name
    effects = clip.components
    for effect in effects:
        if effect.displayName.lower() != effect_name.lower():
            continue
        # filter effect property by name
        for property in effect.properties:
            if property.displayName.lower() != property_name.lower():
                continue
            # check keyframes are supported
            if not property.areKeyframesSupported():
                raise ValueError("Keyframes are not supported on property '{}' of effect '{}' for clip '{}'".format(property.displayName, effect.displayName, clip.name))
            # activate keyframes on proerty (= check the stop watch icon in the ui)
            if not property.isTimeVarying():
                property.setTimeVarying(True)

            # get clip in/out
            start = clip.inPoint.seconds
            end = clip.outPoint.seconds

            # clear keys
            if overwrite:
                property.removeKeyRange(start, end, True)

            # place keys
            while start < end:
                property.addKey(start)
                property.setValueAtKey(start, anim_func(start), True)
                start += keyframe_per_seconds


def time_from_seconds(seconds):
    """
    Many properties need a Time object to represent time, this is an helper to create one
    :param seconds: (float) time in seconds
    :return: (pymiere.Time) preseted time object
    """
    t = pymiere.Time()
    t.seconds = seconds
    return t


def get_system_sequence_presets(category="Digital SLR", resolution="1080p", preset_name="DSLR 1080p25"):
    """
    To create a new sequence via qe.project.newSequence we need to give a sequence preset file (.sqpreset)
    Base presets come installed with premiere. Select one according to your footage.
    Paths examples : (versions may vary)
        on win: C:\Program Files\Adobe\Adobe Premiere Pro 2020\Settings\SequencePresets
        on mac: /Applications/Adobe Premiere Pro CC 2019/Adobe Premiere Pro CC 2019.app/Contents/Settings/SequencePresets
    :param category: (str) category of the sequence preset in SequencePresets folder (AVCHD, RED R3D, ProRes RAW...)
    :param resolution: (str) category subfolder for sequence resolution
    :param preset_name: (str) actual filename of the sqpreset file (with or without extension)
    :return: (str) path of a sqpreset file
    """
    # add ext if needed
    if not preset_name.endswith(".sqpreset"):
        preset_name += ".sqpreset"
    # relative path
    if resolution is None:
        sequence_preset_root = os.path.normpath("Settings/SequencePresets/{}/{}".format(category, preset_name))
    else:
        sequence_preset_root = os.path.normpath("Settings/SequencePresets/{}/{}/{}".format(category, resolution, preset_name))
    # on mac add a Contents folder
    if platform.system().lower() != "windows":
        sequence_preset_root = os.path.join("Contents", sequence_preset_root)
    # absolute path in running Premiere pro directory
    sequence_preset_path = os.path.join(pymiere.objects.app.path, sequence_preset_root)
    # check exists
    if not os.path.isfile(sequence_preset_path):
        raise IOError("Sequence preset '{}' not found on disk".format(sequence_preset_path))
    return sequence_preset_path


def has_media_encoder():
    """
    Check if there is a Media Encoder (AME) version installed that work with the currently running Premiere Pro

    :return: (bool) True if suitable AME version found
    """
    premiere_version = get_premiere_version().version[0]
    encoder_versions = [int(app_name.split("-")[1].split(".")[0]) for app_name in pymiere.objects.apps if app_name.startswith("ame-")]
    return premiere_version in encoder_versions


def clone_sequence(sequence, new_sequence_name=None):
    """
    Equivalent of Sequence.clone() with return value and optional rename
    :param sequence: (Sequence) sequence object to duplicate
    :param new_sequence_name: (str or None) optional new name for the duplicated sequence
    :return: (Sequence) duplicated sequence object
    """
    project = pymiere.objects.app.project
    # store sequences before clone
    before_sequence_names = [s.sequenceID for s in project.sequences]
    # actual clone
    sequence.clone()
    # search clone sequence
    for new_seq in project.sequences:
        if new_seq.sequenceID not in before_sequence_names:
            break
    else:
        raise ValueError("New sequence not found")
    # rename and return
    if new_sequence_name is not None:
        new_seq.name = new_sequence_name
    return new_seq


if __name__ == "__main__":
    pass
