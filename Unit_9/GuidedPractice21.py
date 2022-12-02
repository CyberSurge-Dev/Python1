# Zachary Hoover || Guided Practice #21
# 12-01-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #21   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def greetUsers(names):

  for name in names:
    """Print a simple greeting for each element in the provided list."""
    msg = f" Hello, {name.title()}!"
    print(msg)

  return

def greet_users():
  printHeader()
  
  usernames = ["hannah", "ty", "margot"]
  greetUsers(usernames)

  returnMain()

def print_models_1():
  printHeader()

  unprinted_models = ["phone case", "robot pendent", "dodecahedron"]
  completed_models = []

  while unprinted_models:
    current = unprinted_models.pop()
    print(" Currently printing:", current)
    completed_models.append(current)

  print("\n Completed models:")
  for model in completed_models:
    print(" ", model)

  returnMain()

def printModels(incomplete, complete):
  while incomplete:
    current = incomplete.pop()
    print(" Printing", current)
    complete.append(current)
  return

def showCompletedModels(complete):
  print("\n Completed Models:")
  for model in complete:
    print(" ", model)
  return

def print_models_2():
  printHeader()

  unprinted_models = ["phone case", "robot pendent", "dodecahedron"]
  complete_models = []

  printModels(unprinted_models, complete_models)
  showCompletedModels(complete_models)

  returnMain()

def print_models_3():
  printHeader()

  unprinted_models = ["phone case", "robot pendent", "dodecahedron"]
  complete_models = []

  printModels(unprinted_models[:], complete_models)

  print("\n unprinted_models:", unprinted_models)
  showCompletedModels(complete_models)

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
    import GuidedPractice21 as foo
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
      "greetUsers",
      "printModels",
      "showCompletedModels"
    ]

    usable = []
    print("NOTE: Benchmark mode wont work the first time, \nrun it again and it should work fine")
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
