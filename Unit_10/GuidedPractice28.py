# Zachary Hoover || Guided Practice #28
# 12-14-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #28   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def x_Y_equal_identical():
  printHeader()

  x = 5
  y = 5
  print(" x is equal to y?:", x==y)
  print(" x is identical to y?:", x is y)

  x = 5
  y = 6
  print("\n After variable re-assignment:")
  print(" x is equal to y?:", x==y)
  print(" x is identical to y?:", x is y)

  returnMain()
def literals():
  printHeader()

  x = 5.6
  y = 5.6
  print(" x is equal to y?:", x==y)
  print(" x is identical to y?:", x is y)

  x = 5.6
  y = 10.6
  print("\n After variable re-assignment:")
  print(" x is equal to y?:", x==y)
  print(" x is identical to y?:", x is y)

  returnMain()

def equal_not_identical_lists():
  printHeader()

  x = [4, 9, 8]
  y = [4, 9, 8]
  print(" x is equal to y?:", x==y)
  print(" x is identical to y?:", x is y)

  # because they are identical x does not change y
  x[1] = 5
  print("\n After variable re-assignment:")
  print(" x:", x)
  print(" y:", y)
  print(" x is equal to y?:", x==y)
  print(" x is identical to y?:", x is y)

  returnMain()

def equal_and_identical_lists():
  printHeader()

  # variables share same memory location, essentially linked together
  x = [4, 9, 8]
  y = x
  print(" x is equal to y?:", x==y)
  print(" x is identical to y?:", x is y)

  # because they are linked x changes the value for y aswell
  x[1] = 5
  print("\n After variable re-assignment:")
  print(" x:", x)
  print(" y:", y)
  print(" x is equal to y?:", x==y)
  print(" x is identical to y?:", x is y)

  returnMain()

def identity_of_variables_containing_string_literals():
  printHeader()

  # Equal, not identical
  s1 = "whole milk"
  s2 = "whole milk"

  print("\n s1:", s1)
  print(" s2:", s2)
  print(" s1 equals s2?:", s1 == s2)
  print(" s1 identical to s2?:", s1 is s2)
  print(" s1 not identical to s2?:", s1 is not s2)

  # Equal, identical
  s1 = "whole milk"
  s2 = s1

  print("\n s1:", s1)
  print(" s2:", s2)
  print(" s1 equals s2?:", s1 == s2)
  print(" s1 identical to s2?:", s1 is s2)
  print(" s1 not identical to s2?:", s1 is not s2)

  # Equal, not identical
  s1 = "python"
  s2 = "python"

  print("\n s1:", s1)
  print(" s2:", s2)
  print(" s1 equals s2?:", s1 == s2)
  print(" s1 identical to s2?:", s1 is s2)
  print(" s1 not identical to s2?:", s1 is not s2)

  # Equal, not equal, not identical
  s1 = "python"
  s2 = "java"

  print("\n s1:", s1)
  print(" s2:", s2)
  print(" s1 equals s2?:", s1 == s2)
  print(" s1 identical to s2?:", s1 is s2)
  print(" s1 not identical to s2?:", s1 is not s2)

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
    import GuidedPractice28 as foo
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
