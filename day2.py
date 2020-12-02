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
    least = int(tokens.group(1))
    most = int(tokens.group(2))
    char = tokens.group(3)
    pw = tokens.group(4)
    if least <= pw.count(char) <= most:
        valid+=1

print(valid)
