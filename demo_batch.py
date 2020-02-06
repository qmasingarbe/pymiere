import pymiere
import pymiere.exe_utils as pymiere_exe
import requests

# start premiere
if pymiere_exe.exe_is_running("adobe premiere pro.exe")[0]:
    raise ValueError("There already is a running instance of premiere")
pymiere_exe.start_premiere()

# open a project
pymiere.objects.app.openDocument("C:\\Users\\Quentin\\Desktop\\temp\\test.pproj")

# set sequence named hello world as active sequence
sequences = pymiere.objects.app.project.sequences
sequence = next(filter(lambda s: s.name == "hello world", sequences))
pymiere.objects.app.project.openSequence(sequence.sequenceID)
pymiere.objects.app.project.activeSequence = sequence

# rename sequence and query info
pymiere.objects.app.project.activeSequence.name = "renamed sequence"
print(pymiere.objects.app.project.activeSequence.getPlayerPosition().seconds)
pymiere.objects.app.project.activeSequence.name = "hello world"  # rename back for test to work next time
pymiere.objects.app.project.save()

# close premiere
try:
    pymiere.objects.app.quit()
except requests.exceptions.ConnectionError:
    print("Success")
    pass
