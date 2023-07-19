print("Loading....")
import functions as func
import image as CVimg
import subprocess
from time import sleep
import os


def main():
    print("Compare an image, take a Template image, Sync files from camera or Quit?")
    operation = input("C/T/S/Q ")
    operation = operation.lower()
    if operation == "c":
        name = input("Specify an image name: ")
        imgName = CVimg.takeComparisonImage(name)
        sleep(1)
        print("Select image to compare against ")
        dir = os.listdir("C://Users//Oliver//Downloads//picam//templates")
        print(dir)
        template = input()
        template = "templates/" + template
        image = "images/" + imgName
        CVimg.compare(image, template)
    elif operation == "t":
        CVimg.setTemplateImage()
    elif operation == "s":
        func.syncDir()
    else:
        return


main()

