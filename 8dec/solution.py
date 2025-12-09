import math

with open("test.txt") as f:
    lines = f.read().splitlines()

# NUM_PAIRS = 10
NUM_PAIRS = 1000


def dist(p, q):
    return math.sqrt(
        math.pow((p[0] - q[0]), 2)
        + math.pow((p[1] - q[1]), 2)
        + math.pow((p[2] - q[2]), 2)
    )


boxes = []
for line in lines:
    x = line.split(",")
    boxes.append((int(x[0]), int(x[1]), int(x[2])))

pairs = []
for i in range(len(boxes) - 1):
    for j in range(i + 1, len(boxes)):
        p, q = boxes[i], boxes[j]
        d = dist(p, q)

        pairs.append((p, q, d))


pairs.sort(key=lambda x: x[2])

i = 1
circuits = [{pairs[0][0], pairs[0][1]}]

while i < NUM_PAIRS:
    p, q = pairs[i][0], pairs[i][1]

    cp = -1
    cq = -1

    # find in which circuit (if any) is each box in
    for ci in range(len(circuits)):
        if p in circuits[ci]:
            cp = ci

        if q in circuits[ci]:
            cq = ci

        if cp != -1 and cq != -1:
            break

    # neither of boxes is in a cirtuit
    if cp == -1 and cq == -1:
        # create a new circuit
        circuits.append({p, q})

    # add p to q's cirtuit
    if cp == -1 and cq != -1:
        circuits[cq].add(p)

    # add q to p's circuit
    if cp != -1 and cq == -1:
        circuits[cp].add(q)

    # both in different circuits - unite them
    if cp != -1 and cq != -1 and cp != cq:
        circuits[cp] = circuits[cp].union(circuits[cq])
        circuits.remove(circuits[cq])

    i += 1


circuits.sort(key=lambda x: len(x), reverse=True)

print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))
