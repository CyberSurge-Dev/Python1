# all functions related to the game

# import utilities
from .game_utils import *
from .dopixl import *
from .inits import *

def game_over():
    pass

def finish_level():
    pass

def credits():
    """Displays the credits for the game"""
    clear_windows([screen, input_win, info_win])

    # print details
    print_title(info_win)

    info_win.addstr(15, 2, "Python 1 Final Project", curses.color_pair(1))
    info_win.addstr(16, 2, "Made by Zachary Hoover -- CyberSurge")

    info_win.addstr(18, 2, "Website:", curses.color_pair(2))
    info_win.addstr(18, 11, "https://CyberSurge.dev", curses.color_pair(1))

    info_win.addstr(19, 2, "Github:", curses.color_pair(2))
    info_win.addstr(19, 11, "https://github.com/CyberSurge-Dev", curses.color_pair(1))

    info_win.refresh()

    input_win.addstr(1, 2, "Press enter to return...", curses.color_pair(2))
    input_win.refresh()

    input_win.getch()
    return

def how_to_play():
    """Displays the rules of the game"""
    clear_windows([screen, input_win, info_win])

    # print details
    print_title(info_win)

    info_win.addstr(15, 2, "Welcome to The Final Pizza!", curses.color_pair(1))
    info_win.addstr(16, 2, "Made by Zachary Hoover -- CyberSurge")

    info_win.addstr(18, 2, "In tis game it is your objective to make pizzas as fast as possible.")
    info_win.addstr(19, 2, "You must type out each of the ingredients that the customer wants before time is up.")
    info_win.addstr(20, 2, "If you run out of time, your pizza restaurant gets shut down and the game is over.")
    info_win.addstr(22, 2, "You only get 3 attempts to spell the ingredients correctly, So good luck and have fun!")

    info_win.refresh()

    input_win.addstr(1, 2, "Press enter to return...", curses.color_pair(2))
    input_win.refresh()

    input_win.getch()

def play_level():
    """"""
