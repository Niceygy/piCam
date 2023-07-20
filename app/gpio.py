# on button press, move light 3 ones to the left (clockwise)
# GPIO List:
#   Lights: Pin 2 (5v), Pin 18 (Data), Pin 14 (Ground)
#   Buttons: Pin 1 (3v3), Pin {17, 22, 27} (Inputs), Pin 20 (Ground)
from gpiozero import Button  # type: ignore
from signal import pause
import ledControl as LEDcontrol
import cameraControl as CameraControl

# def checkForLightsToggle():
#     LTbutton = Button(17)
#     LTbutton.when_pressed = LEDcontrol.LEDtoggle
#     pause()


# def checkForLightsMove():
#     LMbutton = Button(22)
#     print("CheckForLightsMove function running...")
#     LMbutton.when_pressed = LEDcontrol.rotateLED
#     pause()


def handleButtons():
    LMbutton = Button(22)  # Light Move
    LTbutton = Button(17)  # Light toggle
    TPbutton = Button(27)  # Take Photo
    print("Button handler running")

    LMbutton.when_pressed = LEDcontrol.rotateLED
    LTbutton.when_pressed = LEDcontrol.LEDtoggle
    TPbutton.when_pressed = CameraControl.takePhoto

    pause()
