# Zachary Hoover || Guided Practice #26
# 12-12-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #26   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here


def slicing_and_unpacking_tuples():
  printHeader()

  T = ('name', [2, 4], 5.3, 19)

  print(" T[1:2]:", T[1:2])
  print(" T[:2]:", T[:2])
  print(" T[-3:-1]:", T[-3:-1])
  print(" T[-3:]:", T[-3:])
  print(" T[:]:", T[:])
  
  returnMain()

def slicing_tuples_examples():
  printHeader()

  T = (12, 24, 'name', 'city')

  # Slice the tuple into numerical and textual tuples
  numerical_tuple = T[0:2]
  print(" Numerical tuple:", numerical_tuple)

  textual_tuple = T[-2:]
  print(" Textual tuple:", textual_tuple)

  returnMain()

def unpacking_tuples():
  printHeader()

  (a, b) = (4, 5)

  print(" Var a:", a)
  print(" var b:", b)

  x, y, z = 1, 2, 3

  print(" Var x:", x)
  print(" Var y:", y)
  print(" Var z:", z)

  returnMain()

def Unpacking_tuples_examples():
  printHeader()

  e1 = 5
  e2 = 109

  print(" Before swapping:")
  print(" e1 = {:3d}\t e2 = {:3d}".format(e1, e2))

  e1, e2 = e2, e1

  print(" After swapping:")
  print(" e1 = {:3d}\t e2 = {:3d}".format(e1, e2))

  returnMain()

def splitNames(name):
  """
  Pack the ariables into a tuple, then return the tuple
  """

  names = name.split(" ")
  first_name = names[0].title()
  last_name = names[-1].title()

  return (first_name, last_name)

def split_names():
  printHeader()

  name = input(" Enter your name (f l): ")
  print(" Tuplized name:", splitNames(name))

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
    import GuidedPractice26 as foo
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
      "splitNames"
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
