with open("test.txt") as f:
    rotations = f.read().splitlines()

dial = 50
zeros = 0

for rotation in rotations:
    direction = rotation[:1]
    amount = int(rotation[1:]) % 100

    if direction == "L":
        dial -= amount

        if dial < 0:
            dial = 100 + dial

    if direction == "R":
        dial += amount

        if dial >= 100:
            dial = dial % 100

    if dial == 0:
        zeros += 1

print(zeros)
