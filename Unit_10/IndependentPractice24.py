# Zachary Hoover || Independent Practice #24
# 12-07-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Independent Practice #24   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def creating_tuples():
  printHeader()

  # create a tuple of random things
  tup = (5, [4.4, 5.3], "Something is here!", (9, 0))

  # print the tuple
  print(" Tuple:", tup)
  
  returnMain()

def modifying_tuples():
  printHeader()

  T = ([43.6, 34], [49, 59], [50, 34.6], [39, 49])

  # Does not work because you cannot hange tuple values
  # T[2] = [59, 20.4]

  print(" Original tuple:", T)

  # reasign values for the tuple
  T = ([43.6, 34], [49, 59], [59, 20.4], [39, 49])
  print(" New tuple:", T)

  returnMain()

def merging_tuples_opt1():
  printHeader()

  # Create two lists to merge
  L1 = [5, 4, 3]
  L2 = [9, 2, 12]

  # Print lists
  print(" L1:", L1)
  print(" L2:", L2)

  # merge the list by using extend()
  L1.extend(L2)

  print(" Final list:", L1)

  TL = tuple(L1)

  print("\n TL type:", type(TL))
  print(" TL values:", TL)
  

  returnMain()

def merging_tuples_opt2():
  printHeader()

  # create tuples
  T1 = (5, 4, 3)
  T2 = (9, 2, 12)

  print(" Original T1:", T1)
  print(" Original T2:", T2)

  # Convert to list
  T1 = list(T1)
  T2 = list(T2)

  print("\n List T1:", T1)
  print(" List T2:", T2)
  # extend T1 with T2
  T1.extend(T2)
  print(" Final list:", T1)

  # convert back to tuple
  Final = tuple(T1)
  print("\n Final tuple:", Final)
  
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
    import IndependentPractice24 as foo
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
