# Zachary hoover || Guided Practice #10
# 10-18-22
import os
from inspect import getmembers, isfunction

# repeating code
################

global clear
clear = lambda: os.system("clear" if os.name == "posix" else "cls")

def printHeader():
    clear()
    print("\n     Guided Practice #10   ")
    print(" ------------+------------\n")
    return

def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()

################################################
# start functions here

def old_Enough_To_Vote():
    printHeader()

    age = int(input(" How old are you?: "))

    if age >= 18:
        print(" you are old eough to vote!")
        print(" Have you regitered to vote yet?")
    else:
        print(" You are not old enough to vote")
        print(" You can register to vote as soon as you turn 18")

    returnMain()

def admission_Print():
    printHeader()

    age = int(input(" How old are you?: "))

    if age < 4:
        print(" Your ticet is free")
    elif age < 18:
        print(" Your admission cost is $25")
    elif age < 65:
        print(" Your admission cost is $35")
    else:
        print(" Your admission cost is $40")

    returnMain()

def admission_Var():
    printHeader()

    cost = 0
    age = int(input(" How old are you?: "))

    if age < 4:
        cost = 0
    elif age < 18:
        cost = 25
    elif age < 65:
        cost = 35
    else:
        cost = 40

    print(f" Your admission cost is ${cost}")
    returnMain()

def admission_NoElse():
    printHeader()

    cost = 0
    age = int(input(" How old are you?: "))

    if age < 4:
        cost = 0
    elif age < 18:
        cost = 25
    elif age < 65:
        cost = 40
    elif age >= 65:
        cost = 35

    print(f" Your admission cost is ${cost}")

    returnMain()

def password_Greeter():
    printHeader()

    name = input(" Enter your name: ")

    if name.upper() == "ROB":
        password = input(" Enter your password: ")
        if password == "secret":
            print(" Hello, Rob")
        else:
            print(" Begone, imposter")
    else:
        print(" You are not the right person. ")

    returnMain()

def password_Greeter_NoElse():
    printHeader()

    name = input(" Enter your name: ")

    if name.upper() == "ROB":
        password = input(" Enter your password: ")
        if password == "secret":
            print(" Hello, Rob")
    else:
        print(" You are not the right person. ")

    returnMain()

################################################

# auto Menu starts
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
		import guidedPractice11 as foo
		
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
