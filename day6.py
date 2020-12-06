import fileinput
import itertools
import functools
import operator

groups = ''.join(fileinput.input()).split('\n\n')
groups = map(lambda x: [set(line) for line in x.split('\n') if line], groups)
count = 0
for group in groups:
    count += len(functools.reduce(operator.and_, group))

print(count)
