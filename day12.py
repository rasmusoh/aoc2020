from fileinput import input
import time
import curses
import math

SPEED = 2
directions = ['N', 'E', 'S', 'W']
nwse = {'N': (0, -1), 'S': (0, 1), 'W': (-1, 0), 'E': (1, 0)}
pos = [0, 0]
waypoint = [10, -1]

for line in input('data/day12.txt'):
    instruction = line[0]
    amount = int(line[1:])
    if instruction in nwse:
        waypoint[0] += nwse[instruction][0]*amount
        waypoint[1] += nwse[instruction][1]*amount
    elif instruction == 'R' or instruction == 'L':
        angle = amount*(2*math.pi)/360
        angle = angle if instruction == 'R' else -angle
        waypoint = [waypoint[0]*round(math.cos(angle)) -
                    waypoint[1]*round(math.sin(angle)),
                    waypoint[0] * round(math.sin(angle)) +
                    waypoint[1]*round(math.cos(angle))]
    elif instruction == 'F':
        pos[0] += waypoint[0]*amount
        pos[1] += waypoint[1]*amount
    else:
        raise ValueError('aah')
    print(
        f'instruction:{line.rstrip()}\t waypoint:{waypoint}\t position:{pos}')
print(f'total:{abs(pos[0])+abs(pos[1])}')
