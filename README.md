# ![Pymiere](https://raw.githubusercontent.com/qmasingarbe/pymiere/master/logo.png) ```Pymiere``` : Python for Premiere Pro
> Use Python to interact with _Adobe Premiere Pro_, gather data, check, edit and automate your projects.

## Why use ```Pymiere```?
If you just want to create a Premiere file programmatically, you can  generate and use an XML file (see [Open Timeline IO to XML](https://opentimelineio.readthedocs.io/en/latest/tutorials/adapters.html#final-cut-pro-xml)). **But** that involves manually exporting and importing files, potentially losing data and with no visual feedback.

**```Pymiere```** was created to enable video editors and 3D/VFX studios to automate some of their workflows using Python rather than Adobe's custom scripting language ExtendScript.

- Want to check if some shots have new versions available?
- Maybe automatically place them on a new track?
- Want to create interactive tools for your editor using Qt, Shotgun API, custom libs...?

No problem!

### Versions
  * Support Python 2 & 3
  * Tested with **Adobe Premiere Pro version 13.0 (2019)** and **version 11.0 (2017)**. I highly recommend the 2019 version because some functionality isn't available in the previous versions. It should work for version 2017+ though.
  * Tested on Windows (10)


## Installation

  1. Install [Python](https://www.python.org/downloads/windows/) if you haven't already.

  2. Install `Pymiere` via pip:

    python -m pip install pymiere

  3. Install the `Pymiere Link` extension for `Premiere Pro`:

      * Download `pymiere_link.zxp` [here](https://github.com/qmasingarbe/pymiere/blob/master/pymiere_link.zxp)
      * Install Adobe's [Extension Manager Command Line tool](https://partners.adobe.com/exchangeprogram/creativecloud/support/exman-com-line-tool.html) (note that the User Interface is deprecated, but we just need to use the command line interface).
        - Download and unzip the folder somewhere
        - Navigate to the folder in Command line or Power shell
        - type `.\ExManCmd.exe /install D:\path_to_extension\pymiere_link.zxp`
      * Alternatively install using [ZXP installer](https://aescripts.com/learn/zxp-installer/) or [Anastasiy Extension Manager](http://install.anastasiy.com) and drag `pymiere_link.zxp` onto the open application window.
      * To check that it is correctly installed, start Premiere, under `Window > Extensions` you should see `Pymiere Link` (clicking on it will do nothing)


  4. Try running some basic code:
```python
import pymiere
print(pymiere.objects.app.isDocumentOpen())
```

## Quick start
Open or create a _Premiere Pro_ project containing a Sequence with at least one video Clip. You can then run or step through [demo.py](https://github.com/qmasingarbe/pymiere/blob/master/demo.py) which demonstrates some basic code. [pymiere/wrappers.py](https://github.com/qmasingarbe/pymiere/blob/master/pymiere/wrappers.py) contains more code examples.

Basically you start by creating a ```project``` object to interact with the opened _Premiere Pro_ application (it needs to be running), after which you can get/set its attributes and call its methods like ```.name``` or ```.save()``` :

    project = pymiere.objects.app.project

Other useful methods e.g. for interacting with Sequences and video Clips are available using ```wrappers```:

    from pymiere import wrappers

    # Get a list of Sequences
    sequences = wrappers.list_sequences()

    # Open a Sequence programmatically
    project.openSequence(sequenceID=sequences[0].sequenceID)

    # Set the active Sequence programmatically
    project.activeSequence = sequences[0]

    # Get a list of all video Clips
    clips = wrappers.list_video(project.activeSequence)

    # Select one or more video Clips on the Timeline
    clips[0].setSelected(True, True)

## Useful links
* [Official doc for Premiere Pro objects](http://ppro.aenhancers.com/)
* [Unofficial doc for Premiere Pro objects](http://www.brysonmichael.com/premiereapi/objects)
* [Advanced Premiere Pro Extendscript usage](https://github.com/Adobe-CEP/Samples/blob/master/PProPanel/jsx/PPRO/Premiere.jsx)

## Contact
For any support, questions or interest please contact me: <a href="mailto:q.masingarbe@gmail.com">q.masingarbe@gmail.com</a>

## How ```Pymiere``` Works
```Pymiere``` is basically a wrapper for _ExtendScript_ (an Adobe flavour of JavaScript used for most of its _Creative Cloud_ software).  Most of the help documentation for _ExtendScript_ therefore applies directly to ```Pymiere```.

In outline, this is how ```Pymiere``` interacts with _Premiere Pro_:
1. ```Pymiere``` converts a Python command (getting a property, executing a function etc.) to _ExtendScript_ code.
2. ```Pymiere``` sends the ExtendScript code to the `Pymiere Link` extension via the _requests_ library using HTTP (*)
3. The `Pymiere Link` extension is essentially a _node.js_ server which receives the _ExtendScript_ code and executes it within Premiere Pro.
4. Where required, `Pymiere Link` will return data as a _JSON_ encoded response back to ```Pymiere```.
5. ```Pymiere``` will then decode the JSON response for further processing in Python.

(*) **NB:** You must have Premiere Pro running for ```Pymiere``` to work - it's can't run "headlessly".  If your script needs to know if Premiere Pro is running, or start it, some functions are included in `pymiere/exe_utils.py` for that.

So `pymiere.objects` are the entry point to access all Premiere Pro objects and functions and can learn more the _old school_ way by browsing the docstrings.

Alternatively, you'll be pleased to know ```Pymiere``` supports code completion and type hinting so it should be easy learn more about these objects dynamically as you code using most modern IDEs.

```Pymiere``` includes a mirror of all Premiere Pro ExtendScript objects in Python which were autogenerated from the Extendscript objects interface.  If you'd like more detail about how I did this, please read my detailed article [here](https://www.linkedin.com/pulse/python-control-adobe-applications-quentin-masingarbe/).

## Future improvements
 - [ ] separate the generic part handling communication between python and ExtendScript from the specific code for Premiere Pro, enabling its use in other applications (Photoshop, Encoder...)
 - [ ] add more examples & more _wrappers_ functions
 - [ ] add support for Premiere _events_
 - [ ] add more documentation, docstrings...
 - [ ] build one Python mirror of ExtendScript objects by Premiere version, as each version adds new objects/functions/properties
 - [ ] add a way to simply customize a panel to call python functions

 ## Thanks
 I'd like to thank everybody that contributed to ```Pymiere``` by reporting bugs, imrpoving the documentation, sending ideas etc. but especially:
 - Isaac brown (https://github.com/ikebenbrown)
 - Roy Nieterau (https://github.com/BigRoy)
 - Peter Fison (https://github.com/Pfython)
