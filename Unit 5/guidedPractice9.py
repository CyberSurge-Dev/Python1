# Zachary hoover || guided practice 9
# 10-6-22
import os
from inspect import getmembers, isfunction


# repeating code
###############

global clear
clear = lambda: os.system("clear" if os.name == "posix" else "cls")

def printHeader():
    clear()
    print("\n     Guided Practice 9   ")
    print(" ------------+------------\n")
    return

def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()

################################################
# start functions here
def getFormatedName(first_name, last_name):
    """Return a full name, neatly formated."""
    full_name = f"{first_name} {last_name}"

    return full_name. title()

name = ""
def formated_name():
    printHeader()

	# Declare the variable global in the function to be able to read and modify it.
    global name

    firstName = input(" What is your first name?: ")
    lastName = input(" What id your last name?: ")

    name = getFormatedName(firstName, lastName)
    print(f" Your name is, {name}")

    returnMain() 

def getFormatedNameMiddle(first_name, last_name, middle_name=""):
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"

	return full_name

def formated_name_middle():
    printHeader()

	# Declare the variable global in the function to be able to read and modify it.
    global name

	# Examples
    person = getFormatedNameMiddle("Olivia", "Newton", "john")
    print(person)

    person = getFormatedName("Isaac", "Newton")
    print(person)

	#asks user for input
    firstName = input(" What is your first name?: ")
    lastName = input(" What id your last name?: ")
    middleName = input(" What is your middle name(leave blank for none)?: ")

    if middleName != "":
        name = getFormatedNameMiddle(firstName, lastName, middleName)
    else:
        name = getFormatedNameMiddle(firstName, lastName)
	
    print(f" Your name is, {name}") 

    returnMain()

################################################

# auto Menu starts
# made this function to automate the menus I use in my assignments, it can also do a bit more.

# these are global variables
menuMode = 0
currentBench = 0

def autoMenu():	

	# telling the function to use these as global variables
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
		import guidedPractice9 as foo
		
		list = getmembers(foo, isfunction)
	
		i = 0
		x = 0
		exceptions = [
			 "autoMenu", "printHeader", "getmembers", "clear", "time", "isfunction",
			 "returnMain", "cls", "getFormatedName", "getFormatedNameMiddle"
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
				usable[usrin-1][1]()
		
		except:
			autoMenu()
		
			
# auto menu ends
if __name__ == "__main__": autoMenu();
