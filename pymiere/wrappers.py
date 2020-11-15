"""
Collection of higher level functions using low level pymiere code
"""
import pymiere

# Premiere Pro uses ticks as its base time unit, this is used to convert from ticks to seconds
TICKS_PER_SECOND = 254016000000


def check_active_sequence(crash=True):
    """
    Check if any project is open and if so, whether any sequence is active

    :param crash: (bool) crash or return status as bool
    :return: (bool), (bool) project is opened, sequence is active
    """
    # Is any project open?
    if not pymiere.objects.app.isDocumentOpen():
        msg = "No project is opened"
        if crash:
            raise IOError(msg)
        print(msg)
        return False, False
    # is there a sequence opened ?
    if not pymiere.objects.app.project.activeSequence:
        msg = "No sequence is currently open in Premiere Pro"
        if crash:
            raise AttributeError(msg)
        print(msg)
        return True, False
    return True, True


def get_item_recursive(item, add_root=False, filter_function=lambda i: True):
    """
    Recursively browse project items returning a list of items and associated filepaths

    :param item: (ProjectItem) initial item to browse from
    :param add_root: (bool) add the root (first given item) to the list and to the path
    :param filter_function: (None or func) function applied to all items; should return a bool adding or dismissing it
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
    List available Sequences in the open project, print info and return objects

    :return: (list of Sequence) all Sequences available in the project
    """
    sequences = pymiere.objects.app.project.sequences
    print("Found {} Sequences in project '{}'\n".format(len(sequences), pymiere.objects.app.project.name))
    for sequence in sequences:
        print("Name : '{}'\nPath : '{}'".format(sequence.name, sequence.projectItem.treePath))
        print("Sequence settings:")
        settings = sequence.getSettings()
        for setting in ["videoFrameRate", "videoFrameWidth", "videoFrameHeight", "videoPixelAspectRatio", "audioSampleRate"]:
            value = settings.__getattribute__(setting)
            if isinstance(value, pymiere.Time):
                value = 1/value.seconds
            print("\t{} : {}".format(setting, value))
        print("\n")
    return sequences


def list_clips(sequence):
    """
    List all video Clips on all tracks for a given Sequence

    :param sequence: (Sequence)
    :return: (list of Clips)
    """
    video_clips = list()
    tracks = sequence.videoTracks
    for track in tracks:
        print("Track:", track.name or track.id)  # Premiere 2017 doesn't have a 'name' property for tracks
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
    Trim or move a Clip. This in not available in Premiere Pro 2017 - use insertClip() or overwriteClip() instead.

    :param clip: (Clip)
    :param start_on_timeline: (int) Frame at which the Clip should start in the Sequence timeline
    :param end_on_timeline: (int) Frame at which the Clip should end in the Sequence timeline
    :param in_point_on_clip: (int) First frame of the Clip we will see (in the Clip's own timeline)
    :param out_point_on_clip: (int) Last frame of the Clip we will see (in the Clip's own timeline)
    :param out_point_on_clip: (int) Last frame we will see of the Clip (in the Clip's own timeline)
    """
    # get Clip fps if no fps given
    if fps is None:
        fps = clip.projectItem.getFootageInterpretation().frameRate  # not available in ppro 2017, use sequence.timebase
    # check length match
    if end_on_timeline - start_on_timeline != out_point_on_clip - in_point_on_clip:
        raise ValueError("Duration in timeline ({} frames) doesn't match duration of Clip ({} frames)".format(end_on_timeline - start_on_timeline, out_point_on_clip - in_point_on_clip))
    # set actual properties
    clip.end = time_from_seconds(end_on_timeline / fps)
    clip.start = time_from_seconds(start_on_timeline / fps)
    clip.inPoint = time_from_seconds(in_point_on_clip / fps)
    clip.outPoint = time_from_seconds(out_point_on_clip / fps)


def move_clip(clip, seconds):
    """
    Move a Clip by the number of seconds.
    Negative values will move the Clip left (before the original position).
    Positive values will move the Clip right (after the original position).
    :param clip: (Clip) Clip object to be moved
    :param seconds: (float) how many seconds we want to move the Clip by, negative value will move left, positive right
    """
    params = ["end", "start"] if seconds > 0 else ["start", "end"]
    for param in params:
        time_object = getattr(clip, param)
        time_object.seconds = time_object.seconds + seconds
        setattr(clip, param, time_object)


def animate_effect_using_function(clip, effect_name, property_name, anim_func, overwrite=True, keyframe_per_seconds=1/25):
    """
    Reproduce the animation of a given function on an effect property
    :param clip: (Clip) Clip object on which we want to change animate the effect
    :param effect_name: (str) name of the effect (ex: 'twirl')
    :param property_name: (str) name of the property on the effect (ex: 'angle')
    :param anim_func: (function) function that takes a float number as input (seconds) and returns the value for the effect at this time as float
    (ex: lambda s: math.cos(s*2)*10 for a sine wave, lambda s: int(s % 2)*10 for a blinking effect etc.)
    :param overwrite: (bool) if True, clear existing keys, else only add keys
    :param keyframe_per_seconds: (float) number of keyframes to add per second
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
                raise ValueError("Keyframes are not supported for property '{}' of effect '{}' for Clip '{}'".format(property.displayName, effect.displayName, clip.name))
            # activate keyframes on property (= click the stop watch icon in the ui)
            if not property.isTimeVarying():
                property.setTimeVarying(True)

            # get Clip in/out
            start = clip.inPoint.seconds
            end = clip.outPoint.seconds

            # clear keyframes
            if overwrite:
                property.removeKeyRange(start, end, True)

            # place keyframes
            while start < end:
                property.addKey(start)
                property.setValueAtKey(start, anim_func(start), True)
                start += keyframe_per_seconds


def time_from_seconds(seconds):
    """
    Many properties need a Time object to represent time, this is a helper to create one.
    :param seconds: (float) time in seconds
    :return: (pymiere.Time) preseted time object
    """
    t = pymiere.Time()
    t.seconds = seconds
    return t


if __name__ == "__main__":
    pass
