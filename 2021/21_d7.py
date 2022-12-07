from aocd import get_data

from timeit import default_timer as timer

data = get_data(day=7, year=2021).strip()
# data = "16,1,2,0,4,2,7,1,2,14"

def calculate_move_fuel_cost(move):
    # each step costs 1 more unit of fuel that the last
    # for example, if the move is 11, fuel cost is 66
    fuel_cost = 0
    for i in range(1, move+1):
        fuel_cost += i
    return fuel_cost


def part1(crab_positions):
    '''Part 1 Implementation'''
    # Get the max && min position of any of the crabs
    max_position = max(crab_positions)
    position_fuel_costs = [0] * (max_position+1)

    # Iterate over the min and max positions
    for i in range(0, max_position+1):
        # If the current position is not in the crab_positions
        fuel_cost = 0
        for crab in crab_positions:
            move = abs(crab - i)
            fuel_cost += move

        position_fuel_costs[i] = fuel_cost

    # Index of the least value in position_fuel_costs is the horizontal position that costs
    # the least fuel to move all crabs to
    min_fuel_cost = min(position_fuel_costs)
    min_fuel_cost_index = position_fuel_costs.index(min_fuel_cost)

    print(f"PART 1: Position: {min_fuel_cost_index}, Fuel Cost: {min_fuel_cost}")


def part2(crab_positions):
    '''Part 2 Implementation'''
    max_position = max(crab_positions)

    position_fuel_costs = [0] * (max_position+1)

    # Iterate over the min and max positions
    for i in range(0, max_position+1):
        # If the current position is not in the crab_positions
        fuel_cost = 0
        for crab in crab_positions:
            move = abs(crab - i)
            # fuel_cost += calculate_move_fuel_cost(move) # Takes 32 Seconds
            fuel_cost += sum([x+1 for x in range(move)])  # Takes 36 Seconds

        position_fuel_costs[i] = fuel_cost

    # Index of the least value in position_fuel_costs is the horizontal position that costs
    # the least fuel to move all crabs to
    min_fuel_cost = min(position_fuel_costs)
    min_fuel_cost_index = position_fuel_costs.index(min_fuel_cost)

    print(f"PART 2: Position: {min_fuel_cost_index}, Fuel Cost: {min_fuel_cost}")

if __name__ == "__main__":
    # crab submarines can only move horizontally
    # input is horizontal position of each crab
    data = [int(x) for x in data.split(',')]

    part1_start = timer()
    part1(data)
    part1_end = timer()

    part2_start = timer()
    part2(data)
    part2_end = timer()

    print(f"Part 1 Time: {part1_end - part1_start}")
    print(f"Part 2 Time: {part2_end - part2_start}")
