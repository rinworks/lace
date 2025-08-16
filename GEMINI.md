This GEMINI.md file provides context and specific instructions for Gemini CLI when working with Inkscape extensions, with a primary focus on the Python-based inkex package and its internal mechanisms.

# 1. Project Overview & Architecture
• Project Name: Inkscape Extensions Codebase Analysis
• Core Technology: Inkscape extensions are primarily written in Python and leverage the inkex Python package.
• Purpose of Extensions: Extensions extend Inkscape's functionality, adding features, supporting hardware, or enabling different export formats. They are typically executed as scripts by the Python interpreter, receiving arguments and an SVG file from Inkscape, and returning data to update the SVG canvas or save to disk.
• Interaction Model: Extensions primarily juggle with XML. They receive a temporary SVG XML file, modify its XML structure, and then return the modified XML. Higher-level operations like boolean unions or blur adjustments are generally not handled directly by Python extensions.
• Inkscape Subsystems Relevance: While Inkscape has complex C++ subsystems (XML, Object Tree, Display, Tools, Extension, Preferences, UI), the Extension subsystem is the direct interface point for Python extensions.


# 2. Key Internal Workings & Relevant Files

## Location of source files
- Core extension infrastructure code is located under the folder `extensions/inkex/`
- Built-in extensions are python files located directly in the folder `extensions/` (not in subfolders)

## Index of Classes
Please use the file `docs/inkex_classes.md` to find the location of Python classes (which module they are contained in),
*instead* of doing a full scan of all source files. This is important, otherwise you will waste a lot of time searching.

## Key modules, files, classes and methods
Understanding inkex involves looking at its core modules and how they contribute to the extension lifecycle:
• Extension Entry Point and Initialization:
    ◦ The main entry point for a Python extension script for an extension named SomeExtension is typically SomeExtension().run() when run from the terminal.
    ◦ Extensions usually implement a class that inherits from inkex.Effect or other intermediate classes.
    ◦ The run method in the InkscapeExtension class (from inkex.extensions module) is the "Main entrypoint for any Inkscape Extension". It handles argument parsing, loads the input SVG, calls the effect() method, and saves the result.
    ◦ The __init__ methods of superclasses SvgInputMixin and InkscapeExtension are automatically invoked.
        ▪ SvgInputMixin.__init__ (likely in inkex.base or related inkex module) calls add_argument for --id and --selected-nodes.
        ▪ InkscapeExtension.__init__ (from inkex.extensions) initializes file_io, options (a Namespace object), document (an etree object), and arg_parser (an ArgumentParser object). It then calls add_arguments.
    ◦ Relevant Files:
        ▪ inkex.base module (likely contains SvgInputMixin).
        ▪ inkex.extensions module (likely contains InkscapeExtension).
• Argument Parsing:
    ◦ Inkscape passes arguments to the Python interpreter (e.g., ['triangle.py', '--s_a=100', ...]).
    ◦ The argparse Python standard library module is used to turn command-line options into accessible variables (e.g., self.options.s_a).
    ◦ The InkscapeExtension class's parse_arguments method calls self.arg_parser.parse_args(args).
    ◦ Custom extension classes, like Triangle, override the add_arguments method (note the plural) to define their specific command-line parameters (e.g., --s_a, --a_b).
    ◦ The parsed arguments are stored in self.options, which is a Namespace object. Important variables like ids and selected_nodes (passed by Inkscape for selected objects) are found here.
    ◦ Relevant Files: inkex.base (for SvgInputMixin), inkex.extensions (for InkscapeExtension). Python's built-in argparse module.
