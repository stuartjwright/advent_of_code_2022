import re
from utils.data import get_filename
from copy import deepcopy

# Setup - get starting position and instructions into reasonable format
with open(get_filename(day=5), 'r') as f:
    start_position, procedure = f.read().split('\n\n')

start_position = start_position.split('\n')[:-1][::-1]
stack_indices = [i+1 for i in range(0, len(start_position[0]), 4)]
start_stacks = []
for idx in stack_indices:
    stack = [row[idx] for row in start_position if idx < len(row) and row[idx] != ' ']
    start_stacks.append(stack)

pattern = r'move (\d+) from (\d+) to (\d+)'
instructions = [[int(num) for num in instruction] for instruction in re.findall(pattern, procedure)]

# Part 1
stacks = deepcopy(start_stacks)
for num_crates, from_idx, to_idx in instructions:
    from_stack = stacks[from_idx-1]
    to_stack = stacks[to_idx-1]
    for _ in range(num_crates):
        to_stack.append(from_stack.pop())

result = ''.join([stack[-1] for stack in stacks])
print(f'Part 1 Solution: {result}')


# Part 2
stacks = deepcopy(start_stacks)
for num_crates, from_idx, to_idx in instructions:
    from_stack = stacks[from_idx-1]
    to_stack = stacks[to_idx-1]
    to_stack.extend(from_stack[-num_crates:])
    for _ in range(num_crates):
        from_stack.pop()

result = ''.join([stack[-1] for stack in stacks])
print(f'Part 2 Solution: {result}')
