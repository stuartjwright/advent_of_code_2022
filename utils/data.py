import os
import numpy as np


DATA_PATH = 'data'


def get_filename(day: int) -> str:
    return os.path.join(DATA_PATH, f'day_{day:02}.txt')


def read_data_as_list(day: int) -> list[str]:
    with open(get_filename(day), 'r') as f:
        return [line.strip() for line in f.readlines()]


def read_data_as_string(day: int) -> str:
    with open(get_filename(day), 'r') as f:
        return f.read().strip()


def read_data_as_int_grid(day: int) -> np.array:
    lst = read_data_as_list(day)
    lst = [[int(c) for c in line] for line in lst]
    return np.array(lst)
