################################################################################
# Check if user has curses, prompt to install if not.

import os

clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')

try:
    import curses
except Exception as e:
    print(" Exception (for debug purposes):", e)
    print(" You are missing a module! (curses). Running without may crash the program")
    i = input(" Do you want to install the missing module? (y/n): ")

    if (i.lower() == "y"):
        os.system("pip install windows-curses")

        # restart program
        dir = os.getcwd()
        os.system(f"python {dir}")

################################################################################
# standard imports

# For Clear() function
from operator import truediv

from pickletools import TAKEN_FROM_ARGUMENT1
# For multi-threading/timer function
import threading
# for sleep function (also for timer)
from time import sleep
import math
from random import choice
import time

# import custom modules
from modules.dopixl import *
from modules.utils import *

################################################################################
# Check if user has curses, prompt to install if not.
try:
    import curses
except Exception as e:
    print(" Exception (for debug purposes):", e)
    print(" You are missing a module! (curses). Running without may crash the program")
    i = input(" Do you want to install the missing module? (y/n): ")

    if (i.lower() == "y"):
        os.system("pip install windows-curses")

        # restart program
        dir = os.getcwd()
        os.system(f"python {dir}")

################################################################################
# Initialize curses and colors
print("Preparing to initialize screen...")
screen = curses.initscr()
num_rows, num_cols = screen.getmaxyx()
curses.start_color()
init_colors(curses)
print("Screen initialized.")


def main():
    """Main funcion and event handler"""
    try:
        add_left_align(screen, """
     ████████ ██   ██ ███████     ███████ ██ ███    ██  █████  ██
        ██    ██   ██ ██          ██      ██ ████   ██ ██   ██ ██
        ██    ███████ █████       █████   ██ ██ ██  ██ ███████ ██
        ██    ██   ██ ██          ██      ██ ██  ██ ██ ██   ██ ██
        ██    ██   ██ ███████     ██      ██ ██   ████ ██   ██ ███████
        """, 1, 0, curses.color_pair(1))

        add_left_align(screen, """
     ██████╗ ██╗███████╗███████╗ █████╗     // ""--.._
     ██╔══██╗██║╚══███╔╝╚══███╔╝██╔══██╗    ||  (_)  _ "-._
     ██████╔╝██║  ███╔╝   ███╔╝ ███████║    ||    _ (_)    '-.
     ██╔═══╝ ██║ ███╔╝   ███╔╝  ██╔══██║    ||   (_)   __..-'
     ██║     ██║███████╗███████╗██║  ██║    \\__..--""
     ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
        """, 7, 0, curses.color_pair(2))

        screen.refresh()

        

    except Exception as e:
        screen.addstr(0, 0, str(e))
        screen.refresh()



if __name__ == "__main__":
    # program start
    main()
