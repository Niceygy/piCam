import subprocess

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