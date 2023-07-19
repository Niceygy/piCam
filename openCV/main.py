print("Loading....")
import functions as func
import image as CVimg
import subprocess
from time import sleep


def main():
    print("Compare an image, take a Template image, Sync files from camera or Quit?")
    operation = input("C/T/S/Q ")
    operation = operation.lower()
    if operation == "c":
        name = input("Specify an image name: ")
        imgName = CVimg.takeTemplateImage(name)
        sleep(1)
        subprocess.run("mv " + imgName + ".png templates/")
        print("Select image to compare against ")
        print(subprocess.run("dir C:/users/oliver/Downloads/picam/templates"))
        template = input()
        CVimg.compare(imgName + ".png", template)
    elif operation == "t":
        CVimg.setTemplateImage()
    elif operation == "s":
        func.syncDir()
    else:
        return


main()
