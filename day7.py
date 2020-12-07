import re
import fileinput


contained_in = {}
contain = {}
for line in fileinput.input():
    split = line.split('bags contain ')
    bag_outer = split[0].strip()
    contain[bag_outer] = []
    for match in re.finditer('([0-9]+) ([a-z| ]*) bags?', split[1]):
        bag_inner = match.group(2)
        contain[bag_outer].append((bag_inner, int(match.group(1))))
        if not bag_inner in contained_in:
            contained_in[bag_inner] = []
        contained_in[bag_inner].append((bag_outer))

## part 1
stack = ['shiny gold']
can_contain = set()
while stack:
    node = stack.pop()
    if node not in contained_in:
        continue
    for outer_bag in contained_in[node]:
        if outer_bag not in can_contain:
            can_contain.add(outer_bag)
            stack.append(outer_bag)
print(len(can_contain))

## part 2
stack = [('shiny gold', 1)]
bags = 0
while stack:
    outer_bag,outer_count = stack.pop()
    for inner_bag,inner_count in contain[outer_bag]:
        count = outer_count*inner_count
        bags+= count
        stack.append((inner_bag,count))
print(bags)
