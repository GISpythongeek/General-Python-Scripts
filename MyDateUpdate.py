# Script Name: MyDateUpdate.py
# Author: Melanie
# Date Created: 25 August 2015
# Last Modified: 25 August 2015
# Version: 1.0

# Modifications: <none>

"""
Description: This script will update the date at the end of each
filename in a folder (directory) IF the date is given in the following
format: DDmonYYYY (e.g., 01jan2015) and IF the filename has a three character
extension (e.g., ".txt" or ".pdf"). So, "filename-01jan2015.pdf" can become
"filename-24feb2015.pdf". 

I created this script because I regularly have to edit numerous files and update the
date in the filename before I send the files to my colleagues. 

I run this script via the command line on my Mac.
"""

import os

print "Folder path? "  # asks for user to type desired folder path
folder = raw_input()  # sets the 'folder' variable to desired folder path

print "New date? ",  # asks for user to type desired new date
new_date = raw_input()  # sets the 'new_date' variable to desired new date

files = os.listdir(folder)  # sets the 'files' variable to a list of all the
# files in the desired folder 
for filename in files:  # initiates our loop through the files
	file1 = filename[:-13]  # stores all the characters in the filename that
	# come before the date as variable 'file1'
	file3 = filename[-4:]  # stores all the characters in the filename that
	# come after the date as variable 'file3'
	new_name = file1 + new_date + file3  # stores our new, updated filename by
	# concatenating our 'file1' variable with our 'new_date' variable with our
	# 'file3' variable
	os.rename(os.path.join(folder,filename),os.path.join(folder,new_name))  # takes
	# our old filename and replaces it with the new filename

print "*** SCRIPT COMPLETE ***"  # prints a message when the script has finished
