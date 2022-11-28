# Zachary Hoover || Independent Practice: #16
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
  print("\n    Independent Practice: #16   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

# Create the list of favorite pizza
favorite_pizzas = [
  "Pepporoni Pizza",
  "Cheese Pizza",
  "\'Special\' Pizza"
  ]

# Create the list of favorite animals
favorite_animals = [
  "Dog",
  "Cat",
  "Turttle"
  ]

"""Pizza 1, lists favorite types of pizza"""
def pizza_1():
  # Declare the list gloabl so it can be used in the function
  global favorite_pizzas
  printHeader()

  print(" Favorite pizzas:")

  # Cycle through all the items in the list
  for pizza in favorite_pizzas:
    print("", pizza)

  returnMain()

"""Pizza 2, lists favorite types of pizza with sentance"""
def pizza_2():
  # Declare the list gloabl so it can be used in the function
  global favorite_pizzas
  printHeader()

  print(" Favorite pizzas:")

  # Cycle through all the items in the list
  sentances = [
    "is the best kind of pizza.",
    "is simple, but has great flavor.",
    "is filled with different flavor"
  ]
  i = 0
  for pizza in favorite_pizzas:
    print("", pizza, sentances[i])
    i+=1

  returnMain()

"""Pizza 3, lists favorite types of pizza with sentance and end statment"""
def pizza_3():
  # Declare the list gloabl so it can be used in the function
  global favorite_pizzas
  printHeader()

  print(" Favorite pizzas:")

  # Cycle through all the items in the list
  sentances = [
    "is the best kind of pizza.",
    "is simple, but has great flavor.",
    "is filled with different flavor"
  ]
  i = 0
  for pizza in favorite_pizzas:
    print("", pizza, sentances[i])
    i+=1

  print("\n Pizza is one of my faorite foods, because of the vast amount of options.")

  returnMain()

"""Animals 1, list favorite animals, and a sentance"""
def animals_1():
  # Declare the list gloabl so it can be used in the function
  global favorite_animals
  printHeader()

  sentances = [
    "s are the most fun to be around.",
    "s are fun to be around... when they want to be.",
    "s are cool."
  ]

  # Cycle through all the items in the list
  i = 0
  for animal in favorite_animals:
    print("", animal + sentances[i])
    i += 1

  returnMain()

"""Animals 2, list favorite animals, a sentance, and an end statment"""
def animals_2():
  # Declare the list gloabl so it can be used in the function
  global favorite_animals
  printHeader()

  sentances = [
    "s are the most fun to be around.",
    "s are fun to be around... when they want to be.",
    "s are cool."
  ]

  # Cycle through all the items in the list
  i = 0
  for animal in favorite_animals:
    print("", animal + sentances[i])
    i += 1

  print("\n All of these animals would make great pets!")

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
    import independentPractice16 as foo
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
