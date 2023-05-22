"""
Dot Calculator
You have to write a calculator that receives strings for input. The dots will represent the number in the equation. There will be dots on one side, an operator, and dots again after the operator. The dots and the operator will be separated by one space.

Here are the following valid operators :

+ Addition
- Subtraction
* Multiplication
// Integer Division
Your Work (Task)
You'll have to return a string that contains dots, as many the equation returns. If the result is 0, return the empty string. When it comes to subtraction, the first number will always be greater than or equal to the second number.

Examples (Input => Output)
* "..... + ..............." => "...................."
* "..... - ..."             => ".."
* "..... - ."               => "...."
* "..... * ..."             => "..............."
* "..... * .."              => ".........."
* "..... // .."             => ".."
* "..... // ."              => "....."
* ". // .."                 => ""
* ".. - .."                 => ""

"""


def convertResultToDots(result):
    result2 = int(result)
    DotsResult = ""
    if result <= 0:
        return ""
    else:
        for i in range(0, result2):
            DotsResult += "."
    return DotsResult


def calculator(txt):
    result = ""
    c1 = 0
    c2 = 0
    operators = txt.split(" ")
    for char in operators[0]:
        c1 += 1
    for char in operators[2]:
        c2 += 1
    if operators[1] == "-":
        result = c1 - c2
        return convertResultToDots(result)
    if operators[1] == "+":
        result = c1 + c2
        return convertResultToDots(result)
    if operators[1] == "//":
        result = c1 / c2
        return convertResultToDots(result)
    if operators[1] == "*":
        result = c1 * c2
        return convertResultToDots(result)