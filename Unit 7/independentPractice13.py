# Zachary hoover || Independent Practice #13
# 11-09-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Independent Practice #13   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

# Prints different parts of the street name "River Oaks"
def program_1():
  printHeader()

  street_name = "River Oaks"
  print("", street_name[:5:2])
  print("", street_name[-3:])

  returnMain()

# Takes user input, and checks to make sure that the second character is i,o, or u.
# if not, then the loop repeats until the user pruduces a word with those requirments. 
def program_2():
  printHeader()
  
  active = True
  while active:
    team_name = input(" Enter a word(Second carracter must be i, o, or u): ")
    secondLetter = [ "i", "o", "u"]

    if team_name[1].lower() not in secondLetter:
      print(" The second letter is not i, o, or u")
      continue
    else:
      active = False
      
  returnMain()

# Asks user for there name, then prints first and last character. 
def program_3():
  printHeader()

  first_name = input(" Enter your frist name: ")
  length = len(first_name)
  s = slice(0, length, length-1)

  print("", first_name[s])

  returnMain()

# prints "act" and then "tic"
def program_4():
  printHeader()

  long_word = "characteristics"

  print("", long_word[ 4:7 ])
  print("", long_word[ -4:-1:1 ])
 
  returnMain()

# print s "sequence"
def program_5():
  printHeader()


  long_word="Consequences"
  print("", long_word[ 3:11 ])

  returnMain()

# prints the first half of a word.
def program_6():
  printHeader()

  long_word = "Consequences"

  print("", long_word[ :6 ])

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
    import independentPractice13 as foo
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
