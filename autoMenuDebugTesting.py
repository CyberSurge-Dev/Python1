# Zachary Hoover || Auto Menu Test Program
# 11-17-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Auto Menu Test Program   ")
  print(" ----------------+----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def func1():
  printHeader()

  print("Func1")

  returnMain()

def func2():
  printHeader()

  print("Func2")

  returnMain()

def func3():
  printHeader()

  print("Func3")

  returnMain()
################################################

menuMode = 0
currentBench = -1
debugMode = 0
usable = []


def autoMenu():
  global menuMode
  global currentBench
  global usable
  global funcName
  global debugMode

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
    if debugMode == 1:
      debugMode = 0
      printHeader()
      
      returnMain()
    elif debugMode == 2:
      debugMode = 0
      printHeader()

      returnMain()
    else:
      printHeader()
      print(">> ----+ Debug Menu +---- <<")
      print("  1. List errors")
      print("  2. Input params")
      print("  3. Return to menu")

      usrin = int(input("\n Enter number of the item: "))
      if usrin == 1:
        debugMode = 1
        autoMenu()
      elif usrin == 2:
        debugMode = 2
        autoMenu()
      elif usrin == 3:
        menuMode = 0
        autoMenu()
      
      

  else:
    printHeader()

    # change were it says 'baseTemplate' to module name.
    import autoMenuDebugTesting as foo
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

# program start
autoMenu()
