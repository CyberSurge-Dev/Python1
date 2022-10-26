# Zachary Hoover || Python Project 1
# 10-24-22


################+ IMPORTANT +################
#                                           #
# This program runs better in a terminal    #
#                                           #
# The screen clearing and Loading bar will  #
# only run inside of a terminal. without    #
# this, you may see some weird text         #
# related issues in the IDLE terminal.      #
#                                           #
################+ IMPORTANT +################


import os
# repeating code
###############

clear = lambda: os.system('cls')
import time
import random

# Header: Clear screen, print title, return to call
def printHeader():
    clear()
    print("\n   Thrill of the Jungle Theme Park!   ")
    print(" ------------------+-----------------\n")
    return

# Return to main: asks user to press enter, then returns user to the main function
def returnMain():
    print("\n Press Enter to continue")
    input()
    main()

##############
# Functions Start Here

"""
Each function will give the user a brief description of the ride, and the rides minimum age
Each function will then ask the user for there age, and tell them if they are able to ride
At the end of the function the user will be asked to go back to the main menu
"""

# This function tells the user about the ride: Scenic River Cruise
def scenicRiverCruise():
    # Prints top Header 
    printHeader()

    print(""" You have selected Scenic River Cruise

 This ride will take you on a calming trip through the river,
 you will see wide variety of the local wildlife, and enjoy
 the beautiful scenic views of the river.

 There is no age limit for this ride.
 """)

    # Returns user to the main menu
    returnMain()

# This function tells the user about the ride: Carnival Carousel
def carnivalCarousel():
    # Prints top Header 
    printHeader()
    
    print(""" You have selected Carnival Carousel

 This ride is the classic experience of a carousel, with a twist.
 This ride brings a new experience by giving the rider a scenic jungle experience
 
 You must be at least 3 years old to ride
 """)
    age = int(input(" What is your age?: "))
    if age < 3:
        print("\n Sorry, You are not old enough to ride this ride.")
    else:
        print("\n You are old enough to ride Carnival Carousel.")

    # Returns user to the main menu
    returnMain()


# This function tells the user about the ride: Jungle Adventure Water Splash
def jungleAdventureWaterSplash():
    # Prints top Header 
    printHeader()

    print(""" You have selected Jungle Adventure Water Splash

 This ride brings you on a thrilling adventure through a realistic jungle.
 You will venture up and down thrilling hills as a researcher searching for
 the infamous river monster. Who knows, you may finally complete the research.

 You must be at least 6 years old to ride
 """)
    age = int(input(" What is your age?: "))
    if age < 6:
        print("\n Sorry, You are not old enough to ride Jungle Adventure Water Splash.")
    else:
        print("\n You are old enough to ride Jungle Adventure Water Splash.")

    # Returns user to the main menu
    returnMain()


# This function tells the user about the ride: Downhill Mountain Run
def downhillMountainRun():
    # Prints top Header 
    printHeader()

    print(""" You have selected Downhill Mountain Run

 This ride will take you on a thrilling adventure around a realistic jungle
 whilst fleeing from the creatures of the jungle. You will be taken around
 thrivilling twists and turns, and jaw dropping drops.
 
 You must be at least 12 years old to ride
 """)
    age = int(input(" What is your age?: "))
    if age < 12:
        print("\n Sorry, You are not old enough to ride Downhill Mountain Run.")
    else:
        print("\n You are old enough to ride Jungle Downhill Mountain Run.")

    # Returns user to the main menu
    returnMain()


# This function tells the user about the ride: The Regurgitator
def theRegurgitator():
    # Prints top Header 
    printHeader()

    print(""" You have selected The Regurgitator

 This ride is the most thrilling in the park, you will be taken on a trip
 like no other, twisting around invigorating turns, and invigorating loops.
 If you love the thrill of the jungle, this ride is for you.
 
 You must be at least 12 years old and less than 70 years old to ride
 """)
    age = int(input(" What is your age?: "))
    if age < 12:
        print("\n Sorry, You are not old enough to ride The Regurgitator.")
    elif age >= 70:
        print("\n Sorry, You are too old to ride The Regurgitator.")
    else:
        print("\n You are old enough to ride The Regurgitator.")

    # Returns user to the main menu
    returnMain()


# This function tells the user about the ride: Jungle Jam
def jungleJam():
    # Prints top Header 
    printHeader()

    print(""" You have selected Jungle Jam

  Jungle Jam puts an interesting twist on the normal bumper cars ride.
  in this ride you will coast around a closed jungle themed area, with
  the goal of bumping your fellow riders out of there cars. 

 You must be at least 10 years old to ride
 """)
    age = int(input(" What is your age?: "))
    if age < 10:
        print("\n Sorry, You are not old enough to ride Jungle Jam.")
    else:
        print("\n You are old enough to ride Jungle Jam.")

    # Returns user to the main menu
    returnMain()


