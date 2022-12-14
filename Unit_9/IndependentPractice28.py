# Zachary Hoover || Independent Practice #28
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
  print("\n    Independent Practice #28   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def containing_strings():
  printHeader()

  # create 2 variables with equal values
  e = "Whole Wheat Bread"
  s = "whole wheat bread".title()

  # create an IDENTICAL variable by assigning s to i (making them 'linked')
  i = s

  # print the value of all the variables
  print(" Values:")
  print(" e --", e)
  print(" s --", s)
  print(" i --", i)

  # Print the comparisons of e and s
  print("\n e equals s?:", e == s)
  print(" e identical to s?:", e is s)
  
  # Print the comparisons of s and i
  print("\n s equals i?:", s == i)
  print(" s identical to i?:", s is i)

  # Print the comparisons of e and i
  print("\n e equals i?:", e == i)
  print(" e identical to i?:", e is i)

  returnMain()

def containing_lists():
  printHeader()

  # create 2 list with equal values
  e = [[-1, 2], [3, 4], [-5, 6]]
  x = [[-1, 2], [3, 4], [-5, 6]]

  # create an IDENTICAL list by assigning i equal to s (making them 'linked')
  i = x

  # print the value of all the variables
  print(" Values:")
  print(" e --", e)
  print(" x --", x)
  print(" i --", i)

  # Print the comparisons of e and x
  print("\n e equals x?:", e == x)
  print(" e identical to x?:", e is x)
  
  # Print the comparisons of s and i
  print("\n i equals x?:", i == x)
  print(" i identical to x?:", i is x)

  # Print the comparisons of e and i
  print("\n e equals i?:", e == i)
  print(" e identical to i?:", e is i)

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
    import IndependentPractice28 as foo
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
