from time import sleep
import cv2
import functions as func

camera = cv2.VideoCapture("tcp://192.168.1.158:33")  # type: ignore #listen to the tcp video strem from the PI
print("Connected!")
import numpy as np
from skimage.metrics import structural_similarity  # type: ignore


def compare(template, image):
    first = cv2.imread(template)
    second = cv2.imread(image)

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
    mask = np.zeros(first.shape, dtype='uint8')
    filled = second.copy()

    for c in contours:
        area = cv2.contourArea(c)
        if area > 100:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(first, (x, y), (x + w, y + h), (36,255,12), 2)
            cv2.rectangle(second, (x, y), (x + w, y + h), (36, 255, 12), 2)
            cv2.drawContours(mask, [c], 0, (0,255,0), -1)
            cv2.drawContours(filled, [c], 0, (0,255,0), -1)
    cv2.imshow("Image comparison - PiCam", second)
    cv2.waitKey()    
    sleep(10)


def takeComparisonImage(i):
    return_value, image = camera.read()
    cv2.imwrite("images/"+str(i) + ".png", image)
    print("Saved image as " + str(i) + ".png")
    res = "images/" + str(i) + ".png"
    return res

def takeTemplateImage(i):
    return_value, image = camera.read()
    cv2.imwrite("templates/"+str(i) + ".png", image)
    print("Saved image as " + str(i) + ".png")
    res = "image" + str(i) + ".png"
    return res

def setTemplateImage():
    name = input("Enter file name for the template: ")
    print("Using current camera feed. Taking image in 3 seconds")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    takeTemplateImage(name)
