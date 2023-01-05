# Zachary Hoover || Guided Practice #31
# 01-04-23
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #32   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def importing_whole_library():
  printHeader()

  # Import math module
  import math

  # compute 2 to the power of 3
  print("", math.pow(2, 3))

  # compute 5 to the power of 2
  print("", math.pow(5, 2))

  returnMain()

def importing_and_renaming():
  printHeader()

  import math as ml

  # compute 2 to the power of 3
  print("", ml.pow(2, 3))

  # compute 5 to the power of 2
  print("", ml.pow(5, 2))

  returnMain()

def import_only_pow():
  printHeader()

  # import 'pow' function from math
  from math import pow

  # compute 2 to the power of 3
  print("", pow(2, 3))

  # compute 5 to the power of 2
  print("", pow(5, 2))

  returnMain()

def import_fabs():
  printHeader()

  import math
  x = -5
  print("", math.fabs(x))

  y = 12
  import math as ml
  print("", ml.fabs(y))

  from math import fabs
  print("", fabs(-5))

  returnMain()

def square_root():
  printHeader()

  from math import sqrt

  # Compute square root of 5
  print("", sqrt(5))

  # Compute square root of 30
  print("", sqrt(30))

  returnMain()

def arithmetic_operators():
  printHeader()

  print(" --Division--")
  # Division
  In = 5/2
  Out = 2.5

  print("", In)
  print("", Out)

  print(" --Division--")
  # Division
  In = 5//2
  Out = 2.5

  print("", In)
  print("", Out)

  print(" --Modulo--")
  # Modulo
  In = 5%2
  Out = 1

  print("", In)
  print("", Out)

  print(" --Exponents--")
  # Exponents
  In = 5**2
  Out = 8

  print("", In)
  print("", Out)

  print(" --Exponents--")
  # Exponents
  In = 5**2
  Out = 25

  print("", In)
  print("", Out)

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
    if currentBench > len(usable)-1:
      menuMode = 0
      currentBench = -1
      autoMenu()
    else:
      currentBench += 1
      funcName = usable[currentBench][0]
      usable[currentBench][1]()
      

  if menuMode == 2:
    if currentBench > len(usable)-1:
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
    import GuidedPractice32 as foo
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
if __name__ == "__main__":
  # program start
  autoMenu()
