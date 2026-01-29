import math

def exec(data):
    print("--------------Execution Started--------------")
    for value in data:
        result = None
        if value["FUNC"] == "as.add":
            result = float(value['ARGS'][0]) + float(value['ARGS'][1])
            print(value["LINE"], ": ", result)
        elif value["FUNC"] == "as.sub":
            result = float(value['ARGS'][0]) - float(value['ARGS'][1])
            print(value["LINE"], ": ", result)
        elif value["FUNC"] == "as.mul":
            result = float(value['ARGS'][0]) * float(value['ARGS'][1])
            print(value["LINE"], ": ", result)
        elif value["FUNC"] == "as.div":
            result = float(value['ARGS'][0]) / float(value['ARGS'][1])
            print(value["LINE"], ": ", result)
        elif value["FUNC"] == "sqrt":
            result = math.sqrt(float(value['ARGS'][0]))
            print(value["LINE"], ": ", result)
        elif value["FUNC"] == "abs":
            result = abs(float(value['ARGS'][0]))
            print(value["LINE"], ": ", result)
        elif value["FUNC"] == "pow":
            result = pow(int(value['ARGS'][0]), int(value['ARGS'][1]))
            print(value["LINE"], ": ", result)

    print("--------------Execution Ended--------------")

