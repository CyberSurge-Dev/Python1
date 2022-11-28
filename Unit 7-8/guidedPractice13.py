# Zachary hoover || Guided Practice #13
# 11-09-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Guided Practice #13   ")
  print(" --------------+--------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def sliceMethod():
  printHeader()

  string = "ASTRING"

  s1 = slice(3) # display everything before index 3
  s2 = slice(1,5,2) # Start at index 1, got to index 5, count every 2
  s3 = slice(-1,-12,-2) # start at index -1, go to index -12, count every 2

  print("", string[s1])
  print("", string[s2])
  print("", string[s3])

  returnMain()

def arraySlicing():
  printHeader()

  string = "COXMILLCHARGERS"
  print(string[:])
  print(string[:7])
  print(string[7:])
  print(string[::2])
  print(string[1:5:2])
  print(string[-1:-12:-2])
  print(string[::-1])

  returnMain()

def stringMethods():
  printHeader()

  word = input(" Enter a word/phrase: ")
  print(f" your word/phrase is {len(word)} characters long")
  print(f" Your word/phrase has {word.count('e')} instances of the letter \'e\'")
  print(f" The letter e is first seen at index {word.find('e')}")

  word = input(" Enter another word/phrase: ")
  for letter in word:
    print("", letter)
  name = input(" Please enter a name: ")
  length = len(name)-1
  index_num = int(input(f" Please enter a number between 0-{length}: "))

  if index_num >= length: print(" Error! invalid input.");
  else: print(name);

  
  returnMain()

################################################

menuMode = 0
currentBench = 0


def autoMenu():
  global menuMode
  global currentBench
  global usable
  global funcName

  funcName = "autoMenu"

  if menuMode == 1:
    if currentBench > len(usable):
      menuMode = 0
      currentBench = 0
      autoMenu()
    else:
      currentBench += 1
      funcName = usable[currentBench][0]
      usable[currentBench][1]()

  if menuMode == 2:
    if currentBench > len(usable):
      menuMode = 0
      currentBench = 0
      autoMenu()
    else:
      currentBench += 1
      funcName = usable[currentBench][0]
      usable[currentBench - 1][1]()

  else:
    printHeader()

    # change were it says 'baseTemplate' to module name.
    import guidedPractice13 as foo
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
