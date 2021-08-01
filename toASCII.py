import cv2
import sys

for count in range(0, 6571):

    def setupAsciiMapping():
        characterSet = list(('W'*18)+'!!!!!!!!')
        for i in range(26):
            for j in range(10):
                asciiToNum[i*10+j]=characterSet[i]

    asciiToNum = {}
    setupAsciiMapping()
    transformedAscii = []

    img = cv2.imread("frame%d.jpg" % count , 0) # default image size is 360x480

    for i in img:
        temp = []
        for j in i:
            temp.append(asciiToNum[j])
        transformedAscii.append(temp)
    ascii = ''
    for i in transformedAscii:
        ascii+= ' '.join(i)
        ascii+='\n'

    with open('asciiFrame%d.jpg' % count, 'w') as f:
        sys.stdout = f
        print(ascii)