# This function tells the user about the ride: River Creek Bash
def riverCreekBash():
    # Prints top Header 
    printHeader()

    print(""" You have selected River Creek Bash

 In this thrilling ride you will ride around on your own personal jungle raft.
 You will move across the creek on your own self guided tour of the beautiful
 wildlife of the park.

 You must be at least 15 years old to ride alone, or at least 3 with an elgible driver
 """)
    age = int(input(" What is your age?: "))
    if age < 15:
        if age > 3:
            userIN = input("\n Do you have an eligible driver with you? (y/n): ")
            if userIN.lower() == "n":
                print(" Sorry, You are not old enough to ride River Creek Bash. ")
            else:
                print(" You are able to ride this ride with your eligible drive")     
        else:
            print(" Sorry, You are not old enough to ride River Creek Bash. ")
    else:
        print("\n You are old enough to ride River Creek Bash.")

    # Returns user to the main menu
    returnMain()


# This function tells the user about the ride: Crocodile Cruise
def crocodileCruise():
    # Prints top Header 
    printHeader()

    print(""" You have selected Crocodile Cruise

 The Crocodile Cruise is one of 2 of the guided cruises we offer at our
 park; But, it is one you won't want to miss, on this tour you will explore
 the river with your guide searching for the crocodiles native to the area.

 You must be at least 3 years old to ride
 """)
    age = int(input(" What is your age?: "))
    if age < 3:
        print("\n Sorry, You are not old enough to ride Crocodile Cruise.")
    else:
        print("\n You are old enough to ride Crocodile Cruise.")

    # Returns user to the main menu
    returnMain()


# This function tells the user about the ride: Blue Lagoon
def blueLagoon():
    # Prints top Header 
    printHeader()

    print(""" You have selected Blue Lagoon

 Blue lagoon is the largest water ride we have at our park, you will be taken
 on a thrilling ride down twists and turns to reach the Blue Lagoon at the bottom
 of the slide.
 
 You must be at least 5 years old to ride
 """)
    age = int(input(" What is your age?: "))
    if age < 5:
        print("\n Sorry, You are not old enough to ride Blue Lagoon.")
    else:
        print("\n You are old enough to ride Blue Lagoon.")

    # Returns user to the main menu
    returnMain()


# This function tells the user about the ride: Ancient Artifacts
def ancientArtifacts():
    # Prints top Header 
    printHeader()

    print(""" You have selected Ancient Artifacts

 Ancient Artifacts is an interactive ride were you venture through
 the chasms of a jungle temple looking for the treasures hidden inside.
 If you return from the ride with the mysterious golden goblet (one per ride group)
 you will receive a prize.

 You must be at least 4 years old to ride
 """)
    age = int(input(" What is your age?: "))
    if age < 4:
        print("\n Sorry, You are not old enough to ride Ancient Artifacts.")
    else:
        print("\n You are old enough to ride Ancient Artifacts.")

    # Returns user to the main menu
    returnMain()


##############


"""
Main function, gives user a list of objects and asks
them to enter the number of the item they want to go to.
calls function user wants to go to.
"""
def main():
    # Prints the programs top header
    printHeader()
    # prints out all of the users options
    print("""   1. Scenic River Cruise
   2. Carnival Carousel
   3. Jungle Adventure Water Splash
   4. Downhill Mountain Run
   5. The Regurgitator
   6. Jungle Jam
   7. River Creek Bash
   8. Crocodile Cruise
   9. Blue lagoon
   10. Ancient Artifacts
          """)

    # asks the user to enter the number of the item
    userIN = input(" Enter the ride that you want: ")

    # Directs user to the Scenic River Cruise function
    if userIN == "1":
        scenicRiverCruise()
        
    # Directs user to the Carnival Carousel function
    elif userIN == "2":
        carnivalCarousel()

    # Directs user to the Jungle Adventure Water Splash function
    elif userIN == "3":
        jungleAdventureWaterSplash()

    # Directs user to the Downhill Mountain Run function
    elif userIN == "4":
        downhillMountainRun()

    # Directs user to the Regurgitator function
    elif userIN == "5":
        theRegurgitator()

    # Directs user to the Jungle Jam function
    elif userIN == "6":
        jungleJam()

    # Directs user to the River Creek Bash function
    elif userIN == "7":
        riverCreekBash()

    # Directs user to the Crocodile Cruise function
    elif userIN == "8":
        crocodileCruise()

    # Directs user to the Blue Lagoon function
    elif userIN == "9":
        blueLagoon()

    # Directs user to the Ancient Artifacts function
    elif userIN == "10":
        ancientArtifacts()

    # if the input is invalid this resets the menu
    else:
        main()


# loading bar at the begining of the program
loadingBar = 0
print("              Loading...             ")
#      [###################################]
while loadingBar < 36:
    # Draws the bar ("end = "\r" is an optinal parameter for the print method. It is used to
    # add something to the end of a line after it has been run. Here it is used to move the cursor
    # back to the begining of the line.)
    print(" [" + "#" * loadingBar + " " * (34 - loadingBar) + "]", end = '\r')
    # pause time between each segment
    time.sleep(random.uniform(0.001, 0.2))
    loadingBar += 1
isLoading = False
main()
