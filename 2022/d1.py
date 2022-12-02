input = open('./inputs/d1.txt').read().strip()

elves = [map(int, elf.splitlines()) for elf in input.split("\n\n")]
sums = [sum(elf) for elf in elves]
sums.sort(reverse=True)

print("Most Calories:", max(sums))
print("Top 3:", sum(sums[:3]))