from operator import itemgetter

with open("test.txt") as f:
    lines = f.read()

ranges, ids = [x.splitlines() for x in lines.split("\n\n")]

ids = [int(x) for x in ids]
ranges = [[int(x) for x in r.split("-")] for r in ranges]
ranges = sorted(ranges, key=itemgetter(0, 1))

fresh = 0

# Part 1
for id in ids:
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            fresh += 1
            break

print(fresh)

# Part 2
merged = [ranges[0]]

for range in ranges:
    last = merged[-1]

    # if next range is entirely inside of the last merged one,
    # (e.g. 1-5, 2-3) just skip it
    if last[0] <= range[0] and range[1] <= last[1]:
        continue

    if last[0] <= range[0] and range[0] <= last[1]:
        m = [last[0], range[1]]
        merged.pop()
        merged.append(m)
    else:
        merged.append(range)

print(sum([x[1] - x[0] + 1 for x in merged]))
