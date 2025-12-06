import re
from operator import mul

with open("test.txt") as f:
    lines = f.read().splitlines()


def reSplit(line: str):
    return re.split(r"\s+", line.strip())


signs = reSplit(lines[-1])

nums = [int(x) for x in reSplit(lines[0])]

for i in range(1, len(lines) - 1):
    nums2 = [int(x) for x in reSplit(lines[i])]

    for j in range(len(nums)):
        if signs[j] == "+":
            nums[j] += nums2[j]
        else:
            nums[j] *= nums2[j]

print("Part 1:", sum(nums))

# Part 2
total = 0

# get real indices of signs
idx = []
i = -1
for s in signs:
    i = lines[-1].find(s, i + 1)
    idx.append(i)
    i += 1

for i in range(len(idx)):
    start = idx[i]
    end = idx[i + 1] - 1 if i + 1 < len(idx) else len(lines[0])

    res = 0
    if signs[i] == "*":
        res = 1

    for j in range(start, end):
        num = 0
        for k in range(0, len(lines) - 1):
            if lines[k][j] != " ":
                num = num * 10 + int(lines[k][j])

        if signs[i] == "+":
            res += num
        else:
            res *= num

    total += res

print("Part 2:", total)
