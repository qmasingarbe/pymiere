import pymiere
import pymiere.exe_utils as pymiere_exe
import requests
sjpwimport PySimpleGUI as sg
from pathlib import Path

# Use PySimpleGui to select a .pproj file
path = Path(sg.popup_get_file("Please select a Premiere Pro project to open", default_path="C:\\Users\\Quentin\\Desktop\\temp\\test.pproj", file_types=(("Premiere Pro", "*.prproj"),)))

# Start Premiere Pro and open the selected project
if not pymiere_exe.exe_is_running("adobe premiere pro.exe")[0]:
    pymiere_exe.start_premiere()
    # TODO: Perhaps rename to just 'pymiere_exe.start'?  Mentioning premiere seems unnecessary...
pymiere.objects.app.openDocument(str(path))
# TODO: It would be nice for .openDocument to take a pathlib object itself (so you don't have to remember str(path).add()
# TODO: It would also be nice to be able to start Premiere and open a Project all in one command by passing a Path argument e.g. pymiere_exe.start(path)

# Open "hello world" and set it as the active sequence; if "hello world" doesn't exist, use the first Sequence found.
project = pymiere.objects.app.project
sequences = project.sequences
# TODO: Can we remove wrappers.list_sequences() from demo.py? This seems easier and more readable!
name = "hello world"
sequence = list([s for s in sequences if s.name == name] or sequences)[0]
project.openSequence(sequence.sequenceID)
project.activeSequence = sequence
# If there's any chance you might be changing the active sequence again, you can keep using 'project.activeSequence' to periodically check the CURRENT active sequence, otherwise the object stored as 'sequence' should do just fine.

# Get some information about the Sequence.
print("Current Sequence:", sequence.name)
print("Resolution:", sequence.frameSizeHorizontal, " x", sequence.frameSizeVertical)
print("Current Position:", round(sequence.getPlayerPosition().seconds, 3), "seconds")
methods_and_attributes = [x for x in dir(sequence) if not x.startswith("_")]
print("Other methods & attributes:")
print("\n".join(methods_and_attributes))

# Backup, then batch-rename Sequences using the Project name as a prefix
backup = {sequence: sequence.name for sequence in sequences}
prefix = project.name.split(".prproj")[0]
for sequence in sequences:
    sequence.name = prefix + " - " + sequence.name

# Restore Sequence names
for sequence, name in backup.items():
    sequence.name = name

# Save the Project and Close Premiere Pro
project.save()
try:
    pymiere.objects.app.quit()
    # TODO: Is there a way to override or preselect an option when the "Save project Yes/No" popup appears?
except requests.exceptions.ConnectionError:
    print("Success")
    pass
