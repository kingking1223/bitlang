def evaluate(code: str):
    oneline = "".join(line.strip() for line in code.splitlines())
    array = []
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    lengthState = 0
    token = ""
    string = ""
    arrayLength = ""
    step = 0
    ptr = 0
    gotoState = 0
    gotoNum = ""

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
            else:
                print(f"Unexpected Token Error: {token} is not expected.\nError Code: 11")
        
        elif token == ";":
            if lengthState == 1:
                lengthState = 0
                array = [0] * int(arrayLength)
            if gotoState == 1:
                

        elif token == "g" and oneline[step+1] == "o" and oneline[step+2] == "t" and oneline[step+3] == "o":
            if gotoState == 0:
                gotoState = 1
            elif gotoState == 1:
                gotoState = 0


        token = ""
        step += 1

 
    print(string)

if __name__ == "__main__":
    evaluate("@12;goto")