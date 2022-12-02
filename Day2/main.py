with open("input.txt") as file:
    lines = file.readlines()

# X (1 point) beats C
# Y (2 points) beats A
# Z (3 points) beats B
winning_dict = {
    'X': ('C', 1),
    'Y': ('A', 2),
    'Z': ('B', 3)
}

# For draws
drawing_dict = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

def parse(list):
    new_list = []
    for element in list:
        new_list.append(element.strip('\n'))
    return new_list
    

def part1(input_list):
    score = 0   # Initializing the total score
    for battle in input_list:
        opponent = battle[0]
        you = battle[-1]
        # Draw
        if drawing_dict[you][0] == opponent:
            score += winning_dict[you][1] + 3
        elif opponent == winning_dict[you][0]:
            score += winning_dict[you][1] + 6
        else:
            score += winning_dict[you][1]

    return score

print(part1(parse(lines)))