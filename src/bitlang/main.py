def evaluate(code: str):
    oneline = "".join(line.strip() for line in code.splitlines())

    array = []
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    token = ""
    string = ""
    lengthState = 0
    arrayLength = ""
    step = 0
    ptr = 0
    gotoState = 0
    gotoNum = ""
    setState = 0
    setNum = ""

    for Char in oneline:
        token += Char
        if token == " ":
            token = ""
 
        elif token == "\n":
            token = ""
 
        elif token == "@":
            if lengthState == 0:
                lengthState = 1
            elif lengthState == 1:
                print("Unexpected Token Error: @ Token not yet ended but another @ is detected.\nError Code: 10")

        elif token in num:
            if lengthState == 1:
                arrayLength += token
            elif gotoState == 1:
                gotoNum += token
            elif setState == 1:
                setNum += token
            else:
                print(f"Unexpected Token Error: {token} is not expected.\nError Code: 11")
        
        elif token == ";":
            if lengthState == 1:
                lengthState = 0
                array = [0] * int(arrayLength)
            elif gotoState == 1:
                if int(gotoNum) > int(arrayLength):
                    print(f"Index Error: Array has length {arrayLength}, but goto command received {gotoNum}.\nError Code: 20")
                else:
                    gotoState = 0
                    ptr = int(gotoNum)
                    gotoNum = ""
            elif setState == 1:
                setState = 0
                array[ptr] = int(setNum)
                setNum = 0

        elif token == "g" and oneline[step+1] == "o" and oneline[step+2] == "t" and oneline[step+3] == "o":
            if gotoState == 0:
                gotoState = 1

        elif token == "`":
            array[ptr] -= 1

        elif token == "~":
            array[ptr] += 1

        elif token == ".":
            print(array[ptr])

        elif token == "s" and oneline[step+1] == "e" and oneline[step+2] == "t":
            if setState == 0:
                setState = 1

        elif token == "a" and oneline[step+1] == "s" and oneline[step+2] == "k":
            array[ptr] = int(input(""))
        
        elif token == "#":


        token = ""
        step += 1

 
    print(string)

inp = """@ 12;
goto 11;
set 10;
```.
goto 10;
ask
.
"""

if __name__ == "__main__":
    evaluate(inp)