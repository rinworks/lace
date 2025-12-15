# Ongoing notes for this project
(more recent notes first)

# December 15, 2025
- We've been setting up our own clone of lace on github...

# August 13 2025 Plan for exploring transforms...
    - Goal is a short primer on inkex use of transforms with links to sources
    - Start investigation with NotebookLM
        - Add SVG sources to NotebookLM including lxml
        - Request overview of how transforms are represented in SVG
        - Request key classes handling transoforms in inkex
        - Request key ways transforms are being used by inkex and by extensions
        - (probably manually) Compose results into a report

    - Notebooklm added 10 sources for SVG and lxml, which all seem relevant. At this point this is the full list of sources:
        - Developer's Guide to SVG Optimization - Cloudinary
        - API Reference — inkex documentation - GitLab
        - Architectural overview - Inkscape Wiki
        - Best Practices for Using Gemini CLI Effectively in Production Codebases | SPG Blog
        - Chapter 3. How Extensions Work - Inkscape Tutorial
        - Finding and replacing XML/SVG element text by id with Python's lxml? - Stack Overflow
        - Gemini CLI | Gemini for Google Cloud
        - Gemini CLI: A comprehensive guide to understanding, installing, and leveraging this new Local AI Agent - Reddit
        - Gemini Context Window/Memory? : r/GoogleGeminiAI - Reddit
        - How can I modify the attributes of an SVG file from Python? - Stack Overflow
        - How do you properly use SVGs for icons in websites? : r/webdev - Reddit
        - Inkscape Extension Development - Jérôme Belleman - GitLab
        - SVG (with CSS) in Python - Shay Allen Hill
        - SVG: Scalable Vector Graphics - MDN Web Docs
        - The lxml.etree Tutorial
        - Tutorial — inkex documentation - GitLab
        - Validation with lxml
        - Welcome to inkex's documentation! - GitLab
        - Why Developers Should Use SVG Files - Delicious Brains
        - lxml - Processing XML and HTML with Python

    - Asked Gemini CLI to explain inkex use of SVG transforms - saved this under docs/inkex_transforms.md
    - Created some simple primitive svg files (under svgs/primitives) to further explore functionality in the debugger

# August 8, 2025 Creatged package and class diagrams with pyreverse
    - With Gemini CLI's help, I ran pyreverse and generated the following two (large!) SVG files:
        classes_inkex.svg
        packages_inkex.svg
    - I had to install graphviz and pylint (in the context of the VM), and also installed graphviz
        - sudo apt-get install graphviz
        - pip install pylint
    - Then run this command:
         /home/jmjdev/github/lace/docs/.venv/bin/pyreverse -o svg -p inkex /home/jmjdev/github/lace/extensions/inkex

# July 21 2025 Using Gemini CLI
    - Prerequesite for installing Gemini CLI: Install node, following instructions here:
https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl
 (I installed nvm using curl, then node usinv nvm. Node version: v22.17.1. I need at least V20 according to Google docs)
    - Installing Gemini CLI instructions: https://github.com/google-gemini/gemini-cli

