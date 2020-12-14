import re
from fileinput import input


def apply_mask(mask, value):
    binvalue = bin(value)[2:].zfill(36)
    return ''.join([bit if maskbit == '0' else maskbit for bit,
                    maskbit in zip(binvalue, mask)])


def set_bit_mask(mem, mask, value):
    if 'X' in mask:
        set_bit_mask(mem, mask.replace('X', '0', 1), value)
        set_bit_mask(mem, mask.replace('X', '1', 1), value)
    else:
        mem[mask] = value


mem = {}
tokenize = re.compile(r'mem\[([0-9]+)\] = ([0-9]+)')
mask = 'X'*36
for line in input('data/day14.txt'):
    if line.startswith('mask'):
        mask = line.split('mask = ')[1].rstrip()
        continue
    adress, value = re.match(tokenize, line).groups()
    memmask = apply_mask(mask, int(adress))
    set_bit_mask(mem, memmask, int(value))

print(sum(mem.values()))
