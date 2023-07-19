import cv2
from time import sleep
import config as conf
import functions as func
import image as CVimg

camera = cv2.VideoCapture("tcp://192.168.1.158:33") # type: ignore #listen to the tcp video strem from the PI

def takeImage(i):
    return_value, image = camera.read()
    cv2.imwrite('image'+str(i)+'.png', image)
    print("Saved image as " + str(i) + ".png")


def setTemplateImage(file):
    if (file == None):
        name = input("Enter file name for the template: ")
        print("Using current camera feed. Taking image in 3 seconds")
        sleep(1)
        print("2")
        sleep(1)
        print("1")
        takeImage(name)

def compareImages(template, img):
    print("Comparing "+img+" against "+template)
    CVimg.compare(img, template)


takeImage(7)