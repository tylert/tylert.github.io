HDWallet Zipapp
---------------

Do the following::

    # Install all pip requirements for the app in an empty directory
    python -m pip install ${MY_PIP_OPTIONS} --target ${MY_APP_DIRECTORY}

    # Cull a bunch of unnecessary gunk here!!!
    rm -rf ${MY_APP_DIRECTORY}/*dist-info
    find ${MY_APP_DIRECTORY} -name '*.py[coz]' | xargs rm
    find ${MY_APP_DIRECTORY} -name 'test*.py' | xargs rm
    for ((i=0; i<10; i++)); do find ${MY_APP_DIRECTORY} -type d -empty | xargs rm -r; done

    # Do any monkey-patching you want here!!!
    # Prepare your top-level script here!!!
    cp ${MY_PYTHON_SCRIPT} ${MY_APP_DIRECTORY}/__main__.py

    # Bundle everything in the directory into an executable zip file
    python -m zipapp -p '/usr/bin/env python' ${MY_APP_DIRECTORY}

Replace all the "sha3.keccak_256()" calls with just "sha3_256()" in
hdwallet/hdwallet.py and hdwallet/libs/base58.py and all "import sha3" lines
with "from hashlib import sha3_256" (assumes you are on Python 3.6+).  This
removes the redundant, non-pure-Python module.

You'll also have to replace all the "mnemonic/wordlist/\*.txt" files with an
equivalent .py file for each language, import them into the appropriate place
at the top of the mnemonic module and do an "eval(language)" and some split()
magic in its init() to get it to spit out the correct stuff.  This is needed
because I haven't yet figured out a good way to read a file packed inside the
zip file that's currently executing.

* https://docs.python.org/3/library/zipapp.html
* https://stackoverflow.com/questions/5355694/python-can-executable-zip-files-include-data-files
