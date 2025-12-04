with open("test.txt") as f:
    lines = f.read().splitlines()

rolls = 0

directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

for i in range(len(lines)):
    for j in range(len(lines[i])):

        if lines[i][j] == "@":
            adj = 0
            for d in directions:
                ai, aj = i + d[0], j + d[1]

                if ai >= 0 and ai < len(lines) and aj >= 0 and aj < len(lines[i]):
                    if lines[ai][aj] == "@":
                        adj += 1

            if adj < 4:
                rolls += 1

print(rolls)
