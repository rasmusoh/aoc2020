import fileinput
from itertools import product

SIZE = 25
ITERATIONS = 6
grid = set()

for (row, line) in enumerate(fileinput.input('data/day17.txt')):
    for (col, char) in enumerate(line.rstrip()):
        if char == '#':
            grid.add((0, 0, row, col))


def get_neighbors(w, z, y, x):
    return product([w-1, w, w+1], [z-1, z, z+1], [y-1, y, y+1], [x-1, x, x+1])


for _ in range(ITERATIONS):
    nextgrid = set()
    to_process = {neighbor for point in map(
        lambda p: get_neighbors(*p), grid) for neighbor in point}
    for point in to_process:
        active = point in grid
        neighbors_active = sum(1 for n in get_neighbors(*point) if n in grid)
        if neighbors_active == 3 or (neighbors_active == 4 and active):
            nextgrid.add(point)
    grid = nextgrid

print(len(grid))
