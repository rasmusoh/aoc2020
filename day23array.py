import time

test = '389125467'
real = '589174263'


def setup(numbers):
    cups = [0]*len(numbers)
    for i, cup in enumerate(numbers):
        cups[cup-1] = numbers[(i+1) % len(numbers)] - 1
    return cups


def move(cups, start, moves):
    current = start
    for _ in range(moves):
        pickup1 = cups[current]
        pickup2 = cups[pickup1]
        pickup3 = cups[pickup2]
        cups[current] = cups[pickup3]
        dest = current
        while True:
            dest = (dest-1) % len(cups)
            if dest not in [pickup1, pickup2, pickup3]:
                cups[dest], cups[pickup3] = pickup1, cups[dest]
                break
        current = cups[current]


def printcups(cups):
    toprint = []
    cur = cups[0]
    for _ in range(len(cups)-1):
        toprint.append(cur+1)
        cur = cups[cur]
    print(''.join(map(lambda x: str(x), toprint)))


# part 1
inputlist = list(map(lambda x: int(x), test))
cups = setup(inputlist)
move(cups, int(inputlist[0]) - 1, 100)
printcups(cups)

# part 2
elements = int(1e6)
inputlist = list(map(lambda x: int(x), test))
total = inputlist+list(range(len(inputlist)+1, elements+1))
cups = setup(total)
timestart = time.time()
move(cups, int(inputlist[0]) - 1, int(1e7))
print(f'elapsed time:{time.time() - timestart}')
a = cups[0]
b = cups[a]
print(a+1, b+1, (a+1)*(b+1))
