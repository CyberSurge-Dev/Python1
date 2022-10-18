# Zachary hoover || Independent Practice #10
# 10-18-22
import os
from inspect import getmembers, isfunction

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

def stages_of_life():
	printHeader()

	age = int(input(" Enter your age: "))

	if age >= 15:
		print(f" You will be {age+10} in 10 years.")
	else:
		print(f" It is good to be {age}")

	returnMain()

def stages_of_life_2():
	printHeader()
	age = int(input(" Enter your age: "))

	if age < 2:
		print(" You are a baby")
	elif age > 2:
		continue
	
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
