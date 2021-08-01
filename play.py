import time

for i in range(0, 6571):
    f = open("Frames/asciiFrame%d.jpg" % i, "r")
    contents = f.read()
    print(contents)
    time.sleep(0.03333)
