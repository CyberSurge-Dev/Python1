# Zachary hoover || {assignmentName}
# {date}
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system('cls')

def printHeader():
    clear()
    print("{assignmentTitle}")
    print("{dashThing}")
    return

def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()

################################################
# start functions here


################################################

# auto Menu starts
benchMode = False
currentBench = 0

def autoMenu():	
	global benchMode
	global currentBench
	global usable

	if benchMode != True:

		printHeader()

		# change were it says 'baseTemplate' to module name.
		# import {moduleName} as foo
		list = []
		# {list = getmembers(foo, isfunction)}
	
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
		print(f"  {x}. Exit program")
	
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
# program start
autoMenu()
