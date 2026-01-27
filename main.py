import lexer
import interpreter 

print("--ALPHASCRIPT RUNTIME TERMINAL--")
source = None
while True:
    filePath = input()
    if not filePath:
        print("Could not find file")
    else: 
        break

with open(filePath, "r", encoding="utf-8") as file:
    source = file.read()

lexer.process(source)





