from aocd import get_data

data = get_data(day=5, year=2021).strip()
# data = open('./input/d5_test.txt').read().strip()

def parse_input(input_data):
    '''Parse the input data'''
    # Input looks like 'x1,y1 -> x2,y2'
    
    # Create a tuple
    # (x1, y1, x2, y2)
    parsed_input = []
    for line in input_data.splitlines():
        coords = line.split(' -> ')
        x1, y1 = coords[0].split(',')
        x2, y2 = coords[1].split(',')
        parsed_input.append((int(x1), int(y1), int(x2), int(y2)))

    # Get the max x2 and y2 values
    max_x1 = max([x[0] for x in parsed_input])
    max_x2 = max([x[3] for x in parsed_input])

    max_y1 = max([x[1] for x in parsed_input])
    max_y2 = max([x[2] for x in parsed_input])

    max_x = max(max_x1, max_x2)
    max_y = max(max_y1, max_y2)

    return max_x+1, max_y+1, parsed_input

def print_sonar_board(sonar_board):
    '''Prints the sonar board'''
    for row in sonar_board:
        print(row)

def mark_position(sonar_board, x, y):
    '''Marks the position on the sonar board'''
    # If the value is a '-1', change it to '1'
    # First index of board is y, second is x

    sonar_board[y][x] += 1

    return sonar_board

def get_overlap_count(sonar_board, min_overlaps):
    '''Get the number of points that have at least min_overlaps'''
    overlap_count = 0
    for row in sonar_board:
        for col in row:
            if col >= min_overlaps:
                overlap_count += 1
    return overlap_count

def part1(max_x, max_y, coords):
    '''Part 1 Implementation'''
    
    # PART 1 - ONLY CONSIDER HORIZONTAL AND VERTICAL LINES

    # Create the blank representation of the sonar board
    sonar_board = [[0 for x in range(max_x)] for y in range(max_y)]

    # Iterate over the coordinates and add the representation to the sonar board
    for i, coord in enumerate(coords):
        x1, y1, x2, y2 = coord
        # print(f"Coords {coord}")
        # print(f"({x1},{y1}) -> ({x2},{y2})")
        # First index of board is y, second is x
        # Check if the line is horizontal or vertical
        if x1 == x2 or y1 == y2:
            # print("Horizontal or Vertical Line")
            # print(f"({x1},{y1}) -> ({x2},{y2})")
            if x1 == x2:
                # Horizontal Line
                # Static X row, iterate over the Y value and add
                range_min = min(y1, y2)
                range_max = max(y1, y2)
                for y in range(range_min, range_max+1):
                    # print(f"\tHorizontal Marking ({x1},{y})")
                    sonar_board = mark_position(sonar_board, x1, y)

            elif y1 == y2:
                # Vertical Line
                # Static Y Column, iterate over the X values and add
                range_min = min(x1, x2)
                range_max = max(x1, x2)

                for x in range(range_min, range_max+1):
                    # print(f"\t Vertical Marking ({x},{y1})")
                    sonar_board = mark_position(sonar_board, x, y1)


    # print_sonar_board(sonar_board)
    print("PART1 - 2 or more overlap count: ", get_overlap_count(sonar_board, 2))

def part2(max_x, max_y, coords):
    '''Part 2 Implementation'''
    # Part 2 considers all lines, not just horizontal and vertical

    # Create the blank representation of the sonar board
    sonar_board = [[0 for x in range(max_x)] for y in range(max_y)]

    # Iterate over the coordinates and add the representation to the sonar board
    for i, coord in enumerate(coords):
        x1, y1, x2, y2 = coord
        # print(f"Coords {coord}")
        print(f"({x1},{y1}) -> ({x2},{y2})")
        # First index of board is y, second is x

        # Build the correct range for the x and y values
        # Possible to need either a asc or desc range

        # Build x range
        if x1 < x2:
            # normal ascending range
            x_range = range(x1, x2+1)
        elif x1 > x2:
            # descending range
            x_range = range(x1, x2-1, -1)
        elif x1 == x2:
            # need to keep the same static value for x for all the y values that need to be marked
            y_range_count = abs(y1-y2)+1
            x_range = [x1]*y_range_count

        # Build y range
        if y1 < y2:
            # ascending
            y_range = range(y1, y2+1)
        elif y1 > y2:
            print("Descending y range")
            y_range = range(y1, y2-1, -1)
        elif y1 == y2:
            x_range_count = abs(x1-x2)+1
            y_range = [y1]*x_range_count

        print("\tx_range: ")
        for i in x_range:
            print(i,end=',')
        print()
        print("\ty_range: ")
        for i in y_range:
            print(i, end=',')
        print()

        # In all cases, we will have the same length for the x and y ranges, cant use nested for loop
        for i in range(0,len(x_range)):
            sonar_board = mark_position(sonar_board, x_range[i], y_range[i])

    print("PART 2 Sonar Board")
    print_sonar_board(sonar_board)
    print("PART2 - 2 or more overlap count: ", get_overlap_count(sonar_board, 2))

if __name__ == "__main__":
    max_x, max_y, parsed_input = parse_input(data)
    part1(max_x, max_y, parsed_input)
    part2(max_x, max_y, parsed_input)
