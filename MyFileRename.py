# Script Name: MyFileRename.py
# Author: Melanie
# Date Created: 27 August 2015
# Last Modified: 27 August 2015
# Version: 1.0

# Modifications: <none>

""" Description: This script will change the file name (excluding the extension)
for files with 3-character extensions only.  NOTE --> My Mac always creates a
weird file (DSstore -- ???), which puts itself first in the list, and I can't get 
rid of it or prevent it from being created. I am careful, then, to take this into 
account when I set my "n" variable (to the number right before I want my real 
filename numbers to start, such as to "0" when I want to start with "1".)  

Naturally, I created this script because I sometimes have numerous files that 
need to have new filenames labeled in sequential order.  

I run this script via my command line on my Mac.
"""

import os

print "Folder path? "  # asks for user to type desired folder path
folder = raw_input()  # sets the 'folder' variable to desired folder path

print "New base filename? "  # asks user to type desired new base filename
base_file = raw_input()  # sets the 'base_file' variable

files = os.listdir(folder)  # sets the 'files' variable to a list of all the
# files in the desired folder 

n = 0
for filename in files:  # initiates our loop through the files
	ext = filename[-4:]  # stores all of the extension characters in the 
	# filename as variable 'ext'
	new_name = base_file + str(n) + ext  # stores our new, updated filename by
	# concatenating our 'base_file' variable with a string of our 'n' variable
	# with our extension variable "ext"
	os.rename(os.path.join(folder,filename),os.path.join(folder,new_name))  # takes
	# our old filename and replaces it with the new filename
	n += 1  # increments our 'n' variable to set the next number in our sequence

print "*** SCRIPT COMPLETE ***"  # prints a message when the script has finished
