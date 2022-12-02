# Zachary hoover || auto menu v1
# 10-6-22
import os
import random
from inspect import getmembers, isfunction

# repeating code
###############

global clear
clear = lambda: os.system("clear" if os.name == "posix" else "cls")

def printHeader():
    clear()
    print("\n     Independent Practice 5   ")
    print(" --------------+--------------\n")
    return

def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()

################################################
# start functions here

# task 1
def rentalCar():
    printHeader()

    print(" Rental car")
    car = input("\n What car do you want?: ")

    print(f" lets see if we can find you a {car}")

    returnMain()

# task 2
def restrauntSeating():
    printHeader()

    print(" Resturant Seating")
    people = int(input("\n How many people are in your group?: "))


    time = random.randint(1,60)
    if people > 8:
        print(f" Sorry, you will have to wait {time} minutes for your table")
    else:
        print(" you can head to your table now.")

    returnMain()

# task 3
def tallEnough():
    printHeader()
    print(" are you tall enought to ride? ")

    height = int(input("\n how tall are you?(in): "))

    if height > 48:
        print("\n you are tall enough to ride!")
    else:
        print("\n You are not tall enough :(")
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
		import independentPractice5 as foo
		
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
if __name__ == "__main__": autoMenu();