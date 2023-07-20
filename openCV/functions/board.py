import functions.image as img

# import functions as func
import os


def findBoard():
    os.listdir("C://Users//Oliver//Downloads/picam//templates")
    board = input("Select board: ")
    name = input("Name this board: ")
    newImg = img.takeComparisonImage(name)
    score = img.getCompareScore(board, newImg)
    if score > 50:
        print("Board found! Proceding")
    else:
        print("Board not found, please try again")
        return


def removeErrors(a, b, c, d):
    if a < 25:
        print("Removed error")
        return
    if b < 25:
        print("Removed error")
        return
    if c < 25:
        print("Removed error")
        return
    if d < 25:
        print("Removed error")
        return
    else:
        return [a, b, c, d]
