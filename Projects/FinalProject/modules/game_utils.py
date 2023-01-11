# contains all printable titles, and screens
from .dopixl import *
from .inits import curses
from .game_funcs import *
import math
import time

current_level = 1
time_remaining = 0
timer_stopped = False


def print_pizza(window):
    """Prints the pizza"""
    lines = [
        "          :~!7?JJJJ??7!^:          ",
        "      .^7      ?7?       J?~.      ",
        "    .7?J      ~~!~~         J!.    ",
        "   ^J         !~~~!          J !   ",
        "  ~J                   !~~~~  ? ?  ",
        " 77  7!!!   J77?       ~~~~~     7 ",
        ":JJ !~~~~~ ?^~~~^               7 :",
        "7?   J?7J   ?7!7                7 7",
        "7 ?              ?77J     !~~~! ? 7",
        ": ?             ^~!~^J    ~~~~~ ? :",
        " 7?    ?!!!7    J7!!?       J  ? ? ",
        "  ?    ^~!~^?        ?77       ?J  ",
        "   !    ???         ^~!~^J    ?~   ",
        "    .7J             J7!!?   ?!.    ",
        "      .^?               J?7^.      ",
        "          :~7??JJJJJ?7~^:          "
    ]

    y = 2
    for line in lines:
        window.addstr(y, 2, line, curses.color_pair(4))
        y += 1


def print_title(window):
    """Prints the games header"""
    lines = [
        "████████ ██   ██ ███████     ███████ ██ ███    ██  █████  ██     ",
        "   ██    ██   ██ ██          ██      ██ ████   ██ ██   ██ ██     ",
        "   ██    ███████ █████       █████   ██ ██ ██  ██ ███████ ██     ",
        "   ██    ██   ██ ██          ██      ██ ██  ██ ██ ██   ██ ██     ",
        "   ██    ██   ██ ███████     ██      ██ ██   ████ ██   ██ ███████"
    ]

    y = 2
    for line in lines:
        window.addstr(y, 2, line, curses.color_pair(2))
        y += 1

    lines = [
        "██████╗ ██╗███████╗███████╗ █████╗     // \"\"--.._      ",
        "██╔══██╗██║╚══███╔╝╚══███╔╝██╔══██╗    ||  (_)  _ \"-._  ",
        "██████╔╝██║  ███╔╝   ███╔╝ ███████║    ||    _ (_)    '-.",
        "██╔═══╝ ██║ ███╔╝   ███╔╝  ██╔══██║    ||   (_)   __..-' ",
        "██║     ██║███████╗███████╗██║  ██║    \\__..--\"\"      ",
        "╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝                      "
    ]
    y += 1
    for line in lines:
        window.addstr(y, 2, line, curses.color_pair(3))
        y += 1


def generate_level():
    """Generates the game data based on the current level."""
    global current_level

    # Get topping count based on current level (uses seemingly random progression curve)
    topping_count = math.floor(1.1 * (math.log(current_level + 1.1813) + 2) + 1)
    total_time = math.floor(-4 * (math.log(current_level + 25) - 7.5))

    play_level(topping_count, total_time)

def print_game_data():
    pass

def game_tracker():
    """Keeps the game stats up-to-date async to the other functions"""
    pass

def timer(time):
    """Counts down from the given time async to the other functions"""

    # set clock
    global time_remaining
    time_remaining = time

    # count down the secconds, update time_remaining
    while (time_remaining > 0):
        time.sleep(1)
        time_remaining -= 1

        if (timer_stopped == True):
            break
    game_over()
