################################################################################
# Check if user has curses, prompt to install if not.

import os

try:
    import modules.inits
except Exception as e:
    print(" Exception (for debug purposes):", e)
    print(
        " You are missing a module! (curses). Running without may crash the program"
    )
    i = input(" Do you want to install the missing module? (y/n): ")

    if (i.lower() == "y"):
        os.system("pip install windows-curses")

        # restart program
        dir = os.getcwd()
        os.system(f"python {dir}")

################################################################################
# standard imports

# import custom modules
from modules.dopixl import *
from modules.game_funcs import *
from modules.game_utils import *
from modules.inits import *


################################################################################


def test_func():
    screen.clear()
    screen.addstr(2, 2, "Thing called", curses.color_pair(1))

    screen.refresh()
    input_win.refresh()
    input_win.getch()

    main()


def main():
    """Main funcion and event handler"""
    try:
        # Clear all windows
        clear_windows([screen, input_win, info_win])

        # Print the main menu
        print_title(info_win)

        add_left_align(info_win, "(1) Play Game", 15, 2)
        add_left_align(info_win, "(2) How to Play", 16, 2)
        add_left_align(info_win, "(3) Credits", 17, 2)
        add_left_align(info_win, "(4) Exit Game", 18, 2)

        # refresh the info window
        info_win.refresh()

        while True:
            # print 'Enter number of item:' to the console and await input
            input_win.addstr(1, 2, "Enter number of item:", curses.color_pair(2))
            user_in = input_win.getstr(1, 3 + len("Enter number of item:"))

            input_win.addstr(1, 3 + len("Enter number of item:"), " " * len(user_in))

            # convert the bytes to a standard string
            i = user_in.decode("utf-8")

            if (i == "1"):
                generate_level()
            elif (i == "2"):
                how_to_play()
            elif (i == "3"):
                credits()
            elif (i == "4"):
                curses.endwin()
                quit()

            main()

            input_win.refresh()

    except Exception as e:
        screen.addstr(0, 0, str(e))
        screen.refresh()


if __name__ == "__main__":
    # program start
    main()
