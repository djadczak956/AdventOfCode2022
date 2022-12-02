# Opening file
with open('input.txt') as file:
    lines = file.readlines()

# Parsing method to create a list of the combined calories for each elf
def parse(list):
    parsed_list = []  # List the total calories FOR EACH elf.

    combined_cals = 0   
    # This loop will intentionally cause an error to stop
    for i in range(len(list) + 1):
        try:
            combined_cals += int(list[i])
        except:     # Only a ValueError is expected
            parsed_list.append(combined_cals)     # haha logic in try/except
            combined_cals = 0
    return parsed_list

def part1():
    return max(parse(lines))

def part2():
    calories_list = parse(lines)
    calorie_sum = 0

    for i in range(3):
        calorie_sum += max(calories_list)
        calories_list.remove(max(calories_list))

    return calorie_sum

# MAIN
print(f"Most calories contained by an elf: {part1()}")
print(f"Total calories contained by the top 3 elves with the most snacks: {part2()}")