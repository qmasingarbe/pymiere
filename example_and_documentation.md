# Use cases & examples
Here you will find little snippets and explanations for things you may want to do with `Pymiere`.

## Import clips and add them to sequence
```python
import pymiere  
from pymiere.wrappers import time_from_seconds  
project = pymiere.objects.app.project  
  
media_path = r"C:\path\to\media.mp4"  
  
# import media into Premiere  
success = project.importFiles(  
    [media_path], # can import a list of media  
    suppressUI=True,  
    targetBin=project.getInsertionBin(),  
    importAsNumberedStills=False  
)  
# find media we imported  
items = project.rootItem.findItemsMatchingMediaPath(media_path, ignoreSubclips=False)  
# add clip to active sequence  
project.activeSequence.videoTracks[0].insertClip(items[0], time_from_seconds(0))
```

## Update, move and cut clips
#### Change clip media path
```python
import pymiere  
# get first clip of first video track of active sequence  
clip = pymiere.objects.app.project.activeSequence.videoTracks[0].clips[0]  
# change media path on clip  
clip.projectItem.changeMediaPath(r"C:\new\media\path.mp4", overrideChecks=True)
```
#### Move clip
There are two ways to move a clip.
Note that any linked audio clips will not be moved at the same time.
##### Using in and out points (only working from Premiere Pro 2019+)
```python
import pymiere  
from pymiere.wrappers import time_from_seconds  
# get first clip of first video track of active sequence  
clip = pymiere.objects.app.project.activeSequence.videoTracks[0].clips[0]  
# move clip right 10 seconds
clip.end = time_from_seconds(clip.end.seconds + 10)  
clip.start = time_from_seconds(clip.start.seconds + 10)
```
##### Using QE move method
(see QE section)
```python
import pymiere  
# get first video track of active sequence  
track = pymiere.objects.qe.project.getActiveSequence().getVideoTrackAt(0)  
# get first clip in track (QE list empty spaces as items)  
for x in range(track.numItems):    
    item = track.getItemAt(x)    
    if item.type != "Empty":    
        break
# move clip right (use "-10.0" to move left)  
item.move("10.0")
```

## New/open/save project
```python
import pymiere  
project_path = r"C:\path\to\project.prproj"  
# create new empty project  
pymiere.objects.app.newProject(project_path)  # from Premiere 2020  
pymiere.objects.qe.newProject(project_path)  # before Premiere 2020  
# open existing project  
pymiere.objects.app.openDocument(project_path)  
# save project  
pymiere.objects.app.project.save()  
pymiere.objects.app.project.saveAs(project_path)  
# close project  
pymiere.objects.app.project.closeDocument()
```

## New/open sequence
```python
import pymiere
# new sequences are created from sqpreset files  
# basic presets come installed with Premiere and can be accessed using
from pymiere.wrappers import get_system_sequence_presets  
sequence_preset_path = get_system_sequence_presets(category="HDV", resolution=None, preset_name="HDV 1080p25")  
# or you can use a custom sqpreset file anywhere  
sequence_preset_path = r"C:\path\to\custom.sqpreset"  
# create sequence # (don't use pymiere.objects.app.project.createNewSequence() as it pop a window requiring user intervention)
sequence_name = "My new sequence"  
pymiere.objects.qe.project.newSequence(sequence_name, sequence_preset_path)  
# find newly created sequence by name  
sequence = [s for s in pymiere.objects.app.project.sequences if s.name == sequence_name][0]  
# open sequence in UI  
pymiere.objects.app.project.openSequence(sequenceID=sequence.sequenceID)  
# this is now our active sequence  
print(pymiere.objects.app.project.activeSequence)
```


