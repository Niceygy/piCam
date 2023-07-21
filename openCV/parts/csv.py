filename = (
    "openCV/parts/parts.txt"  # using % instead of "," because python doeesnt like it
)

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
    with open(filename, "a") as file:
        file.write(partName + "%" + imageName + "\n")
    return


def listAllParts():
    res = []
    with open(filename, "r") as r:
        line = r.read()
        for i in line:
            res.append(i)
    return res


def test():
    name = input()
    addPart(name, name + "-img.png")


# test()
