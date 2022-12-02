# Zachary hoover || Independent Practice #12
# 11-03-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system("clear" if os.name == "posix" else "cls")
funcName = ""

def printHeader():
    clear()
    print("\n    Independent Practice #12   ")
    print(" -----------------+-----------------")
    print(f" Function: {funcName}\n")
    
    return


def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()


################################################
# start functions here

# exit loop using if-else
def pizzaToppings_break():
    toppings = []

    while True:
        printHeader()
        print("Current Toppings:")
        for x in toppings:
            print(" ", x)
        print(" What toppings do you want on your pizza?")
        topping = input(" Enter a topping (enter \"quit\" to exit): ")

        if topping != "quit":
            toppings.append(topping)
        else:
            break
        
    returnMain()

# Pizza loop using a simple if conditional
def pizzaToppings_condition():
    toppings = []
    while topping != "quit":
        printHeader()
        print("Current Toppings:")
        for x in toppings:
            print(" ", x)
        print(" What toppings do you want on your pizza?")
        topping = input(" Enter a topping (enter \"quit\" to exit): ")

        if topping != "quit":
            toppings.append(topping)
    returnMain()


# Pizza loop using fags
def pizzaToppings_flag():
    active = True
    toppings = []

    while active:
        printHeader()
        print("Current Toppings:")
        for x in toppings:
            print(" ", x)
        print(" What toppings do you want on your pizza?")
        topping = input(" Enter a topping (enter \"quit\" to exit): ")

        if topping != "quit":
            toppings.append(topping)
        else:
            active = False
 
    returnMain()

def movieTickets_flag():

    underThree = 0
    ThreetoTwelve = 10
    overTwelve = 15

    tickets = []
    active = True

    while active:
        printHeader()
        x = 0
        y = 0
        z = 0
        print(" Current Tickets:")
        for ticket in tickets:
            if ticket == "under3":
                x += 1
            elif ticket == "3to12":
                y += 1
            elif ticket == "over12":
                z += 1
        print(f"  Child Free      x{x} - ${x*underThree}")
        print(f"  3 to 12 tickets x{y} - ${y*ThreetoTwelve}")
        print(f"  Over 12 ticket  x{z} - ${z*overTwelve}")
        print(f"\n Total: ${(x*underThree) + (y*ThreetoTwelve) + (z*overTwelve)}")

        print("""
 Tickets:
  1. Under 3 -- Free
  2. 3 to 12 -- $10
  3. Over 12 -- $15
""")
        usrIn = input(" How old are you? (Enter \"quit\" to exit): ")
        if usrIn != "quit":
            usrIn = int(usrIn)

            if usrIn < 3:
                tickets.append("under3")
            elif usrIn < 13:
                tickets.append("3to12")
            elif usrIn > 12:
                tickets.append("over12")
        else:
            active = False

    returnMain()



def movieTickets_break():

    underThree = 0
    ThreetoTwelve = 10
    overTwelve = 15

    tickets = []

    while True:
        printHeader()
        x = 0
        y = 0
        z = 0
        print(" Current Tickets:")
        for ticket in tickets:
            if ticket == "under3":
                x += 1
            elif ticket == "3to12":
                y += 1
            elif ticket == "over12":
                z += 1
        print(f"  Child Free      x{x} - ${x*underThree}")
        print(f"  3 to 12 tickets x{y} - ${y*ThreetoTwelve}")
        print(f"  Over 12 ticket  x{z} - ${z*overTwelve}")
        print(f"\n Total: ${(x*underThree) + (y*ThreetoTwelve) + (z*overTwelve)}")

        print("""
 Tickets:
  1. Under 3 -- Free
  2. 3 to 12 -- $10
  3. Over 12 -- $15
""")
        usrIn = input(" How old are you? (Enter \"quit\" to exit): ")
        if usrIn != "quit":
            usrIn = int(usrIn)

            if usrIn < 3:
                tickets.append("under3")
            elif usrIn < 13:
                tickets.append("3to12")
            elif usrIn > 12:
                tickets.append("over12")
        else:
            break

    returnMain()

def movieTickets_condition():

    underThree = 0
    ThreetoTwelve = 10
    overTwelve = 15

    tickets = []
    usrIn = ""
    
    while usrIn != "quit":
        printHeader()
        x = 0
        y = 0
        z = 0
        print(" Current Tickets:")
        for ticket in tickets:
            if ticket == "under3":
                x += 1
            elif ticket == "3to12":
                y += 1
            elif ticket == "over12":
                z += 1
        print(f"  Child Free      x{x} - ${x*underThree}")
        print(f"  3 to 12 tickets x{y} - ${y*ThreetoTwelve}")
        print(f"  Over 12 ticket  x{z} - ${z*overTwelve}")
        print(f"\n Total: ${(x*underThree) + (y*ThreetoTwelve) + (z*overTwelve)}")

        print("""
 Tickets:
  1. Under 3 -- Free
  2. 3 to 12 -- $10
  3. Over 12 -- $15
""")
        usrIn = input(" How old are you? (Enter \"quit\" to exit): ")
        if usrIn != "quit":
            usrIn = int(usrIn)

            if usrIn < 3:
                tickets.append("under3")
            elif usrIn < 13:
                tickets.append("3to12")
            elif usrIn > 12:
                tickets.append("over12")

    returnMain()

def zzz_infiniteLoop():
    printHeader()
    x = 1

    while x < 10:
        print(x)
        print("zzz")
    
    

################################################

menuMode = 0
currentBench = 0


def autoMenu():
    global menuMode
    global currentBench
    global usable
    global funcName

    funcName = "autoMenu"
    if menuMode == 1:
        if currentBench > len(usable):
            menuMode = 0
            currentBench = 0
            autoMenu()
        else:
            currentBench += 1
            funcName = usable[currentBench - 1][0]
            usable[currentBench - 1][1]()

    if menuMode == 2:
        if currentBench > len(usable):
            menuMode = 0
            currentBench = 0
            autoMenu()
        else:
            currentBench += 1
            funcName = usable[currentBench - 1][0]
            usable[currentBench - 1][1]()

    else:
        printHeader()

        # change were it says 'baseTemplate' to module name.
        import independentPractice12 as foo
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
                funcName = usable[usrin - 1][0]
                usable[usrin - 1][1]()

        except:
            autoMenu()


# auto menu ends

if __name__ == "__main__": autoMenu();
