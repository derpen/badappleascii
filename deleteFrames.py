import os

frameNames = os.listdir('Frames')

def delete():
    for files in frameNames:
        if "jpg" in files:
            print(f"deleting {files}")
            os.remove(os.path.join('Frames', files))

def deleteAll():
    for files in frameNames:
        print(f"deleting {files}")
        os.remove(os.path.join('Frames', files))
