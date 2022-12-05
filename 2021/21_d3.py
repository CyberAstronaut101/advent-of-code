from aocd import get_data

data = get_data(day=3, year=2021).splitlines()
# data = open('./input/d3_test.txt').read().strip().splitlines()

def most_frequent(list):
    return max(set(list), key = list.count)

def least_frequent(list):
    return min(set(list), key = list.count)

def part1(data):
    gamma = ''
    epsilon = ''
    for i in range(0, len(data[0])):
        # Get the list from all debug lines with the character in in the ith position
        index_items = [int(x[i]) for x in data]
        print(index_items)
        gamma += str(most_frequent(index_items))
        epsilon += str(least_frequent(index_items))

    # Each index in debug_compiled is the most frequent value in the ith position of the input
    print(f"Gamma: {gamma}, Epsilon: {epsilon}")
    print(f"Power Consumption: {int(gamma, 2) * int(epsilon, 2)}")

def part2(data):

    # Calculate O2 Rating
    oxygen_filtered = data
    for i in range(0, len(data[0])):

        if len(oxygen_filtered) == 1:
            break

        bit_1_count = len([x for x in oxygen_filtered if x[i] == '1'])
        bit_0_count = len([x for x in oxygen_filtered if x[i] == '0'])

        if bit_1_count > bit_0_count or bit_1_count == bit_0_count:
            oxygen_filtered = [x for x in oxygen_filtered if x[i] == '1']
        else:
            oxygen_filtered = [x for x in oxygen_filtered if x[i] == '0']

        print(oxygen_filtered)

    oxygen_generator_rating = int(oxygen_filtered[0], 2)
    print(f"Oxygen filtered: {oxygen_filtered}, {oxygen_generator_rating}")

    # Calculate C02 Scrubber Rating
    co2_filtered = data
    # Need to filter for each bit till no bits left
    for i in range(0, len(data[0])):

        if len(co2_filtered) == 1:
            break

        bit_1_count = len([x for x in co2_filtered if x[i] == '1'])
        bit_0_count = len([x for x in co2_filtered if x[i] == '0'])

        # Filter and keep the bit count with the least count
        if bit_1_count < bit_0_count:
            co2_filtered = [x for x in co2_filtered if x[i] == '1']
        elif bit_1_count > bit_0_count:
            co2_filtered = [x for x in co2_filtered if x[i] == '0']
        else:
            # Equal, keep 0
            co2_filtered = [x for x in co2_filtered if x[i] == '0']

    co2_rating = int(co2_filtered[0], 2)
    print(f"Oxygen filtered: {co2_filtered}, {co2_rating}")


    print(f"O2: {oxygen_generator_rating}, CO2: {co2_rating}")
    print(f"Answer: {oxygen_generator_rating * co2_rating}")
    
    # print(first_bit_1_count, first_bit_0_count)

    # # first_bit_most_frequent = most_frequent([int(x[0]) for x in data])
    # print(f"First bit most frequent: {first_bit_most_frequent}")

    # # Filter the data list to only include numbers that start with the most frequent bit
    # data = [x for x in data if int(x[0]) == first_bit_most_frequent]
    # print(data)

    # for i in range(0, len(data[0])):
    #     c = [int(x[i]) for x in data]
    #     each_bit_most_frequent.append(most_frequent(c))

    # print(each_bit_most_frequent)
    

    # CO2 Scrubber rating
    #


part1(data)
part2(data)