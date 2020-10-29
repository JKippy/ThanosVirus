import os, random
files = len([name for name in os.listdir('.') if os.path.isfile(name)])
names = [name for name in os.listdir('.') if os.path.isfile(name)]

def play_movie(path):
    from os import startfile
    startfile(path)

play_movie("thanosvid.mp4")

half = files/2
while half > 0:
	ran = random.randint(0,files-1)
	if names[ran] != "thanos.py" and names[ran] != "thanosvid.mp4":
		if os.path.exists(names[ran]):
			print "Removing: " + names[ran]
			half = half-1
print "Stopped"
