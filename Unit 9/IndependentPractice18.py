# Zachary Hoover || Independent Practice #18
# 11-28-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Independent Practice #18   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def slices():
  printHeader()

  # Create list of items
  items = [ 
      "Item1", 
      "Item2",
      "item3", 
      "Super creative 4th item", 
      "This is the 5th item", 
      "Item 6", 
      "Item 7", 
      "This is the last one", 
      "Nvm, this is the last one"
  ]   

  # assign the length of the list to a variable
  length = len(items)  

  print("\n The list:", items) # prints the list
  print("\n The first three items in the list are:", items[:3]) # Prints the first 3 items in the list
  S1 = int(length/3) # Gets the start of were the middle 3 would be
  S2 = int(( (length/3) + (length/3) )) # Gets the end of were the middle 3 should be
  # Prints the middle 3 items assuming that the list is divisable by 3
  print("\n Three items from the middle of the list are:", items[S1 : S2]) 
  # Prints the last 3 ite,s
  print("\n The last three items in the list are:", items[-3:])

  returnMain()

def pizzas():
  printHeader()

  # Create a list of pizzas
  favorite_pizzas = [
    "Pepporoni Pizza",
    "Cheese Pizza",
    "\'Special\' Pizza"
  ]

  # Duplicate the list into a new list
  friends_pizzas = favorite_pizzas[:] # Does not work: friends_pizzas = favorite_pizzas

  # Adds to friends_pizzas list
  friends_pizzas.append("BBQ Pizza")
  # Adds to favorite_pizzas
  favorite_pizzas.append("Sausage pizza")

  # prints all items in favorite_pizza
  print("\n My favorite pizzas are:")
  for pizza in favorite_pizzas:
    print(" ", pizza)

  # Prints all the pizzas in friends_pizzas
  print("\n My friend's favorite pizzas:")
  for pizza in friends_pizzas:
    print(" ", pizza)

  print("\n Difference (Prints only the additions to friends list):")

  # Prints the difference between both list
  for pizza in friends_pizzas :
    if pizza not in favorite_pizzas:
      print(" ", pizza)


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
    import IndependentPractice18 as foo
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
