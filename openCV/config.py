def piStreamAddr():
    res = open("/root/code/cw/picam/openCV/config.txt", "r")
    res = str(res)
    if (res == None):
        print("Config.txt not configured properly! See README.txt for instructions")
        return
    else:
        return res
