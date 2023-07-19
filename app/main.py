import ledControl as LEDcontrol
import cameraControl as cameraControl
import sys
import gpio as IO

argOne = sys.argv[1]


def main():
    LEDcontrol.LEDon()

    operation = int(argOne)
    if operation == 1:
        print("Starting LED  manager...")
        IO.handleButtons()
    elif operation == 2:
        while True:
            cameraControl.run("raspivid -l -o tcp://0.0.0.0:33 -t 1000000")

main()