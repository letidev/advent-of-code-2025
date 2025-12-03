with open("test.txt") as f:
    rotations = f.read().splitlines()

dial = 50
zeros = 0

for rotation in rotations:
    direction, amount = rotation[:1], int(rotation[1:])

    if direction == "L":
        dial -= amount

        if dial <= 0:
            zeros += abs(dial) // 100

            if dial != -amount:
                zeros += 1

    if direction == "R":
        dial += amount

        if dial >= 100:
            zeros += dial // 100

    dial %= 100


print(zeros)
