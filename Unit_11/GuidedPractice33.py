# Zachary Hoover || Guided Practice #33
# 01-06-23
import os
from inspect import getmembers, isfunction

# import math module
import math

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #33   ")
  print(" --------------+--------------")
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
    from random import randint
    return(randint(1, 6))

  def odd_random():
    from random import randrange
    return randrange(1,101,2)

  def RPS():
    from random import choice

    options = ["Rock", "Paper", "Scissors"]
    return choice(options)

  def pick_card():
    from random import choice

    card_type = ["Clubs", "Diamonds", "Hearts", "Spades"]
    card_number = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

    # Choose a type at random
    t = choice(card_type)
    n = choice(card_number)

    return n, t

  

def ceiling():
  printHeader()


  x = math.ceil(31.8)
  print("", x)

  returnMain()

def truncate():
  printHeader()
  x = math.trunc(31.8)
  print("", x)

  returnMain()

def floor():
  printHeader()

  x = math.floor(31.8)
  print("", x)

  returnMain()

def round_examples():
  printHeader()

  from math import floor, ceil, trunc

  prize = 213

  option1 = floor(prize/2)

  print(f" You get {option1} and your friend gets {prize-option1}")

  option2 = ceil(prize/2)

  print(f" You get {option2} and your friend gets {prize-option2}")

  returnMain()

def random_ints():
  printHeader()

  from random import randint, randrange
  
  print("", randint(1, 10))
  print("", randrange(1, 11))
  print("", randrange(1, 11, 2))

  returnMain()

def die_roller():
  printHeader()

  print("", norun.die_roller())
  
  returnMain()

def odd_random():
  printHeader()

  print("", norun.odd_random())

  returnMain()

def random_sequences():
  printHeader()

  
  print( "", norun.RPS() )
  

  returnMain()

def shuffling():
  printHeader()

  from random import shuffle
  x = ["Ana", "John", "Mike", "Sally"]

  shuffle(x)

  print("", x)

  returnMain()

def pick_playing_card():
  printHeader()

  print("", norun.pick_card())

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
    import GuidedPractice33 as foo
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
