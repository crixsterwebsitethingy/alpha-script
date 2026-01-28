import utils
import re
import interpreter

runtime = []
counter = 0
linecount = 0
def findarg(args):
    left_text = args[:len(args)//2].strip()
    right_text = args[len(args)//2:].strip()
def process(src):
    global linecount 
    global counter 

    for line in src.splitlines():
        linecount += 1 
        if not line:
            runtime.insert(counter, {"LINE": linecount, "FUNC": "empty"})
        else:
            runtime.insert(counter, {
                "LINE": linecount, 
                "FUNC": line.split("(", 1)[0], 
                "ARGS": line.strip("asAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz,.()").split(",")
            }) 
        
        counter += 1

    return runtime


