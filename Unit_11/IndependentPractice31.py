# Zachary Hoover || Independent Practice #31
# 01-04-23
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Independent Practice #31   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def printing_models():
  printHeader()

  # Import module 'printing functions'
  import printing_functions as pf

  # declare varibles
  unprinted_designs = ["Phone case", "robot pendant", "dodecahedron"]
  completed_models = []

  # 'print' the models and then print what models were 'printed'
  pf.print_models(unprinted_designs, completed_models)
  pf.show_completed_models(completed_models)

  returnMain()

def import_mn():
  printHeader()

  # Import the module/function to be used
  import imported_funcs

  # Create data for the function (md list for colums and rows)
  data = [
      ["col 1", "col 2", "col 3"],
      ["1", "2", "3"],
      ["1^2", "2^2", "3^2"],
      ["1^3", "2^3", "3^3"],
      ["1^4", "2^4", "3^4"],
      ["1^5", "2^5", "3^5"]
    ]

  # pass the data into the imported function (func prints result)
  # display_data(table_name, table)
  imported_funcs.display_data("Powers", data)

  returnMain()


def from_mn_import_fn():
  printHeader()

  # Import the module/function to be used
  from imported_funcs import display_data

  # Create data for the function (md list for colums and rows)
  data = [
      ["col 1", "col 2", "col 3"],
      ["1", "2", "3"],
      ["1^2", "2^2", "3^2"],
      ["1^3", "2^3", "3^3"],
      ["1^4", "2^4", "3^4"],
      ["1^5", "2^5", "3^5"]
    ]

  # pass the data into the imported function (func prints result)
  # display_data(table_name, table)
  display_data("Powers", data)

  returnMain()


def from_mn_import_fn_as_fn():
  printHeader()

  # Import the module/function to be used
  from imported_funcs import display_data as dd

  # Create data for the function (md list for colums and rows)
  data = [
      ["col 1", "col 2", "col 3"],
      ["1", "2", "3"],
      ["1^2", "2^2", "3^2"],
      ["1^3", "2^3", "3^3"],
      ["1^4", "2^4", "3^4"],
      ["1^5", "2^5", "3^5"]
    ]

  # pass the data into the imported function (func prints result)
  # display_data(table_name, table)
  dd("Powers", data)

  returnMain()

def import_mn_as_mn():
  printHeader()

  # Import the module/function to be used
  import imported_funcs as impF

  # Create data for the function (md list for colums and rows)
  data = [
      ["col 1", "col 2", "col 3"],
      ["1", "2", "3"],
      ["1^2", "2^2", "3^2"],
      ["1^3", "2^3", "3^3"],
      ["1^4", "2^4", "3^4"],
      ["1^5", "2^5", "3^5"]
    ]

  # pass the data into the imported function (func prints result)
  # display_data(table_name, table)
  impF.display_data("Powers", data)

  returnMain()

# Has to be located outside of a function (on module level)
from imported_funcs import *
def from_mn_import_all():
  printHeader()

  # Import the module/function to be used
  import imported_funcs

  # Create data for the function (md list for colums and rows)
  data = [
      ["col 1", "col 2", "col 3"],
      ["1", "2", "3"],
      ["1^2", "2^2", "3^2"],
      ["1^3", "2^3", "3^3"],
      ["1^4", "2^4", "3^4"],
      ["1^5", "2^5", "3^5"]
    ]

  # pass the data into the imported function (func prints result)
  # display_data(table_name, table)
  display_data("Powers", data)

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
    import IndependentPractice31 as foo
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
      "display_data"
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
