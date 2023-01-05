# Zachary Hoover || Independent Practice #30
# 12-16-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Independent Practice #30   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

class noMenu:
   def generate_star(star):
     """Genetrate a drawn image from inputed multi-dimmensional list"""

     for row in star:
       for col in row:
         print(f" {col}", end = "")
       print()
     return

def counting_specific_numbers():
  printHeader()

  # Create list of nums
  lst = [9, 0, -2, -4, -5, 2, -15, 6, -65, -7]

  # declare variables
  even_positives = 0
  odd_negatives = 0
  zeros = 0

  # Cycle through the items in the list
  for num in lst:
    # if the number is greater than zero
    if (num > 0):
      # if the number is even, add it to even_positives
      if ((num % 2) == 0):
        even_positives += 1
    # if the number is even add it zeros
    elif (num == 0):
      zeros += 1
    # if the number is odd
    else:
      # Make number even temporarily
      Tnum = num*-1
      # iff the negative number is odd at it odd_negatives
      if ( (Tnum % 2) != 0 ):
        odd_negatives += 1

  print(" Even positives:", even_positives)
  print(" Odd negatives:", odd_negatives)
  print(" Zeros:", zeros)
  returnMain()

def character_art():
  printHeader()

  # get user input
  width = int(input(" Enter a width for the star: "))
  height = int(input(" Enter height of the start (for paralax): "))
  paralax = input(" Paralax (logic error in code, but eneded up looking cool so I kept it) (y / n): ")

  star = []
  if (paralax == "y"):
    # loop through height and width
    for i in range(height):
      for x in range(width):
        # create empty list of empty strings
        TL = ["" for x in range(width)]
        # set the X's on the edges
        TL[x] = "X"
        TL[(x + 1) * -1] = "X"

        # add list to star
        star.append(TL)
  else:
    # loop through height and list and draw star in array
    for i in range(height):
      TL = ["" for x in range(height)]
      TL[i] = "X"
      TL[(i + 1) * -1] = "X"
      star.append(TL)
      
  # print star
  noMenu.generate_star(star)

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
    import IndependentPractice30 as foo
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
