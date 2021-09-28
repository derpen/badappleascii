import time
import os

def playvideo():
    amountOfFrames = len(os.listdir('Frames'))

    if amountOfFrames == 0:
        print("No Frames to play")
        exit()

    framerate = 1.0/30

    for i in range(0, amountOfFrames):
        f = open("Frames/asciiFrame%d.txt" % i, "r")
        contents = f.read()
        print(contents)
        time.sleep(framerate) 
