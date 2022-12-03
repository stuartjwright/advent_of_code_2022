from string import ascii_lowercase, ascii_uppercase
from utils.data import read_data_as_list


characters = list(ascii_lowercase) + list(ascii_uppercase)
priority_lookup = dict(zip(characters, range(1, len(characters) + 1)))

rucksacks = read_data_as_list(day=3)


# Part 1
total = 0
for rucksack in rucksacks:
    midpoint = len(rucksack) // 2
    compartment_1, compartment_2 = set(rucksack[:midpoint]), set(rucksack[midpoint:])
    common_item = compartment_1.intersection(compartment_2).pop()
    priority = priority_lookup[common_item]
    total += priority
print(f'Part 1 Solution: {total}')


# Part 2
group_size = 3
total = 0
for i in range(0, len(rucksacks), group_size):
    rucksack_1, rucksack_2, rucksack_3 = rucksacks[i: i+3]
    common_item = set(rucksack_1).intersection(rucksack_2).intersection(rucksack_3).pop()
    priority = priority_lookup[common_item]
    total += priority
print(f'Part 2 Solution: {total}')
