# Zachary Hoover || Independent Practice #26
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
  print("\n    Independent Practice #26   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def slicing_tuples():
  printHeader()

  # create a tuple of numbers
  T = (5, 4, 3, 9, 2, 12)

  # slice the tuple T to create T1 and T2
  T1 = T[:3]
  T2 = T[-3:]

  # print out each uple that was created
  print(" T1 -- T[:4]:",  T1)
  print(" T2 -- T[-3:]:",  T2)

  returnMain()

def unpacking_tuples():
  printHeader()

  # Write an expresion to unpack 'T' into:
  # 1) x = 5
  # 2) i = [3, 5.3]
  # 3) s = 'something'
  # 4) t = (9, 0)


  # create tuple
  T = (5, [3, 5.3], "something", (9, 0))

  # unpack tuple into variables
  x, i, s, t = T[0], T[1], T[2], T[3]

  """
  Alternative method:
  x = T[0]
  i = T[1]
  s = T[2]
  t = T[3]
  """
  

  # print variables out
  print(" After unpacking tuple:")
  print(" x:", x)
  print(" i:", i)
  print(" s:", s)
  print(" t:", t)

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
    import IndependentPractice26 as foo
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
    print("NOTE: benchmark mode is still broken, I might re-write the program \nbefore the end of the semester because of numerous weird bugs.")
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
