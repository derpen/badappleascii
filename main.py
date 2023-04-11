from extractFrame import extract
from toASCII import convert
from deleteFrames import delete
from deleteFrames import deleteAll
from play import playvideo

if __name__ == '__main__':
    while(True):
        print("Video2ASCII converter (rename ur file in extractFrame.py)")
        print("Select choice")
        print("1. Extract Frames")
        print("2. Convert to ASCII")
        print("3. Play")
        print("4. Delete ASCII Frames")
        print("5. Delete Everything")
        print("6. Exit")
        userInput = input()
        if userInput == "1":
            extract()
            print("Done extracting. Now run convert to ascii")
        elif userInput == "2":
            convert()
            print("Done!")
        elif userInput == "3":
            playvideo()
        elif userInput == "4":
            delete()
        elif userInput == "5":
            deleteAll()
            print("Everything is gone")
        elif userInput == "6":
            print("Bye")
            exit()
        else:
            print("ENTER THE CORRECT NUMBER YOU FOUL!")

