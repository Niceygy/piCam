from time import sleep
import time
import cv2
import functions.findBoard as FB
import numpy as np
from skimage.metrics import structural_similarity  # type: ignore

timeName = str(time.time())


#############################REPLACE ME!!!!###############################################
camera = cv2.VideoCapture("tcp://192.168.1.158:33")  # type: ignore #listen to the tcp video stream from the PI
print("Connected!")


def compare(template, image, findBoard=False):
    first = cv2.imread(image)
    second = cv2.imread(template)

    # Convert images to grayscale
    first_gray = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
    second_gray = cv2.cvtColor(second, cv2.COLOR_BGR2GRAY)

    # Compute SSIM between two images
    score, diff = structural_similarity(first_gray, second_gray, full=True)
    print("Similarity Score: {:.3f}%".format(score * 100))

    # The diff image contains the actual image differences between the two images
    # and is represented as a floating point data type so we must convert the array
    # to 8-bit unsigned integers in the range [0,255] before we can use it with OpenCV
    diff = (diff * 255).astype("uint8")

    # Threshold the difference image, followed by finding contours to
    # obtain the regions that differ between the two images
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    # Highlight differences
    mask = np.zeros(first.shape, dtype="uint8")
    filled = second.copy()

    logNum = 0
    for c in contours:
        area = cv2.contourArea(c)
        if area > 100:
            x, y, w, h = cv2.boundingRect(c)

            cv2.rectangle(first, (x, y), (x + w, y + h), (0, 115, 115), 5)
            cv2.rectangle(second, (x, y), (x + w, y + h), (0, 115, 115), 5)
            # print(
            #     "W,X,Y,H = " + str(w) + " " + str(x) + " " + str(y) + " " + str(h) + " "
            # )
            cv2.drawContours(mask, [c], 0, (0, 255, 0), -1)
            cv2.drawContours(filled, [c], 0, (0, 255, 0), -1)

    if findBoard != False:
        print("test")
        Warr = []
        Harr = []
        Yarr = []
        Xarr = []
        cv2.imwrite("tmp/" + timeName + ".png", second)  # saves image with date as name
        for i in contours:
            area = cv2.contourArea(i)
            if area > 100:
                x, y, w, h = cv2.boundingRect(i)
                Warr.append(w)
                Harr.append(h)
                Xarr.append(x)
                Yarr.append(y)
        h2, w2 = FB.removeFalseAlerts(Warr, Harr)
        x2, y2 = FB.removeFalseAlerts(Xarr, Yarr)
        print(str(h2) + " " + str(w2))
        imageNumpy = cv2.imread("tmp/" + timeName + ".png")
        cv2.rectangle(second, (x2, y2), (x2 + w2, y2 + h2), (300, 0, 0), 5)
        cv2.imshow("Image comparison - PiCam2", second)
        cv2.waitKey(0)

        # FB.cropImage(int(x), int(h), int(w), int(y), imageNumpy)

    else:
        cv2.imshow("Image comparison - PiCam", second)
        cv2.waitKey()
    return score * 100


def getCompareScore(template, image):
    first = cv2.imread(image)
    second = cv2.imread(template)

    # Convert images to grayscale
    first_gray = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
    second_gray = cv2.cvtColor(second, cv2.COLOR_BGR2GRAY)

    # Compute SSIM between two images
    score, diff = structural_similarity(first_gray, second_gray, full=True)
    # print("Similarity Score: {:.3f}%".format(score * 100))
    return score * 100


def findImageInImage(lookingFor, lookingIn, name):
    img_rgb = cv2.imread(lookingIn)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(lookingFor, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)  # type: ignore

    cv2.imwrite("output/" + name + "-picam.png", img_rgb)
    cv2.imshow("Image comparison - PiCam", img_rgb)
    cv2.waitKey(0)


def takeComparisonImage(name, location="images/"):
    return_value, image = camera.read()
    cv2.imwrite(str(location) + str(name) + ".png", image)
    print("Saved image as " + str(name) + ".png")
    res = "images/" + str(name) + ".png"
    return res


def takeTemplateImage(i):
    return_value, image = camera.read()
    cv2.imwrite("templates/" + str(i) + ".png", image)
    print("Saved image as " + str(i) + ".png")
    res = "image" + str(i) + ".png"
    return res


def setTemplateImage():
    name = input("Enter file name for the template: ")
    print("Using current camera feed. Taking image in 3 seconds", end="\r")
    sleep(1)
    print("Using current camera feed. Taking image in 2 seconds", end="\r")
    sleep(1)
    print("Using current camera feed. Taking image in 1 second ")
    takeTemplateImage(name)
