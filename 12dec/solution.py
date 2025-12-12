import math
from operator import mul

with open("test.txt") as f:
    lines = f.read().splitlines()

ans = 0
for i in range(30, len(lines)):
    a, b = lines[i].split(": ")

    size = math.prod([int(x) / 3 for x in a.split("x")])
    count = sum([int(x) for x in b.split(" ")])

    if size >= count:
        ans += 1

print(ans)
