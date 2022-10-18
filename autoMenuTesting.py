# Zachary hoover || auto menu v1
# 10-6-22
from distutils.log import error
import os
from inspect import getmembers, isfunction
from tkinter import E

# repeating code
###############
global clear
clear = lambda: os.system('cls')
functionErrors = []
autoMenuErrors = []

def printHeader():
    clear()
    print("\n     Independent Practice 5   ")
    print(" --------------+--------------\n")
    return

def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()

try:
################################################
# start functions here

	def func1():
		printHeader()
		print("func1")
		returnMain()

	def func2():
		printHeader()
		print("func2")
		returnMain()

	def func3():
		printHeader()
		print("func3")
		returnMain()

	def divByZero():
		5/0

################################################
except Exception as e:
	functionErrors.append(e)


# auto Menu starts
# made this function to automate the menus I use in my assignments, it can also do a bit more.
try:
	menuMode = 0
	currentBench = 0

	def autoMenu():	
		global menuMode
		global functionErrors
		global autoMenuErrors
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
			printHeader()
			print("  1. testParameters")
			print("  2. Error log")
		
		else:
			printHeader()

			# change were it says 'baseTemplate' to module name.
			import baseTemplate as foo
			
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
					usable[usrin-1][1]()
			
			except:
				autoMenu()
			##########
except Exception as e:
	autoMenuErrors.append(e)
			
		
	# auto menu ends
	#program start

autoMenu()