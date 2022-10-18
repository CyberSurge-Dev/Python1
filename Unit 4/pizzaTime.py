# Zachary hoover || Pizza Time!
# 10-7-22

# imports
from asyncore import ExitNow
import os
from inspect import getmembers, isfunction
from tkinter import END

# basic repeating code
global clear
clear = lambda: os.system('cls')

def printHeader():
    clear()
    print("\n           Pizza Time!        ")
    print(" ---------------+--------------\n")
    return

def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()

# start functions here
#############################################################

# pizza order calculator 
def pizzaOrderCalc():
	printHeader()
	try:
		students_int = int(input(" How many students?: "))
		pizza_count = (students_int / 1.5)

		if students_int % 3 != 0:
			pizza_count += 1

		print(f" you will need {pizza_count} pizzas")

		returnMain()
	except:
		pizzaOrderCalc()

def moduloTesting():
	printHeader()

	number = input(" Enter a number, and I'll tell you if it's even or odd: ")
	number = int(number)

	if number % 2 == 0:
		print(f"\nThe number {number} is even.")
	else:
		print(f"\nThe number {number} is odd.")

	returnMain()
#############################################################

# auto Menu starts
# made this function to automate the menus I use in my assignments

benchMode = False
currentBench = 0

def autoMenu():	
	global benchMode
	global currentBench
	global usable

	printHeader()

	if benchMode != True:
		# change were it says 'baseTemplate' to module name.
		import pizzaTime as foo
		
		list = getmembers(foo, isfunction)
	
		i = 0
		x = 0
		exceptions = [
			 "autoMenu", "printHeader", "getmembers", "clear", "time", "isfunction",
			 "returnMain", "cls"
			]
		
		usable = []
		
		while i < len(list):		
			if list[i][0] not in exceptions:
				x += 1
				print(f"  {x}. {list[i][0]}")
				usable.append(list[i]) 
			i += 1
	
		x += 1
		print(f"  {x}. Exit program (enter twice to confirm)")
	
		x += 1
		print(f"  {x}. Benchmark (run all)")
	
		x += 1
		print(f"  {x}. Debug (to be added later)")
		
		
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
#program start
autoMenu()