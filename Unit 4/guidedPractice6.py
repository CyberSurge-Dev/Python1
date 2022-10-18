# Zachary Hoover || Guided Practice #6
# 10-6-22

import os
from sqlite3 import Time
global clear
clear = lambda: os.system('cls')
import time

def returnMain():
    print("\n press any key to continue")
    input()
    main()
# prints the top header
def printHeader():
    clear()
    print("\n       Guided Practice #6       ")
    print(" --------------+---------------\n")

def eggTimer():
    printHeader()

    Time = int(input(" Eter the cooking time in seconds: "))

    print("\n put the egg in boiling water")
    time.sleep(Time)
    print(" Take the egg out of the water")

    returnMain()

def main():
    printHeader()
    print("  1. eggTimer")
    print("  2. Exit program")

    usrIn = input("\n Enter the number of the item: ")

    if usrIn == "1":
        eggTimer()
    elif usrIn == "2":
        quit()
    else:
        main()

#Program starts
#call main function
main()