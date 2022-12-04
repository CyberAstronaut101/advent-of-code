# ==== AoC 21 Day 1 ====
inputFile = open('./inputs/d1.txt','r')
depths = list(map(int, inputFile.read().splitlines()))

result_pt1 = 0
result_pt2 = 0

# ===== Part 1 =====
for i in range(len(depths)-1):
    if depths[i] < depths[i+1]:
        result_pt1 += 1

# ===== Part 2 =====
# Now we are using a 3 sample sliding window, sum the range, and then do the same increasing check
# Calculate the initial window sum
prev_window_sum = sum(depths[0:3])

print("Running pt 2")
for i in range(3, len(depths)):
    # print(i)
    # For each of these steps, we will get the next i+1 value, but subtract the i-3 value
    curr_sum = prev_window_sum + depths[i] - depths[i-3]
    if curr_sum > prev_window_sum:
        result_pt2 += 1

print(f"Part 1: {result_pt1}")
print(f"Part 2: {result_pt2}")
