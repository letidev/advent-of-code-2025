with open("test.txt") as f:
    lines = f.read().splitlines()

nodes = {}


def dfs(start, end, path, allPaths):
    path.append(start)

    if start == end:
        allPaths.append(path.copy())
    else:
        for node in nodes[start]:
            if node not in path:
                dfs(node, end, path, allPaths)

    path.pop()


for line in lines:
    start, ends = line.split(": ")
    ends = set(ends.split(" "))
    nodes[start] = ends

path = []
allPaths = []
dfs("you", "out", path, allPaths)

print(len(allPaths))
