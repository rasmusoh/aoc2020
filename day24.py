import fileinput

directions = {
    'nw': (0, 1, -1),
    'ne': (1, 0, -1),
    'e': (1, -1, 0),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1),
    'w': (-1, 1, 0)
}

# part 1
black = set()
for line in fileinput.input('data/day24.txt'):
    lineiter = iter(line.rstrip())
    pos = [0, 0, 0]
    for d in lineiter:
        if d == 'n' or d == 's':
            d += next(lineiter)
        direction = directions[d]
        pos[0] += direction[0]
        pos[1] += direction[1]
        pos[2] += direction[2]
    pos = tuple(pos)
    if pos in black:
        black.remove(pos)
    else:
        black.add(pos)
print(len(black))

# part 2


def neighbors(tile):
    for direction in directions:
        d = directions[direction]
        yield (tile[0]+d[0], tile[1]+d[1], tile[2]+d[2])


for i in range(100):
    nextblack = set()
    to_process = black | {neighbor for point in map(
        lambda p: neighbors(p), black) for neighbor in point}
    for point in to_process:
        point_black = point in black
        neighbors_black = sum(1 for n in neighbors(point) if n in black)
        if (point_black and 0 < neighbors_black <= 2) or (
                not point_black and neighbors_black == 2):
            nextblack.add(point)
    black = nextblack
    print(f'Day {i+1}: {len(black)}')
