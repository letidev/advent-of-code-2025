with open("test.txt") as f:
    lines = f.read().splitlines()

nodes = {}

for line in lines:
    start, ends = line.split(": ")
    ends = set(ends.split(" "))
    nodes[start] = ends


def dfs(start, end):
    if start == end:
        return 1

    key = (start, end)
    if key in memo:
        return memo[key]

    total = 0

    if start in nodes:
        for adj in nodes[start]:
            total += dfs(adj, end)

    memo[key] = total
    return total


# Part 1
memo = {}
print(dfs("you", "out"))


# Part 2
memo = {}
print(dfs("svr", "fft") * dfs("fft", "dac") * dfs("dac", "out"))
print(dfs("svr", "dac") * dfs("dac", "fft") * dfs("fft", "out"))
