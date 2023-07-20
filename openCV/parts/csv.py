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
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            row = str(row)
            row.split(",")
            parts.append(row[0] + "-" + row[1])  # adds partname-partImage to array
    return parts


def addPart(partName, imageName):
    dataToFile = [str(partName), str(imageName)]
    with open(filename, "w") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(dataToFile)
