from fileinput import input
import cmath

nwse = {'N': 1j, 'S': -1j, 'W': -1, 'E': 1}

pos = 0
waypoint = 10+1j
for line in input('data/day12.txt'):
    instruction = line[0]
    units = int(line[1:])
    if instruction in nwse:
        waypoint += nwse[instruction]*units
    elif instruction == 'R':
        angle = -units*(2*cmath.pi)/360
        waypoint *= cmath.exp(angle*1j)
    elif instruction == 'L':
        angle = units*(2*cmath.pi)/360
        waypoint *= cmath.exp(angle*1j)
    elif instruction == 'F':
        pos += waypoint*units
    else:
        raise ValueError('aah')
    print(
        f'instruction:{line.rstrip():6}\t waypoint:{waypoint:6.0f}\t position:{pos:6.0f}')
total = round(abs(pos.real)+abs(pos.imag))
print(f'total:{total}')
