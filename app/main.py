import ledControl as LEDcontrol
import cameraControl as cameraControl


def startup(): # check if it need to create photo and video dirs
    firstStart = cameraControl.run("cat config.txt")
    if (firstStart != "Version v1.1"):
        cameraControl.run("touch config.txt && echo Version v1.1 >> config.txt")
        cameraControl.run("mkdir /home/$USER/picam && mkdir /home/$USER/pivid")
    else:
        return

def main():
    #startup()
    LEDcontrol.LEDon()
    print("Select operation: ")
    print("1. Live feed")
    print("2. Take image")
    print("3. Take a video of x seconds")
    print("4. Take an image every x seconds")
    print("5. Exit")
    operation = int(input())
    if (operation == 1):
        cameraControl.liveCam()
    elif (operation == 2):
        cameraControl.takePhoto()
    elif (operation == 3):
        videoTime = input("How many seconds? ")
        cameraControl.video(int(videoTime))
    elif (operation == 4):
        secs = input("How many seconds between photos? ")
        num = input("How many photos? ")
        cameraControl.photoEverySec(secs, num)
    elif (operation == 5):
        return
    elif (operation == 6):
        print("Debug mode starting...")
        print("Live feed started for 5 seconds")
        cameraControl.liveCam(5)
        print("Taking photo...")
        cameraControl.takePhoto()
        print("Taking photo every 2 seconds for 10 seconds...")
        cameraControl.photoEverySec(2, 5)
        print("Debug mode finished!")
    else:
        print("Invalid input")
        main()
    
main()