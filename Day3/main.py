import string

with open('input.txt') as file:
    lines = file.readlines()

letters = string.ascii_lowercase + string.ascii_uppercase   # Gathering letters for use in determining priority for the total sum of priorities

# Function to through input and remove new lines
def parse(list):
    new_list = []
    for element in list:
        new_list.append(element.strip('\n'))
    return new_list

def part1(input_list):
    sum = 0
    for element in input_list:
        half = int(len(element) / 2)
        first, second = element[:half], element[half:]
        for letter in first:
            if letter in second:
                #print(f"Sum: {sum}, Letter: {letter}, Index: {letters.index(letters)}")
                sum += letters.index(letter) + 1
                break
    
    return sum

print(part1(parse(lines)))