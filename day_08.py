import numpy as np
from utils.data import read_data_as_int_grid


# Load 2-d grid of ints as numpy array
grid = read_data_as_int_grid(day=8)
y, x = grid.shape


# Part 1
count = 0
extremes = np.array([0, 0, 0, 0])
for i in range(y):
    for j in range(x):
        if i == 0 or j == 0 or i == y-1 or j == x-1:
            count += 1
        else:
            height = grid[i, j]
            extremes[0] = grid[i, :j].max()  # left
            extremes[1] = grid[i, j+1:].max()  # right
            extremes[2] = grid[:i, j].max()  # top
            extremes[3] = grid[i+1:, j].max()  # bottom
            if (height > extremes).any():
                count += 1
print(f'Part 1 Solution: {count}')


# Part 2
max_score = 0
for i in range(y):
    for j in range(x):
        if i == 0 or j == 0 or i == y-1 or j == x-1:
            continue
        height = grid[i, j]
        left = grid[i, :j][::-1]
        right = grid[i, j+1:]
        top = grid[:i, j][::-1]
        bottom = grid[i+1:, j]
        score = 1
        for direction in (left, right, top, bottom):
            comparison = direction >= height
            if ~comparison.any():
                score *= comparison.shape[0]
            else:
                score *= comparison.argmax() + 1
        if score > max_score:
            max_score = score
print(f'Part 2 Solution: {max_score}')
