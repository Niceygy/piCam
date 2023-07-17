import time
from time import sleep
import datetime
import getpass #what user
import subprocess #camera only works with leagcy shell commands


def user():
    return getpass.getuser()

imageDir = "/home/" + user() + "/picam/" # e.g: user "test" would have a dir of /home/test/picam/

def run(cmd):
    runCmd = "bash -c " + cmd
    subprocess.run(runCmd, shell=True)

def dateTime():
    d = datetime.date(2015,1,5)

    unixtime = time.mktime(d.timetuple())
    res = str(unixtime)
    return res

def takePhoto():
    now = str(dateTime())
    fileName = now + ".jpg"
    file = imageDir + fileName
    file = "'" + file + "'"
    run("raspistill --focus -o - >> " + file)
    print("Captured image " + fileName + " to /home/" + user() + "/picam/")

def photoEverySec(seconds, number):
    if (int(number) / int(number) != 0):
        number = 1000
    i = 0
    while number > i:
        i = i + 1
        takePhoto()
        sleep(int(seconds))


def liveCam(time):
    if (time / time != 0):
        time = 100
    time = time * 1000
    time = str(time)
    run("raspivid --focus -t " + time)

def video(time=10):
    time = int(time)
    time = time * 1000
    dir = "/home/" + user() + "/pivid/"
    fileName = dateTime() + ".h264"
    file = dir + fileName
    cmd = "raspivid  -o - >> " + file
    run(cmd)

def main():
    print("Select operation: ")
    print("1. Live feed")
    print("2. Take image")
    print("3. Take a video of x seconds")
    print("4. Take an image every x seconds")
    print("5. Exit")
    operation = int(input())
    if (operation == 1):
        liveFeedTime = input("How long for? (100S)")
        liveCam(liveFeedTime)
    elif (operation == 2):
        takePhoto()
    elif (operation == 3):
        videoTime = input("How many seconds? ")
        video(int(videoTime))
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