from fileinput import input
import os
from time import sleep
from copy import deepcopy

seatmap = [list(line.rstrip())for line in input(
    'data/day11.txt') if line.rstrip()]

SPEED = 30

directions = {(1, 0), (1, 1), (0, 1), (-1, 1),
              (-1, 0), (-1, -1), (0, -1), (1, -1)}


def total_occupied(seats):
    return len([seat for row in seats
                for seat in row if seat == '#'])


def look_direction(seats, x, y, direction):
    while True:
        x += direction[0]
        y += direction[1]
        if not (0 <= x < len(seats[0]) and 0 <= y < len(seats)):
            return 0
        if seats[y][x] == 'L':
            return 0
        if seats[y][x] == '#':
            return 1


def update_map(seats):
    new = deepcopy(seats)
    for y in range(len(seats)):
        for x in range(len(seats[0])):
            if seats[y][x] == '.':
                continue
            occupied = 0
            for direction in directions:
                occupied += look_direction(seatmap, x, y, direction)
            if occupied == 0:
                new[y][x] = '#'
            elif occupied >= 5:
                new[y][x] = 'L'
    return new


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in seatmap:
        print(''.join(row))
    print(f'occupied:{total_occupied(seatmap)}')
    new_map = update_map(seatmap)
    if new_map == seatmap:
        break
    seatmap = new_map
    sleep(1/SPEED)
