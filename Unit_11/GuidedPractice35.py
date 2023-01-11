# Zachary Hoover || Guided Practice #35
# 01-10-23
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #35   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def definition():
  printHeader()

  from datetime import timedelta
  delta1 = timedelta(days = 7, hours = 2)
  print("", delta1)

  returnMain()

def datetime():
  printHeader()

  from datetime import datetime
  dt1 = datetime(year = 2017, month = 1, day = 1)
  dt2 = datetime(year = 2017, month = 1, day = 2)

  delta1 = dt2 - dt1
  print("", delta1)

  returnMain()

def timedelta():
  printHeader()

  from datetime import timedelta
  delta1 = timedelta(days = 7, hours = 2)

  print("", delta1.days)
  print("", delta1.seconds)
  print("", delta1.microseconds)

  print("", delta1.total_seconds())

  returnMain()

def math():
  printHeader()

  from datetime import datetime, timedelta

  one_hundred_days = timedelta(days = 100)

  current_date = datetime.today()

  new_date = current_date + one_hundred_days

  print(" After 100 days:", new_date.strftime("%b/%d/%Y"))

  returnMain()

def two_hundred_three_hundred():
  printHeader()
  
  from datetime import datetime, timedelta

  hundred1 = timedelta(days = 100)
  hundred2 = hundred1 * 2
  hundred3 = hundred1 * 3

  curdate = datetime.today()

  ndate1 = curdate + hundred2
  ndate2 = curdate + hundred3

  print(" After 200 days:", ndate1.strftime("%b/%d/%Y"))
  print(" After 300 days:", ndate2.strftime("%b/%d/%Y"))

  returnMain()

def birthdays():
  printHeader()

  from datetime import date

  bir1 = date(year = 1993, month = 3, day = 5)
  bir2 = date(year= 2003, month = 3, day = 20)

  if (bir1 > bir2):
    print(" Person 2 is older")
  elif (bir2 > bir1):
    print(" Person 1 is older")
  else:
    print(" Person 1 and 2 are the same age")

  returnMain()


def examples():
  printHeader()

  from datetime import datetime

  today = datetime.today()

  solstice = datetime(month = 12, day = 21, year = 1)

  solstice = solstice.replace(year = (datetime.today().year))

  count = solstice - today

  print(" There are", count.days, "days until the December solstice!")

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
    import GuidedPractice35 as foo
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
