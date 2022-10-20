# Zachary hoover || Independent Practice #11
# 10-19-22
import os
from inspect import getmembers, isfunction
import random

# repeating code
###############

global clear
clear = lambda: os.system('cls')

def printHeader():
    clear()
    print("\n    Independent Practice #11   ")
    print(" -----------------+-----------------\n")
    return

def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()

################################################
# start functions here

def alien_colors1():
    printHeader()

    # chooses random alien color
    alienColor = random.choice(["green", "yellow", "red"])

    if alienColor == "green":
        print(" you got 5 poits!")
    else:
        print(" You got no points")

    returnMain()

def alien_colors1_2():
    printHeader()

    # chooses random alien color
    alienColor = "yellow"

    if alienColor == "green":
        print(" you got 5 poits!")
		
    returnMain()

def alien_colors2():
    printHeader()
    # chooses random alien color
    alienColor = random.choice(["green", "yellow", "red"])
    print(f" The alien is {alienColor}")

    if alienColor == "green":
        print(" You earned 5 points!")
    elif alienColor == "yellow!":
        print(" You earned 10 points!")
    returnMain()

def alien_colors2_2():
    printHeader()
    # chooses random alien color
    alienColor = random.choice(["green", "yellow", "red"])
    print(f" The alien is {alienColor}")

    if alienColor == "green":
        print(" You earned 5 points!")
    else:
        print(" You earned 10 points!")

    returnMain()

def alien_colors3():
    printHeader()

    # chooses random alien color
    score = 0
    alienColor = random.choice(["green", "yellow", "red"])
    print(f" The alien is {alienColor}")

    if alienColor == "green":
        score = 5
    elif alienColor == "yellow":
        score = 10
    elif alienColor == "red":
        score = 15

    print(f" You have {score} points!")

    returnMain()
    

def favorite_fruit():
	printHeader()

	favorite_fruits = [ "strawberry", "watermelon", "apple" ]

	if "bannana" in favorite_fruits:
		print("You really like bannanas!")
	elif "strawberry" in favorite_fruits:
		print("You really like strawberries!")
	elif "mango" in favorite_fruits:
		print("You really like mangos!")
	elif "watermelon" in favorite_fruits:
		print("You really like watermelons!")
	elif "apple" in favorite_fruits:
		print("You really like apples!")
	elif "tomato" in favorite_fruits:
		print("You really like tomatos! weirdo.")

	returnMain()

################################################

# auto Menu starts
# made this function to automate the menus I use in my assignments, it can also do a bit more.

menuMode = 0
currentBench = 0

def autoMenu():	
	global menuMode
	global currentBench
	global usable

	if menuMode == 1:
		if currentBench > len(usable):
			menuMode = 0
			currentBench = 0
			autoMenu()
		else:
			currentBench += 1
			usable[currentBench-1][1]()
			
			

	if menuMode == 2:
		if currentBench > len(usable):
			menuMode = 0
			currentBench = 0
			autoMenu()
		else:
			currentBench += 1
			usable[currentBench-1][1]()
	
	else:
		printHeader()

		# change were it says 'baseTemplate' to module name.
		import IndependentPractice11 as foo
		
		list = getmembers(foo, isfunction)
	
		i = 0
		x = 0
		exceptions = [
			 "autoMenu", "printHeader", "getmembers", "clear", "time", "isfunction",
			 "returnMain", "cls", "makeShirt", "makeShirt2", "describeCity"
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
			usrin = int(input("\n>> Enter number of the item: "))
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
				usable[usrin-1][1]()
		
		except:
			autoMenu()
					
# auto menu ends
#program start
autoMenu()
