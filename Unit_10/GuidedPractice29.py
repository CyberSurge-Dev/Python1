# Zachary Hoover || Guided Practice #29
# 12-15-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #29   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def list_containment():
  printHeader()

  lst_container = [4, 8, 5, 6]

  x = 5
  if (x in lst_container):
    print(f" {x} is contained in list")
  else:
    print(f" {x} is not contained in list")

  print("")

  x = 10
  if (x in lst_container):
    print(f" {x} is contained in list")
  else:
    print(f" {x} is not contained in list")

  returnMain()

def element_contained_in_list():
  printHeader()

  lst_container = [4, [7, 3], 'string element']

  x = 4
  print(f" {x} is contained in list:", x in lst_container)

  x = 7
  print(f" {x} is contained in list:", x in lst_container)

  x = [7, 3]
  print(f" {x} is contained in list:", x in lst_container)

  returnMain()

def string_containment():
  printHeader()

  sentance = "This is a test sentance"
  w1 = "test"
  w2 = "something"

  if (w1 in sentance):
    print(f" {w1} is in: {sentance}")
  else:
    print(f" {w1} is not in: {sentance}")

  print("")

  if (w2 in sentance):
    print(f" {w2} is in: {sentance}")
  else:
    print(f" {w2} is not in: {sentance}")

  print("")

  if (w2 not in sentance):
    print(f" {w2} is not in: {sentance}")
  else:
    print(f" {w2} is in: {sentance}")

  

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
    import GuidedPractice29 as foo
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
