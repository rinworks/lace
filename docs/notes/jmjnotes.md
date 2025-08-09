# Ongoing notes for this project
(more recent notes first)

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