## Render
#### Direct render in Premiere
```python
import pymiere
# find the sequence we want to export
sequence = pymiere.objects.app.project.activeSequence
result = sequence.exportAsMediaDirect(
    r"D:\tmp\hello.mp4",  # path of the exported file
    r"C:\Program Files\Adobe\Adobe Premiere Pro 2020\Settings\IngestPresets\Transcode\Match Source - H.264 High Bitrate.epr",  # path of the export preset file
    pymiere.objects.app.encoder.ENCODE_ENTIRE  # what part of the sequence to export. Others are: ENCODE_IN_TO_OUT or ENCODE_WORKAREA
)
print(result)  # log after the export is done or has crashed
print(result.strip() == "No result")  # success log
```

#### Queue render to Media Encoder
**TODO** : send me an email if you badly need this and I will take a shot at it


## Add & manipulate effects
#### Add video effect using QE
(see QE section)
```python
import pymiere  
qe_project = pymiere.objects.qe.project  
# see all available video effects  
print(list(qe_project.getVideoEffectList()))  
# get first clip of first video track  
track = qe_project.getActiveSequence().getVideoTrackAt(0)  
for x in range(track.numItems):  
    clip = track.getItemAt(x)  
    if clip.type != "Empty":  
        break  
# add Twirl video effect on clip
clip.addVideoEffect(qe_project.getVideoEffectByName("Twirl"))
```

#### Manipulate effects properties
Each clip in Premiere has components. The first 2 components of a video clips are usually `Opacity` and `Motion`, they are added by default and allow control over the opacity and position/rotation/scale of the clip. They can be controlled like effects. Each additional effect on a clip is a new component.
```python
import pymiere  
# first clip of first video track of active sequence  
clip = pymiere.objects.app.project.activeSequence.videoTracks[0].clips[0]  
# find our effect in components  
for component in clip.components:  
    if component.displayName == "Twirl":  
        break  
else:  
    raise ValueError("No effect 'Twirl' found on first clip")  
# change some properties value or get the value  
for property in component.properties:  
    # set the twirl angle to 50  
    if property.displayName == "Angle":  
        property.setValue(50, True)  
    if property.displayName == "Twirl Radius":  
        print("Twirl radius value:", property.getValue())
```

## Text & Motion Graphics
There is at least 4 ways to add text in Premiere Pro and none of them are perfectly integrated in the API so you may need to be a bit creative. The short answer is: use custom `Motion Grapic Templates`.
#### Type Tool Text
Text added by the `Type Tool` in Premiere is not supported by the API.
It seems to be added as an effect on a clip but the source text is not unfortunately not editable.

#### Simple Text Effect
`Simple Text` is an effect that can be added on any video clip (see Add & manipulate effects). We can change the text programmatically but this seems buggy/unreliable. Also the options are very limited (opacity, position and size)
```python
import pymiere  
# first clip of first video track of active sequence  
clip = pymiere.objects.app.project.activeSequence.videoTracks[0].clips[0]  
# find our effect in components  
for component in clip.components:  
    if component.displayName == "Simple Text":  
        break  
else:  
    raise BaseException("No effect 'Simple Text' found on first clip")  
# change some properties value or get the value  
for property, property_name in zip(component.properties, ["?", "Position", "Justification", "Size", "Opacity", "Content"]):  
    if property_name == "Position":  
        property.setValue([0.5, 0.5], True)  
    if property_name == "Content":  
        property.setValue(" New text ", True)
```
#### Captions
Not tried to use them with Pymiere yet...

#### Motion Graphics Templates
Motion Graphic Templates are basically After Effects compositions exported to be used in Premiere Pro.
On export you choose which composition parameters should be available as properties in Premiere.
These seems to be the best option as you can create more complicated animations and designs than basic text and expose all the options you want to be modified in Premiere.
Note: Although it has been implemented since Premiere 2019 some of the property types exposed from After Effects are not editable via the API. 
It's especially true for the text property than an't be edited as a compound property so you can only edit the text not the font etc...
If you want to edit the font via the API in Premiere you will have to promote it through a custom control in After Effects.

