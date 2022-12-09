from collections import deque

with open('test-input.txt') as file:
    lines = file.readlines()

def parse(list):
    new_list = []
    for element in list:
        new_list.append(element.strip('\n'))
    return new_list

def grid_to_matrix(input_grid):
    matrix = []
    for line in input_grid:
        pass
    return matrix