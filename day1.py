import re
import fileinput
from functools import reduce
from operator import mul

pattern = r'(\d+)-(\d+) (\w): (\w+)'

numbers = []
for line in fileinput.input():
    line = line.rstrip()
    if line:
        numbers.append(int(line))
numbers.sort()


def find(n, total):
    if n == 1:
        for number in numbers:
            if number == total:
                return [number]
            if number > total:
                return []
    else:
        for number in numbers:
            result = find(n - 1, total - number)
            if len(result) > 0 and not number in result:
                return result + [number]
    return []


result = find(3, 2020)

print(result)
print(reduce(mul, result, 1))
