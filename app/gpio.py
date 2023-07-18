#on button press, move light 3 ones to the left (clockwise)
#GPIO List: 
#   Lights: Pin 2 (5v), Pin 18 (Data), Pin 14 (Ground)
#   Buttons: Pin 1 (3v3), Pin {17, 22, 27} (Inputs), Pin 20 (Ground)
from gpiozero import Button
from signal import pause
import ledControl as LEDcontrol

def checkForLightsToggle():
    LTbutton = Button(17)
    LTbutton.when_pressed = LEDcontrol.LEDtoggle()
    pause()


def checkForLightsMove():
    LMbutton = Button(22)
    print("CheckForLightsMove function running...")
    LMbutton.when_pressed = LEDcontrol.rotateLED
    pause()

