import os


DATA_PATH = 'data'


def get_filename(day: int) -> str:
    return os.path.join(DATA_PATH, f'day_{day:02}.txt')


def read_data_as_list(day: int) -> list[str]:
    with open(get_filename(day), 'r') as f:
        return [line.strip() for line in f.readlines()]
