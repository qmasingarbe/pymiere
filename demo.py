import time
import pymiere
from pymiere import wrappers

# check project is opened
project_opened, sequence_active = wrappers.check_active_sequence(crash=False)
if not project_opened:
    raise ValueError("please open a project")

project = pymiere.objects.app.project

# open sequences if none active
if not sequence_active:
    sequences = wrappers.list_sequences()
    for seq in sequences:
        project.openSequence(sequenceID=seq.sequenceID)
    project.activeSequence = sequences[0]

# list videos
clips = wrappers.list_video(project.activeSequence)

# get sequence fps (timebase in ticks to be converted to frame per seconds)
fps = 1/(project.activeSequence.timebase/wrappers.TICKS_PER_SECONDS)
print("Sequence as a framerate of {} fps".format(fps))

# edit clip
start_frame = 0
end_frame = 200
clips[0].setSelected(1, 1)

# the next code will do nothing in ppro 2017 cause the clip were not editable at the time
# fun (to me) animation of clip advancing in timeline
for i in range(30):
    increment = i * 5
    wrappers.edit_clip(clips[0], start_frame + increment, end_frame + increment, start_frame, end_frame, fps=fps)
    time.sleep(0.1)
