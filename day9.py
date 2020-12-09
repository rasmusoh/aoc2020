from collections import deque
from fileinput import input
from itertools import combinations

N = 25
numbers = []
cur = 0
q = deque()
for line in input('data/day9.txt'):
    cur = int(line)
    numbers.append(cur)
    if len(q) < N:
        q.append(cur)
        continue
    is_valid = False
    if any(i + j == cur for i, j in combinations(q, 2)):
        q.append(cur)
        q.popleft()
    else:
        break
print(cur)
solution_range = [slice(i, j) for (i,j) in combinations(range(len(numbers)), 2) if sum(numbers[i:j]) == cur][0]
print(max(numbers[solution_range])+ min(numbers[solution_range]))
