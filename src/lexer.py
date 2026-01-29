import utils
import re
import interpreter

runtime = []
counter = 0
linecount = 0
variables = {}
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
        elif "=" in line and "(" not in line:
            name, value = map(str.strip, line.split("=", 1))
            variables[name] = value

            runtime.insert(counter, {
                "LINE": linecount,
                "FUNC": "var_def",
                "NAME": name,
                "VALUE": value
            })

        else:
            if line.split("(", 1)[0] == "print":
                runtime.insert(counter, {
                    "LINE": linecount,
                    "FUNC": "print",
                    "ARGS": line.strip("print()")

                })
            runtime.insert(counter, {
                "LINE": linecount, 
                "FUNC": line.split("(", 1)[0], 
                "ARGS": line.strip("asAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz,.()").split(",")
            }) 
        
        counter += 1
    interpreter.receive(variables)
    return runtime


