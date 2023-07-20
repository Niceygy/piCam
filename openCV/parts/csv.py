import csv

filename = "openCV/parts/parts.csv"

fields = []
rows = []
parts = []


def getNumOfParts():
    with open(filename, "r") as f:
        return len(f.readlines())


def getParts():
    res = []
    with open(filename, "r") as csvfile:
        line = csvfile.read()
        for i in line:
            res.append(i)
    return res


def addPart(partName, imageName):
    with open(filename, "w+") as file:
        file.write(partName + "-" + imageName + "\n")


def listAllParts():
    res = []
    with open(filename, "r") as r:
        line = r.read()
        for i in r:
            res.append(r)
    return res
