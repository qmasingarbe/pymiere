# ![Pymiere logo](logo.png) Pymiere : Python for Premiere Pro
Use Python to interact with Adobe Premiere Pro. Use your favorite libs to process gathered data from your edit and modify it accordingly.

## Why using Pymiere ?
Pymiere comes from an observation that has a Pipeline TD in 3D/VFX studio we add no easy/good way to add Premiere Pro to our workflow.
Of course, if you want to create programmatically a Premiere file the easiest way is to create an XML file (see [Open Timeline IO & XML](https://opentimelineio.readthedocs.io/en/latest/tutorials/adapters.html#final-cut-pro-xml)). But that require exporting and importing files, potentially loosing some data and without quick visual feedback.  
That where Pymiere comes in handy. Want to inform your editor that some shots have new versions available ? Maybe automatically place them on a new track on top ? Want to create tools for your editor using Qt, Shotgun or custom libs ?

## Installation
Works with Python 2.7 & 3.6. Tested with Premiere Pro 13.0 (2019) and Premiere Pro 11.0 (2017). Recommended for version newer than 2017 because some functionality where unavailable at the time

## Documentation
usefull link
* [GitHub](http://github.com)

doc ???

## Lib structure and internal working


## Futur improvements
  * separate the generic part for communication between python and ExtendScript and the specific code for Premiere Pro, enabling it to be use in other application (Photoshop, Encoder...)
  * add more examples & more _wrappers_ functions
  * add support for Premiere events
  * add more documentation, docstrings...
  * building one py file mirror of ExtendScript objects by version, as each Premiere version adds new functions/properties
  * add a way to simply customize a panel to call python functions

## Contact
For any support, questions or interest please contact me : <a href="mailto:q.masingarbe@gmail.com">q.masingarbe@gmail.com</a>

```python
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```