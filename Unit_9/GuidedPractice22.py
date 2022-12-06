# Zachary Hoover || Guided Practice #22
# 12-05-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #22   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def sort():
  printHeader()

  cars = ["bmw", "audi", "toyota", "subaru"]
  print(" Pre-sorted list:", cars)

  cars.sort()
  print(" Sorted list:", cars)

  returnMain()

def reverse():
  printHeader()

  cars = ["bmw", "audi", "toyota", "subaru"]
  print(" Pre-sorted list:", cars)

  cars.sort(reverse=True)
  print(" Sorted list:", cars)
  

  returnMain()

def temp_sort():
  printHeader()

  cars = ["bmw", "audi", "toyota", "subaru"]
  print(" Original list:", cars)

  print(" Sorted cars:", sorted(cars))
  print(" Original list again:", cars)

  returnMain()

def sorted_func():
  printHeader()

  game_points = [3, 14, 0, 8, 21, 1, 3, 8]
  # set sorted list to a var
  sorted_points = sorted(game_points)

  print(" Game points:", game_points)
  print(" Sorted points:", sorted_points)

  returnMain()

def sorted_func_2():
  printHeader()

  x = [2, 8, 1, 4, 6, 3, 7]

  print(" Sorted list returned:", sorted(x))
  print(" Reverse ssort:", sorted(x, reverse=True))
  print("\n Original list:", x)

  returnMain()

def sorted_string():
  printHeader()

  x = "python"
  print(" Sorted string:", x)

  returnMain()

def reverse_list():
  printHeader()

  cars = ["bmw", "audi", "toyota", "subaru"]
  print(" Cars:", cars)

  cars.reverse()
  print(" Cars reverse:", cars)
  
  returnMain()

def length_of_list():
  printHeader()

  cars = ["bmw", "audi", "toyota", "subaru"]
  print(" Length of cars:", cars)

  returnMain()

def extend_list():
  printHeader()

  example1 = [1, 2, 3]
  print(" Original list:", example1)
  example1.extend([4, 5, 6])
  print(" Extended list:", example1)

  returnMain()

def extend_by_lst():
  printHeader()

  example1 = [1, 2, 3]
  example2 = [4, 5, 6]

  print(" Example 1:", example1)
  print(" Example 2:", example2)

  # extend exampe1
  example1.extend(example2)

  print("\n Extended list:", example1)

  returnMain()
  

################################################

menuMode = 0
currentBench = -1
usable = []


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
    import GuidedPractice22 as foo
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
    print("NOTE: Benchmark mode is still broken on first run,\nrun it again and things should work fine. (i'll fix it eventually)")
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
