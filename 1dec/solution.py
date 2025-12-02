with open("test.txt") as f:
    rotations = f.read().splitlines()

dial = 50
zeros = 0
at0 = False  # shows whether you start the current rotation from 0

for rotation in rotations:
    direction, amount = rotation[:1], int(rotation[1:])
    at0 = dial == 0

    if direction == "L":
        dial = dial - amount

        if dial <= 0:
            zeros += abs(dial) // 100

            if not at0:
                zeros += 1

            if dial % 100 == 0:
                dial = 0
            elif dial != 0:
                dial = 100 - (abs(dial) % 100)

    if direction == "R":
        dial += amount

        if dial >= 100:
            zeros += dial // 100
            dial = dial % 100


print(zeros)
