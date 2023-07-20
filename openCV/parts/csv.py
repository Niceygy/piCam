import csv

filename = "openCV/parts/parts.csv"

fields = []
rows = []
parts = []


def getNumOfParts():
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        i = 0
        for row in csvreader:
            i = i + 1
            row = str(row)
            row.split(",")
            parts.append(row[0] + "-" + row[1])  # adds partname-partImage to array
    return i


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
