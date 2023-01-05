# Imports and color data
################################################################################

# For Clear() function
import os
# For multi-threading/timer function
import threading
# for sleep function (also for timer)
from time import sleep
import math

# Set the value of clear to be used throughout the program to clear the screen (cant belive this isnt default)
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')


# calss of color codes used in the program
class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    WHITE = "\033[0;37m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"


################################################################################
"""
Threading code (for timer)
time = threading.Thread(target=timer, args=(20, ))
time.start()
"""
# Create global variables
current_level = 1
time_remaining = 0


def print_header():
    print(Colors.BLUE + """
 ████████ ██   ██ ███████     ███████ ██ ███    ██  █████  ██
    ██    ██   ██ ██          ██      ██ ████   ██ ██   ██ ██
    ██    ███████ █████       █████   ██ ██ ██  ██ ███████ ██
    ██    ██   ██ ██          ██      ██ ██  ██ ██ ██   ██ ██
    ██    ██   ██ ███████     ██      ██ ██   ████ ██   ██ ███████""" +
          Colors.END)
    print(
        Colors.LIGHT_RED +
        """
 ██████╗ ██╗███████╗███████╗ █████╗     // ""--.._
 ██╔══██╗██║╚══███╔╝╚══███╔╝██╔══██╗    ||  (_)  _ "-._
 ██████╔╝██║  ███╔╝   ███╔╝ ███████║    ||    _ (_)    '-.
 ██╔═══╝ ██║ ███╔╝   ███╔╝  ██╔══██║    ||   (_)   __..-'
 ██║     ██║███████╗███████╗██║  ██║    \\__..--""
 ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
        """ + Colors.END)


def timer(time):
    global time_remaining
    time_remaining = time
    while (time_remaining > 0):
        sleep(1)
        time_remaining -= 1


def play_level():
    pass


def generate_level():
    global current_level

    # Get topping count based on current level (uses seemingly random progression curve)
    while True:
        topping_count = math.floor(1.1 * (math.log(current_level + 1.1813) + 2))
        print(f" Level {current_level}: {topping_count}")
        current_level += 1
        sleep(0.3)


def credits():
    # Clear screen and print the header again
    clear()
    print_header()

    print(Colors.WHITE)
    # Details on the project
    print(" Python 1 Final Project")
    print(" Made by Zachary Hoover -- CyberSurge")

    # Links to my website and github (Clickable links are dependent on the terminals capabilities)
    text = "https://www.CyberSurge.Dev"
    target = "https://cybersurge.dev"
    print("\n Website: " + f"\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\")

    text = "https://github.com/CyberSurge-Dev"
    target = "https://github.com/CyberSurge-Dev"
    print(" Github: " + f"\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\")

    # Wait for user input, then return to main()
    input("\n\n Press enter to return...")

    print(Colors.END)
    main()


def how_to_play():
    # Clear screen and print the header again
    clear()
    print_header()

    print(Colors.WHITE)

    print("""
 Welcome to The Final Pizza!

 In tis game it is your objective to make pizzas as fast as possible.
 You must type out each of the ingredients that the customer wants before time is up.
 If you run out of time, your pizza restraunt gets shut down and the game is over.

 You only get 3 attempts to spell the ingredients correctly, So good luck and have fun!
    """)

    input("\n\n Press enter to return...")

    print(Colors.END)
    main()


def main():
    # Clear the screen and print the header
    clear()
    print_header()

    # print the users options
    print(Colors.WHITE)
    print(" (1). Start Game")
    print(" (2). How to Play")
    print(" (3). Credits")
    print(" (4). Exit Game")


    # get user input and use if-elif-else to navigate program
    selected = input(Colors.BOLD + Colors.WHITE + "\n Input number of the item: " + Colors.LIGHT_BLUE)
    if (selected == "1"):
        generate_level()
    elif (selected == "2"): \
        how_to_play()
    elif (selected == "3"):
        credits()
    elif (selected == "4"):
        exit()
    else:
        main()


# if the file is not imported as a module, run the main() function
if __name__ == "__main__":
    # program start
    main()
