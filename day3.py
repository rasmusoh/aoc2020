import fileinput
import time
import curses
import math

treemap = [line.rstrip() for line in fileinput.input() if line.rstrip()]
pos = [0, 0]
directions = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
track = []
speed = 30


def has_tree(x, y):
    return treemap[y][x % (len(treemap[0]))] == '#'


def render_treemap(stdscr, screen_pos):
    for y in range(curses.LINES - 1):
        for x in range(curses.COLS-1):
            if y+screen_pos[1] >= len(treemap):
                stdscr.addstr(y, x, ' ')
            elif has_tree(x+screen_pos[0], y+screen_pos[1]):
                stdscr.addstr(
                    y, x, '#', curses.color_pair(curses.COLOR_GREEN))
            else:
                stdscr.addstr(y, x, '.')


def render_track(stdscr, screen_pos):
    for t in track:
        screen_x = t[0]-screen_pos[0]
        screen_y = t[1]-screen_pos[1]
        if 0 <= screen_x < curses.COLS-1 and 0 <= screen_y < curses.LINES-1:
            if has_tree(t[0], t[1]):
                stdscr.addstr(screen_y, screen_x, 'X',
                              curses.color_pair(curses.COLOR_GREEN))
            else:
                stdscr.addstr(screen_y, screen_x, 'O')


def render_toboggan(stdscr, screen_pos):
    stdscr.addstr(pos[1]-screen_pos[1], pos[0]-screen_pos[0],
                  '@', curses.color_pair(curses.COLOR_RED))


def render_total(stdscr, collisions, collisions_all):
    collisions_product = math.prod(collisions_all)
    stdscr.addstr(
        curses.LINES-1, 0, f'collisions: {collisions}, all:{collisions_all} product_total:{collisions_product}')


def main(stdscr):
    stdscr.clear()
    curses.curs_set(False)  # remove cursor highlight

    # color init
    curses.use_default_colors()
    for y in range(0, curses.COLORS):
        curses.init_pair(y, y, -1)

    collisions_all = []
    for direction in directions:
        pos[0] = 0
        pos[1] = 0
        collisions = 0
        while True:
            time.sleep(1/speed)
            pos[0] += direction[0]
            pos[1] += direction[1]
            if pos[1] >= len(treemap):
                break
            if has_tree(pos[0], pos[1]):
                collisions += 1
            track.append(pos.copy())

            maxrow = curses.LINES - 1
            maxcol = curses.COLS - 1
            screen_pos = [max(pos[0] - maxcol // 2, 0),
                          max(pos[1] - maxrow // 2, 0)]
            render_treemap(stdscr, screen_pos)
            render_track(stdscr, screen_pos)
            render_toboggan(stdscr, screen_pos)
            render_total(stdscr, collisions, collisions_all)
            stdscr.refresh()
        collisions_all.append(collisions)
        render_total(stdscr, collisions, collisions_all)
        stdscr.refresh()
    while ((ch := stdscr.getch()) == -1):  # -1 means no more input
        pass


curses.wrapper(main)
