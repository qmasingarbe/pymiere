import pymiere

# test = int(120)
# print(type(test))
# print(isinstance(test, object))

PYMIERE = pymiere.Pymiere()
sequence_info = PYMIERE.eval_script("$._pymiere['myFirstId'] = app.project.activeSequence; JSON.stringify($._pymiere['myFirstId']);")
sequence = pymiere.core.PymiereGenericObject('myFirstId', name=sequence_info["name"], id=sequence_info["id"], videoTracks=sequence_info["videoTracks"])
print(sequence.name)
print(sequence.videoTracks)
print(sequence.projectItem)
print(sequence.getInPointAsTime())
print(sequence.getInPoint())
sequence.setPlayerPosition(254016000000*3)