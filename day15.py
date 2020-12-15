test = [0, 3, 6]
test2 = [1, 3, 2]
test3 = [2, 1, 3]
real = [7, 14, 0, 17, 11, 1, 2]

turns = 30000000
start = real
spoken = {number:i for i, number in enumerate(start[:-1])}
last = start[-1]
for i in range(len(start)-1, turns-1):
    if last in spoken:
        new = i - spoken[last]
        spoken[last] = i
        last = new
    else:
        spoken[last] = i
        last = 0
print(last)
