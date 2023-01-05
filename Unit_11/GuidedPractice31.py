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
  print("\n    Guided Practice #31   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def run_make_pizza():
  printHeader()

  import pizza

  pizza.make_pizza(18, "pepperoni")
  pizza.make_pizza(18, "pepperoni", "mushrooms", "green peppers")

  returnMain()

def run_make_pizza_func_import():
  printHeader()

  from pizza import make_pizza
  
  make_pizza(18, "pepperoni")
  make_pizza(18, "pepperoni", "mushrooms", "green peppers")

  returnMain()

def run_make_pizza_from_alias():
  printHeader()

  from pizza import make_pizza as mp
  
  mp(18, "pepperoni")
  mp(18, "pepperoni", "mushrooms", "green peppers")

  returnMain()

def run_make_pizza_from_module_alias():
  printHeader()

  import pizza as p
  
  p.make_pizza(18, "pepperoni")
  p.make_pizza(18, "pepperoni", "mushrooms", "green peppers")

  returnMain()


# Has to be outside of a function (on the module level)
from pizza import *

def run_make_pizza_func_import():
  printHeader()

  
  
  make_pizza(18, "pepperoni")
  make_pizza(18, "pepperoni", "mushrooms", "green peppers")

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
    import GuidedPractice31 as foo
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
      "make_pizza"
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
