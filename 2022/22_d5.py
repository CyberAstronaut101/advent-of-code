from aocd import get_data

# data = get_data(day=5, year=2022).strip() # Was not the correct input
# data = open('./input/d5_test.txt').read().splitlines()
data = open('./input/d5.txt').read().splitlines()

def create_initial_test_stacks():
    stacks = []
    for i in range(0, 3):
        stacks.append([])
    # Seed stacks with data
    stacks[0] = ['z','n']
    stacks[1] = ['m','c','d']
    stacks[2] = ['p']
    return stacks

def create_initial_stacks():
    stacks = [[],[],[],[],[],[],[],[],[]]
    # for i in range(0, 10):
    #     print(i)
    #     stacks.append([])

    # Seed the stacks with data
    stacks[0] = ['z', 'p', 'm','h','r']
    stacks[1] = ['p','c','j','b']
    stacks[2] = ['s','n','h','g','l','c','d']
    stacks[3] = ['f','t','m','d','q','s','r','l']
    stacks[4] = ['f','s','p','q','b','t','z','m']
    stacks[5] = ['t','f','s','z','b','g']
    stacks[6] = ['n','r','v']
    stacks[7] = ['p','g','l','t','d','v','c','m']
    stacks[8] = ['w', 'q','n','j','f','m','l']
    return stacks

def parse_move(move):
    move = move.split(' from ')
    print(move)
    move_count = int(move[0].split()[1])
    print(f"Move Count: {move_count}")
    from_stack, to_stack = int(move[1].split(' to ')[0]), int(move[1].split(' to ')[1])
    print(f"From Stack: {from_stack}")
    print(f"To Stack: {to_stack}")
    # -1 to account for 0 indexing
    return move_count, from_stack-1, to_stack-1

def execute_move(stacks, move_count, from_stack, to_stack):
    # Check if the move is valid (enough elements in stack index)
    print("\nExecuting move")
    print(stacks)

    # make sure from_stack has enough elements to do the from_stack move
    if len(stacks[from_stack]) < move_count:
        print("Invalid move")
        return stacks

    # Get boxes to move from stack in order

    boxes_to_move = stacks[from_stack][-move_count:]
    # Delete the boxes that have to move from the stack
    stacks[from_stack] = stacks[from_stack][:-move_count]
    # Add the boxes to the new stack
    stacks[to_stack].extend(boxes_to_move)

    return stacks

def get_stack_tops(stacks):
    answer = []
    for stack in stacks:
        answer.append(stack.pop())
    return answer

# stacks = create_initial_test_stacks()
stacks = create_initial_stacks()

for move in data:
    move_count, from_stack, to_stack = parse_move(move)
    stacks = execute_move(stacks, move_count, from_stack, to_stack)

stack_tops = get_stack_tops(stacks)
print(stack_tops)
print("Puzzle Answer: ",''.join(stack_tops))
print(f"Total Moves: ", len(data))
