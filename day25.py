import itertools
test = (5764801, 17807724)
real = (335121, 363891)

card_pbk, door_pbk = real


def transform(subject, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * subject) % 20201227
    return value


card_loop_size = None
door_loop_size = None
value = 1
for i in itertools.count(1):
    value = (value * 7) % 20201227
    if value == card_pbk:
        card_loop_size = i
    elif value == door_pbk:
        door_loop_size = i
    if card_loop_size or door_loop_size:
        break

if card_loop_size:
    print(transform(door_pbk, card_loop_size))
else:
    print(transform(card_pbk, door_loop_size))
