print("Loading....")
import functions.functions as func
import functions.image as CVimg
import os


def main():
    print("Select operation: ")
    print("C. Compare images ")
    print("T. Take a new Template image ")
    print("S. Sync from the camera ")
    print("F. Find a part in an image or ")
    print("A. Add a new part ")
    operation = input("# ")
    operation = operation.lower()
    if operation == "c":
        name = input("Specify an image name: ")
        image = CVimg.takeComparisonImage(name)
        # sleep(1)
        print("Select image to compare against ")
        dir = os.listdir("C://Users//Oliver//Downloads//picam//templates")
        print(dir)
        template = input()
        template = "templates/" + template
        removeErrs = input(
            "Would you like to try and remove any errors in the image? (Y/N) "
        )
        removeErrs = str(removeErrs).lower()
        if removeErrs == "y":
            print("Removing errors...")
            CVimg.compare(image, template, True)
        else:
            CVimg.compare(image, template)
        main()
    elif operation == "t":
        CVimg.setTemplateImage()
        main()
    elif operation == "s":
        func.syncDir()
        main()
    elif operation == "f":
        print("What board/part would you like to find? ")
        dir = os.listdir("C://Users//Oliver//Downloads//picam//templates")
        print(dir)
        lookingFor = input(" ")
        lookingFor = "C:\\Users\\Oliver\\Downloads\\picam\\templates\\" + lookingFor
        print("Specify an image name: ")
        imageName = input(" ")
        image = CVimg.takeComparisonImage(imageName)  # just taken
        CVimg.findImageInImage(lookingFor, image, imageName)
        main()
    elif operation == "a":
        func.addNewPart()
        main()
    elif operation == "q":
        return
    else:
        print("Invalid option")
        main()


main()
