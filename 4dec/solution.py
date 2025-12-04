with open("test.txt") as f:
    lines = f.read().splitlines()

total_rolls = 0

directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

removed = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]
rolls = 1

while rolls != 0:

    rolls = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):

            if lines[i][j] == "@" and not removed[i][j]:
                adj = 0
                for d in directions:
                    ai, aj = i + d[0], j + d[1]

                    if ai >= 0 and ai < len(lines) and aj >= 0 and aj < len(lines[i]):
                        if lines[ai][aj] == "@" and not removed[ai][aj]:
                            adj += 1

                if adj < 4:
                    removed[i][j] = True
                    rolls += 1

    if rolls > 0:
        total_rolls += rolls

print(total_rolls)
