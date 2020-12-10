from fileinput import input
from operator import sub

joltages = [int(line)
            for line in input('data/day10.test2.txt') if line.strip()]
joltages.sort()
connect_to = joltages.copy()
joltages.append(0)
connect_to.append(max(joltages)+3)

# part 1
diffs = list(map(sub, connect_to, joltages))
print(diffs.count(1)*diffs.count(3))


MAX_JUMP = 3
paths = [0]*len(joltages)
paths[-1] = 1  # one path from last to


def count_paths(joltages, paths,  start=0):
    if paths[start]:
        return paths[start]
    i = start+1
    n_paths = 0
    while i < len(joltages) and joltages[i] - joltages[start] <= MAX_JUMP:
        n_paths += count_paths(joltages, paths, i)
        i += 1
    paths[start] = n_paths
    return n_paths


print(count_paths(joltages, paths))
