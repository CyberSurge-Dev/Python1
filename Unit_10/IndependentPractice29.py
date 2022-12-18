# Zachary Hoover || Independent Practice #29
# 12-15-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Independent Practice #29   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def number_containment():
  printHeader()

  # create tuple with numbers
  T = [22, 89, 69, 78, 58, 22, 3, 74, 8, 32, 58, 8, 63, 46, 79, 9, 38]

  # prompt the user for number until the number is in the tuple
  while (True):
    print(" Guess a valid number to exit loop.")
    num = int(input(" Enter a number between 1-100: "))

    # check if num is in the tuple of numbers
    if (num in T):
      break

  print("\n You guessed the correct number!")

  returnMain()

def list_containment():
  printHeader()

  # create a list of records and a new record to check
  records = [["Colette", 22347], ["Skye", 35803], ["Alton", 45825], ["Jin", 24213]]
  new_record = ["Joana", 20294] 

  # check if record is in the previous records, print result
  if (new_record in records):
    print(f" {new_record} is in records")
  else:
    print(f" {new_record} is not in records")

  returnMain()

def string_containment():
  printHeader()

  # Create a tupe of vowels
  vowels = ("a", "e", "i", "o", "u")

  # prompt user to enter a character until it is in the list
  while (True):
    print(" Enter the correct character to exit loop")
    char = input(" Enter a letter:")

    # check if given char is in vowels
    if (char in vowels):
      break
    else:
      print(" Incorrect! please try again")

  print(" You guessed correctly!")

  returnMain()

def operator_precedence():
  printHeader()

  # Equation modified to be true and print result
  A = ((6 + 2) < 9) == True
  print(" A: ", A)

  # Equation modified to be true and print result
  B = 3 ** (2 + 1) >= (3 * 8) + 1
  print(" B: ", B)

  # Equation modified to be true and print result
  C = (5 + 3) * 2 == 16
  print(" C: ", C)
  # Equation modified to be true and print result
  D = ((4 > 3) and (5 + 6 > 7)) == True
  print(" D: ", D)

  returnMain()

def boolean_values():
  printHeader()

  # create variables x and y for opperations
  x = 84
  y = 17

  # Three expressions equivilent to x >= y and print the result
  E1 =  ((x ** y)/3) * 2 >=((y/29) + 4)
  print(" E1: ", E1)

  E2 = (((x*32)/7) - 6) * 9 >= ((y*3)/27 + 3)
  print(" E2: ", E2)

  E3 = (x*5)/3 >= ((y/7) + 4) 
  print(" E3: ", E3)
  
  # Three expressions equivilent to x <= y and print the result
  print("")

  E1 =  (x ** 4)/3 <= (y * x) ** 2
  print(" E1-2: ", E1)

  E2 = ((x ** 12)/2) * 19 <= ((y ** (x/22))/102) + 5
  print(" E2-2: ", E2)

  E3 = (x ** (10*y)) + 321 <= ((y ** 5)/32) + 69
  print(" E3-2: ", E3)

  returnMain()

def boolen_operators():
  printHeader()

  # Create x and y variables for opperations
  x = True
  y = False

  # Three expressions equivilent to True and print the result
  E1 =  (x == y) or (x == (not y))
  print(" E1: ", E1)

  E2 = y == (not x) and y == y
  print(" E2: ", E2)

  E3 = y == ((not x) and x == (not y)) or (x != y) and (y != x)
  print(" E3: ", E3)
  
  # Three expressions equivilent to False and print the result
  print("")

  E1 =  y == x or (x == (not x) and y == (not y))
  print(" E1-2: ", E1)

  E2 = y == (not x != ( not y) or x != y)
  print(" E2-2: ", E2)

  E3 = x == ((y != y) or (x != x)) and ((y != x) or (x != x))
  print(" E3-2: ", E3)

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
    import IndependentPractice29 as foo
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
