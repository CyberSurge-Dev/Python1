# Zachary Hoover || Independent Practice 2: Variables
# 9-23-22

import os
global clear
clear = lambda: os.system("clear" if os.name == "posix" else "cls")

# prints a simple message from a variable
def simpleMessage():
    clear()
    print("\n simpleMessage(): \n")
    message = " Hello! this is a simple message."
    print(message)
    message = " this is a new message!"
    print(message)
    input()
    Main()

# asks user for name, then says hello to them.
def personalMessage():
    clear()
    print("\n personalMessage(): \n")
    print(" what is your name?")
    name = input()
    print(f" Hello, {name} how are you?")
    input()
    Main()

# Asks for message. then prints it upper, lower, and title
def nameCase():
    clear()
    print("\n nameCase(): \n")
    print(" Type in a message: ")
    message = input()

    print(" Input: " + message)
    print(" upper: " + message.upper())
    print(" lower: " + message.lower())
    print(" title: " + message.title())
    input()
    Main()

#prints a famous quote
def famousQuote():
    clear()
    print("\n famousQuote(): \n")
    quote = '"The greatest glory in living lies not in never falling, but in rising every time we fall."'
    print(f" Nelson Mandela said, {quote}")
    input()
    Main()
    
# main function
def Main():
    clear()
    print(" Variable practice:")
    print("   1. simpleMessage()")
    print("   2. personalMessage()")
    print("   3. nameCase()")
    print("   4. famousQuote()")
    print("\n Input the number of the item \n------------------------------\n")

    item = input()

    if item == "1":
        simpleMessage()
        
    elif item == "2":
        personalMessage()
    elif item == "3":
        nameCase()
    elif item == "4":
        famousQuote()
    else:
        Main()

if __name__ == "__main__": Main()
