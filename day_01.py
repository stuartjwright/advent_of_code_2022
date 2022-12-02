from utils.data import read_data_as_list


data = read_data_as_list(day=1)

# Part 1
max_calories = 0
current_elf_calories = 0
for line in data:
    if not line:
        if current_elf_calories > max_calories:
            max_calories = current_elf_calories
        current_elf_calories = 0
    else:
        current_elf_calories += int(line)

print(f'Part 1 Solution: {max_calories}')


# Part 2
elves = []
elf = 0
for line in data:
    if not line:
        elves.append(elf)
        elf = 0
    else:
        elf += int(line)
top_three = sum(sorted(elves, reverse=True)[:3])
print(f'Part 2 Solution: {top_three}')
