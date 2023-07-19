import subprocess
import requests
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
        req = requests.get("http://192.188.1.158:8000/images")
        req = str(req)
        arr = req.splitlines()
        validImages = []
        for i in arr:
             if ".jpg" in i:
                  validImages.append(i)
        imageNames = []
        for g in validImages:
                    h = g.split("=") 
                    h = h[1] #leaves us with "1689763487.jpg">1689763487.jpg</a></li>
                    j = h.split(">")
                    j = j[1] #leaves us with 1689763487.jpg</a></li>
                    k = j.replace("</a></li>", "")
                    k = str(k) #leaves us with 1689763487.jpg
                    imageNames.append(k)
        for img in imageNames:
              res = requests.get("http://192.188.1.158:8000/images/"+img)
              run("echo "+str(res)+" >> images/"+img) #saves to an image on local disk
