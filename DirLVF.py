#! /usr/bin/python3
# vim: set cc=80 tw=79:

"""
Print to file an indented directory structure listing, ready for vim folding.

Looking recursively in the current directory,
print to file a vim modeline, and then entire directory contents,
with filepaths visually compacted, and files listed all in one sentence.

Requires these accompanying vimfiles:
    ftplugin/dirl.vim - for the vim folding
    $vimfiles/syntax/dirl.vim
        - for helpful syntax highlighting of the directory names

Reason for this:
    Handily folded, compact, easily searchable in vim,
    archive list of a directory.

From the root of what you want to list, do something like this:
  In Arch:  [sudo] python3 $onGH/FM-DirLVF/DirLVF.py
  In Windows 10:  py $onGH\FM-DirLVF\DirLVF.py
"""
import datetime
import os
import re
import sys

# Get the datetime:
startd = datetime.datetime.now().isoformat(' ')

# Get the current working directory path
cwdp = os.getcwd()
# and, from that, the current working directory name
cwdn = os.path.split(cwdp)[1].replace(" ", "_")
# get this script's filename without extension
scriptfilename = (os.path.basename(os.path.splitext(sys.argv[0])[0]))
# and prepare the output file from them:
outfile = cwdn + '_' + scriptfilename + '.dirl'
print('When this is done, you should open :\n', outfile)


def rec_ind_dirlist(dirTolist):
    """ Prepare a recursive directory list,
    with subnodes indented one space relative to parent nodes,
    and no paths repeated
    (ie each directory name appears just once, like a header).
    Show a progress count while working."""
    print('Looking at contents of', cwdp, ':')
    dlc = 0
    # Initialise the list just with the base folder path, and date:
    dirList = cwdp+' - scanned '+startd
    for root, folders, files in os.walk(dirTolist, topdown=True):
        folders[:] = [fo for fo in folders if fo not in 'rsnapshot']
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


# file object
fo = open(outfile, 'w', encoding='utf-8')
fo.write(rec_ind_dirlist('.'))
fo.close()
print()
