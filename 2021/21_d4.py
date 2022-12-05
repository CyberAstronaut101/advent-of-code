from aocd import get_data

data = get_data(day=4, year=2021).strip()
# data = open('./input/d4_test.txt').read().strip()

def build_table(board):
    '''
    Builds 2D array of ints based on the board inputs
    '''
    board_array = [[int(i) for i in parse] for parse in (row.split() for row in board)]
    return board_array

def pretty_print_board(board):
    '''
    Pretty prints the board
    '''
    for row in board:
        print(row)

def check_if_board_won(board):
    '''
    Checks if the board has been won
    - Either a full row or column has all -1 values
    '''
    # First check the rows
    for row in board:
        if all(item == -1 for item in row):
            return True

    # Check Columns
    for column in range(0, len(board[0])):
        if all(item == -1 for item in [row[column] for row in board]):
            return True

def calculate_unplayed_sum(board):
    '''
    Calculates the sum of the remaining unplayed values on the board
    '''
    # Iterate over the 2d board and sum all non -1 values
    point_sum = 0
    for row in board:
        for item in row:
            if item != -1:
                point_sum += item
    return point_sum

def part1(game_boards, game_plays):
    '''Part 1 Implementation'''
    for play in game_plays:
        for i, board in enumerate(game_boards):
            for row in board:
                for c, col in enumerate(row):
                    if row[c] == play:
                        row[c] = -1
                        if check_if_board_won(board):
                            # Board has been won, return state
                            return play, i, game_boards
    return game_boards

# add docstring here
def part2(game_boards, game_plays):
    '''Part 2 Implementation'''
    # Do the same thing as part 1, but instead track the order that the game_boards are won in

    won_board_state_tracking = []
    won_game_boards = []

    for play in game_plays:
        for i, board in enumerate(game_boards):
            
            # Check if this board already reached a min board win state, if so skip
            if i in won_game_boards:
                continue

            # Else, see if there is a valid play on the board
            for row in board:
                for c, col in enumerate(row):
                    if col == play:
                        # We have a valid play, mark it as played
                        row[c] = -1
                        # Check if board has won
                        if check_if_board_won(board):
                            won_board_state_tracking.append([play, game_boards[i]])
                            # Add the board to the won game_boards list
                            won_game_boards.append(i)
                            # Not returning because we need to play all boards till completion

    return won_board_state_tracking

if __name__ == "__main__":

    inputs = data.split('\n\n')
    plays = [int(i) for i in inputs[0].split(',')]
    boards = [build_table(y) for y in (x.split('\n') for x in inputs[1:])]

    # PART 1
    winning_number, board_index, played_boards = part1(boards, plays)
    remaining_sum = calculate_unplayed_sum(played_boards[board_index])
    print("PART1: ", winning_number * remaining_sum)

    # PART 2
    board_tracking = part2(boards, plays)
    remaining_sum = calculate_unplayed_sum(board_tracking[-1][1])
    final_winning_play = board_tracking[-1][0]
    print("PART2: ", final_winning_play * remaining_sum)
