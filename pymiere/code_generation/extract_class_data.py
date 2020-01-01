from pprint import pprint
from pymiere.core import eval_script
from pymiere import utils

filepath = r"D:\code\prpro\pymiere\code_generation\jsxObjectToPythonObject.jsx"

things_to_extract = [
    ('$.global', "$"),
    ('qe', "bababababa"),
    ('app.project.rootItem.children[0].getFootageInterpretation()', "bababababa"),
    ('app.project.rootItem.children[0].getOutPoint()', "bababababa"),
    ('app.project.activeSequence.videoTracks[0]', "bababababa"),
    ('app.project.activeSequence.videoTracks[0].clips[0]', "bababababa"),
    ('app.project.activeSequence.getSettings()', "bababababa"),
    ('app.project.activeSequence.markers.getFirstMarker()', "bababababa"),
    ('app.project.activeSequence.videoTracks[0].clips[0].components[0]', "bababababa"),
    ('$', "global"),
    ('Folder.current.getFiles("*.exe")', "bababababa"),
    ('app.project.activeSequence.videoTracks[0].clips[0].components[0].properties[0]', "bababababa"),
    ('app.encoder.getExporters()[0]', "bababababa"),
    ('app.encoder.getExporters()[0].getPresets()[0]', "bababababa")
]

for thing_to_extract in things_to_extract:
    # using encoding 'utf-8-sig' to work with file saved with Adobe ExtendScript Toolkit
    with open(filepath, encoding='utf-8-sig') as f:
        code = f.read()
    code = code.replace("__PLACEHOLDER__", '{}, "{}"'.format(thing_to_extract[0], thing_to_extract[1]))
    data = eval_script(code=code)
    print("Result :")
    pprint(data, depth=2)
    filename = thing_to_extract[0].replace(".","").replace("[","").replace("]","").replace("(","").replace(")","").replace("*","").replace('"','')
    utils.write_json_file(r"D:\code\prpro\pymiere\code_generation\class_datas\classDataExtract_{}.json".format(filename), data)