# Zachary Hoover || Independent Practice #17
# 11-18-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Independent Practice #17   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

"""Prints numbers 1-10"""
def counting_to_twenty():
  printHeader()

  for num in range(1,11):
    print("", num)

  # alternative to print the list of nums
  lst = list(range(1,11))
  print(" Full list:", lst)

  returnMain()

"""Prints 1 to one million"""
def one_million():
  printHeader()

  # a loop to break your computer by printing
  # a million numbers
  for num in range(1, 1000001):
    print(num)

  returnMain()

"""Prints min, max, and sum of all numbers in list 1 to 1 million"""
def summing_a_million():
  printHeader()

  nums = list(range(1, 1000001))

  print(" List Max:", max(nums))
  print(" List Min:", min(nums))
  print(" List Sum:", sum(nums))

  returnMain()
  
"""Prints od numbers between 1-20"""
def odd_numbers():
  printHeader()

  # Creates list
  nums = list(range(1, 21, 2))

  # Prints numbers
  for num in nums:
    print("", num)

  returnMain()


"""Prints multiples of 3 from 3 to 30"""
def threes():
  printHeader()

  # over complex way of getting multiples of 3, but it looks cool.
  # if a number is not a multiple of 3, replace it with a zero
  multiples = [value if (value % 3) == 0 else value-value for value in range(3,31)]

  # over complicated double-pass to remove all zeros
  i = 0
  for num in multiples:
    if num == 0:
      del multiples[i]
    i += 1
  i = 0
  for num in multiples:
    if num == 0:
      del multiples[i]
    i += 1

  # print the list
  print(multiples)

  returnMain()

"""Prints the cubes of numbers 1 to 10"""
def cubes():
  printHeader()
  nums = []

  # create list
  for x in range(1, 11):
    nums.append(x ** 3)

  # print nums
  for l in nums:
    print(l)
  
  returnMain()

"""Print cubes using list comprehension"""
def cube_comprehension():
  printHeader()

  lst = [value**3 for value in range(1, 11)]

  for x in lst:
    print(x)

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
    import independentPractice17 as foo
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
    print(" Note: In Function \'one_million\' press ctrl+c to return to menu")
    print(" (program will crash in \'Benchmark\' mode)\n")
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
  
