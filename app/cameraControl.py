import getpass #what user
import subprocess #camera only works with leagcy shell commands
from time import sleep
import time
import numpy as np
import cv2
import pyautogui

def user():
    return "oliver"

imageDir = "/home/" + user() + "/picam/images" # e.g: user "test" would have a dir of /home/test/picam/

def run(cmd):
    runCmd = "bash -c " + cmd
    return subprocess.run(runCmd, shell=True)

def dateTime():
    unixtime = run("date +%s")
    res = str(unixtime)
    return res

def takePhoto():
    nowArr = str(time.time())
    nowArr = nowArr.split(".")
    now = nowArr[0]
    fileName = now + ".png"
    file = imageDir + fileName
    file = "'" + file + "'"
    # run("raspistill --focus -o - >> " + file)
    # take screenshot using pyautogui
    image = pyautogui.screenshot()
   
    # since the pyautogui takes as a 
    # PIL(pillow) and in RGB we need to 
    # convert it to numpy array and BGR 
    # so we can write it to the disk
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
   
    # writing it to the disk using opencv
    cv2.imwrite(fileName, image)
    run("mv *.png images/")
    print("Captured image " + fileName + " to /home/" + user() + "/picam/images")

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
        run("./app/cam.sh")

def video(time=10):
    time = int(time)
    time = time * 1000
    dir = "/home/" + user() + "/pivid/"
    fileName = dateTime() + ".h264"
    file = dir + fileName
    cmd = "raspivid  -o - >> " + file
    run(cmd)