# Zachary hoover || auto menu v1
# 10-6-22
import os
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system("clear" if os.name == "posix" else "cls")

def printHeader():
    clear()
    print("\n     Guided Practice 8   ")
    print(" ------------+------------\n")
    return

def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()

################################################
# start functions here

"""Describe pet functions"""
def describePet(animal_type, animal_name):
	printHeader()

	print(f"\n you have a {animal_type}")
	print(f"\n your {animal_type}'s name is {animal_name.title()}")

	returnMain()

def describe_pet():
	printHeader()

	animalType = input("\n what is your pet?: ")
	animalName = input("\n what is your pets name?: ")

	describePet(animalType, animalName)

def describe_pet2():
	describePet("Fipps", "dog") # positional variables

def keywords_describePet():
	describePet(animal_name="Fipps", animal_type="dog")



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
		currentBench += 1
		if currentBench > len(usable):
			menuMode = 0
			currentBench = 0
			autoMenu()
		else:		
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
		import guidedPractice8 as foo
		
		list = getmembers(foo, isfunction)
	
		i = 0
		x = 0
		exceptions = [
			 "autoMenu", "printHeader", "getmembers", "clear", "time", "isfunction",
			 "returnMain", "cls", "describePet"
			]
		
		usable = []
		
		print("\n>> ----+ Functions +---- <<")
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
				usable[usrin-1][1]()
		
		except:
			autoMenu()
		##########
		
			
# auto menu ends
#program start
autoMenu()