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

    print(f"Most calories contained by an elf: {max(calories_list)}")


# MAIN
part1()