from operator import itemgetter

with open("test.txt") as f:
    lines = f.read()


ranges, ids = [x.splitlines() for x in lines.split("\n\n")]

ranges = [[int(x) for x in r.split("-")] for r in ranges]
ids = [int(x) for x in ids]

fresh = 0

ranges = sorted(ranges, key=itemgetter(0, 1))

for id in ids:
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            fresh += 1
            break

print(fresh)
