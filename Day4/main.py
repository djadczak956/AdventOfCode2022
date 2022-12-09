with open("input.txt") as file:
    lines = file.readlines()

def parse(list):
    new_list = []
    for element in list:
        new_list.append(element.strip('\n'))
    return new_list

def part1(input_list):
    sum = 0

    for element in input_list:
        first, second = element.split(',')
        first_first = int(first.split('-')[0])
        first_last = int(first.split('-')[-1])
        second_first = int(second.split('-')[0])
        second_last = int(second.split('-')[-1])

        if (first_first >= second_first and first_last <= second_last) or (second_first >= first_first and second_last <= first_last):
            sum += 1

    return sum

def part2(input_list):
    sum = 0
    
    for element in input_list:
        first, second = element.split(',')
        first_first = int(first.split('-')[0])
        first_last = int(first.split('-')[-1])
        second_first = int(second.split('-')[0])
        second_last = int(second.split('-')[-1])

        id1_list = [number for number in range(first_first, first_last + 1)]
        id2_list = [number for number in range(second_first, second_last + 1)]

        if any(num in id2_list for num in id1_list):
            sum += 1

    return sum
        

# print(part1(parse(lines)))
print(part2(parse(lines)))