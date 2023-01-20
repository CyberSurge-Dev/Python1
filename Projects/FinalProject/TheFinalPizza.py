# Created By: Zachary Hoover
# Created Date: 1/9/2022
# Version: 2.43
# --------------------------------------------------------------------------------
"""
This program runs the main manu for the user.
The user will be presented with a title screen,
and wil enter a number to be sent to a function
corresponding to the option they chose.
"""
# --------------------------------------------------------------------------------
import os

# Check for user password (has to be before curses init)
while True:
    user_in = str(input("Enter passwrod: "))
    if user_in == "password":
        break

# Attempt to import curses, prompt the user to install if not
try:
    import modules.inits
except Exception as e:
    print(" Exception (for debug purposes):", e)
    print(
        " You are missing a module! (curses). Running without may crash the program"
    )
    i = input(" Do you want to install the missing module? (y/n): ")

    if (i.lower() == "y"):
        # run command to install
        os.system("pip install windows-curses")

        # restart program
        dir = os.getcwd()
        os.system(f"python {dir}")

# import content from all modules
from modules.dopixl import *
from modules.game_funcs import *
import modules.game_utils as gu
from modules.inits import *

print("[DEBUG] start called")
# --------------------------------------------------------------------------------
def main():
    """Main funcion and event handler"""

    print("[DEBUG] main called")
    if (gu.no_menu == False):
        print("[DEBUG] main run")

        # Clear all windows
        clear_windows([screen, input_win, info_win])

        # Print the main menu
        gu.print_title(info_win)

        add_left_align(info_win, "(1) Play Game", 15, 2)
        add_left_align(info_win, "(2) How to Play", 16, 2)
        add_left_align(info_win, "(3) Credits", 17, 2)
        add_left_align(info_win, "(4) Exit Game", 18, 2)

        # refresh the info window
        info_win.refresh()

        while gu.no_menu == False:
            # print 'Enter number of item:' to the console and await input
            input_win.addstr(1, 2, "Enter number of item:", curses.color_pair(2))
            user_in = input_win.getstr(1, 3 + len("Enter number of item:"))

            input_win.addstr(1, 3 + len("Enter number of item:"),
                             " " * len(user_in))

            # convert the bytes to a standard string
            i = user_in.decode("utf-8")

            if (i == "1"):
                gu.no_menu = True
                gu.generate_level()
            elif (i == "2"):
                how_to_play()
            elif (i == "3"):
                credits()
            elif (i == "4"):
                curses.endwin()
                quit()
            main()

            input_win.refresh()


if __name__ == "__main__":
    # program start
    main()
