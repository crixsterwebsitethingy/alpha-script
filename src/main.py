import lexer
import interpreter 
import os

print("--ALPHASCRIPT RUNTIME TERMINAL--")
source = None
while True:
    print("Input file path (full):")
    filePath = input()
    if not filePath:
        print("Could not find file")
    else: 
        break

with open(filePath, "r", encoding="utf-8") as file:
    source = file.read()

two = lexer.process(source)
interpreter.exec(two)




