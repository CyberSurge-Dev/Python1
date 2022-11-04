# Zachary Hoover || "Self Timer" Party Game
# 9-27-22

# import things
import os
import time
import random
global clear

clear = lambda: os.system("clear" if os.name == "posix" else "cls")

# loads the top header (made to simplify repeating code)
def loadHeader():
    clear()
    print("\n     Welcome to self time!    ")
    print(" --------------+-------------- \n")
    return

# play the game, using a random number
def game():

    # explain the rules
    loadHeader()
    
    print(" make sure everyone is standing")
    time.sleep(1)
    print(" stay standing until you think the time has ended \n\n")
    time.sleep(3)
    print(" Press Enter to start!")
    input()

    loadHeader()

    # get random number
    num = random.randint(5, 20)

    # start game
    print(" stay standing for ", num, "seconds")
    time.sleep(2)
    print(" Ready?")
    time.sleep(3)
    print(" Go!")
    time.sleep(num)
    
    
    # print times up in large font
    clear()
    print("  _______ _                                   _ ")
    print(" |__   __(_)                                 | |")
    print("    | |   _ _ __ ___   ___  ___   _   _ _ __ | |")
    print("    | |  | | '_ ` _ \ / _ \/ __| | | | | '_ \| |")
    print("    | |  | | | | | | |  __/\__ \ | |_| | |_) |_|")
    print("    |_|  |_|_| |_| |_|\___||___/  \__,_| .__/(_)")
    print("                                       | |      ")
    print("                                       |_|      ")
    print("\n")
    print(" Press Enter to continue!")
    input()
    Main()
    

# Game menu
def Main():
    loadHeader()
    print(" Enter the number of the item \n")
    print("   1. Start game")
    print("   2. Exit")
    userIn = input()

    if userIn == "1":
        game()
    elif userIn == "2":
        quit()
    else:
        Main()
        
Main()
