# Zachary Hoover || Guided Practice #18
# 11-28-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #18   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def slicing_a_list():
  printHeader()

  players = ["Spoorthi", "Kelly", "Yakairia", "Ariana", "Marcela", "Rachel"]
  print("", players[0:3]) # Prints first 3 items
  print("", players[1:4]) # Prints second tird and fourth items
  print("", players[:4]) # prints first 4 items
  print("", players[2:]) # prints index 2 to the end of the list
  print("", players[-3:]) # prints from the 3rd to last index to the end

  returnMain()

def looping_through_a_list():
  printHeader()

  players = ["eric", "caden", "jack", "nathan", "bhargava", "aiden"]

  print(" First 3 players on the team: ")
  for player in players[:3]:
    print("", player.title())

  returnMain()
 
def copy_of_list():
  printHeader()

  my_foods = ["pizza", "CORN", "beets"]
  friend_foods = my_foods[:]

  print(" My favorite foods are: ", end="")
  print(friend_foods)
  print(" My friend's favorite foods are: ", end="")
  print(friend_foods)

  returnMain()

def copy_of_list_not_work():
  printHeader()

  # Does not work

  my_foods = ["pizza", "corn", "beets"]
  friend_foods = my_foods

  my_foods.append("chineese")
  friend_foods.append("frogs")
  
  print(" My favorite food is:", my_foods)
  print(" My friend's favorite foods:", friend_foods)

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
    import GuidedPractice18 as foo
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
