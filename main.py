import time
from picamera import PiCamera #camera
from time import sleep
import datetime
import getpass #what user
import shutil# file moving
from threading import Thread # 2 things at once

def user():
    return getpass.getuser()

camera = PiCamera()
imageDir = "/home/" + user() + "/picam/" # e.g: user "test" would have a dir of /home/test/picam/

def dateTime():
    now = datetime.datetime.now()
    res = str(now)
    return res

def takePhoto():
    fileName = dateTime + ".jpg"
    camera.capture(fileName)
    shutil.move(fileName, imageDir)
    print("Captured image " + fileName + " to /home/" + user() + "/picam/")

def photoEverySec(seconds, number):
    if (int(number) / int(number) != 0):
        number = 1000
    i = 0
    while number > i:
        i = i + 1
        takePhoto()
        sleep(int(seconds))


def liveCam():
    camera.start_preveiw

def test():
    from picamera2 import Picamera2, Preview

    picam = Picamera2()

    config = picam.create_preview_configuration()
    picam.configure(config)

    picam.start_preview(Preview.QTGL)

    picam.start()
    time.sleep(2)
    picam.capture_file("test-python.jpg")

    picam.close()

def main():
    print("Select operation: ")
    print("1. Live feed")
    print("2. Take image")
    print("3. Live feed and take an image every x seconds")
    print("4. Take an image every x seconds")
    print("5. Exit")
    operation = int(input())
    if (operation == 1):
        liveCam()
    elif (operation == 2):
        takePhoto()
    elif (operation == 3):
        secs1 = input("How many seconds between photos? ")
        num1 = input("How many photos? ")
        print("Not yet finished, sorry!")

    elif (operation == 4):
        secs = input("How many seconds between photos? ")
        num = input("How many photos? ")
        photoEverySec(secs, num)
    elif (operation == 5):
        return
    elif (operation == 6):
        test()
    else:
        print("Invalid input")
        main()
    
main()