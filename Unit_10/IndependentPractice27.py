# Zachary Hoover || Independent Practice #27
# 12-13-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
    clear()
    print("\n    Independent Practice #27   ")
    print(" -----------------+-----------------")
    print(f" Function: {funcName} \n")
    return


def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()


################################################
# start functions here

def average():
    printHeader()

    # create a tuple of integers
    T = (23, 45, 93, 59, 35, 58, 19, 3)

    # create variable to store total in and loop through and add values of T to the total
    total = 0
    for num in T:
        total += num

    # divide the total by the len of the list (to get the average)
    avg = total / len(T)

    # print out without decimal, using string formating
    print(" Averaged of T: {:.0f}".format(avg))
    print(" Average without formating: {}".format(avg))

    returnMain()


def maximum():
    printHeader()

    # create a tuple of integers
    T = (23, 45, 93, 59, 35, 58, 19, 3)

    # store max value in a valriable
    maxValue = max(T)

    # print value
    print(" Max value of tuple:", maxValue)

    returnMain()


def user_input():
    printHeader()

    # create a tuple of integers
    T = (23, 45, 93, 59, 35, 58, 19, 3)

    # loop through until user guesses a number in the tuple
    active = True
    while (active):
        print(" Guess a number in the tuple to exit.")

        # Gets user input and stores it in a variable
        num = int(input(" Please enter a number: "))

        # check if the variable is in the tuple
        if (num in T):
            # Set active to false, terminating the loop
            active = False

    print(" You guessed the correct number!")

    returnMain()


################################################

menuMode = 0
currentBench = -1


def autoMenu():
    global menuMode
    global currentBench
    global usable
    global funcName

    funcName = "autoMenu"

    if menuMode == 1:
        if currentBench > len(usable) - 1:
            menuMode = 0
            currentBench = -1
            autoMenu()
        else:
            currentBench += 1
            funcName = usable[currentBench][0]
            usable[currentBench][1]()

    if menuMode == 2:
        if currentBench > len(usable) - 1:
            menuMode = 0
            currentBench = -1
            autoMenu()
        else:
            currentBench += 1
            funcName = usable[currentBench][0]
            usable[currentBench][1]()


    else:
        printHeader()

        # change were it says 'baseTemplate' to module name.
        import IndependentPractice27 as foo
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
        print(f"  {x + 1}. Exit program")
        print(f"  {x + 2}. Benchmark (run all)")
        print(f"  {x + 3}. Debug (to be added later)")

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
                funcName = usable[usrin - 1][0]
                usable[usrin - 1][1]()

        except:
            autoMenu()


# auto menu ends
if __name__ == "__main__":
    # program start
    autoMenu()
