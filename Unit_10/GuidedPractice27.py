# Zachary Hoover || Guided Practice #27
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
    print("\n    Guided Practice #27   ")
    print(" --------------+--------------")
    print(f" Function: {funcName} \n")
    return


def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()


################################################
# start functions here
def containment():
    printHeader()

    T = (4, [5, 6], 'name', 3.5, True)

    print(" 4 contained in T?:", 4 in T)
    print(" 5 not contained in T?:", 5 not in T)
    print(" False contained in T?:", False in T)

    returnMain()

def equivlent_tuples():
    printHeader()

    # Equivlent tuples, not identical
    T1 = (10, [2, 4], 59)
    T2 = (10, [2, 4], 59)

    if (T1 == T2):
        print(" Equal tuples")
    else:
        print(" Tuples are not equal")

    if (T1 is T2):
        print(" Tuples are identical")
    else:
        print(" Tuples are not identical")

    returnMain()

def identical_tuples():
    printHeader()

    # Identical tuples (also equivalent)
    T1 = (10, [2, 4], 59)
    T2 = T1

    if (T1 == T2):
        print(" Equal tuples")
    else:
        print(" Tuples are not equal")

    if (T1 is T2):
        print(" Tuples are identical")
    else:
        print(" Tuples are not identical")

    returnMain()

def tuple_changes():
    printHeader()

    # Changing one of 2 identical tuples
    T1 = (10, [2, 4], 59)
    T2 = T1

    # A change in T1 is changed in T2
    T1[1][0] = 20

    print(" T1:", T1)
    print(" T2:", T2)

    returnMain()

def tuple_concatenation():
    printHeader()

    T1 = ("First", "Last")
    T2 = ("Middle",) # Single element tuple

    T = T1 + T2

    print(" Added tuples:", T)

    T1 = (10, [2, 4], 59)
    T2 = (59, [2, 4], 'name', 3.5, True)

    # Concatenating sliced tuples
    T = T1[1:] + T2[0:2]
    print("\n New added tuple:", T)

    returnMain()

def length_of_tuple():
    printHeader()

    T1 = (10, [2, 4], 59)
    print(" Length of T1:", T1)

    T1 = (10, [2, 4], 59)
    for i in range(len(T1)):
        print(" T1[{:d}] = {}".format(i, T1[i]))

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
        import GuidedPractice27 as foo
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
