from fileinput import input
from time import sleep
import curses

seatmap = [line.rstrip() for line in input(
    'data/day11.test.txt') if line.rstrip()]

SPEED = 10


def update_map(seats):
    new = [x[:] for x in seats]
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            adjacent_i = slice(max( i-1, 0), min(i+2, len(seats)))
            adjacent_j = slice(max( j-1, 0), min(j+2, len(seats[0])))
            surroundings = seats[adjacent_i][adjacent_j]
            print(surroundings)


def main(stdscr):
    stdscr.clear()
    curses.curs_set(False)  # remove cursor highlight

    while True:
        for i in range(len(seatmap)):
            stdscr.addstr(i, 0, seatmap[i])
        stdscr.refresh()
        sleep(1/SPEED)
        seatmap = update_map(seatmap)
    stdscr.refresh()

    while ((ch := stdscr.getch()) == -1):  # -1 means no more input
        pass


#curses.wrapper(main)
update_map(seatmap)
