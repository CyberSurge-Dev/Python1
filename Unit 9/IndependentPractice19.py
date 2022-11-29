# Zachary Hoover || Independent Practice: #19
# 11-29-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Independent Practice: #19   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def hello_admin():
  printHeader()

  # Create a list of users
  users = ["admin", "James", "Jack", "Adison", "Brandon", "Maddie"]

  # Check if the username is equal to admin, and print a special message
  for person in users:
    if person == "admin":
      print(" Hello admin, would you like to see a status report?")
    else:
      # Greet the non-admin users
      print(f" Hello {person}, thank you for logging in again.")

  returnMain()

def no_users():
  printHeader()

  # Create an empty list
  users = []

  # Check if the list has no components
  if not users:
    print(" We need t find more users!")

  returnMain()

def checkig_usernames():
  printHeader()

  # Create a list of users, ad new users
  current_users = ["admin", "James", "Jack", "John", "Brandon"]
  new_users = ["Maddie", "Anna", "Alex", "George", "John"]

  # Create a list of lowercase users, and new users. 
  lc_current_users = [x.lower() for x in current_users]
  lc_new_users = [x.lower() for x in new_users]

  # print the original lists (Mostly for debug purposes)
  print(" current_users:", current_users)
  print(" new_users:", new_users, "\n")

  # print the new list after they have become lowercase (mostly for debug purposes)
  print(" lc_current_users:", lc_current_users)
  print(" lc_new_users:", lc_new_users, "\n")

  # Cycle through the lists and check if there are any overlaping usernames.
  for user in lc_new_users:
    if user in lc_current_users:
      print(f" {user} will have to create a new username")
    else:
      print(f" {user} is available")

  print("\n Done.")
  returnMain()

def original_numbers():
  printHeader()
  # Loop through a list of numbers 1-9
  for number in range(1,10):
    
    # Check if the number is 1, 2, or 3 and change output accordingly
    if number == 1:
      print(" 1st")
    elif number == 2:
      print(" 2nd")
    elif number == 3:
      print(" 3rd")
      
    # else, continue with 'th' ending
    else:
      print(f" {number}th")
      
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
    import IndependentPractice19 as foo
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

# program start
autoMenu()
