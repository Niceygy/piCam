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
    res = run("ls "+dir)
    res = str(res)
    return res
def syncDir():
        print("Loading URL...")
        req = requests.get("http://192.168.1.158:8000/images")
        #print(str(req.text))
        req = str(req.text)
        print("Recived! Parsing....")
        arr = req.splitlines()
        validImages = []
        for i in arr:
             if ".jpg" in i:
                  validImages.append(i)
                  print("Found image "+i)
        imageNames = []
        num = 0
        totalNum = len(validImages)
        for g in validImages:
                    h = g.split("=") 
                    h = h[1] #leaves us with "1689763487.jpg">1689763487.jpg</a></li>
                    j = h.split(">")
                    j = j[1] #leaves us with 1689763487.jpg</a></li>
                    k = j.replace("</a></li>", "")
                    k = k.replace("</a", "")
                    k = str(k) #leaves us with 1689763487.jpg
                    num = num + 1
                    print("Validated "+str(num)+"/"+str(totalNum), end='\r')
                    imageNames.append(k)
        for img in imageNames:
              #res = requests.get("http://192.168.1.158:8000/images/"+img)
              print("Loading "+img+" onto disk")
              wget.download("http://192.168.1.158:8000/images/"+img, "images/"+img)
              print(" Loaded!")
        print("Complete!")
