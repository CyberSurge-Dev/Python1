# Zachary Hoover || Independent Practice: #15
# 11-15-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Independent Practice: #15   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

# list of inventations for people
def attending_people():
  printHeader()
  
  guest_list = [
  "John Smith",
  "Jerry Dimbat",
  "Knuffle Timson"
  ]

  print(f" Hey {guest_list[0]}, want to come to my awsome dinner party?")
  print(f" Hey {guest_list[1]}, would be interested in a dinner party")
  print(f" Hey {guest_list[2]}, would like to go to a dinner party?")

  returnMain()

# Changing guest_list because someone can't show up
def changing_guest_list():
  printHeader()
  guest_list = [
  "John Smith",
  "Jerry Dimbat",
  "Knuffle Timson"
  ]

  print(" Jerry Dimbat cant come to dinner")
  guest_list[1] = "Joshua Winefield"

  print(" The new person is Joshua Winefield")
  print(" People going are:", guest_list, "\n")

  print(f" Hey {guest_list[0]}, want to come to my awsome dinner party?")
  print(f" Hey {guest_list[1]}, would be interested in a dinner party")
  print(f" Hey {guest_list[2]}, would like to go to a dinner party?")

  returnMain()

# Inviting 3 more quest because of new dinner table
def inviting_more_guest():
  printHeader()
  guest_list = [
  "John Smith",
  "Joshua Winefield",
  "Knuffle Timson"
  ]

  
  print(" Hey, I found a bigger table!")
  print(" I can now add 3 more guest!\n")

  # Inviting new guests
  print(" My first new guest will be Jim Dimbat (Jerry Dimbat's son)")
  guest_list.insert(0, "Jerry Dimbat")
  print(" My second guest will be Ryan Gillwood")
  guest_list.insert(1, "Ryan Gillwood")
  print(" Lastly, ill invite Loyton Joanna")
  guest_list.append("Loyton Joanna")

  print("")

  # Sending inventations
  for name in guest_list:
    print(f" Hey {name}, you interested in going to a dinner party?")

  returnMain()

# Dinner table cant show up in time, shrink guest list to 2
def shrinking_guest_list():
  printHeader()
  guest_list = [
  "John Smith",
  "Joshua Winefield",
  "Knuffle Timson",
  "Jerry Dimbat",
  "Ryan Gillwood",
  "Loyton Joanna"
  ]

  print(" Darn! my dinner table won't be here in time.")
  print(" I can only invite 2 people! \n")

  y = 0
  # Cycle through people in list, leave all but 2
  # Also, i am unsure why I needed to put a +2 at the end to get
  # my code to work properly, it seems to be a weird things
  # with loops not doing the full amount of iterations.
  print(" [pop]")
  while y < len(guest_list)+2:
    x = guest_list.pop()
    print(f" Sorry {x}, you cant come to dinner because I wont have a large enough table.")
    y += 1
    
  # used del function to delete items
  print("\n [del]")
  print(f" Sorry {guest_list[0]}, you cant come to dinner because I wont have a large enough table.")
  del guest_list[0]
  print(f" Sorry {guest_list[0]}, you cant come to dinner because I wont have a large enough table.")
  del guest_list[0]

  print("\n Final Guest List:", guest_list)
    
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
    import independentPractice15 as foo
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

if __name__ == "__main__": autoMenu();
