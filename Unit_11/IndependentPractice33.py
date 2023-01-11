# Zachary Hoover || Independent Practice #33
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
  print("\n    Independent Practice #33   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

class norun:
  def die_roller():
    """Returns randrange 1,7"""
    from random import randrange
    
    return randrange(1, 7)

  def dice_roller():
    """Returns 2 random numbers"""
    from random import randint
    return randint(1, 6), randint(1,6)

  def odd_random():
    """Returns 10 odd numbers between 1 and 100"""
    
    from random import randint
    retlist = []

    # get 10 random numbers and add them to retlist
    while (len(retlist) < 10):
      ranint = randint(1, 101)
      if ((ranint % 2) != 0):
        retlist.append(ranint)

    return retlist

  def pick_card():
    """returns a random card pair"""
    from random import shuffle
    
    suits = ["spades", "clubs", "diamonds", "hearts" ]
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Ace", "jack", "Queen", "King"]

    shuffle(suits)
    shuffle(cards)

    return suits[0], cards[0]
      

def rounding_numbers():
  printHeader()

  from math import floor, ceil

  # set num
  num = 75.34

  # use floor and ceil to get 75 and 76
  print("", floor(num))
  print("", ceil(num))

  returnMain()


def modify_die_roller():
  printHeader()

  # run die_roller
  print("", norun.die_roller())

  returnMain()

def modify_odd_random():
  printHeader()

  print("", norun.odd_random())

  returnMain()

def two_dice():
  printHeader()

  num1, num2 = norun.dice_roller()

  print("", num1)
  print("", num2)

  returnMain()

def card_shuffle():
  printHeader()

  suit, card = norun.pick_card()

  print("", suit)
  print("", card)
  
  returnMain()

def random_city():
  printHeader()

  from random import choice

  cities = [
    "New York",
    "Los Angles",
    "Chicago",
    "Huston",
    "Phoenix",
    "Philadelphia",
    "San Antonio",
    "San Diego",
    "Dallas",
    "San Jose"
    ]

  print("", choice(cities))

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
    import IndependentPractice33 as foo
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
