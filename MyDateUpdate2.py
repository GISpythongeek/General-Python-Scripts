# Script Name: MyDateUpdate2.py
# Author: Melanie
# Date Created: 26 August 2015
# Last Modified: 26 August 2015
# Version: 2.0

# Modifications: Added the ability to change filenames with extensions of various
# lengths (e.g., '.ai', '.txt', '.docx').

"""
Description: This script will update the date at the end of each
filename in a folder (directory) IF the date is given in the following
format: DDmonYYYY (e.g., 01jan2015) and places immediately before the 
extension, and IF the filename has a 2-, 3-, or 4-character
extension. So, "filename-01jan2015.pdf" can become "filename-24feb2015.pdf". 

I created this script because I regularly have to edit numerous files and update the
date in the filename before I send the files to my colleagues. 

I run this script via my command line on my Mac.
"""

import os

print "Folder path? "  # asks for user to type desired folder path
folder = raw_input()  # sets the 'folder' variable to desired folder path

print "New date? ",  # asks for user to type desired new date
new_date = raw_input()  # sets the 'new_date' variable to desired new date

files = os.listdir(folder)  # sets the 'files' variable to a list of all the
# files in the desired folder 
for filename in files:  # initiates our loop through the files
	if filename[-3] == ".":  # evaluates if the extension is 2-characters long
		file1 = filename[:-12]  # stores all the characters in the filename that
		# come before the date as variable 'file1'
		file3 = filename[-3:]  # stores all the characters in the filename that
		# come after the date as variable 'file3'
		new_name = file1 + new_date + file3  # stores our new, updated filename by
		# concatenating our 'file1' variable with our 'new_date' variable with our
		# 'file3' variable
		os.rename(os.path.join(folder,filename),os.path.join(folder,new_name))  # takes
		# our old filename and replaces it with the new filename
	elif filename[-4] == ".":  # evaluates if the extension is 3-characters long
		file1 = filename[:-13]
		file3 = filename[-4:]
		new_name = file1 + new_date + file3
		os.rename(os.path.join(folder,filename),os.path.join(folder,new_name))
	elif filename[-5] == ".":  # evaluates if the extension is 4-characters long
		file1 = filename[:-14]
		file3 = filename[-5:]
		new_name = file1 + new_date + file3
		os.rename(os.path.join(folder,filename),os.path.join(folder,new_name))
	else:  # prints a notice if the extension is anything other than 2-, 3-, or
	# 4-characters long
		print "ALERT! File %s is a total freak, and I can't work with it!" % filename
	
	
print "*** SCRIPT COMPLETE ***"  # prints a message when the script has finished
