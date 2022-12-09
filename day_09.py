from utils.data import read_data_as_list


# Setup
data = [line.split() for line in read_data_as_list(day=9)]
instructions = [(line[0], int(line[1])) for line in data]
axis_map = {
    'D': 1,
    'U': 1,
    'R': 0,
    'L': 0
}
sign_map = {
    'D': -1,
    'U': 1,
    'R': 1,
    'L': -1
}

# Part 1
positions = {(0, 0)}
head, tail = [0, 0], [0, 0]
for direction, distance in instructions:
    for _ in range(distance):
        axis = axis_map[direction]
        sign = sign_map[direction]
        head[axis] += sign
        if abs(tail[0] - head[0]) > 1 and tail[1] == head[1]:
            tail[0] += sign
        elif abs(tail[1] - head[1]) > 1 and tail[0] == head[0]:
            tail[1] += sign
        elif abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
            tail[axis] += sign
            other_axis = int(not axis)
            other_direction = -1 if tail[other_axis] - head[other_axis] > 0 else 1
            tail[other_axis] += other_direction
        positions.add(tuple(tail))
print(f'Part 1 Solution: {len(positions)}')


# Part 2
results = {(0, 0)}
positions = [[0, 0] for _ in range(10)]
for direction, distance in instructions:
    for _ in range(distance):
        axis = axis_map[direction]
        sign = sign_map[direction]
        head = positions[0]
        head[axis] += sign
        for i in range(1, len(positions)):
            tail = positions[i]
            if abs(tail[0] - head[0]) > 1 and tail[1] == head[1]:
                tail[0] += 1 if tail[0] < head[0] else -1
            elif abs(tail[1] - head[1]) > 1 and tail[0] == head[0]:
                tail[1] += 1 if tail[1] < head[1] else -1
            elif abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
                tail[0] += 1 if tail[0] < head[0] else -1
                tail[1] += 1 if tail[1] < head[1] else -1
            head = tail
        results.add(tuple(tail))
print(f'Part 2 Solution: {len(results)}')
