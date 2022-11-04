# Zachary hoover || auto menu v1
# 10-6-22
from email import message
import os
from inspect import getmembers, isfunction
import random

# repeating code
###############

global clear
clear = lambda: os.system("clear" if os.name == "posix" else "cls")

def printHeader():
    clear()
    print("\n     Independent Practice 8   ")
    print(" --------------+--------------\n")
    return

def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()

################################################
# start functions here
"""
T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.  
The function should print a sentence summarizing the size of the shirt and the message printed on it.  
- Call the function once using positional arguments to make a shirt. 
- Call the function a second time using keyword arguments.
"""
def makeShirt(size, message, bypassReturn = False):
	if bypassReturn == False:
		printHeader()
		print(f" You ordered a {size} shirt with the message of \"{message}\"")
		returnMain()
	else:
		print(f" You ordered a {size} shirt with the message of \"{message}\"")
		return

def make_shirt():
	printHeader()

	# gets user input
	print("\n Buying a shirt")
	m = input(" What message do you want on the shirt?: ")
	s = input(" What size do you want the shirt to be?: ")

	# calls the function one of 2 ways
	randint = random.randint(1,2)
	if (randint == 1):
		makeShirt(s, m)
	else:
		makeShirt(message=m, size=s)


"""
Large Shirts:  Modify the make_shirt( ) function so that shirts are large by default with a message that reads 'I love Python'. 
- Make a large shirt and a medium shirt with the default message, 
- and a shirt of any size with a different message.
"""

# defaults for siza, and message
def makeShirt2(size = "large", message = "I love Python", bypassReturn = False):
	if bypassReturn == False:
		printHeader()
		print(f" You ordered a {size} shirt with the message of \"{message}\"")
		returnMain()
	else:
		print(f" You ordered a {size} shirt with the message of \"{message}\"")
		return

def large_shirts():
	printHeader()

	# gets user input
	print("\n Buying a shirt")
	m = input(" What message do you want on the shirt?(leave blank for 'I love Python'): ")
	s = input(" What size do you want the shirt to be?(leave blank for large): ")
	# checks if any user input was blank
	if (m == "" and s == ""):
		makeShirt2()
	elif (m == ""):
		makeShirt2(size = s)
	elif (s == ""):
		makeShirt2(message = m)
	else:
		makeShirt2(m, s)

"""
Cities: Write a function called describe_city( ) that accepts the name of a city and its country.  
The function should print a simple sentence, such as Harrisburg is in Pennsylvania.  Give the parameters for the country a default value.  
Call your function for three different cities, at least one of which is not in the default country,
"""

def describeCity(city, country = "The United States of America", bypassReturn = False):
	if bypassReturn == False:
		printHeader()
		print(f" {city.title()} is in {country.title()}")
		returnMain()
	else:
		print(f" {city.title()} is in {country.title()}")
		return

def describe_city():
	printHeader()

	# gets user input
	print("\n Describing a city")
	city = input(" What city?: ")
	country = input(" What country is the city in?: ")
	# checks if any user input was blank
	if (country == ""):
		describeCity(city)
	else:
		describeCity(city, country)

"""Rns assignment as intended, with no user input"""
def run_without_input():
	printHeader()

	makeShirt("Medium", "I'm a message on a shirt!", bypassReturn=True)
	makeShirt(message = "Message, but with a keyword!", size = "Large", bypassReturn=True)
	print("\n")

	makeShirt2("Medium", bypassReturn=True)
	makeShirt2("Small", "Message on a shirt", bypassReturn=True)
	makeShirt2(message="This is a message!", bypassReturn=True)
	makeShirt2(bypassReturn=True)
	print("\n")

	describeCity("Madrid", "Spain", bypassReturn=True)
	describeCity("Berlin", "Germany", bypassReturn=True)
	describeCity("Concord", bypassReturn=True)

	returnMain()
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
		import independentPractice8 as foo
		
		list = getmembers(foo, isfunction)
	
		i = 0
		x = 0
		exceptions = [
			 "autoMenu", "printHeader", "getmembers", "clear", "time", "isfunction",
			 "returnMain", "cls", "makeShirt", "makeShirt2", "describeCity"
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
			usrin = int(input("\n>> Enter number of the item: "))
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
#program start
autoMenu()
