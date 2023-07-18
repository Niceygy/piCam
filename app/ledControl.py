import board
import neopixel 

pixels = neopixel.NeoPixel(board.D18, 16) # assign GPIO 18 for 16 LEDs
LEDcount = range(15) # 0 through 15
global LEDrotate
LEDrotate = 0
global LEDtoggleStatus
LEDtoggleStatus = 0

def LEDon():
    for i in LEDcount:
        pixels[i] = (255, 100, 1)
        i = i + 1

def LEDoff():
    for i in LEDcount:
        pixels[i] = (0, 0, 0)
        i = i + 1

def LEDtoggle():
    print("Toggling LED")
    global LEDtoggleStatus
    if (LEDtoggleStatus == 0):
        LEDoff()
        LEDtoggleStatus = LEDtoggleStatus + 1
    else:
        LEDon()
        LEDtoggleStatus =  LEDtoggleStatus - 1

def rotateLED():
    LEDrotateInt = LEDrotate + 3
    litLED1 = LEDrotateInt #8
    litLED2 = LEDrotateInt - 1 #7
    litLED3 = LEDrotateInt - 2 #6
    for i in LEDcount:
        if i == litLED1:
            pixels[i] = (255, 100, 1)
        elif i == litLED2:
            pixels[i] = (255, 100, 1)
        elif i == litLED3:
            pixels[i] = (255, 100, 1)
        

                
LEDoff() #if you run this file manually, it will turn off the LED
#it wont normally be run, just imported from