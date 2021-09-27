import time
import os

amountOfFrames = len(os.listdir('Frames'))

for i in range(0, amountOfFrames):
    f = open("Frames/asciiFrame%d.txt" % i, "r")
    contents = f.read()
    print(contents)
    time.sleep(0.03333) # Framerate
