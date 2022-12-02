with open("test-input.txt") as file:
    lines = file.readlines()

# X (1 point) beats C
# Y (2 points) beats A
# Z (3 points) beats B
winning_dict = {
    'X': ('C', 1),
    'Y': ('A', 2),
    'Z': ('B', 3)
}

def parse(list):
    new_list = []
    for element in list:
        new_list.append(element.strip('\n'))
    

def part1(input_list):
    score = 0   # Initializing the total score
    for battle in input_list:
        opponent = battle[0]
        you = battle[-1]
        # Draw
        if you == opponent:
            score += winning_dict[you][1] + 3
        elif opponent == winning_dict[you][0]:
            score += winning_dict[you][1] + 6
        else:
            score += winning_dict[you][1]

    return score

print(part1())