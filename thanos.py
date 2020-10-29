import os, random
files = len([name for name in os.listdir('.') if os.path.isfile(name)])
names = [name for name in os.listdir('.') if os.path.isfile(name)]
half = files/2
while half > 0:
	ran = random.randint(0,files-1)
	if names[ran] != "thanos.py":
		if os.path.exists(names[ran]):
			print "Removing: " + names[ran]
			half = half-1
print "Stopped"
