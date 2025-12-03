import time

with open("test.txt") as f:
    lines = f.read().splitlines()

ans = 0

# NUM_SIZE = 2 # Part 1
NUM_SIZE = 12

start = time.time()

for line in lines:
    num = 0
    idx = 0

    for num_dig in reversed(range(0, NUM_SIZE)):
        mx = 0
        for i in range(idx, len(line) - num_dig):
            digit = int(line[i])
            if digit > mx:
                mx = digit
                idx = i + 1

        num = num * 10 + mx

    ans += num

end = time.time()
print(f"--- {end - start} seconds ---")
print(ans)
