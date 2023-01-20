# Created By: Zachary Hoover
# Created Date: 1/9/2022
# Version: 1.49
# --------------------------------------------------------------------------------
"""
This program contains a variety of functions required in the program.
These functions include the variety of text ASCII grahics used in the program.
Additionally, this is also were all non-user interface functions are contained
"""
# --------------------------------------------------------------------------------
from tkinter import Y
from .inits import *

import threading

import modules.game_funcs as gf
import modules.dopixl as dopixl

import math
import time

# --------------------------------------------------------------------------------

current_level = 1
time_remaining = 0
timer_stopped = True


# game variables
toppings = []
completed_toppings = []
strikes = 0

game_active = False
no_menu = False


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

    y = 4
    for line in lines:
        window.addstr(y, math.floor(curses.COLS * 0.15), line,
                      curses.color_pair(4))
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
    print("[DEBUG] Generate level called")

    # Get topping count based on current level (uses seemingly random progression curve)
    topping_count = math.floor(1.1 * (math.log(current_level + 1.1813) + 2) + 1)
    total_time = math.floor(-4 * (math.log(current_level + 25) - 7.5))

    # start the level
    play = threading.Thread(target=gf.play_level, args=(topping_count, total_time,))
    # gf.play_level(topping_count, total_time)
    play.start()


def print_game_data():
    """Prints the level data for the user. (now live updates because of curses windows, the only reason why I remade the entire program)"""

    # Clear previous data (to remove lingering artifacts)
    dopixl.add_right_align(info_win,
                           "     ".center(len("Seconds Remaining:")), 8,
                           math.floor(curses.COLS * 0.24), curses.color_pair(1))
    y = 14
    for topping in toppings:
        dopixl.add_right_align(
            info_win, " " * (len(topping) + 4), y,
                      math.floor(curses.COLS * 0.24) - len("seconds remaining"),
            curses.color_pair(1))

    # Update data
    dopixl.add_right_align(info_win,
                           str(time_remaining).center(len("Seconds Remaining:")),
                           8, math.floor(curses.COLS * 0.24),
                           curses.color_pair(1))
    dopixl.add_right_align(info_win,
                           f"{strikes}/3".center(len("Seconds Remaining:")), 10,
                           math.floor(curses.COLS * 0.24), curses.color_pair(1))

    y = 14
    for topping in toppings:
        if topping not in completed_toppings:
            dopixl.add_left_align(
                info_win, "✘ " + topping, y,
                          math.floor(curses.COLS * 0.76) - len("seconds remaining:"),
                curses.color_pair(3))
        else:
            dopixl.add_left_align(
                info_win, "✔ " + topping, y,
                          math.floor(curses.COLS * 0.76) - len("seconds remaining:"),
                curses.color_pair(5))
        y += 1

    # refresh the window
    info_win.refresh()


def game_tracker(timess):
    """Keeps the game stats up-to-date async to the other functions"""
    # Use global variables
    global current_level
    global timer_stopped
    global time_remaining
    global strikes
    global no_menu

    global game_active

    # set globals
    game_active = True
    time_remaining = timess
    timer_stopped = False

    print(f"[DEBUG] Thread started: game_tracker || {current_level}")

    dopixl.clear_windows([info_win])

    # Print most titles before to reduce the amound of info that needs to be updated
    print_pizza(info_win)
    dopixl.add_center(info_win, "The Final Pizza", 1, curses.color_pair(1))

    dopixl.add_right_align(info_win,
                           "Current Level:".center(len("Seconds Remaining:")), 4,
                           math.floor(curses.COLS * 0.24), curses.color_pair(2))
    dopixl.add_right_align(info_win,
                           str(current_level).center(len("Seconds Remaining:")),
                           5, math.floor(curses.COLS * 0.24),
                           curses.color_pair(1))
    dopixl.add_right_align(info_win, "Seconds Remaining:", 7,
                           math.floor(curses.COLS * 0.24), curses.color_pair(2))

    dopixl.add_right_align(info_win,
                           "Strikes:".center(len("Seconds Remaining:")), 9,
                           math.floor(curses.COLS * 0.24), curses.color_pair(2))

    dopixl.add_left_align(
        info_win, "Toppings:", 13,
        math.floor(curses.COLS * 0.76) - len("seconds remaining:"),
        curses.color_pair(2))

    info_win.refresh()

    while (game_active):
        # check game stats
        if ((strikes > 2) or (time_remaining < 1)):
            timer_stopped = True
            game_active = False

            gover = threading.Thread(target=gf.game_over, args=())
            gover.start()

            # raise exception to close thread
            print(f"[DEBUG] Thread 'closed': game_watcher || {current_level}")
            # raise Exception("Close thread"
            break

        # check if user completed the level
        elif (len(toppings) == len(completed_toppings)):
            timer_stopped = True
            game_active = False

            # start finish_level for end of level
            finlev = threading.Thread(target=gf.finish_level, args=())
            finlev.start()

            # raise exception to close thread
            print(f"[DEBUG] Thread 'closed': game_watcher || {current_level}")
            # raise Exception("Close thread")
            break
        else:
            # print the game data
            print_game_data()

        time.sleep(0.5)
    pass


def get_toppings(count):
    """Returns an array of random toppings based on the amount given"""
    from random import choice

    # available toppings
    toppss = [
        "pepperoni", "mushroom", "cheese", "onion", "black olives", "green pepper",
        "garlic", "tomato", "basil", "pineapple", "salmon", "tuna", "ham",
        "turkey", "mango", "beetroot", "crab", "chocolate", "peas",
        "caramelised onion", "apple", "goat cheese"
    ]

    # return list
    return_toppings = []

    # cycle through until a complete list of the requested length is created.
    while count > 0:
        current = choice(toppss)
        if (current not in return_toppings):
            return_toppings.append(current)
            count -= 1
        else:
            # else block for readability
            continue

    return return_toppings


def timer():
    """Counts down from the given time async to the other functions"""

    # set clock
    global time_remaining
    global timer_stopped

    print(f"[DEBUG] Thread started: timer || {current_level}")

    # count down the secconds, update time_remaining
    while (time_remaining > 0):
        time.sleep(1)
        time_remaining -= 1

        if (timer_stopped == True):
            # raise Exception("Close Thread")
            break

    print(f"[DEBUG] Thread 'closed': timer || {current_level}")
