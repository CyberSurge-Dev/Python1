# Zachary Hoover || Guided Practice #30
# 12-16-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #30   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()

################################################
# start functions here

class noMenu:
  def char_art(steps):
    for row in range(steps):
      for col in range(steps):
        if (col <= row):
          print(" []", end = "")
      print()

    return

  def useless_function():
    pass



def does_nothing():
  printHeader()

  for i in range(10):
    pass

  if (5 < 6):
    pass

  returnMain()

def nested_loops():
  printHeader()

  # list of lists
  table = [[5, 2, 6], [4, 6, 0], [9, 1, 8], [7, 3, 8]]

  for row in table:
    for col in row:
      # print the value col followed by a tab
      print("", col, end = "\t")

    # Print a new line
    print()

  returnMain()

def character_art():
  printHeader()

  noMenu.char_art(6)

  returnMain()

def largest_even_number():
  printHeader()

  lst = [102, 34, 55, 166, 20, 67, 305]

  largest = 0

  for num in lst:
    if ((largest < num) and (num % 2 == 0)):
      largest = num

  print(" Largest even number in the list:", largest)

  returnMain()

def counting_within_ranges():
  printHeader()

  ages = (86, 38, 30, 19, 29, 6, 95, 22, 23, 82, 39, 73, 30, 98, 5, 68, 57, 34, 35, 81, 54, 77, 29,
        75, 83, 14, 88, 7, 8, 32, 93, 76, 42, 1, 32, 70, 70, 3, 34, 52, 44, 41, 7, 77, 73, 97, 34,
        13, 33, 54, 8, 82, 21, 55, 72, 41, 34, 98, 72, 73, 24, 55, 50, 63, 38, 92, 43, 68, 52, 68,
        69, 51, 19, 24, 35, 55, 74, 47, 8, 19, 69, 12, 96, 96, 11, 30, 97, 73, 22, 25, 19, 85, 37,
        68, 39, 76, 73, 18, 45, 42)

  # Initial count
  children = 0
  teens = 0
  young_adults = 0
  adults = 0

  for age in ages:
    if (age <= 12):
      children += 1
    elif ((age >= 13) and (age <= 19)):
      teens += 1
    elif((age >= 20) and (age <= 30)):
      young_adults += 1
    elif (age > 30):
      adults += 1

  print(" Number of children:", children)
  print(" Number of teens:", teens)
  print(" Number of young_adults:", young_adults)
  print(" Number of adults:", adults)

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
    import GuidedPractice30 as foo
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
