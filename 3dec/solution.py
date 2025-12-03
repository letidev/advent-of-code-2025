with open("test.txt") as f:
    lines = f.read().splitlines()

ans = 0


for line in lines:
    batteries = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

    for i in range(len(line)):
        d = int(line[i])

        batteries[d].append(i)

    found = False

    for i in reversed(range(1, 10)):
        for j in reversed(range(1, 10)):
            if (
                len(batteries[i]) > 0
                and len(batteries[j]) > 0
                and (i != j or (i == j and len(batteries[i]) > 1))
                and batteries[i][0] < batteries[j][-1]
            ):
                ans += i * 10 + j
                found = True
                break

        if found:
            break

print(ans)
