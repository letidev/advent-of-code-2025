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

print(sum(nums))
