input = open('./inputs/d2.txt').read().strip().split('\n')

# print(input)


opponent_rock = 'A'
rock = 'X'
rock_score = 1

opponent_paper = 'B'
paper = 'Y'
paper_score = 2

opponent_sissor = 'C'
sissor = 'Z'
sissor_score = 3

lose = 0
draw = 3
win = 6

# Rock -> Paper == win
# Rock -> Rock == draw
# Rock -> sissor = lose

# Paper -> Paper = draw
# Paper -> Rock = lose
# Paper -> sissor = win

# Sissor -> Paper = lose
# sissor -> sissor = draw
# sissor -> rock = win

def score(plays):
    # play[0] is the opponent
    # play[1] is the player

    # Part 2 logic
    # we = plays[1]
    # If we play an X - We need to lose
    # If we play a Y - need to draw
    # If we play a Z - we need to win

    if plays[0] == opponent_rock:
        if plays[1] == rock:
            return draw + rock_score
        elif plays[1] == paper:
            return win + paper_score
        elif plays[1] == sissor:
            return lose + sissor_score

    elif plays[0] == opponent_paper:
        if plays[1] == rock:
            return lose + rock_score
        elif plays[1] == paper:
            return draw + paper_score
        elif plays[1] == sissor:
            return win + sissor_score

    elif plays[0] == opponent_sissor:
        if plays[1] == rock:
            return win + rock_score
        elif plays[1] == paper:
            return lose + paper_score
        elif plays[1] == sissor:
            return draw + sissor_score



def score2(plays):
    # If we play a X - Lose
    # If we play a Y - Draw
    # If we play a Z - Win

    if plays[1] == rock:
        # Lose scenario
        if plays[0] == opponent_rock:
            return lose + sissor_score
        if plays[0] == opponent_paper:
            return lose + rock_score
        if plays[0] == opponent_sissor:
            return lose + paper_score

    if plays[1] == paper:
        # Draw scenario
        if plays[0] == opponent_rock:
            return draw + rock_score
        if plays[0] == opponent_paper:
            return draw + paper_score
        if plays[0] == opponent_sissor:
            return draw + sissor_score

    if plays[1] == sissor:
        # Win scenario
        if plays[0] == opponent_rock:
            return win + paper_score
        if plays[0] == opponent_paper:
            return win + sissor_score
        if plays[0] == opponent_sissor:
            return win + rock_score

    print("Error", plays)

total_pt1 = 0
total_pt2 = 0
for line in input:
    plays = line.split()
    total_pt1 += score(plays)
    total_pt2 += score2(plays)
    
# sum = [sum(round) for round in score(plays)]
print(f"PT1: {total_pt1} -- PT2: {total_pt2}")

