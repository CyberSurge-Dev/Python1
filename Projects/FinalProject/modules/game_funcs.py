# Created By: Zachary Hoover
# Created Date: 1/9/2022
# Version: 1.49
# --------------------------------------------------------------------------------
"""
This program contains all "user-interface" functions. These are functions that are
responsible for displaying and receiving to and from the user.
"""
# --------------------------------------------------------------------------------
import threading
from .inits import *
import time

import modules.game_utils as gu
import modules.dopixl as dopixl
# --------------------------------------------------------------------------------


def game_over():
    """Print game over screen"""
    curses.flushinp()

    # print game title
    dopixl.clear_windows([info_win, input_win])

    lines = [
        " ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████ ",
        "██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██",
        "██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████ ",
        "██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██",
        " ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██"
    ]

    y = 2
    for line in lines:
        info_win.addstr(y, 2, line, curses.color_pair(3))
        y += 1

    info_win.addstr(y + 1, 2, f"You made it to level: {gu.current_level}",
                    curses.color_pair(2))

    input_win.addstr(1, 2, "Press enter to return...", curses.color_pair(2))

    # reset game data
    gu.current_level = 1
    gu.no_menu = False

    info_win.refresh()
    input_win.refresh()

    # return to main
    return


def finish_level():
    """Prints level complete screen, moves the user to the next level"""
    dopixl.clear_windows([info_win, input_win])

    # print game title
    lines = [
        "██      ███████ ██    ██ ███████ ██     ",
        "██      ██      ██    ██ ██      ██     ",
        "██      █████   ██    ██ █████   ██     ",
        "██      ██       ██  ██  ██      ██     ",
        "███████ ███████   ████   ███████ ███████"
    ]

    y = 2
    for line in lines:
        info_win.addstr(y, 2, line, curses.color_pair(2))
        y += 1

    lines = [
        " ██████  ██████  ███    ███ ██████  ██      ███████ ████████ ███████ ██",
        "██      ██    ██ ████  ████ ██   ██ ██      ██         ██    ██      ██",
        "██      ██    ██ ██ ████ ██ ██████  ██      █████      ██    █████   ██",
        "██      ██    ██ ██  ██  ██ ██      ██      ██         ██    ██        ",
        " ██████  ██████  ██      ██ ██      ███████ ███████    ██    ███████ ██"
    ]

    y = 8
    for line in lines:
        info_win.addstr(y, 2, line, curses.color_pair(3))
        y += 1

    info_win.addstr(y + 1, 2, f"Next level: {gu.current_level + 1}",
                    curses.color_pair(2))
    info_win.refresh()

    input_win.addstr(1, 2, "Press enter to play next level...",
                     curses.color_pair(2))
    input_win.refresh()

    # get input, start new level
    input_win.getkey()
    curses.flushinp()

    gu.current_level += 1
    print("[DEBUG] levcom pre gen")

    # generate next level
    gu.generate_level()
    # genlev = threading.Thread(target=gu.generate_level, args=())
    # genlev.start()

    print("[DEBUG] levcom ended")


def credits():
    """Displays the credits for the game"""
    dopixl.clear_windows([screen, input_win, info_win])

    # print details
    gu.print_title(info_win)

    info_win.addstr(15, 2, "Python 1 Final Project", curses.color_pair(1))
    info_win.addstr(16, 2, "Made by Zachary Hoover -- CyberSurge")

    info_win.addstr(18, 2, "Website:", curses.color_pair(2))
    info_win.addstr(18, 11, "https://CyberSurge.dev", curses.color_pair(1))

    info_win.addstr(19, 2, "Github:", curses.color_pair(2))
    info_win.addstr(19, 11, "https://github.com/CyberSurge-Dev",
                    curses.color_pair(1))

    info_win.refresh()

    # return user to main function
    input_win.addstr(1, 2, "Press enter to return...", curses.color_pair(2))
    input_win.refresh()

    input_win.getch()
    return


def how_to_play():
    """Displays the rules of the game"""
    dopixl.clear_windows([screen, input_win, info_win])
    curses.flushinp()

    # print details
    gu.print_title(info_win)

    info_win.addstr(15, 2, "Welcome to The Final Pizza!", curses.color_pair(1))
    info_win.addstr(16, 2, "Made by Zachary Hoover -- CyberSurge")

    info_win.addstr(
        18, 2,
        "In tis game it is your objective to make pizzas as fast as possible.")
    info_win.addstr(
        19, 2,
        "You must type out each of the ingredients that the customer wants before time is up."
    )
    info_win.addstr(
        20, 2,
        "If you run out of time, your pizza restaurant gets shut down and the game is over."
    )
    info_win.addstr(
        22, 2,
        "You only get 3 attempts to spell the ingredients correctly, So good luck and have fun!"
    )

    info_win.refresh()

    # return user to main function
    input_win.addstr(1, 2, "Press enter to return...", curses.color_pair(2))
    input_win.refresh()

    input_win.getch()

    return


def play_level(topping_count, total_time):
    """Main game screen, and user input manager for the game"""

    print("[DEBUG] play_level started")

    # flush input, turn on key echo

    gu.toppings = gu.get_toppings(topping_count)
    gu.completed_toppings = []
    gu.strikes = 0

    # set threaded functions
    times = threading.Thread(target=gu.timer, args=())
    level_watcher = threading.Thread(target=gu.game_tracker, args=(total_time,))

    # start threaded funcs
    level_watcher.start()
    time.sleep(0.05)
    times.start()

    while (gu.game_active):
        # clear input window
        dopixl.clear_windows([input_win])

        # get user input
        input_win.addstr(1, 2, "Type here:", curses.color_pair(2))
        # refresh the window
        input_win.refresh()

        user_in = input_win.getstr(1, 3 + len("Type here:"))
        curses.flushinp()


        i = user_in.decode("UTF-8")

        # check if the input is valid
        if (i.lower() in gu.toppings and i.lower() not in gu.completed_toppings):
            gu.completed_toppings.append(i.lower())
        else:
            gu.strikes += 1
    print("[DEBUG] play_level ended")
