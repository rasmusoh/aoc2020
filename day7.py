import re
import fileinput


contained_in = {}
for line in fileinput.input():
    split = line.split('bags contain ')
    bag = split[0]
    contains = {}
    for match in re.finditer('([0-9]+) ([a-z| ]*) bags?', split[1]):
        contains[match.group(2)] = int(match.group(1))
    print(contains)
