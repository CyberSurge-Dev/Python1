# Zachary Hoover || Guided Practice #25
# 12-08-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #25   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def string_formatters():
  printHeader()

  print(" Sammy has {} ballons".format(5))

  open_string = "Sammy loves {}"
  print("", open_string.format("open_source"))

  returnMain()

def formatters_multiple_placeholders():
  printHeader()

  open_string = "Sammy loves {} {}."
  print("", open_string.format("open-source", "software")) # pass 2 strings

  open_string = "Sammy loves {} {}, and has {} {}."
  print("", open_string.format("open-source", "software", 5, "balloons")) # pass 3 strings and an int

  returnMain()

def reordering_Formatters():
  printHeader()

  print(" Sammy the {} has a pet {}!".format("shark", "pilot fish"))

  print(" Sammy the {0} has a pet {1}!".format("shark", "pilot fish"))

  print(" Sammy the {1} has a pet {0}!".format("shark", "pilot fish"))
  returnMain()

def specifying_type():
  printHeader()

  print(" Sammy at {0:f} percent of a {1}".format(75, "pizza"))

  print(" Sammy at {0:.1f} percent of a pizza!".format(75.765367))

  print(" Sammy ate {0:.0f} percent of a pizza!".format(75.765367))

  returnMain()

def uaing_variables():
  printHeader()

  nBalloons = 8
  print(" Sammy has {} balloons today!".format(nBalloons))

  sammy = "Sammy has {} balloons today!"
  print("", sammy.format(nBalloons))

  returnMain()

def padding_variable_subsitutions():
  printHeader()

  print(" Sammy has {0:4} red {1:16}!".format(5, "balloons"))
  print(" Sammy has {0:<4} red {1:^16}!".format(5, "balloons"))

  print(" {:*^20s}".format("Sammy"))

  print(" Sammy ate {0:5.0f} percent of a pizza!".format(75.765367))
  
  returnMain()

def using_formatters_to_organize():
  printHeader()
  
  # no formmaters
  for i in range(3,13):
    print("", i, i*i, i*i*i)

  print(" Formated string nums:")
  for i in range(3, 13):
    print(" {:3d} {:4d} {:5d}".format(i, i*i, i*i*i))

  print(" Formated string nums 2:")
  for i in range(3, 13):
    print(" {:6d} {:6d} {:6d}".format(i, i*i, i*i*i))

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
    import GuidedPractice25 as foo
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
