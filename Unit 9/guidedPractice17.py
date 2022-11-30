# Zachary Hoover || Guided Practice #17
# 11-18-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #17   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def range_loop():
  printHeader()

  # prints 1-5
  for value in range(1,6):
    print("",value)

  returnMain()

def range_list():
  printHeader()

  # creates a list of numbers 1-5
  numbers = list(range(1,6))

  # print the list
  print(" List of nums:", numbers)
  returnMain()

def range_even_numbers():
  printHeader()

  # creates a list of even numbers.
  even_numbers = list(range(2, 11, 2))
  print(" Even numbers:", even_numbers)
  
  returnMain()

def range_squares():
  printHeader()

  squares = []

  for value in range(1,11):
    squares.append(value ** 2)

  print(" Squares 1-10:", squares)

  returnMain()

def min_max_sum():
  printHeader()
  
  digits = [3, 7, 9, 11, 2, 2, 7, 3, 12, 13, 3, 5, 2]

  print(" Sum of list:", sum(digits))
  print(" Max in list:", max(digits))
  print(" Min of list", min(digits))
  

  returnMain()

def list_comprehension():
  printHeader()

  # Creates a list of squares 1-10 
  squares = [value**2 for value in range(1,11)]
  print(" Squares 1-10:", squares)

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
    import guidedPractice17 as foo
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
