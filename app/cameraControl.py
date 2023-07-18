import getpass #what user
import subprocess #camera only works with leagcy shell commands
from time import sleep, time
import datetime

def user():
    return getpass.getuser()

imageDir = "/home/" + user() + "/picam/" # e.g: user "test" would have a dir of /home/test/picam/

def run(cmd):
    runCmd = "bash -c " + cmd
    return subprocess.run(runCmd, shell=True)

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

def liveCam():
        print("raspivid --focus -t 0")
        run("raspivid --focus -t 0")

def video(time=10):
    time = int(time)
    time = time * 1000
    dir = "/home/" + user() + "/pivid/"
    fileName = dateTime() + ".h264"
    file = dir + fileName
    cmd = "raspivid  -o - >> " + file
    run(cmd)