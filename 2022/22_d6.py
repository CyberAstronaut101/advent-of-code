from aocd import get_data

data = get_data(day=6, year=2022).strip()
# data = open('./input/d6_test.txt').read().strip()

def part1(input_data, non_repeating_length):
    '''Part 1 Implementation'''
    # detect start of packet marker
    # start of packet indicated by sequence of non_repeating_length
    # characters that are all different
    for i in range(3, len(input_data)):
        # print(character)
        # look forward in input_data by 3 characters to see if they are all different that current index
        if len(set(input_data[i:i+non_repeating_length])) == non_repeating_length:
            print(f"Found start of packet at [{i} -> {i+non_repeating_length}]")
            print("Marker position: ", i+non_repeating_length)
            return

if __name__ == "__main__":
    # Part 1
    part1(data, 4)
    # Part 2 just with non-repeating requirement of 14
    part1(data, 14)
