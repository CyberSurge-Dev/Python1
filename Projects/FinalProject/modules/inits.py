# Created By: Zachary Hoover
# Created Date: 1/9/2022
# Version: 1.49
# --------------------------------------------------------------------------------
"""
This program contains all inits to be used accross the entire program.
This program exits to keep only one instance of the curses module running.
This allows for variables like color pairs to be shared throughout the program,
rather than being assigned in each file.
"""
# --------------------------------------------------------------------------------
import curses
# --------------------------------------------------------------------------------


def init_colors(curses):
    """Initiates all color pairs for use in the program (colored text)"""
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)


# window variables for refferance in other functions (set in init_screens())
screen = curses.initscr()
input_win = curses.newwin(3, curses.COLS - 1, curses.LINES - 4, 0)
info_win = curses.newwin(curses.LINES - 5, curses.COLS - 1, 0, 0)

# Set curses to keep variables consistant
curses = curses

curses.curs_set(0)
curses.start_color()
init_colors(curses)
