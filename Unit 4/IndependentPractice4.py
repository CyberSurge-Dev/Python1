# Zachary Hoover || Independent Practice 4
# 10-5-22

import os
import random
clear = lambda: os.system("clear" if os.name == "posix" else "cls")

# prints top header
def printHeader():
    clear()
    print("\n     Guided Practice #5   ")
    print(" ------------+------------\n")
    return

# returns to main menu, with input prompt
def returnMain():
    print("\n Press Enter to continue")
    input()
    main()

# all things in task 1
def task1():
    printHeader()

    # task 1A
    bucket = 16
    print("", bucket, " || Type || ", type(bucket))

    # task 1B
    bucket = "words"
    print("", bucket, " || Type || ", type(bucket))

    # task 1C
    bucket = "\"Word2\""
    print("", bucket, " || Type || ", type(bucket))

    # task 1D
    bucket = "12"
    print("", bucket, " || Type || ", type(bucket))

    # task 1E
    bucket = 12
    print("", bucket, " || Type || ", type(bucket))

    # task 1F
    bucket = -12
    print("", bucket, " || Type || ", type(bucket))

    # task 1G
    bucket = 12.0
    print("", bucket, " || Type || ", type(bucket))

    # task 1H
    bucket = 1.55
    print("", bucket, " || Type || ", type(bucket))

    returnMain()

# all things in task 2
def task2():
    printHeader()

    # task 2A
    var1 = random.randint(1,20)
    var2 = random.randint(1,20)
    print("", var1, "is a number,", var2, "is also a number.")

    # task 2B
    street_name = input(" What is your street name?: ")
    street_num = input(" What is your street number?: ")

    print(street_num, street_name)

    # task 2C
    print("\n Make a reservation")

    # tast 2D
    name = input(" What is your name?: ")
    peopleCount = input(" How many people are in your party?: ")
    whatTime = input(" What is the time for your reservation?: ")

    # task 2E
    min_early = "15 mins"

    print("Reservation confirmation: ")
    print(f"Training is scheduled at {whatTime} PM for the {name} group of {peopleCount} attendees. you should arive {min_early} early")

    returnMain()

def main():
    printHeader()

    print(" 1. Task 1")
    print(" 2. task 2")
    print(" 3. Exit program")

    usrIn = input(" Enter number of item: ")

    if usrIn == "1":
        task1()
    elif usrIn == "2":
        task2()
    elif usrIn == "3":
        quit()
    else:
        main()

# start of program

if __name__ == "__main__": main()