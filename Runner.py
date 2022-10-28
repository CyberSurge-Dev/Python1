# Zachary Hoover || File Runner v1.0
# 10-27-22

from asyncio import exceptions
import os
from re import X

global clear
clear = lambda: os.system("cls")


def main():
    clear()
    folders = [
        "Unit 3",
        "Unit 4",
        "Unit 5",
        "Unit 6",
        "Projects",
        "Other"      
    ]

    i = 0

    print(">> ----+ Folders +---- <<")
    while i < len(folders):
        print(f"  {i+1}. {folders[i]}")
        i += 1
    print(f"  {i+1}. Current Dir")

    userIN = int(input("\n Enter number of the item: "))
    if userIN == len(folders) + 1:
        usable = []
        clear()
        print(">> ----+ Files +---- <<")

        x = 1
        for filename in os.listdir():
            if filename not in folders:
                print(f"  {x}. {filename}")
                usable.append(filename)
                x += 1
        
        print("\n>> ----+ Utils +---- <<")
        print(f"  {x}. Return to menu")

        userIN = int(input("\n Enter number of the item: "))

        if (userIN > len(usable)) or (userIN < 0):
            main()
        else:
            # f"{selectedFolder}\\{usable[userIN-1]}"
            os.startfile(f"{usable[userIN-1]}")
    elif (userIN > len(folders)) or (userIN < 1):
        main()
    else:
        selectedFolder = folders[userIN-1]
        usable = []
        clear()
        print(">> ----+ Files +---- <<")
        
        i = 1
        for filename in os.listdir(folders[userIN-1]):
            print(f"  {i}. {filename}")
            usable.append(filename)
            i += 1
        
        print("\n>> ----+ Utils +---- <<")
        print(f"  {i}. Return to menu")

        userIN = int(input("\n Enter number of the item: "))

        if (userIN > len(usable)) or (userIN < 0):
            main()
        else:
            # f"{selectedFolder}\\{usable[userIN-1]}"
            os.startfile(f"{selectedFolder}\\{usable[userIN-1]}")
main()
