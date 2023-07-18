import board
import neopixel 

pixels = neopixel.NeoPixel(board.D18, 16) # assign GPIO 18 for 16 LEDs
LEDcount = range(15) # 0 through 15

def LEDon():
    for i in LEDcount:
        pixels[i] = (255, 2, 1)
        i = i + 1

def LEDoff():
    for i in LEDcount:
        pixels[i] = (0, 0, 0)
        i = i + 1
LEDoff() #if you run this file manually, it will turn off the LED
#it wont normall be run, just imported from