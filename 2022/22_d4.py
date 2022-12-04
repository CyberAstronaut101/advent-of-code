from aocd import get_data

data = get_data(day=4,year=2022).splitlines()

def part1(data):
    full_overlap_count = 0
    for assignment in data:
        left, right = assignment.split(",")

        l = [int(x) for x in left.split("-")]
        r = [int(x) for x in right.split("-")]

        lrange = set(range(l[0], l[1]+1))
        rrange = set(range(r[0], r[1]+1))
        
        if lrange.issubset(rrange) or rrange.issubset(lrange):
            full_overlap_count += 1

    print(f"Part 1: {full_overlap_count}")

def part2(data):
    any_overlap_count = 0
    for assignment in data:
        left, right = assignment.split(",")

        l = [int(x) for x in left.split("-")]
        r = [int(x) for x in right.split("-")]

        lrange = range(l[0], l[1]+1)
        rrange = range(r[0], r[1]+1)

        if len(set(lrange) & set(rrange)) > 0:
            any_overlap_count += 1

    print(f"Part 2: {any_overlap_count}")

part1(data)
part2(data)