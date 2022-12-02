# Zachary hoover || Independent Practice #7
# 10-6-22
import os
from inspect import getmembers, isfunction

# repeating code
################

global clear
clear = lambda: os.system("clear" if os.name == "posix" else "cls")

def printHeader():
    clear()
    print("\n     Guided Practice 7   ")
    print(" ------------+------------\n")
    return

def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()

################################################
# start functions here

# dockstring function example
def dockSrings():
	printHeader()

	num1=5
	num2=9
	num3=num1 + num2

	""" Returns the sum of num1 & num2 """

	"""
	These are docstrings.

	They're like multi-line comments.
	"""

	print(num3)

	returnMain()

# Hello function example
def welcomeFuction():
	printHeader()
	print("Welcome to GFG!")
	returnMain()

	"""
	Call this function useing:

	welcomeFunction()
	"""

def greet_user():
	name = input(" What is your name?: ")
	return name

def greetUser():
	printHeader()	

	"""Display simple greeting."""
	print(f" Hello, {greet_user()}")

	returnMain()

def add (num1, num2):
		return num1 + num2

def addNums():
	printHeader()

	print(" Add 2 numbers")
	num1 = int(input(" What is your first number?: "))
	num2 = int(input(" What is your second number?: "))

	print(f" the result is {add(num1, num2)}")

	returnMain()



################################################

# auto Menu starts
# this function automates the menus I use in my assignments.

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
			benchMode = False
			currentBench = 0
			autoMenu()
		else:
			currentBench += 1
			usable[currentBench-1][1]()

	
	else:
		printHeader()

		# change were it says 'baseTemplate' to module name.
		import guidedPractice7 as foo
		
		list = getmembers(foo, isfunction)
	
		i = 0
		x = 0
		exceptions = [
			 "autoMenu", "printHeader", "getmembers", "clear", "time", "isfunction",
			 "returnMain", "cls", "greet_user", "add"
			]
		
		usable = []
		
		while i < len(list):		
			if list[i][0] not in exceptions:
				x += 1
				print(f"  {x}. {list[i][0]}")
				usable.append(list[i]) 
			i += 1


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
				# calls the function corosponding to the number inputed
				usable[usrin-1][1]()	
		except:
			autoMenu()
			
# auto menu ends
#program start

if __name__ == "__main__": autoMenu();