```python
import pymiere  
from pymiere.wrappers import time_from_seconds  
sequence = pymiere.objects.app.project.activeSequence  
# import mogrt template into sequence  
# path to mogrt (some come with Premiere install in C:\Program Files\Adobe\Adobe Premiere Pro 2020\Essential Graphics)  
mogrt_path = r"C:\path\to\template.mogrt"  
mgt_clip = sequence.importMGT(  
    path=mogrt_path,  
    time=time_from_seconds(1),  # start time  
    videoTrackIndex=1, audioTrackIndex=1  # on which track to place it  
)  
# get component hosting modifiable template properties  
mgt_component = mgt_clip.getMGTComponent()  
# iter through MGT properties, display and change values  
for prop in mgt_component.properties:  
    print(prop.displayName)
    value = prop.getValue()  # for color properties use getColorValue() and setColorValue()
    print(value)  
    prop.setValue(value, True)
```

## QE
QE (Quality Engineering) is an hidden, undocumented API for Premiere Pro.
It is used by Adobe to run automated tests for development purposes.
Although it is not officially supported by Adobe, it is usable alongside the official API.
Pymiere offer an entry point to QE using `pymiere.objects.qe`.
Python objects in QE won't have autocompletion or docstrings but you can inspect the available properties and method by calling the `inspect` method (ex: `pymiere.object.qe.inspect()`)
Some functionality are available only in QE or only in the official API, so you may need to use both in your script.
Note that QE is not fail proof and you may crash Premiere while exploring it. Also some of the methods seems to not be working or we don't know the proper arguments for them.

#### Similarity with the official API
The structure of a project is kind of similar between QE and the API. This snippet show some code to access project/sequence/tracks/clip/components in both APIs
```python
import pymiere  
# project  
project = pymiere.objects.app.project  
qe_project = pymiere.objects.qe.project  
# active sequence  
sequence = project.activeSequence  
qe_sequence = qe_project.getActiveSequence()  
# first video track  
track = sequence.videoTracks[0]  
qe_track = qe_sequence.getVideoTrackAt(0)  
# first clip  
clip = track.clips[0]  
for x in range(qe_track.numItems):  
    qe_clip = qe_track.getItemAt(x)  
    if qe_clip.type != "Empty":  
        # qe list empty portion of track like item and we don't want them  
        break  
else:  
    raise ValueError("No clip found on track")  
# components  
print([c.displayName for c in clip.components])  
print([qe_clip.getComponentAt(i).name for i in range(qe_clip.numComponents)])
```

#### Actions only in QE
So far these actions are only available through QE:
  - Listing and adding video/audio effects (see Add & manipulate effects)
  - Listing and adding video/audio transitions
  - Creating new items such as Transparent Video, Universal Counter, Bars&Tones, Black Video...
  - Controlling playback (I may be wrong for this one)
  - Making clip cut (razor tool)
  - Many more that I didn't found yet...

#### Know method signature
Here a couple of method in QE with a bit of documentation deducted through testing
  - newTransparentVideo (create new transparent video in root bin)
```python
pymiere.objects.qe.project.newTransparentVideo(1280, 720, 0, 1, 1)
"""
arg1: (int) x size in pixel
arg2: (int) y size in pixel
arg3: (int) ?
arg4: (int) ? probably aspect ratio ?
arg5: (int) ? probably aspect ratio ?
"""
```

  - razor (split clip using Razor Tool)
```python
pymiere.objects.qe.project.getActiveSequence().getVideoTrackAt(0).razor("1.0")
"""
arg1: (str) string representation of a float number representing the time in second where to cut
"""
```

  - move (move a clip left or right in a track)
```python
pymiere.objects.qe.project.getActiveSequence().getVideoTrackAt(0).getItemAt(1).move("10.0", False, False)
"""
arg1: (str) string representation of time in second (can be negative)
arg2: (bool) duplicate?
arg3: (bool) offset everything around?
"""
```

  - control playback (play/pause sequence)
```python
player = pymiere.objects.qe.project.getActiveSequence().player  
player.play(1)  # arg seems to be playback speed
print(player.isPlaying)  # only available since Premiere 2020
player.stop()
```