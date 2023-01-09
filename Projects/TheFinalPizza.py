# Imports and color data
################################################################################

# For Clear() function
import os
# For multi-threading/timer function
import threading
# for sleep function (also for timer)
from time import sleep
import math
from random import choice

# Set the value of clear to be used throughout the program to clear the screen (cant belive this isnt default)
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
terminal_size = size = os.get_terminal_size()

# Checks if colorama is installed (program will not run without)
try:
    from colorama import init
    init()
    has_colorama = True
except Exception as e:
    print(f" Exception (for debug purposes): {e}")
    has_colorama = False


def move_to(y, x):
    """Moves cursor to specific spot in the terminal (another function thats standard in other languages.)"""
    # print("\033[{%d};{%d}H".format(y, x))
    print("\033[%d;%dH" % (y, x), end="")


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

# Create global variables for keeping track of level progression
current_level = 1
time_remaining = 0


def print_header():
    """Prints the game's ACSII title"""

    print(Colors.LIGHT_BLUE + """
 ████████ ██   ██ ███████     ███████ ██ ███    ██  █████  ██
    ██    ██   ██ ██          ██      ██ ████   ██ ██   ██ ██
    ██    ███████ █████       █████   ██ ██ ██  ██ ███████ ██
    ██    ██   ██ ██          ██      ██ ██  ██ ██ ██   ██ ██
    ██    ██   ██ ███████     ██      ██ ██   ████ ██   ██ ███████
          """ + Colors.END)

    print(Colors.LIGHT_RED + """
 ██████╗ ██╗███████╗███████╗ █████╗     // ""--.._
 ██╔══██╗██║╚══███╔╝╚══███╔╝██╔══██╗    ||  (_)  _ "-._
 ██████╔╝██║  ███╔╝   ███╔╝ ███████║    ||    _ (_)    '-.
 ██╔═══╝ ██║ ███╔╝   ███╔╝  ██╔══██║    ||   (_)   __..-'
 ██║     ██║███████╗███████╗██║  ██║    \\__..--""
 ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝""" + Colors.END)

    return

def print_pizza():
    """Prints ACSII Pizza (for game screen), this has undergone several variations"""
    print(Colors.YELLOW + f"""
          :~!7?JJJJ??7!^:
      .^7      ?7?       J?~.
    .7?J      ~~!~~         J!.
   ^J         !~~~!          J !
  ~J                   !~~~~  ? ?
 77  7!!!   J77?       ~~~~~     7
:JJ !~~~~~ ?^~~~^               7 :
7?   J?7J   ?7!7                7 7
7 ?              ?77J     !~~~! ? 7
: ?             ^~!~^J    ~~~~~ ? :
 7?    ?!!!7    J7!!?       J  ? ?
  ?    ^~!~^?        ?77       ?J
   !    ???         ^~!~^J    ?~
    .7J             J7!!?   ?!.
      .^?               J?7^.
          :~7??JJJJJ?7~^:
    """)
    return

def count_down(toppings, game_time):
    """Looks similar to game screen, but has ACSII 3,2,1 for the start of a level"""
    clear()

    print(Colors.LIGHT_RED + """
          ^7777~
         :?JJJJ!
    .:^~7?J???J!
    ~JJJJJ????J!
    ~?????????J!
     ....!J???J!
         ~J???J!
         ~J???J!
         ~J???J!
         ~J???J!
         ~JJJJJ!
         :~~~~~
    """ + Colors.END)

    # move cursor and print the gui elements
    print()
    move_to(3, 30)
    print(Colors.LIGHT_BLUE + Colors.BOLD + "Seconds Remaining:" + Colors.END)
    move_to(4, 30)
    print(Colors.WHITE + str(game_time).center(len("Seconds Remaining:")) + Colors.END)

    move_to(6, 30)
    print(Colors.LIGHT_BLUE + "Ingredients:" + Colors.END)
    x = 7
    for topping in toppings:
        move_to(x, 31)
        print(Colors.RED + "X " + topping)
        x += 1
    sleep(1)

    clear()

    print(Colors.YELLOW + """
       .:~!!77!~^:
     .~?JJJJJJJJJ?7^
    .7JJ??J???JJ??JJ!
    !J??J?~. .^?J???J:
    ?JJJJ7     ?J??J?.
    :::::.  .^?J?JJ?^
          :!?JJJJ?!:
       .~?JJJJ?7~.
     :!?JJ???!^......
    ~JJ??????????????:
   .?JJJJJJJJJJJJJJJJ:
   .77777777777777777.
    """ + Colors.END)

    # move cursor and print the gui elements
    print()
    move_to(3, 30)
    print(Colors.LIGHT_BLUE + Colors.BOLD + "Seconds Remaining:" + Colors.END)
    move_to(4, 30)
    print(Colors.WHITE + str(game_time).center(len("Seconds Remaining:")) + Colors.END)

    move_to(6, 30)
    print(Colors.LIGHT_BLUE + "Ingredients:" + Colors.END)
    x = 7
    for topping in toppings:
        move_to(x, 31)
        print(Colors.RED + "X " + topping)
        x += 1
    sleep(1)

    clear()

    print(Colors.GREEN + """
       :^~!!77!~^.
    ^7Y55PPPPPPP5Y?^
    ~YPP5YJJ?JY5P5PP7
      ~!:      .?P55P~
                7P55P~
          ~???JY5555?.
          ?PPPPP555?:
          ^!!7?Y55555!
                !P5555:
    .!J~:.     .?P55P5.
    !5PPP5YYJJJY5P5PPY^
    .^7Y55PPPPPPP5Y?~.
        .^~!!!!!~:.
          """ + Colors.END)

    # move cursor and print the gui elements
    print()
    move_to(3, 30)
    print(Colors.LIGHT_BLUE + Colors.BOLD + "Seconds Remaining:" + Colors.END)
    move_to(4, 30)
    print(Colors.WHITE + str(game_time).center(len("Seconds Remaining:")) + Colors.END)

    move_to(6, 30)
    print(Colors.LIGHT_BLUE + "Ingredients:" + Colors.END)
    x = 7
    for topping in toppings:
        move_to(x, 31)
        print(Colors.RED + "X " + topping)
        x += 1



