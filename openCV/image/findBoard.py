from PIL import Image
import cv2


def cropImage(left, top, bottom, right, imgCV):
    """Crops an image
    INPUTS: Left, Top Bottom & Right are the coords for the crop,
    imgPath is the path of the .png for it to crop
    """
    im = imgCV  # Image.open("C:/Users/Oliver/Downloads/picam/" + imgPath)
    im1 = im.crop((left, top, right, bottom))
    cv2.imwrite("tmp2.png", im1)


def removeFalseAlerts(Warr, Harr):  # Width array, Height array
    boardW = 0
    boardH = 0
    for i in Warr:
        if i > 25:
            # valid box probably
            boardW = i
        else:
            print("Removed invalid selection")
    for h in Harr:
        if h > 25:
            # valid box probably
            boardW = h
        else:
            print("Removed invalid selection")
    return [boardH, boardW]
