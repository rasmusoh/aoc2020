import re
import fileinput

pattern = r'(\d+)-(\d+) (\w): (\w+)'
valid = 0
for line in fileinput.input():
    line = line.rstrip()
    if not line:
        continue
    tokens = re.search(pattern, line)
    if tokens is None:
        print(f"failed to parse line:{line}")
        continue
    pos1 = int(tokens.group(1))
    pos2 = int(tokens.group(2))
    char = tokens.group(3)
    pw = tokens.group(4)
    if (pw[pos1-1]==char) ^ (pw[pos2-1]==char):
        valid+=1

print(valid)
