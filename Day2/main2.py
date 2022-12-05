with open("input.txt") as file:
    lines = file.readlines()

def parse(list):
    new_list = []
    for element in list:
        new_list.append(element.strip('\n'))
    return new_list

# Dictionary values in form of (lose, win, draw)
dict = {
    'A': ('Z', 'Y', 'X'),
    'B': ('X', 'Z', 'Y'),
    'C': ('Y', 'X', 'Z')
}

score_dict = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

def part1(input_list):
    score = 0   # Initializing the total score
    for battle in input_list:
        opponent = battle[0]
        you = battle[-1]
        # Draw
        if you == dict[opponent][2]:
            score += score_dict[you] + 3
        # Win 
        elif you == dict[opponent][1]:
            score += score_dict[you] + 6
        # Lose
        else:
            score += score_dict[you]

    return score



def part2(input_list):
    sum = 0
    new_input = []  # Changes inputs into a way that part1 method can be used
    
    for element in input_list:
        key = element[0]
        you = element[-1]
        if you == 'X':
            new_input.append(f"{key} {dict[key][0]}")
        elif you == 'Y':
            new_input.append(f"{key} {dict[key][2]}")
        elif you == 'Z':
            new_input.append(f"{key} {dict[key][1]}")

    return part1(new_input)

print(part1(parse(lines)))
print(part2(parse(lines)))