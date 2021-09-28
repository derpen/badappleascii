import cv2
import os
from PIL import Image

def extract():
    vidcap = cv2.VideoCapture('BadApple.mkv') # Change this
    success,image = vidcap.read()

    if not os.path.exists('Frames'):
        os.makedirs('Frames')

    count = 0;
    while success:
        success,image = vidcap.read()
        cv2.imwrite("Frames/frame%d.jpg" % count, image)

        resizedPic = Image.open("Frames/frame%d.jpg" % count)
        resizedPic.thumbnail((75,75)) # Set size
        resizedPic.save("Frames/frame%d.jpg" % count)

        if cv2.waitKey(10) == 27:
            break
        print("Done extracting frame %d" % count)
        count +=1
