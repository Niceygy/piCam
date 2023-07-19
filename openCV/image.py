import cv2

def compare(img, template):
    # load the input image and template image from disk, then display
    # them on the screen
    print("[INFO] loading images...")

    cv2.imshow("Image", img)
    cv2.imshow("Template", template)

    # convert both the image and template to grayscale
    imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # perform template matching
    print("[INFO] performing template matching...")
    result = cv2.matchTemplate(imageGray, templateGray,
    	cv2.TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

    # determine the starting and ending (x, y)-coordinates of the
    # bounding box
    (startX, startY) = maxLoc
    endX = startX + template.shape[1]
    endY = startY + template.shape[0]

    # draw the bounding box on the image
    cv2.rectangle(img, (startX, startY), (endX, endY), (255, 0, 0), 3)
    # show the output image
    cv2.imshow("Output", img)
    cv2.waitKey(0)

def showDiffrences(img, template):
    from skimage.metrics import structural_similarity
    import numpy as np

    first = cv2.imread('clownfish_1.jpeg')
    second = cv2.imread('clownfish_2.jpeg')

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
            x,y,w,h = cv2.boundingRect(c)


