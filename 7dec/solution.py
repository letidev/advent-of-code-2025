with open("test.txt") as f:
    grid = f.read().splitlines()

n, m = len(grid), len(grid[0])
x, y = 0, grid[0].find("S")

visited = [[False for _ in range(m)] for _ in range(n)]


# Part 1
def beams(x, y, n, m):
    if x < 0 or x >= n or y < 0 or y >= m or visited[x][y]:
        return 0

    visited[x][y] = True

    if grid[x][y] == "^":
        return 1 + beams(x + 1, y - 1, n, m) + beams(x + 1, y + 1, n, m)
    else:
        return beams(x + 1, y, n, m)


print(beams(x, y, n, m))

# Part 2
found = [[-1 for _ in range(m)] for _ in range(n)]


def paths(x, y, n, m):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0

    if x == n - 1:
        return 1

    if found[x][y] != -1:
        return found[x][y]

    if grid[x][y] == "^":
        found[x][y] = paths(x + 1, y - 1, n, m) + paths(x + 1, y + 1, n, m)
    else:
        found[x][y] = paths(x + 1, y, n, m)

    return found[x][y]


print(paths(x, y, n, m))
