# Zachary Hoover || Independent Practice #32
# 01-05-23
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Independent Practice #32   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def importing_modules():
  printHeader()

  # import gcd for greatest commn divisor
  from math import gcd
  print(f" The GCD of 16 and 18 is {gcd(16, 18)}")

  # get 2 seperate number from the user using .split()
  nums = input(" Enter 2 nums with a space between: ").split(" ")

  # Convert all the nums to int
  nums = [int(x) for x in nums]

  # print the nums
  print("\n Your first num is:", nums[0])
  print(" Your secnd num is:", nums[1])

  # print the GCD of the inputed nums
  print("\n The GCD of your nums is:", gcd(nums[0], nums[1]))

  returnMain()

def math_functions():
  printHeader()

  x = 5;

  # checks if x is even or odd, print result
  if ( (x % 2) == 0 ):
    print(f" {x} is even.")
  else:
    print(f" {x} is odd.")

  returnMain()

def even_numbers():
  printHeader()

  # import sqrt
  from math import sqrt

  # create list of nums
  L = [25, 34, 193, 2, 81, 26, 44]

  # cycle through all items
  for num in L:
    # Check if the item is even
    if ( (num % 2) == 0 ):
      # print the sqrt of the current item
      print(f" The sqrt of {num} is {sqrt(num)}")


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
    import IndependentPractice32 as foo
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
