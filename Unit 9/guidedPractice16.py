# Zachary Hoover || Guided Practice #16
# 11-17-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #16   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def list_magicians_1():
  printHeader()

  print(" Magicians:")
  magicians = ['alice', 'david', 'carolina']
  for magician in magicians:
    print("", magician)

  returnMain()

def list_magicians_2():
  printHeader()

  magicians = ['alice', 'david', 'carolina']
  for magician in magicians:
    print(f" {magician.title()}, that was a great trick!")

  returnMain()

def list_magicians_3():
  printHeader()

  magicians = ['alice', 'david', 'carolina']
  for magician in magicians:
    print(f" {magician.title()}, that was a great trick!")
    print(f" I can't wait to see your next trick, {magician.title()}\n")

  returnMain()

def list_magicians_4():
  printHeader()

  magicians = ['alice', 'david', 'carolina']
  for magician in magicians:
    print(f" {magician.title()}, that was a great trick!")
    print(f" I can't wait to see your next trick, {magician.title()}\n")

  print(" Thank you everyone, that was a great show!")

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
    import guidedPractice16
    list = []
    list = getmembers(guidedPractice16, isfunction)

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

if __name__ == "__main__": autoMenu();
