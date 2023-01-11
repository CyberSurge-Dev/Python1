# Zachary Hoover || Guided Practice #34
# 01-09-23
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #34   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def in_order():
  printHeader()

  from datetime import time

  t = time(20, 55, 20, 500)
  print("", t)

  print("\n by name:")
  t = time(minute=10, hour=9, microsecond=900000, second=20)
  print("", t)
  
  returnMain()

def some_attributes():
  printHeader()

  from datetime import time

  t = time(hour = 1, minute = 10)
  print("", t)

  returnMain()

def wrong_value():
  printHeader()

  from datetime import time

  try:
    t = time(hour = 29)
  except Exception as e:
    print(" t = time(hour = 29) causes error:")
    print("", e)

  returnMain()
  

def getting_an_attribute():
  printHeader()

  from datetime import time

  # assign value to t
  t = time(hour=9, minute=10, second=43, microsecond=100)

  h = t.hour
  m = t.minute
  s = t.second
  ms = t.microsecond

  print(f" The time is {h} hours, {m} minutes, {s} seconds and {ms} microseconds")

  returnMain()

def modifying_attributes():
  printHeader()

  from datetime import time

  t = time(hour = 9, minute = 10, second = 43, microsecond = 100)
  print(" Old time:", t)

  # modify attribute
  t = t.replace(hour = 8, minute = 8)
  print(" New time", t)

  returnMain()

def date_objects():
  printHeader()

  from datetime import date

  date1 = date(2013, 5, 7)
  print(" Date 1:", date1)

  date2 = date(day = 23, month = 4, year = 1999)
  print(" Date 2:", date2)
 
  returnMain()


def date_attribute():
  printHeader()

  from datetime import date

  # assign a date value
  SpecialDate = date(year= 2017, month = 11, day = 15)

  y = SpecialDate.year
  m = SpecialDate.month
  d = SpecialDate.day

  print(f" The special date is {m}/{d}/{y}")

  returnMain()

def modifying_date_object():
  printHeader()

  from datetime import date

  d = date(year = 2015, day = 28, month = 2)
  print(" Old date:", d)

  d = d.replace(year = 2016, day = 29)
  print(" New date:", d)

  returnMain()

def currnet_local_date():
  printHeader()

  from datetime import date

  # todays date
  d = date.today()

  print("", d)

  returnMain()


def assign_datetime():
  printHeader()

  from datetime import datetime

  # assign a date value
  dt = datetime(2022, 7, 4, 16, 30)

  print("", dt)

  returnMain()

def getting_datetime():
  printHeader()

  from datetime import datetime

  # assign a date value
  dt = datetime(2022, 7, 4, 16, 30)

  y = dt.year
  m = dt.month
  d = dt.day
  h = 16
  m = 30
  
  print(f" The special date is {m}/{d}/{y} and the time is {h}:{m}")

  returnMain()

def modifying_datetime():
  printHeader()

  from datetime import datetime

  # todays date
  d = datetime.today()

  d.replace(year = 2020, second = 30)

  print("", d)

  returnMain()

def current_datetime():
  printHeader()

  from datetime import datetime

  dt = datetime.today()
  print("", dt)

  returnMain()

def spliting_datetime():
  printHeader()

  from datetime import datetime, time, date

  dt = datetime.today()

  t = dt.time()
  print(" Time is:", t)

  d = dt.date()
  print(" Date is:", d)

  returnMain()

def combining_datetime():
  printHeader()

  from datetime import datetime, time, date

  # assign a time object
  t = time(hour = 6, minute = 45, second = 0)

  d = date.today()

  dt = datetime.combine(date = d, time = t)

  print("", dt)

  returnMain()

def formating_time():
  printHeader()

  from datetime import time
  t = time(hour = 10, minute = 15)

  formated_string = t.strftime("%I:%M %p")
  print(" First fromat:", formated_string)

  formated_string = t.strftime("%H:%M:%S")
  print("Second format:", formated_string)

  returnMain()

def fromating_date():
  printHeader()

  from datetime import date
  d = date(year = 1999, month = 11, day = 3)

  fs = d.strftime("%B, %d. %y")
  print(" first format:", fs)

  fs = d.strftime("%b #d %y")
  print(" Second format:", fs)

  returnMain()

def formating_datetime():
  printHeader()

  from datetime import datetime
  dt = datetime.today()

  fs = dt.strftime("%B, %d, %Y @ %I:%M %p")
  print(" First format:", fs)

  fs = dt.strftime("%b %d %y / %H:%M:%S")
  print(" Second format:", fs)

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
    import GuidedPractice34 as foo
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
