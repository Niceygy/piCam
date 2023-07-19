import functions as func
import image as CVimg

def main():
    print("Compare an image, take a Template image, Sync files from camera or Quit?")
    operation = input("C/T/S/Q ")
    operation = operation.lower()
    if (operation == "c"):
        name = input("Specify an image name: ")
        imgName = CVimg.takeImage(name)
        print("Select image to compare against ")
        func.listDir("templates")
        template = input()
        CVimg.compare(imgName, template)
    elif (operation == "t"):
        CVimg.setTemplateImage()
    elif (operation == "s"):
        
    else:
        return

main()