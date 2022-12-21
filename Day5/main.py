from collections import deque
import string

with open('test-input.txt') as file:
    lines = file.readlines()

def parse(list):
    new_list = []
    for element in list:
        new_list.append(element.strip('\n'))
    return new_list

# Read after the line break i.e. getting the directions
def read_after_break(input_list):
    directions = []
    for element in input_list:
        directions.append(element)
        if element == "":   # Will cause the list to only 
            directions = [] 
    return directions

def part1(input_list):
    letters = []
    # Adds lines until an empty line
    # Stops when past the crates
    for line in input_list:
        if "[" in line:
            letters.append(line)
        else:
            break

    stacks = []
    for col in range(1, len(letters[0]), 4):
        stacks.append([])
        for row in range(len(letters)):
            if letters[row][col].isalpha():
                stacks[(col + 1) // 4].append(letters[row][col])

    return stacks
    

def part2():
    pass

# --------------- MAIN ----------------------
print(read_after_break(parse(lines)))