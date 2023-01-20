# Zachary Hoover || Independent Practice #34
# 01-11-23
from calendar import month
from datetime import date, datetime
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Independent Practice #34   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def time_object_1():
  printHeader()

  # import time
  from datetime import time

  # create and print time variable, 8:45
  t1 = time(minute=45, hour=8)
  print("", t1)

  returnMain()

def time_object_2():
  printHeader()

  # import time
  from datetime import time

  # create and print time variable, 8:45
  t1 = time(minute=45, hour=8, second=1, microsecond=150)
  print("", t1)

  returnMain()

def hours():
  printHeader()

  # import time
  from datetime import time

  # create variable and print
  t1 = time(hour = 15, minute = 10, second = 0)
  print("", t1.strftime("%I:%M %p"))

  # modify variable and print
  t1 = t1.replace(hour = 4, minute = 10)
  print("", t1.strftime("%I:%M %p"))

  returnMain()

def date_object():
  printHeader()

  from datetime import date
  
  # create and print date object 
  d1 = date(month=3, day=28, year=2012)
  print("", d1)

  returnMain()

def date_object_2():
  printHeader()

  # import date
  from datetime import date

  # get user's day
  day = int(input(" Enter a day: "))
  month = int(input(" Enter a month: "))
  year = int(input(" Enter a year: "))

  # create variable and print
  date = date(day=day, month=month, year=year)
  print("\n Date:\n ", date.strftime("%m/%d/%Y"))

  returnMain()

def datetime_object():
  printHeader()

  # import datetime
  from datetime import datetime

  # create varibale
  dt = datetime(day=17, month=8, year=2007, hour=7, minute=46)

  d = dt.date()
  t = dt.time()

  # print date and time
  print(" Date:", d)
  print(" Time:", t)

  returnMain()

def dates_and_time():
  printHeader()

  # import date
  from datetime import date

  # set date
  d = date(year=2018, month=10, day=23)

  # print date in different formats
  print(" date 1:", d.strftime("%b %d, %Y")) # Oct 23, 2018
  print(" date 1:", d.strftime("%m/%d/%Y")) # 10/23/18
  print(" date 1:", d.strftime("%d/%B/%Y")) # 23/October/2018
  print(" date 1:", d.strftime("%A %B %d")) # Tuesday October 23

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
    import IndependentPractice34 as foo
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
