# Zachary Hoover || Guided Practice #5
# 10-5-22

import os
from unicodedata import name
clear = lambda: os.system("clear" if os.name == "posix" else "cls")

# prints top header
def printHeader():
    clear()
    print("\n     Guided Practice #5   ")
    print(" ------------+------------\n")
    return

# returns to main menu, with input prompt
def returnMain():
    print("\n Press Enter to continue")
    input()
    main()
# Tests different value types and return there tpe using type()
def typeExample():
    printHeader()
    a = "this is a string"
    b = 10.23
    c = 100

    print(a, " || Type || ", type(a))
    print(b, " || Type || ", type(b))
    print(c, " || Type || ", type(c))
    
    returnMain()

# prints whatever the user inputs
def simpleInput():
    printHeader()
    print(" type something")
    var = input()
    print(var)

    returnMain()

# asks 3 questions, and inputs the result into a string
def varInputExample():
    printHeader()
    
    color = input(" what color is your nose?: ")
    print(" Nose is ", color)

    name = input(" Enter yur name: ")
    print(" Hello ", name)

    num = int(input(" Enter a number: "))
    add = num + 1
    print(" here is your number + 1: ", add)

    returnMain()

# asks for 5 grades, adds them together and gets the average
def gradeExample():
    printHeader()

    print(" Please enter 5 grades")

    grade1 = int( input(" Grade 1: ") )
    grade2 = int( input(" Grade 2: ") )
    grade3 = int( input(" Grade 3: ") )
    grade4 = int( input(" Grade 4: ") )
    grade5 = int( input(" Grade 5: ") )

    totalGrade = grade1 + grade2 + grade3 + grade4 + grade5
    calculated = totalGrade/5

    print("\n Grade total: ", totalGrade)
    print(" Calculated grade(x/5): ", calculated)

    returnMain()

# asks user for name, then formats it
def inputString():
    printHeader()

    message = input(" Type in your name: ")
    print("Hello,", message.upper(), "(upper)")
    print("Hello,", message.title(), "(title)")

    returnMain()

# main function/menu
def main():
    printHeader()

    print("  1. typeExample")
    print("  2. simpleInput")
    print("  3. varInputExample")
    print("  4. gradeExample")
    print("  5. inputString")

    usrIn = input(" \nInput the number of the item: ")

    if usrIn == "1":
        typeExample()
    elif usrIn == "2":
        simpleInput()
    elif usrIn == "3":
        varInputExample()
    elif usrIn == "4":
        gradeExample()
    elif usrIn == "5":
        inputString()

#start of program
#call main
if __name__ == "__main__": main()
