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
    print(input_list)
    for line in input_list:
        if "[" in line:
            letters.append(line)
        else:
            break
        
    
    for col in range(5, len(letters), 4):
        for row in letters[col]:
            pass

    return letters
    

def part2():
    pass

# --------------- MAIN ----------------------
print(part1(parse(lines)))