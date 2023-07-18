import ledControl as LEDcontrol
import cameraControl as cameraControl
import sys
import gpio as IO

argOne = sys.argv[1]


def startup():  # check if it need to create photo and video dirs
    firstStart = cameraControl.run("cat config.txt")
    if firstStart != "Version v1.1":
        cameraControl.run("touch config.txt && echo Version v1.1 >> config.txt")
        cameraControl.run("mkdir /home/$USER/picam && mkdir /home/$USER/pivid")
    else:
        return


def main():
    # startup()
    LEDcontrol.LEDon()

    operation = int(argOne)
    if operation == 1:
        print("Starting LED  manager...")
        IO.handleButtons()



main()
