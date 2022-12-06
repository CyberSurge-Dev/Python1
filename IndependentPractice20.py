# Zachary Hoover || Independent Practice: #20
# 11-30-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Independent Practice: #20   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def deli():
  printHeader()

  # Create a list of sandwich orders and finished sandwiches
  sandwich_orders = ["ham and cheese", "italian", "baloney", "BLT", "turkey club"]
  finished_sandwiches = []

  # Cycle through sandwich list, print message, add to finished sandwhich
  while sandwich_orders:
    current = sandwich_orders.pop()

    print(f" I made your {current} sandwich")
    finished_sandwiches.append(current)

  # print complete finished sandwiches list
  print("\n Finished Sandwiches:", finished_sandwiches)
  
  returnMain()

def no_pastrami():
  printHeader()

  # Create a list of sandwich orders and alert customers of the lack of pastrami
  sandwich_orders = ["ham and cheese", "pastrami", "italian", "pastrami","baloney", "BLT", "turkey club", "pastrami",]
  print(" The deli has run out of pastrami! \n if your order contains pastrami, it will be removed.")

  i = 0
  # remove all occurances of "pastrami" in the list
  while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
    i += 1

  # Print the remaining items
  print("\n Remaining orders:", sandwich_orders)
  print(f" {i} orders removed.")
  
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
    import IndependentPractice20 as foo
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
