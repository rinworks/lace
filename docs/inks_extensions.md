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
# Getting started with Enlistment and development
To get a a Python development environment that works for testing the Inkscape extensions and your own extension code follow these steps
1. Set up an Ubuntu Linux instance version 24.x with WSL 2. If you have an existing one already you can reuse it. Unless specified otherwise, do the remaining steps in a Ubuntu terminal window (bash or zsh)
1. *Python* - Ubuntu 24.04 comes with Python 3.12 or greater included. Confirm by running `python3 --version`.
1. *Git* - Ubuntu 24.04 includes a recent version of *git* (2.43 or later). Confirm by running `git --version`.
1. *Github* - You should install GitHub CLI if you don't have it using `sudo apt install gh`. This will let you authenticate to GitHub by typing `gh auth login` on the command line. The GitHub CLI auth command will spit out a code. Next go to a browser window where you have GitHub access (such as on Windows) and navigate to github.com/login/device. Enter the code and any other authentication steps that GitHub guides you to do. If successful your `gh auth login` command will exit and report that you have successfully cached credentials.
1. *Clone the code* - 
    ```
    git clone --recurse-submodules https://github.com/rinworks/lace.git
    ```
    Use the correct GitHub https URL. The *extensions* subfolder is a git submodule and should be pulled in automatically.
1. *Install Poetry* - Poetry expects to be installed at the system level (like Python, PIP etc.). Install as follows:
    ```
    sudo apt install pipx
    pipx install poetry
    ```
1. *[Optional] Create or activate your Python Virtual Environment* 
1. *Install Extensions Dependencies* with `poetry install`. This references the *pyproject.toml* file in the extensions directory.  Currently there is an error  from one dependency (*pycairo). Work around was to remove the top level dependency (*pygobject*):
    ```
    poetry remove pygobject
    ```
    If your shell is not already in a Python virtual environment, Poetry will create one. You can enter it with:
    `eval $(poetry env activate)`
1. *Run the tests* with `pytest` from the *extensions* folder
1. Run a specific extension from the command line by changing to the *extensions* folder and running the extension python file as in the example below
    ```
   python distribute_along_path.py --id=g12668 --id=path8143 tests/data/svg/scatter.svg
    ```
    The above example spits the modified svg to standard out by default.



# Current Explorations
We have picked this extension to explore in detail: Distribute Along Path:
- Generate From Path -> Distribute Along Path (distribute_along_path.py).
- distribute_along_path imports pathmodifier, which seems to contain classes and methods that support these extensions:
    - distrubute_along_path - makes copies of a pattern to following along (on top of) a path
    - patternalongpath.py - bends a pattern to follow a path
    - rubberstretch.py - not clear what this does (there is no help text)
