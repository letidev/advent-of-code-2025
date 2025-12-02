import re

with open("test.txt") as f:
    ranges = f.read().split(",")

ans = 0

for r in ranges:
    s = r.split("-")
    start, end = int(s[0]), int(s[1])

    for i in range(start, end + 1):
        id = str(i)

        # if re.match("^(\\d+)\\1{1}$", id): # part 1
        if re.match("^(\\d+)\\1+$", id):
            ans += i

print(ans)
