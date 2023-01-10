# color class for easy refferance
import curses as cs
def init_colors(curses):
    curses.init_pair(1, cs.COLOR_BLUE, cs.COLOR_BLACK)
    curses.init_pair(2, cs.COLOR_RED, cs.COLOR_BLACK)
