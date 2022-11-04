# Zachary Hoover || Independent Practice: Booleans
# 9-29-22

import os
import random
clear = lambda: os.system("clear" if os.name == "posix" else "cls")

# def setVars():

#    return

# prints top header
def printHeader():
    clear()
    print("\n    Independent Practice: Boolean   ")
    print(" -----------------+-----------------\n")
    return

# returns to main menu, with input prompt
def returnMain():
    print("\n Press Enter to continue")
    input()
    Main()

# uses 6 string test, prints the result
def stringTest():
    printHeader()

    var = "is alpha"
    print(" ", var, " | isalpha? | ", var.isalpha())

    var = "123hello"
    print(" ", var, " | isalnum? | ", var.isalnum())

    var = "This Is A Title"
    print(" ", var, " | istitle? | ", var.istitle())

    var = "123hello"
    print(" ", var, " | isalnum? | ", var.isalnum())

    var = "HELLOWORLD"
    print(" ", var, " | isaupper? | ", var.isupper())

    var = "helloworld"
    print(" ", var, " | isallower? | ", var.islower())

    var = "hello, this is a string"
    print(" ", var, " | starts with 'hello'? | ", var.startswith("hello"))

    returnMain()

def numericTests():
    printHeader()

    var = 5 > 3
    print(" ", "is 5 greater than 3?", var)

    var = 3 < 5
    print(" ", "is 3 less than 5?", var)

    var = (5 == 6)
    print(" ", "is 5 equal to 3?", var)

    var = 9 >= 9
    print(" ", "is 9 greater than or equal to 9?", var)

    returnMain()

def boolTests():
    printHeader()
    
    num1 = random.randint(1, 5)
    num2 = random.randint(1, 5)
    num3 = random.randint(1, 5)
    num4 = random.randint(1, 5)

    var = num1 == num2
    print(" Randomized nubers where used")
    print(" ", f"is {num1} equal to {num2}?", var)

    var = num1 == num2 or num1 > num3
    print(" Randomized nubers where used")
    print(" ", f"is {num1} equal to {num2} or greater than {num3}?", var)

    var = num1 == num2 or num1 < num3
    print(" ", f"is {num1} equal to {num2} or less than {num3}?", var)

    var = num4 > num3
    print(" ", f"is {num4} greater than {num3}?", var)

    returnMain()

# global BenchMode
# BenchMode = False
# global CurrentBench
# CurrentBench = 0

# Main event handler, and main menu
def Main():
    printHeader()
    print(" Input number of item")
    print("   1. stringTests")
    print("   2. numericTests")
    print("   3. boolTests")
    userIn = input()
    if userIn == "1":
        stringTest()
    elif userIn == "2":
        numericTests()
    elif userIn == "3":
            boolTests()
    else:
        Main()

# calls main function
Main()
