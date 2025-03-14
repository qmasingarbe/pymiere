# ![Pymiere](https://raw.githubusercontent.com/qmasingarbe/pymiere/master/logo.png) ```Pymiere``` : Python for Premiere Pro
> Use Python to interact with _Adobe Premiere Pro_, gather data, check, edit and automate your projects.

> [!WARNING]
> Pymiere is not maintained anymore.  
> It should still work fine but some newer part of the Premiere pro api may not be wrapped.

## Why use ```Pymiere```?
If you just want to create a Premiere file programmatically, you can  generate and use an XML file (see [Open Timeline IO to XML](https://opentimelineio.readthedocs.io/en/latest/tutorials/adapters.html#final-cut-pro-xml)). **But** that involves manually exporting and importing files, potentially losing data and with no visual feedback.

**```Pymiere```** was created to enable video editors and 3D/VFX studios to automate some of their workflows using Python rather than Adobe's custom scripting language ExtendScript.

- Want to check if some shots have new versions available?
- Maybe automatically place them on a new track?
- Want to create interactive tools for your editor using Qt, Shotgun API, custom libs...?

No problem!

### Versions
  * Support Python 2 & 3
  * Tested with **Adobe Premiere Pro version 23.1 (2023)**, **version 15.1 (2021)**, **version 14.5 (2020)**, **version 13.0 (2019)** and **version 11.0 (2017)**. I highly recommend version 2019+ because some functionality isn't available in the previous versions. It should work for version 2017+ though.
  * Tested on Windows 10 & macOS Catalina


## Installation

  1. Install [Python](https://www.python.org/downloads) if you haven't already.

  2. Install `Pymiere` via pip:

    python -m pip install pymiere

  3. Install the `Pymiere Link` extension for `Premiere Pro`:
      * Via the automatic `extension_installer` script
        - Download the installer script [for windows](https://raw.githubusercontent.com/qmasingarbe/pymiere/master/extension_installer_win.bat) or [for mac](https://raw.githubusercontent.com/qmasingarbe/pymiere/master/extension_installer_mac.sh)
        - Navigate to the download folder in Command line/Power shell (Windows) or terminal (Mac)
        - Run the script by typing `extension_installer_win.bat` (Windows) or `./extension_installer_mac.sh` (Mac)
        - Check the script output to see if it properly worked 
      * Alternatively via Adobe's Extension Manager
        - Download [Extension Manager Command Line tool](https://partners.adobe.com/exchangeprogram/creativecloud/support/exman-com-line-tool.html) (note that the User Interface is deprecated, but we just need to use the command line interface).
        - Unzip the folder somewhere
        - Download `pymiere_link.zxp` [here](https://github.com/qmasingarbe/pymiere/blob/master/pymiere_link.zxp)
        - Navigate to the folder in Command line/Power shell (Windows) or terminal (Mac)
        - Type (Windows) `.\ExManCmd.exe /install D:\path_to_extension\pymiere_link.zxp`
        - Type (Mac) `./ExManCmd --install /path_to_extension/pymiere_link.zxp`
      * Alternatively via [ZXP installer](https://aescripts.com/learn/zxp-installer/) or [Anastasiy Extension Manager](http://install.anastasiy.com)
      * **To check that the extension is correctly installed**, start Premiere, under `Window > Extensions` you should see `Pymiere Link` (clicking on it will do nothing)


  4. Try running some basic code:
```python
import pymiere
print(pymiere.objects.app.isDocumentOpen())
```

## Quick start
Open or create a _Premiere Pro_ project containing a Sequence with at least one video Clip. You can then run or step through [demo.py](https://github.com/qmasingarbe/pymiere/blob/master/demo.py) which demonstrates some basic code. [pymiere/wrappers.py](https://github.com/qmasingarbe/pymiere/blob/master/pymiere/wrappers.py) contains more code examples.

Basically you start by creating a ```project``` object to interact with the opened _Premiere Pro_ application (it needs to be running), after which you can get/set its attributes and call its methods like ```.name``` or ```.save()``` :

    project = pymiere.objects.app.project

For more snippets and examples see [pymiere documentation](https://github.com/qmasingarbe/pymiere/blob/master/example_and_documentation.md).

## Useful links
* [Official doc for Premiere Pro objects](http://ppro.aenhancers.com/)
* [Unofficial doc for Premiere Pro objects](http://www.brysonmichael.com/premiereapi/objects)
* [Advanced Premiere Pro Extendscript usage](https://github.com/Adobe-CEP/Samples/blob/master/PProPanel/jsx/PPRO/Premiere.jsx)

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
 - [ ] add support for Premiere _events_
 - [ ] add a way to simply customize a panel to call python functions

 ## Thanks
 I'd like to thank everybody that contributed to ```Pymiere``` by reporting bugs, imrpoving the documentation, sending ideas etc. but especially:
 - Isaac brown (https://github.com/ikebenbrown)
 - Roy Nieterau (https://github.com/BigRoy)
 - Peter Fison (https://github.com/Pfython)
