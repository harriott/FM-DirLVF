DirLVF
======
A Python script that works recursively through the directory its in,
listing all of the contents into a text file, ready for folded-up Vim viewing.

Can easily handle large numbers of files (my biggest yet is 340,000, generating a 100,000 line file, but nicely folded up and easily searchable in gVim).

requirements
------------
To get the full benefit - folded and syntax highlighted in gVim -
you will need in your installation of gVim:

- [ftplugin/dirlist.vim](https://github.com/harriott/vimfiles/blob/master/ftplugin/dirlist.vim)
- [syntax/dirlist.vim](https://github.com/harriott/vimfiles/blob/master/syntax/dirlist.vim)

related
-------
The unix command `ls -R1` also produces a nicely formatted listing, but it would need post-processing to compact it down, and is less convenient, of course, to access in Windows 7.

