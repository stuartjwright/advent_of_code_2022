from utils.data import read_data_as_string


def solution(data: str, n: int) -> int:
    for i in range(n, len(data) + 1):
        chars = data[i-n: i]
        unique = set(chars)
        if len(unique) == n:
            return i


if __name__ == '__main__':
    buffer = read_data_as_string(day=6)
    print(f'Part 1 Solution: {solution(buffer, 4)}')
    print(f'Part 2 Solution: {solution(buffer, 14)}')
