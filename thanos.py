#!/usr/bin/python
import os, random

files = len([name for name in os.listdir('.') if os.path.isfile(name)])
names = [name for name in os.listdir('.') if os.path.isfile(name)]

half = files/2
while half > 0:
	ran = random.randint(0,files-1)
	if names[ran] != "thanos.py" and names[ran] != "thanosvid.mp4":
		if os.path.exists(names[ran]):
			print "Removing: " + names[ran]
			os.remove(names[ran])
			half = half-1
print "Stopped"
