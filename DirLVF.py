#!/usr/bin/python3
# vim: set cc=80 tw=79:

"""
Print to file an indented directory structure listing, ready for vim folding.

Looking recursively in the current directory,
print to file a vim modeline, and then entire directory contents,
with filepaths visually compacted, and files listed all in one sentence.

Requires these accompanying vimfiles:
    ftplugin/dirlist.vim - for the vim folding
    syntax/dirlist.vim
        - for helpful syntax highlighting of the directory names

Reason for this:
    Handily folded, compact, easily searchable in vim,
    archive list of a directory.

In openSUSE, from the root of what you want to list, do something like this:
    python3 ~/Files/IT_stack/DirLVF/DirLVF.py
In Arch:
    python3 /mnt/WD2000JD/Files/IT_stack/DirLVF/DirLVF.py
    python3 /mnt/WD30EZRZ/More/IT_stack/DirLVF/DirLVF.py
"""
import datetime
import os
import re
import sys

# Get the datetime:
startd = datetime.datetime.now().isoformat(' ')

# Get this script's directory path
scriptdirpath = os.getcwd()
# and, from that, this script's directory name
scriptdir = os.path.split(scriptdirpath)[1].replace(" ", "_")
# and this script's filename without extension
scriptfilename = (os.path.basename(os.path.splitext(sys.argv[0])[0]))
# and prepare the output file from them:
outfile = scriptdir + '_' + scriptfilename + '.txt'
print('When this is done, you should open :\n', outfile)


def rec_ind_dirlist(dirTolist):
    """ Prepare a recursive directory list,
    with subnodes indented one space relative to parent nodes,
    and no paths repeated
    (ie each directory name appears just once, like a header).
    Show a progress count while working."""
    print('Looking at contents of', scriptdirpath, ':')
    dlc = 0
    # Initialise the list just with the base folder path, and date:
    dirList = scriptdirpath+' - scanned '+startd
    for root, folders, files in os.walk(dirTolist):
        if root == '.':
            dirList += '\n.'
        else:
            dirList += '\n'+re.sub(r'.*?\\', r'.\\', root)
        fL = '\n'
        fLc = 1
        for file in files:
            # Report a progress count:
            dlc += 1
            print('\r', dlc, end=' ')
            if len(fL)+len(file) < fLc*2801:
                fL += ' · '+file
            else:
                fLc += 1
                fL += '\n · '+file
        dirList += fL
    return dirList

# Create a file object for output:
fo = open(outfile, 'w', encoding='utf-8')
# Write vim modeline and the list to the file object (and close it):
fo.write('vim: set ft=dirlist:\n\n'+rec_ind_dirlist('.'))
fo.close()
print()
