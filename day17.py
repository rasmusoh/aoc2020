import fileinput
import numpy as np

SIZE = 25
ITERATIONS = 6
grid = np.zeros((SIZE, SIZE, SIZE, SIZE), dtype=int)
nextgrid = np.zeros((SIZE, SIZE, SIZE, SIZE), dtype=int)

for (row, line) in enumerate(fileinput.input('data/day17.txt')):
    for (col, char) in enumerate(line.rstrip()):
        grid[SIZE//2, SIZE//2, SIZE//2-1+row, SIZE //
             2-1+col] = 1 if char == '#' else 0


for _ in range(ITERATIONS):
    for (w, z, y, x), value in np.ndenumerate(grid):
        current = grid[w, z, y, x]
        nbgrid = grid[w-1:w+2, z-1:z+2, y-1:y+2, x-1:x+2]
        neighbors = np.sum(nbgrid)
        nextgrid[w, z, y, x] = 1 if neighbors == 3 or (
            neighbors == 4 and current == 1) else 0
    grid, nextgrid = nextgrid, grid
print(np.sum(grid))
