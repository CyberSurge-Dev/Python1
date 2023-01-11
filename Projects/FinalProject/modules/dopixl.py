# dupixl -- custom mini library just to make curses a little easier to use
import curses


def add_center(screen, message, row=-1, color=curses.COLOR_WHITE):
    """Adds the given string at the center of the screen"""
    num_rows, num_cols = screen.getmaxyx()

    if (row == -1):
        middle_row = int(num_rows / 2)
    else:
        middle_row = row

    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 2)
    x_position = middle_column - half_length_of_message

    # Draw the text to screen (not refresh)
    screen.addstr(middle_row, x_position, message, color)
    return


def add_left_align(screen, message, row=0, padding=0, color=curses.COLOR_WHITE):
    """Left aligns the given string on given row with given padding on given screen (theres a trend here)"""
    screen.addstr(row, padding, message, color)
    return


def add_right_align(screen, message, row=0, padding=0, color=curses.COLOR_WHITE):
    """Right aligns the given string on given row with given padding on given screen (theres a trend here)"""
    num_rows, num_cols = screen.getmaxyx()
    screen.addstr(row, (num_cols - padding) - len(message), message, color)
    return

def clear_windows(windows):
    """Refreshes all screens passed in parameters"""
    for window in windows:
        window.clear()
        window.refresh()
    return