# Zachary hoover || Independent Practice #10
# 10-18-22
import os
from inspect import getmembers, isfunction
from random import random


# repeating code
###############

global clear
clear = lambda: os.system('cls')

def printHeader():
    clear()
    print("\n    Independent Practice #10   ")
    print(" ---------------+---------------\n")
    return

def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()

################################################
# start functions here

# asks user for age, uses simple if statemnt to show 1 of 2 results
def stages_of_life():
	printHeader()

	age = int(input(" Enter your age: "))

	if age >= 15:
		print(f" You will be {age+10} in 10 years.")
	else:
		print(f" It is good to be {age}")

	returnMain()

# Asks user for age, tells them what stage of life they are in
def stages_of_life_2():
    printHeader()
	
    age = int(input(" Enter your age: "))

    if age < 2:
        print(" You are a baby")
    elif age < 4:
        print(" You are a toddler")
    elif age < 13:
        print(" You are a kid")
    elif age < 20:
        print(" You are a teenager")
    elif age > 65:
        print(" You are an adult")
    else:
        print(" you are a senior")
	
    returnMain()

# Asks user to input the first char. of a color, prints the full color
def rainbow_colors():
    printHeader()

    userin = input(" Enter a color(R,O,Y,G,B,I,V): ")
    color = ""

    if userin.lower() == "r":
        color = "Red"
    elif userin.lower() == "o":
        color = "Orange"
    elif userin.lower() == "y":
        color = "Yellow"
    elif userin.lower() == "g":
        color = "Greed"
    elif userin.lower() == "b":
        color = "Blue"
    elif userin.lower() == "i":
        color = "Indigo"
    elif userin.lower() == "v":
        color = "Violet"
    else:
        color = "Not a Valid Color"

    print(f" the color you selceted is {color}")

    returnMain()

# Asks user for how much cheese they want.
def cheeseOrder():
        printHeader()

	# randoms did not work for some reason
        max = 20
        min = 3

        cheesePrice = 15

        print(f" The current price of cheese is ${cheesePrice} per pound")
        print(f" The current minimum weight purchable is {min} pounds")
        print(f" The current maximum weight purchable is {max} pounds")
        userin = int(input(" Enter the amount of cheese in pounds: "))

        if userin > max:
                print(" You have ordered to much cheese, please order less")
        elif userin < min:
                print(" you have ordered to little cheese, please order more.")
        else:
                print(f" You have ordered {userin} pounds of cheese costing ${userin * cheesePrice}")
	
        returnMain()


	
################################################

# auto Menu starts
# made this function to automate the menus I use in my assignments, it can also do a bit more.

benchMode = False
currentBench = 0

def autoMenu():	
	global benchMode
	global currentBench
	global usable

	if benchMode != True:

		printHeader()

		# change were it says 'baseTemplate' to module name.
		import independentPractice10 as foo
		list = []
		list = getmembers(foo, isfunction)
	
		i = 0
		x = 0
		exceptions = [
			 "autoMenu", "printHeader", "getmembers", "clear", "time", "isfunction",
			 "returnMain", "cls"
			]
		
		usable = []
		print(">>---+ Functions +---<<")
		while i < len(list):		
			if list[i][0] not in exceptions:
				x += 1
				print(f"  {x}. {list[i][0]}")
				usable.append(list[i]) 
			i += 1

		print(">>---+ Utilities +---<<")
		print(f"  {x+1}. Exit program")
		print(f"  {x+2}. Benchmark (run all)")
		print(f"  {x+3}. Debug (to be added later)")
		
		
		try:
			usrin = int(input("\n Enter number of the item: "))
			if usrin == len(usable) + 1:
				SystemExit()
			elif usrin == len(usable) + 2:
				benchMode = True
				print("Bench")
				autoMenu()
			elif usrin == len(usable) + 3:
				SystemExit()
			else:
				usable[usrin-1][1]()
		
		except:
			autoMenu()
			
	else:
		if currentBench > len(usable):
			benchMode = False
			currentBench = 0
			autoMenu()
		else:
			currentBench += 1
			usable[currentBench-1][1]()
			
# auto menu ends
# program start
autoMenu()
