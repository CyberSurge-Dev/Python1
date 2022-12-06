# Zachary Hoover || Guided Practice #15
# 11-15-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #15   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

# Modifying list
def modifying_list_intro():
  motorcycles = ["honda", "yamaha", "suzuki"]
  printHeader()

  print(" Base list:", motorcycles)

  motorcycles[0] = "ducati"
  print(" Change at index 0:", motorcycles)
  

  returnMain()

# Function for adding items to a list
def adding_to_list():
  printHeader()

  motorcycles = []

  motorcycles.append("honda")
  motorcycles.append("yamaha")
  motorcycles.append("suzuki")

  print(" List:", motorcycles)

  returnMain()

# function using insert on a list
def inserting_into_list():
  printHeader()
  
  motorcycles = ["honda", "yamaha", "suzuki"]
  print(" Base list:", motorcycles)
  
  motorcycles.insert(1, "ducati")
  print(" insert(1, \'ducati\'):", motorcycles)
  
  returnMain()

# Function to delete items from a list
def delete_items():
  printHeader()

  motorcycles = ["honda", "yamaha", "suzuki"]
  print(" Base list:", motorcycles)

  del motorcycles[0]
  print(" del index 0:", motorcycles)

  del motorcycles[1]
  print(" del index 1:", motorcycles)

  returnMain()

# function using pop method (remove last item)
def pop_method():
  printHeader()
  
  motorcycles = ["honda", "yamaha", "suzuki"]
  print(" Base list:", motorcycles, "\n")

  popped_motorcycle = motorcycles.pop()
  print(" Popped list:", motorcycles)
  print(" Popped motorcycle:", popped_motorcycle)

  returnMain()

# Function to print the last motorcycle owned
def last_owned():
  printHeader()
  
  motorcycles = ["honda", "yamaha", "suzuki"]

  last_owned = motorcycles.pop()

  print(f" The last motorcycle owned was {last_owned.title()}")

  returnMain()

def removing_items():
  printHeader()

  motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
  print(" Base list:", motorcycles, "\n")
  
  motorcycles.remove("ducati")
  print(" Remove \'ducati\':", motorcycles)
  
  returnMain()

def remove_items_variable():
  printHeader()
  
  motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
  too_expensive = "ducati"

  print(" Base list:", motorcycles, "\n")

  motorcycles.remove(too_expensive)
  print(" remove too_expensive:", motorcycles)
  

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
    import guidedPractice15 as foo
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
