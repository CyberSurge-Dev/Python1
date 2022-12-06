# Zachary Hoover || Independent Practice #22
# 12-05-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Independent Practice #22   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def seeing_the_world():
  printHeader()

  # Create list of placces
  places = [
    "Dubai",
    "France",
    "Canada",
    "Australia",
    "Germany",
    "Sweeden",
    "Norway",
    "Netherlands",
    "Poland",
    "Belarus"
    ]

  # print orgiginal list
  print(" Original list:", places)
  # Print sorted list
  print("\n Sorted list:", sorted(places))
  # Print reversed list
  places.reverse()
  print("\n Reversed list", places)
  # Reverse to original again
  print("\n Reversed to original:", places)
  # sorted list
  places.sort()
  print("\n Sorted list:", places)
  # Reverse sort
  places.sort(reverse=True)
  print("\n Reversed sort:", places)
  
  returnMain()

def dinner_guest():
  printHeader()

  # Create list of pepople going
  people = ["John", "jerry", "malisa", "Aaron", "Pluto", "Jack", "Andy", "Jamia"]

  # print the list
  print(" People:", people)

  # print amount of people going
  print(" Amount of people going:", len(people))

  returnMain()

def combine_lists():
  printHeader()

  # create list of common birds
  common_birds = ['chicken', 'blue jay', 'crow', 'pigeon']

  # print list
  print(" Orgignal birds:", common_birds)

  # create list of birds seen
  birds_seen = ["eagle", "hawk", "segal"]
  # extend common_birds
  common_birds.extend(birds_seen)
  # print common_birds
  print(" Extended common birds:", common_birds)

  returnMain()

def combine_lists_2():
  printHeader()

  # create list of 0-9
  zero_nine = []
  zero_nine.extend( range(0, 10) )

  # create list of 10-100 by 10s
  ten_onehundred = []
  ten_onehundred.extend( range(10, 101, 10) )

  # print each list
  print(" 0-9:", zero_nine)
  print(" 10-100 by 10:", ten_onehundred)

  # add lists together
  all_nums = zero_nine + ten_onehundred

  # print final list
  print("\n All nums:", all_nums)

  returnMain()

def merge_and_sort():
  printHeader()

  # create animal list
  animals = [
    "turtle",
    "dog",
    "cat"
    ]

  # create add animal list
  add_animals = [
    "zebra",
    "giraffe",
    "elephant"
    ]

  # print original lists
  print(" Animals:", animals)
  print(" Add_animals:", add_animals)
  
  # add add_animals to animals
  animals.extend(add_animals)

  # print list
  print("\n Combined animals:", animals)

  # sort and print list
  animals.sort()
  print(" Sorted animals:", animals)

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
    import IndependentPractice22 as foo
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
