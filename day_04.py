import re
from utils.data import read_data_as_list


data = read_data_as_list(day=4)
pairs = [[int(match) for match in re.findall(r'\d+', pair)] for pair in data]


def range_contains(a1, a2, b1, b2):
    return (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2)


results = [pair for pair in pairs if range_contains(*pair)]
print(f'Part 1 Solution: {len(results)}')


def overlap(a1, a2, b1, b2):
    return len(set(range(a1, a2+1)).intersection(set(range(b1, b2+1)))) > 0


results = [pair for pair in pairs if overlap(*pair)]
print(f'Part 2 Solution: {len(results)}')
