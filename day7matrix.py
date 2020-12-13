import re
import numpy as np
import fileinput

lines = [line.split(' bags contain') for line in fileinput.input(
    'data/day7.txt') if line.rstrip()]
bag_index = {line[0]: i for line,
        i in zip(lines, range(len(lines)))}

bag_graph = np.zeros((len(lines), len(lines)), dtype=int)
for line in lines:
    for match in re.finditer('([0-9]+) ([a-z| ]*) bags?', line[1]):
        bag_graph[bag_index[line[0]],bag_index[match.group(2)]] = int(match.group(1))

shiny_gold = np.zeros(len(lines), dtype=int)
shiny_gold[bag_index['shiny gold']] = 1

# part one
contained = shiny_gold
can_contain = set()
while contained.any():
    contained =  bag_graph @ contained
    can_contain.update(np.nonzero(contained)[0])
print(f'shiny gold can be contained in {len(can_contain)} different bags')

# part two
inside = shiny_gold
n_bags = 0
while inside.any():
    inside = inside @ bag_graph
    n_bags += np.sum(inside)
print(f'shiny gold contains {n_bags} bags')
