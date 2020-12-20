import numpy as np
import math
import fileinput

tileinputs = [group.split('\n') for group in ''.join(
    fileinput.input('data/day20.txt')).split('\n\n') if group]
seamonster = []
seamonster_height = 0
seamonster_width = 0
for i, line in enumerate(fileinput.input('data/day20.seamonster.txt')):
    for j, char in enumerate(line):
        if char == '#':
            seamonster.append((i, j))
            seamonster_height = max(seamonster_height, i)
            seamonster_width = max(seamonster_width, j)

tiles = {}
for tileinput in tileinputs:
    tile_id = int(tileinput[0].lstrip('Title ').rstrip(':'))
    tileinput = tileinput[1:]
    if len(tileinput[-1]) == 0:
        tileinput = tileinput[:-1]
    tile = np.zeros((len(tileinput), len(tileinput[0])), dtype=int)
    for i in range(len(tileinput)):
        for j in range(len(tileinput)):
            tile[i, j] = 1 if tileinput[i][j] == '#' else 0
    tiles[tile_id] = tile
side_length = math.isqrt(len(tiles))


def lside(tile):
    return tiles[tile][:, 0]


def rside(tile):
    return tiles[tile][:, -1]


def transformations(tile):
    for _ in range(2):
        for _ in range(4):
            yield tile
            tile = np.rot90(tile)
        tile = np.fliplr(tile)


def solve_one_tile(left, right, free_tiles):
    for tile in free_tiles:
        for transformation in transformations(tiles[tile]):
            tiles[tile] = transformation
            if (rside(tile) == left).all():
                return tile, "left"
            elif (lside(tile) == right).all():
                return tile, "right"


def solve_strip(start_id, free_tiles):
    strip = [start_id]
    start = tiles[start_id]
    left = start[:, 0]
    right = start[:, -1]
    for _ in range(side_length-1):
        tile, side = solve_one_tile(left, right, free_tiles - set(strip))
        if side == 'left':
            left = lside(tile)
            strip.insert(0, tile)
        else:
            right = rside(tile)
            strip.append(tile)
    return strip


def solve_board(start_id):
    free_tiles = set(tiles.keys())
    strip = solve_strip(start_id, free_tiles)
    strips = []
    free_tiles -= set(strip)
    for tile in strip:
        tiles[tile] = np.rot90(tiles[tile], 3)
        strips.append(solve_strip(tile, free_tiles))
        free_tiles -= set(strips[-1])
    return strips


def connect_board(board):
    tile_size = np.size(tiles[board[0][0]], 1) - 2
    full_size = len(board)*(tile_size)
    connected = np.zeros((full_size, full_size), dtype=int)
    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            connected[i*tile_size:(i+1)*tile_size,
                      j*tile_size:(j+1)*tile_size] = tiles[tile][1:-1, 1:-1]
    return connected


def find_monsters(board):
    monsters = []
    for i in range(np.size(board, 0)-seamonster_height+1):
        for j in range(np.size(board, 1)-seamonster_width):
            if all(map(lambda p: board[i+p[0], j+p[1]] == 1, seamonster)):
                monsters.append((i, j))
    return monsters


solved = solve_board(next(iter(tiles.keys())))
print(solved[0][0]*solved[0][-1]*solved[-1][0]*solved[-1][-1])
connected = connect_board(solved)

for trans in transformations(connected):
    monsters = find_monsters(trans)
    if len(monsters) > 0:
        print(np.sum(trans) - len(monsters)*len(seamonster))
        break
