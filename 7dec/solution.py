with open("test.txt") as f:
    grid = f.read().splitlines()

n, m = len(grid), len(grid[0])
x, y = 0, grid[0].find("S")

visited = [[False for _ in range(m)] for _ in range(n)]


def beams(x, y, n, m):
    if x < 0 or x >= n or y < 0 or y >= m or visited[x][y]:
        return 0

    visited[x][y] = True

    if grid[x][y] == "^":
        return 1 + beams(x + 1, y - 1, n, m) + beams(x + 1, y + 1, n, m)
    else:
        return beams(x + 1, y, n, m)


print(beams(x, y, n, m))
