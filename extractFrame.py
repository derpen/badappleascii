import cv2
from PIL import Image

vidcap = cv2.VideoCapture('BadApple.mkv')
success,image = vidcap.read()

count = 0;
while success:
    success,image = vidcap.read()
    cv2.imwrite("frame%d.jpg" % count, image)

    resizedPic = Image.open("frame%d.jpg" % count)
    resizedPic.thumbnail((50,50))
    resizedPic.save("frame%d.jpg" % count)

    if cv2.waitKey(10) == 27:
        break
    count +=1
