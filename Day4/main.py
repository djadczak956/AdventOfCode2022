with open("test-input.txt") as file:
    lines = file.readlines()

def parse(list):
    new_list = []
    for element in list:
        new_list.append(element.strip('\n'))
    return new_list

def part1(input_list):
    for element in input_list:
        first, second = element.split(',')
        
