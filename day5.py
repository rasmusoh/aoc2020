import fileinput

boarding_passes = [line.rstrip()
                   for line in fileinput.input() if line.rstrip()]

ROW_CHARS = 7
COL_CHARS = 3

ids = []
for bpass in boarding_passes:
    seat_from = 0
    seat_to = 127
    for i in range(ROW_CHARS):
        half_range = (seat_to - seat_from) // 2 + 1
        if bpass[i] == 'F':
            seat_to -= half_range
        elif bpass[i] == 'B':
            seat_from += half_range
        else:
            raise ValueError('Unrecognized char in seat')
    row = seat_from
    seat_from = 0
    seat_to = 7
    for i in range(COL_CHARS):
        half_range = (seat_to - seat_from) // 2 + 1
        if bpass[ROW_CHARS+i] == 'L':
            seat_to -= half_range
        elif bpass[ROW_CHARS+i] == 'R':
            seat_from += half_range
        else:
            raise ValueError('Unrecognized char in seat')
    col = seat_from
    ids.append(row*8+col)

ids.sort()

for i in range(len(ids)-1):
    if ids[i+1]-ids[i] == 2:
        print(ids[i]+1)
