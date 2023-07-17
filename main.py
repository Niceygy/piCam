import time
#from picamera import PiCamera #camera
from time import sleep
import datetime
import getpass #what user
import shutil# file moving
import subprocess #camera only works with leagcy shell commands
#import RPI.GPIO as GPIO #GPIO for lights

def user():
    return getpass.getuser()

# camera = PiCamera()
imageDir = "/home/" + user() + "/picam/" # e.g: user "test" would have a dir of /home/test/picam/

def dateTime():
    now = datetime.datetime.now()
    res = str(now)
    return res

def takePhoto():
    fileName = dateTime + ".jpg"
    # camera.capture(fileName)
    subprocess.run("raspistill -o " + fileName, shell=True)
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


def liveCam(time=0):
    time = str(time)
    subprocess.run("raspistill -t " + time, shell=True)


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
        print("Debug mode starting...")
        print("Live feed started for 5 seconds")
        liveCam(5)
        print("Taking photo...")
        takePhoto()
        print("Taking photo every 2 seconds for 10 seconds...")
        photoEverySec(2, 5)
        print("Debug mode finished!")
    else:
        print("Invalid input")
        main()
    
main()