def get_toppings(count):
    """Returns an array of random toppings based on the amount given"""

    # available toppings
    toppings = [
        "pepperoni", "mushroom", "cheese", "onion", "black olives", "green pepper",
        "garlic", "tomato", "basil", "pineapple", "salmon", "tuna", "ham",
        "turkey", "mango", "beetroot", "crab", "chocolate", "peas",
        "caramelised onion", "apple", "apple", "goat cheese"
    ]

    # return list
    return_toppings = []

    # cycle through until a complete list of the requested length is created.
    while count > 0:
        current = choice(toppings)
        if (current not in return_toppings):
            return_toppings.append(current)
            count -= 1
        else:
            # else block for readability
            continue

    return return_toppings


def timer(time):
    """
    Counts down the amount of seconds from variable 'time'.
    (This function is meant to run async to the play_level() function)
    """
    # assign the global variable time_remaining
    global time_remaining
    time_remaining = time

    # Count down every second and subtract from remaining time
    while (time_remaining > 0):
        sleep(1)
        time_remaining -= 1


def play_level(topping_count, total_time):
    """Creates a level for the play bassed on the parameters passed in by the level generator."""
    global time_remaining
    clear()

    # Get toppings for game
    toppings = get_toppings(topping_count)

    count_down(toppings, total_time)

    game_running = True

    input()


def generate_level():
    """Generates a level based on the current level."""
    global current_level

    # Get topping count based on current level (uses seemingly random progression curve)
    topping_count = math.floor(1.1 * (math.log(current_level + 1.1813) + 2) + 1)
    total_time = math.floor(-4 * (math.log(current_level + 25) - 7.5))

    play_level(topping_count, total_time)


def credits():
    """Display the games credits"""
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
    input(Colors.LIGHT_BLUE + "\n\n Press enter to return..." + Colors.END)

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
 If you run out of time, your pizza restaurant gets shut down and the game is over.

 You only get 3 attempts to spell the ingredients correctly, So good luck and have fun!
    """)

    input(Colors.LIGHT_BLUE + "\n Press enter to return..." + Colors.END)

    print(Colors.END)
    main()


def main():
    # Clear the screen and print the header
    if (has_colorama == False):
        print(" You are missing a module required to run this program (colorama)")
        i = input(Colors.LIGHT_BLUE + " would you like to install it? (y/n): ")
        if (i.lower() == "y"):
            # run pip command
            os.system("pip install colorama")
            input(Colors.LIGHT_BLUE + "\n Press enter to restart program..." + Colors.END)

            # restart program
            dir = os.getcwd()
            os.system(f"python {dir}")

    clear()
    print_header()

    # print the users options
    print(Colors.WHITE)
    print(("{:^" + str(terminal_size.columns) + "}").format("""
   (1). Start Game
   (2). How to Play
   (3). Credits
   (4). Exit Game
  """))

    # get user input and use if-elif-else to navigate program
    selected = input(Colors.BOLD + Colors.LIGHT_BLUE +
                     "\n Input number of the item: " + Colors.LIGHT_BLUE)
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


print(Colors.END)
# if the file is not imported as a module, run the main() function
if __name__ == "__main__":
    # program start
    main()
