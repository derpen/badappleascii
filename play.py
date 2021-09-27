import time
import os

amountOfFrames = len(os.listdir('Frames'))

framerate = 1.0/30

for i in range(0, amountOfFrames):
    f = open("Frames/asciiFrame%d.txt" % i, "r")
    contents = f.read()
    print(contents)
    time.sleep(framerate) 
