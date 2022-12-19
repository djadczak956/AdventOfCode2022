from collections import deque

with open('test-input.txt') as file:
    lines = file.readlines()

def parse(list):
    new_list = []
    for element in list:
        new_list.append(element.strip('\n'))
    return new_list

def part1(input_list):
    letters = []
    # Adds lines until an empty line
    for line in input_list:
        if "\n" in line:
            break
        letters.append(line)
    return letters
    

def part2():
    pass

# --------------- MAIN ----------------------
print(part1(parse(lines)))