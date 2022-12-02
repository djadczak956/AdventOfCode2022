# Opening file
with open('input.txt') as file:
    lines = file.readlines()

def part1():
    calories_list = []  # List the calories FOR EACH elf.

    combined_cals = 0   # Initializing em
    for element in lines:
        try:
            combined_cals += int(element)
        except:     # Only a ValueError is expected
            calories_list.append(combined_cals)     # haha logic in try/except
            combined_cals = 0

    return max(calories_list)

def part2():
    calorie_sum = 0
    for i in range(3):


# MAIN
print(f"Most calories contained by an elf: {part1()}")