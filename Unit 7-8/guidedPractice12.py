# Zachary hoover || Guided Practice #12
# 11-02-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system("clear" if os.name == "posix" else "cls")


def printHeader():
    clear()
    print("\n    Guided Practice #12   ")
    print(" --------------+--------------\n")
    return


def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()


################################################
# start functions here

# prints numbers between 1-5
def simple_while_1to5():
    printHeader()

    current_number = 1
    
    print(" Basic count loop")
    while current_number <= 5:
        print("", current_number)
        current_number += 1
    
    returnMain()

# quit while using no if, prints every message including "quit"
def quitWhile():
    printHeader()

    prompt = "\n quit while, no if \n"
    prompt += "\n Tell me something, and I will repeat it back to you. "
    prompt += "\n Enter 'quit' to end the program: "
    message = ""
    
    while message != 'quit':
        message = input(prompt)
        print("", message)

    returnMain()

# quit whie using if-else
def quitWhile_withSimpleIf():
    printHeader()

    prompt = "\n quit while with if != quit \n"
    prompt += "\n Tell me something, and I will repeat it back to you. "
    prompt += "\n Enter 'quit' to end the program: "
    message = ""
    while message != 'quit':
        message = input(prompt)
        if message != 'quit':
            print("", message)

    returnMain()

# uses a flag in a loop
def quitWhile_withFlags():
    printHeader()

    prompt = "\n quit while with flag \n"
    prompt += "\n Tell me something, and I will repeat it back to you. "
    prompt += "\n Enter 'quit' to end the program: "

    active = True
    while active:
        message = input(prompt)

        if message == 'quit':
            active = False
        else:
            print(message)

    returnMain()

# prints message, user enters "quit" to exit the loop
def quitWhile_withBreak():
    printHeader()

    prompt = "\n exit while if-else \n"
    prompt += "\n Please enter the name of a city you have visited. "
    prompt += "\n (Enter 'quit' when you are finished.): "

    while True:
        city = input(prompt)

        if city == 'quit':
            break
        else:
            print(f" I'd love to go to {city.title()}!")
    
    returnMain()

# uses continue key-word to return to begining of loop.
# prints multibles of 2 within a range
def continueWhile_multiplesOf2():
    printHeader()

    print(" Continue while, print multiples of 2")
    current_number = 0
    while current_number < 10:
        current_number += 1
        if current_number % 2 == 0:
            # return to the begining of the loop
            continue

        print("", current_number)

    returnMain()

# counts from 1-5
def count_1to5():
    printHeader()

    print(" count 1 to 5")
    x = 1
    while x <= 5:
        print("", x)
        x += 1
    
    returnMain()

# a basic for loop with a list
def forLoopNames():
    printHeader()

    names = [ 'Rob', 'Mary', 'David', 'Jenny', 'Chris', 'Imogen' ]
    print(" print all names in list")

    for name in names:
        print("", name)

    returnMain()

# displays times table of inputed value
def timesTable():
    printHeader()
    
    times_value = int(input(" Enter a multiplication factor: "))
    print(" prints a times table of inputed number:")

    for count in range(0, 16):
        result = count * times_value
        print("", count, "times", times_value, "equals", result)

    returnMain()

# Function call for getting a formated name
def getFormatedName(firstName, lastName):
    """Return a full name formated correctly"""

    full_name = f"{firstName} {lastName}"

    return full_name.title()

# user input area for getting the users formated name
def get_formated_name():
    printHeader()

    first = ""
    while first != "quit":
        print(" Enter your name (enter \"quit\" to exit)")
        first = input(" Enter your first name: ")
        if first != "quit":
            second = input(" Enter your last name: ")
            print("\n", getFormatedName(first, second), "\n")
        else:
            break

    returnMain()
        
        

# loop runs forever
"""
infinite loop

x = 1
while x < 10:
    print(x)
"""


################################################

menuMode = 0
currentBench = 0

def autoMenu():
    global menuMode
    global currentBench
    global usable

    if menuMode == 1:
        if currentBench > len(usable):
            menuMode = 0
            currentBench = 0
            autoMenu()
        else:
            currentBench += 1
            usable[currentBench - 1][1]()

    if menuMode == 2:
        if currentBench > len(usable):
            menuMode = 0
            currentBench = 0
            autoMenu()
        else:
            currentBench += 1
            usable[currentBench - 1][1]()

    else:
        printHeader()        

        # change were it says 'baseTemplate' to module name.
        import guidedPractice12 as foo
        list = []
        list = getmembers(foo, isfunction)

        i = 0
        x = 0
        exceptions = [
            "autoMenu",
            "printHeader",
            "getmembers",
            "clear",
            "time",
            "isfunction",
            "returnMain",
            "cls",
            "getFormatedName"
        ]

        usable = []

        print(">> ----+ Functions +---- <<")
        while i < len(list):
            if list[i][0] not in exceptions:
                x += 1
                print(f"  {x}. {list[i][0]}")
                usable.append(list[i])
            i += 1

        print("\n>> ----+ Utilities +---- <<")
        print(f"  {x+1}. Exit program")
        print(f"  {x+2}. Benchmark (run all)")
        print(f"  {x+3}. Debug (to be added later)")

        try:
            usrin = int(input("\n Enter number of the item: "))
            if usrin == len(usable) + 1:
                SystemExit()
            elif usrin == len(usable) + 2:
                menuMode = 1
                print("Bench")
                autoMenu()
            elif usrin == len(usable) + 3:
                menuMode = 2
                print("Debug")
                autoMenu()
            else:
                usable[usrin - 1][1]()

        except:
            autoMenu()


# auto menu ends

# program start
autoMenu()
