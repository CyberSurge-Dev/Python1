# Zachary Hoover || File Runner v1.0
# 10-27-22

import os

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
    print(f"  {i}. Current Dir")

    userIN = int(input("\n Enter number of the item: "))
    if (userIN > len(folders)) or (userIN < 1):
        main()
    else:
        usable = []
        clear()
        print(">> ----+ Files +---- <<")
        i = 1
        for filename in os.listdir(folders[i-1]):
            print(f"  {i}. {filename}")
            usable.append(filename)
            i += 1
        
        print("\n>> ----+ Utils +---- <<")
        print(f"  {i}. Return to menu")

        userIN = int(input("\n Enter number of the item: "))

        if (userIN > len(usable)) or (userIN < 0):
            main()
        else:
            exec(open(usable[userIN-1]).read())
main()
