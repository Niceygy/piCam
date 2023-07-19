from time import sleep
import subprocess
import requests
import wget


def run(cmd):
    runCmd = "bash -c " + cmd
    return subprocess.run(runCmd, shell=True)


def dateTime():
    unixtime = run("date +%s")
    res = str(unixtime)
    return res


def listDir(dir):
    res = run("ls " + dir)
    res = str(res)
    return res


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
            print("Found "+str(n)+" images", end="\r")
    print("Found "+str(n)+" images.")
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
        sleep(0.5)
        imageNames.append(k)
    print("All images validated!")
    x = 0
    for img in imageNames:
        # res = requests.get("http://192.168.1.158:8000/images/"+img)
        x = x + 1
        print("Loading " + img + " onto disk ("+x+"/"+num+")")
        wget.download("http://192.168.1.158:8000/images/" + img, "images/" + img)
        print(" Loaded!")
    print("Complete!")
