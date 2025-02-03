## Notes about the Inkscape Python Extension ecosystem, python dependencies etc.

- Where are useful tutorials on Inkscape extensions?
  - [Inkscape extensions user docs](https://inkscape-manuals.readthedocs.io/en/latest/extensions.html)
  - https://inkscapetutorial.org/pages/extension.html
  - https://inkscape.gitlab.io/extensions/documentation/tutorial/index.html
  
- Where is the python code for the inkex extension?

  C:\Program Files\Inkscape\share\inkscape\extensions
  
- How is the current inkscape document made available in the extension?

   The inkscape working doc appears to be available as a temporary SVG file to the extension. The extension python library is passed the SVG file name. The load_svg() method loads the file
  into the SvgInputMixin object where it is made available as the *svg* member. This member is of type *ISVGDocumementElement*, which is extended from *etree.ElementBase* from the *lxml* XML library.
- What libraries are used for working with SVG in an an extension?

  First off there are class libraries in inkex: *InkscapeExtension*, and *SvgThroughMixin* (which is just a combination of *SvgInputMixin* and *SvgOutputMixin*).

# Current Explorations
We have picked this extension to explore in detail: Distribute Along Path:
- Generate From Path -> Distribute Along Path (distribute_along_path.py).
- distribute_along_path imports pathmodifier, which seems to contain classes and methods that support these extensions:
    - distrubute_along_path - makes copies of a pattern to following along (on top of) a path
    - patternalongpath.py - bends a pattern to follow a path
    - rubberstretch.py - not clear what this does (there is no help text)
