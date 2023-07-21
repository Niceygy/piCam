from time import sleep
import subprocess
import requests
import wget
import functions.image as image
import parts.csv as csv


def run(cmd):
    runCmd = "bash -c " + cmd
    return subprocess.run(runCmd, shell=True)


def syncDir():
    print("Loading URL...")
    req = requests.get("http://192.168.1.158:8000/images")
    # print(str(req.text))
    req = str(req.text)
    print("Recived! Parsing....")
    arr = req.splitlines()
    validImages = []
    n = 0
    for i in arr:
        if ".jpg" in i:
            validImages.append(i)
            n = n + 1
            print("Found " + str(n) + " images", end="\r")
            sleep(0.1)
    print("Found " + str(n) + " images.")
    imageNames = []
    num = 0
    totalNum = len(validImages)
    for g in validImages:
        h = g.split("=")
        h = h[1]  # leaves us with "1689763487.jpg">1689763487.jpg</a></li>
        j = h.split(">")
        j = j[1]  # leaves us with 1689763487.jpg</a></li>
        k = j.replace("</a></li>", "")
        k = k.replace("</a", "")
        k = str(k)  # leaves us with 1689763487.jpg
        num = num + 1
        print("Validated " + str(num) + "/" + str(totalNum), end="\r")
        sleep(0.1)  # to prevent buffer issues
        imageNames.append(k)
    print("All images validated!")
    x = 0
    for img in imageNames:
        # res = requests.get("http://192.168.1.158:8000/images/"+img)
        x = x + 1
        print("Loading " + img + " onto disk (" + str(x) + "/" + str(num) + ")")
        wget.download("http://192.168.1.158:8000/images/" + img, "images/" + img)
        print(" Loaded!")
    print("Complete!")


def addNewPart():
    name = input("Name the part you want to add: ")
    print(
        "Please put the part under the camera.\n Ideally as clear and large as possible"
    )
    input("Press Enter to continue ")
    imageName = image.takeComparisonImage(name, "templates/")
    csv.addPart(name, imageName)
