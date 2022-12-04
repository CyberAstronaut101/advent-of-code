from aocd import get_data

data = get_data(day=3, year=2022).splitlines()
# data = open('./inputs/d3_test.txt').read().strip().splitlines()

# print(data)

def priority_of_present(present):
    # lowercase items a through z have priorities 1 through 26
    # uppercase items A through Z have priorities 27 through 52
    if present.isupper():
        return ord(present) - 38
    else:
        return ord(present) - 96

def part1(data):
    priority_sum = 0 
    for rucksack in data:
        # print(rucksack)
        # make all characters lowercase
        # rucksack = rucksack.lower()
        # split rucksack in half by length
        rucksack = [rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]]
        common_present = set(set(rucksack[0]) & set(rucksack[1])).pop()
        priority_sum += priority_of_present(common_present)

        print(f"Rucksack: {rucksack} \n common element: {common_present} - priority: {priority_of_present(common_present)}")

    print(f"Part 1 Sum of priorities: {priority_sum}")

def part2(data):
    priority_sum = 0 
    for i in range(3, len(data)+3, 3):
        common_elem = set(
            set(data[i-3]) & set(data[i-2]) & set(data[i-1])
        )
        print(f"Common element: {common_elem}")
        priority_sum += priority_of_present(common_elem.pop())
        print(i)

    print(f"Part 2 Sum of priorities: {priority_sum}")

part1(data)
part2(data)
