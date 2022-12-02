# Zachary Hoover || Independent Practice #21
# 12-01-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
funcName = ""


def printHeader():
  clear()
  print("\n    Independent Practice #21   ")
  print(" -----------------+-----------------")
  print(f" Function: {funcName} \n")
  return


def returnMain():
  print("\n Press Enter to continue")
  input()
  autoMenu()


################################################
# start functions here

def showMessages(messages):
  """Cylces through provided list and prints each item"""
  for m in messages:
    print(" ", m)

  return



def messages_():
  printHeader()

  # create a list of messages
  mlist = [
    "Hello, this is the first message!",
    "This one is the second message!",
    "Messages are cool.",
    "Wow, I can't belive that there is a 4th one!",
    "This is probably the last one. :("
    ]

  # send messages to be printed
  print(" Printed messages:")
  showMessages(mlist)

  

  returnMain()

def sendMessages(messages):
  """Cylces through provided list and prints each item and adds it to the list"""
  sent = []
  while messages:
    current = messages.pop()
    print(" ", current)
    sent.append(current)

  return sent

def sending_messages():
  printHeader()

  # Create a list of messages
  messages = [
    "Hello, this is the first message!",
    "This one is the second message!",
    "Messages are cool.",
    "Wow, I can't belive that there is a 4th one!",
    "This is probably the last one. :("
    ]

  # rverse the list (so items remain in order)
  messages.reverse()

  # print the messages
  print(" Printed messages:")
  sent_messages = sendMessages(messages)

  # print the lists
  print("\n Messages list:", messages)
  print("\n Sent messages list:", sent_messages)
  
  returnMain()

def archived_messages():
  printHeader()

  # create a list of messages
  messages = [
    "Hello, this is the first message!",
    "This one is the second message!",
    "Messages are cool.",
    "Wow, I can't belive that there is a 4th one!",
    "This is probably the last one. :("
    ]

  # reverse the list (so items remain in order)
  messages.reverse()

  # print messages using a copy of the ist as a parameter
  print(" Printed messages:")
  sent_messages = sendMessages(messages[:])

  
  # reverse list again so it can be in order when printed
  messages.reverse()
  
  # prints both lists, which both have items
  print("\n Messages list:", messages)
  print("\n Sent messages list:", sent_messages)
  
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
    import IndependentPractice21 as foo
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
      "showMessages",
      "sendMessages"
    ]

    usable = []

    print("NOTE: Benchmark mode will not run correctly the first time, \nrun it again and everything should work fine.")
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
