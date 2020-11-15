"""
Interact with Premiere Pro using the Pymiere library.
"""
import time
import pymiere
from pymiere import wrappers

# Check for an open project
project_opened, sequence_active = wrappers.check_active_sequence(crash=False)
if not project_opened:
    raise ValueError("please open a project")

project = pymiere.objects.app.project

# Open Sequences in Premiere Pro if none are active
if not sequence_active:
    sequences = wrappers.list_sequences()
    for seq in sequences:
        project.openSequence(sequenceID=seq.sequenceID)
    # Set the first Sequence in the list as the active Sequence
    project.activeSequence = sequences[0]

# List all videos clips in the active Sequence
clips = wrappers.list_clips(project.activeSequence)

# Convert timebase in ticks per second to Frame Per Second (FPS)
fps = 1/(float(project.activeSequence.timebase)/wrappers.TICKS_PER_SECOND)
print("Sequence as a framerate of {} fps".format(fps))

# Select the first video clip in the Timeline
clips[0].setSelected(True, True)

# The following code will not work in Premiere Pro 2017 (clips were not editable at the time)
# Periodically advance the first video clip through the Timeline
start_frame = 0
end_frame = 100
for i in range(30):
    increment = i * 5
    wrappers.edit_clip(clips[0], start_frame + increment, end_frame + increment, start_frame, end_frame, fps=fps)
    time.sleep(0.1)
