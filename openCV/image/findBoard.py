from PIL import Image
import cv2
from time import sleep


def cropImage(left, top, bottom, right, imgCV):
    """Crops an image
    INPUTS: Left, Top Bottom & Right are the coords for the crop,
    imgPath is the path of the .png for it to crop
    """
    im = imgCV  # Image.open("C:/Users/Oliver/Downloads/picam/" + imgPath)
    # im1 = im.crop((left, top, right, bottom))
    croppedImage = im[left : left + top, right : right + bottom]
    cv2.imwrite("tmp2.png", croppedImage)
    cv2.waitKey(0)


def removeFalseAlerts(Warr, Harr):  # Width array, Height array
    boardW = 0
    boardH = 0
    num = 0
    for i in Warr:
        # sleep(0.05)
        if i > 25:
            # valid box probably
            boardW = i
        else:
            num = num + 1
            print("Removed " + str(num) + " invalid selections (W) ", end="\r")
    for h in Harr:
        # sleep(0.05)
        if h > 25:
            # valid box probably
            boardW = h
        else:
            num = num + 1
            print("Removed " + str(num) + " invalid selections (H) ", end="\r")
    print("Removed " + str(num) + " invalid selections total!  ")
    return [boardH, boardW]
