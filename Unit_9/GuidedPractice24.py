# Zachary Hoover || Guided Practice #24
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
  print("\n    Guided Practice #24   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def tuple_basics():
  printHeader()

  T = (13, 5, 92)
  print(f" {T} is a:", type(T))

  T = [13, 5, 92]
  print(f" {T} is a:", type(T))

  # this is an int because thee is no comma
  T = (5)
  print(f" {T} is a:", type(T))

  # using a comma
  T = (5,)
  print(f" {T} is a:", type(T))

  returnMain()

def creating_tuples():
  printHeader()

  # create homogeneous int tuple
  T_int = (10, -4, 59, 58, 23, 50)
  print(f" {T_int} is a:", type(T_int))

  # create homogeneous string tuple
  T_string = ("word", "letter", "vowel", "spell", "book", "write", "read")
  print(f" {T_string} is a:", type(T_string))

  returnMain()

def heterogeneous_tuples():
  printHeader()

  T = ("Tobias", 23, 25, 25.3,[])
  print(f" {T} is a:", type(T))

  # datetime object can be a tuple element
  from datetime import datetime
  now = datetime.today()

  T = ((1.5, 2.6), "home", now)
  print(f"\n {T} is a:", type(T))
  

  returnMain()

def single_element_tuples():
  printHeader()

  T = ("switch") # not a tuple
  print(f"\n {T} is a:", type(T))

  T = ("switch",) # is a tuple
  print(f"\n {T} is a:", type(T))

  returnMain()

def to_from_tuples():
  printHeader()

  name_list = [
    "Deepthi",
    "Cassandra",
    "Echo",
    "Arllington",
    "Kermit",
    "Trey",
    "Monik",
    "Ayush",
    "Deepya"
    ]

  sorted_list = sorted(name_list)
  names_tuple = tuple(sorted_list)

  print(" name_list type:", type(name_list))
  print(" sorted_list type:", type(sorted_list))
  print(" names_tuple type:", type(names_tuple))

  print("\n first name is: {:s}".format(names_tuple[0]))
  print(" last name is: {:s}".format(names_tuple[-1]))

  returnMain()

def create_tuples_from_input():
  printHeader()

  L = []
  # collect 3 inputs
  for i in range(3):
    tmp = int(input("\n Enter an int {:d}/3: ".format(i+1)))
    L.append(tmp ** 2)

  T = tuple(L)

  print(" Tuple of squares is:", T)

  # print items on new lines
  for i in range(3):
    print(" T[{0:d}] = {1:d}".format(i, T[i]))
    
  returnMain()

def changing_tuple_elements():
  printHeader()

  T = ("Tobias", 23, 25.3, [])

  # does not work
  # T[0] = "hello"

  T[-1].append(44)
  print(" Tuple:", T)
  print(" List:", T[-1])

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
    import GuidedPractice24 as foo
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
