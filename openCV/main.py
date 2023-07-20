print("Loading....")
import functions as func
import image.image as CVimg
from time import sleep
import os


def main():
    print(
        "Compare an image, take a Template image, Sync files from camera or Find board?"
    )
    operation = input("C/T/S/F ")
    operation = operation.lower()
    if operation == "c":
        name = input("Specify an image name: ")
        image = CVimg.takeComparisonImage(name)
        sleep(1)
        print("Select image to compare against ")
        dir = os.listdir("C://Users//Oliver//Downloads//picam//templates")
        print(dir)
        template = input()
        template = "templates/" + template
        CVimg.compare(image, template)
    elif operation == "t":
        CVimg.setTemplateImage()
    elif operation == "s":
        func.syncDir()
    elif operation == "f":
        print("s")


main()
