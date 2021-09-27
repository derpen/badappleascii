import os

frameNames = os.listdir('Frames')

for files in frameNames:
    if "jpg" in files:
        print(f"deleting {files}")
        os.remove(os.path.join('Frames', files))
