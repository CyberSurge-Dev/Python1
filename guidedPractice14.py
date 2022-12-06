# Zachary hoover || Independent Practice #14
# 11-14-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Independent Practice #14   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

namess = []
has_names = False


def names():
  # Get user's 5 friends if they havent already(if they have any)
  global has_names
  global namess

  if has_names == False:
    for x in range(1, 6):
      printHeader()
      print(" Enter the names of 5 of your friends.")
      print(" If you dont have enough friends, or dont have 5")
      print(
        " you can exit the questions early by typing \'i don't have friends :(\' \n"
      )

      name = input(f" What is the name of friend {x}: ")
      if name == "i don't have friends :(":
        break
      else:
        namess.append(name)
    has_names = True

  printHeader()

  # Multible ways to do this section i could also use 'for name in names:'
  for x in range(0, len(namess)):
    print("", namess[x])

  returnMain()


def greetings():
  # Get user's 5 friends if they havent already(if they have any)
  global has_names
  global namess

  if has_names == False:
    for x in range(1, 6):
      printHeader()
      print(" Enter the names of 5 of your friends.")
      print(" If you dont have enough friends, or dont have 5")
      print(
        " you can exit the questions early by typing \'i don't have friends :(\' \n"
      )

      name = input(f" What is the name of friend {x}: ")
      if name == "i don't have friends :(":
        break
      else:
        namess.append(name)
    has_names = True

  printHeader()

  for x in range(0, len(namess)):
    print(f" Hello {namess[x]}. How has your day been going?")

  returnMain()


def favorite_music():
  printHeader()

  from numpy import random

  # Set of random artisits I found online
  music_artists = [
    "Taylor Swift", "Eton John", "Johnny Cash", "James Taylor", "Celine Dion",
    "George Strait", "Luke Bryan", "Billie Ellish", "Bob Marley", "Rod Stewert"
  ]
  sentances = [
    "name is a person that exist",
    "name is a person that makes music that people listen to",
    "name has had at least one good song", "name makes good music",
    "i think name is a pretty cool person",
    "have you heard of name? they make music", "name is the best artist",
    "name makes some good music sometimes", "name has an amazing voice",
    "I love the music that name makes", "name makes music sometimes"
  ]
  usedSentances = []

  print(" All artists, and sentances were selected at random\n")
  i = 0
  while i < len(music_artists):
    sentance = random.choice(sentances)
    if sentance in usedSentances:
      continue

    string = sentance.replace("name", music_artists[i])
    print(f" {string}.")
    usedSentances.append(sentance)
    i += 1

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
    if currentBench > len(usable):
      menuMode = 0
      currentBench = -1
      autoMenu()
    else:
      currentBench += 1
      try:
        funcName = usable[currentBench][0]
        usable[currentBench][1]()
      except:
        print("Index out of range!")

  if menuMode == 2:
    if currentBench > len(usable):
      menuMode = 0
      currentBench = -1
      autoMenu()
    else:
      currentBench += 1
      try:
        funcName = usable[currentBench][0]
        usable[currentBench][1]()
      except:
        print("Index out of range!")

  else:
    printHeader()

    # change were it says 'baseTemplate' to module name.
    import guidedPractice14 as foo
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