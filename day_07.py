import re
from utils.data import read_data_as_list


class Node:
    parent = None
    children = None
    name = None
    type = None
    size = 0

    def __init__(self, parent, name, size, node_type):
        self.parent = parent
        self.name = name
        self.size = size
        self.node_type = node_type
        self.children = {}
        self.total_size = 0

    def add_child(self, child):
        self.children[child.name] = child

    def print_tree(self, indent=0):
        space = ' ' * indent
        print(f'{space} {self}')
        for name, child in self.children.items():
            child.print_tree(indent+4)

    def __repr__(self):
        return f'- {self.name} ({self.node_type}) - {self.total_size}'

    def calculate_total_size(self):
        if self.node_type == 'file':
            self.total_size = self.size
            return self.size
        total = 0
        for name, child in self.children.items():
            total += child.calculate_total_size()
        self.total_size = total
        return total

    def get_all_dir_sizes(self):
        if self.node_type == 'file':
            return []
        sizes = [self.total_size]
        for name, child in self.children.items():
            sizes.extend(child.get_all_dir_sizes())
        return sizes


def construct_tree(lines):
    root = Node(None, 'root', 0, 'dir')
    current = root
    for line in lines:
        if match := re.match(r'(\d+)\s(\w+.?\w*)$', line):
            size, name = match.groups()
            child = Node(current, name, int(size), 'file')
            current.add_child(child)
        elif match := re.match(r'dir\s(\w+)$', line):
            name = match.group(1)
            child = Node(current, name, 0, 'dir')
            current.add_child(child)
        elif line == '$ cd ..':
            current = current.parent
        elif line == '$ cd /':
            current = root
        elif line.startswith('$ cd'):
            name = line.split()[-1]
            current = current.children[name]
    return root


if __name__ == '__main__':
    # Construct file system
    data = read_data_as_list(day=7)
    file_system = construct_tree(data)
    file_system.calculate_total_size()
    file_system.print_tree()

    # Part 1
    dir_sizes = file_system.get_all_dir_sizes()
    result = sum(size for size in dir_sizes if size <= 100000)
    print(f'Part 1 Solution: {result}')

    # Part 2
    total_space = 70000000
    required_space = 30000000
    used_space = file_system.total_size
    size_to_delete = used_space + required_space - total_space
    result = min([size for size in dir_sizes if size >= size_to_delete])
    print(f'Part 2 Solution: {result}')
