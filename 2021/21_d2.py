from aocd import get_data

data = get_data(day=2, year=2021).splitlines()

# print(data)
# Get the total of up/down movements and forward/backward movements
depth = 0
horizontal = 0

# Part 1
for move in data:
    # print(move)
    movement, amount = move.split(' ')
    # print(movement, amount)
    if movement == 'up':
        depth -= int(amount)
    if movement == 'down':
        depth += int(amount)

    if movement == 'forward':
        horizontal += int(amount)
    if movement == 'backward':
        horizontal -= int(amount)

print(f"PT1| Depth: {depth} -- Horizontal: {horizontal} -- Answer: {depth * horizontal}")

# Part 2
depth = 0
horizontal = 0
aim = 0

for move in data:
    movement, amount = move.split(' ')
    if movement == 'down':
        aim += int(amount)
    if movement == 'up':
        aim -= int(amount)

    if movement == 'forward':
        horizontal += int(amount)
        depth += aim * int(amount)

print(f"PT2| Depth: {depth} -- Horizontal: {horizontal} Aim: {aim} -- Answer: {depth * horizontal}")