• XML Document Manipulation (SVG I/O):
    ◦ Extensions work directly with a temporary XML file that Inkscape provides.
    ◦ The inkex module "happens to simply use The ElementTree XML API". You can create nodes using inkex.etree.SubElement(parent, 'tagname').
    ◦ Selected nodes within the SVG are available via self.options.ids. (self.selected is a dictionary and unordered, less reliable for selection order).
    ◦ After modifications, the extension calls self.save_raw(self.effect()) to send the data back to Inkscape.
    ◦ To save the document explicitly (e.g., before running an external inkscape command), use self.document.write(self.svg_file).
    ◦ Relevant Files:
        ▪ inkex.elements package: Contains modules like _base, _parser, _svg, _selected, _groups, etc., which are crucial for manipulating SVG elements programmatically.
        ▪ inkex.colors package: For color manipulation, with submodules for different color spaces (e.g., rgb, hsl, cmyk).
        ▪ inkex.styles module: For managing CSS styles within SVG.
        ▪ inkex.units module: For handling SVG units.
        ▪ inkex.transforms module: For applying transformations (like scaling, rotation, translation) to SVG elements, often involving transformation matrices.
        ▪ inkex.paths package: For programmatic manipulation of SVG path data.
• Testing and Debugging:
    ◦ inkex.tester is a package to facilitate unit testing of extensions. It includes modules for decorators, filters, mock objects, SVG testing, and XML diffing.
    ◦ Do not print to stdout from an extension script, as this causes Inkscape to crash. Only print to stderr (messages appear in a dialogue and suspend execution).
    ◦ Relevant Files: inkex.tester package.
• GUI Elements (Advanced):
    ◦ inkex.gui provides a way to ship GTK interfaces with extensions. This includes modules for applications, list views, pixmaps, and windows.
    ◦ Relevant Files: inkex.gui package.
• Deprecated Modules:
    ◦ Be aware of the inkex.deprecated package, which contains older, deprecated modules like deprecatedeffect and main. Older extensions (before Inkscape 1.0) might use optparse instead of argparse.

# 3. Gemini CLI Interaction Guidelines
• Contextual Understanding: Gemini CLI will automatically read this GEMINI.md file to understand the project's context.
• Decompose Tasks: Break down complex requests into structured, incremental tasks. For example, instead of "Explain Inkscape extensions," ask "Describe the class initialization process for an Inkscape extension, focusing on __init__ methods in SvgInputMixin and InkscapeExtension classes" [previous turn].
• Leverage File Reading and Shell Integration:
    ◦ Use read-file <filename.py> to load specific Python source files into Gemini's context for analysis.
    ◦ If you have a testing setup (e.g., using inkex.tester), you can ask Gemini to run tests using ! <test_command> and then analyze the output for self-correction.
• Focus on Python-specific behavior: Pay attention to how Python's inheritance and method resolution order affect the execution flow within inkex (e.g., the peculiar call sequence of __init__ methods in SvgInputMixin and InkscapeExtension).
• Generate Tests: Use gemini ask "Write pytest tests for this Inkscape extension's effect() method" to generate tests.
• Generate Documentation: Use gemini docs --input src --output docs to create documentation for code segments within the inkex codebase.
• Refactor Incrementally: If proposing refactoring, guide Gemini step-by-step; for example, "Break this long function into smaller pure functions and add comments".

# 4. What Gemini Must Avoid / Key Considerations
• Output to stdout: DO NOT suggest or generate code that prints directly to stdout for debugging or user interaction within Inkscape extensions, as this will crash Inkscape. ONLY use stderr for messages that should appear in a dialogue.
• Selected Nodes: When accessing selected Inkscape objects, prioritize self.options.ids as it provides a reliable list of selected IDs, unlike self.selected which is an unordered dictionary.
• XML Manipulation: Remember that extensions directly manipulate XML. When generating code for SVG modification, focus on using ElementTree-style operations (e.g., inkex.etree.SubElement).
• Global Edits: Avoid broad "rename across the codebase" requests; instead, guide explicitly or ask Gemini to list usages first.
• Architectural Rewrites: Do not expect a single command to re-architect a large system; incremental, step-by-step guidance is necessary for complex changes.
