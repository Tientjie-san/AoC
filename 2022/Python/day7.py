from utils import read_file
from typing import List

class Directory:
    def __init__(self, name: str, parent = None):
        self.parent= parent
        self.name: str = name
        self.dirs = dict()
        self.files = []
    
    def get_size(self):
        total = 0
        for dir in self.dirs.values():
            total += dir.get_size()
        total += sum(self.files)
        global sizes
        sizes.append(total)
        return total

    def __repr__(self):
        return f"name: {self.name},\n directories : {self.dirs},\n files : {self.files}"


def part1(input: List[str]) -> int:

    main_directory = Directory("/")
    current_directory = main_directory

    for line in input:
        line = line.split(" ")

        if line[0] == "$" and line[1] == "ls":
            continue
        elif line[0] == "dir":
            directory_name = line[1]
            if directory_name not in current_directory.dirs:
                current_directory.dirs[directory_name] = Directory(directory_name, current_directory)
        elif line[0].isdigit():
            current_directory.files.append(int(line[0]))
        elif line[0] == "$" and line[1] == "cd" and line[2] != "..":
            directory_name = line[2]
            if directory_name == "/":
                current_directory = main_directory
            else:
                current_directory = current_directory.dirs[directory_name]
        elif line[0] == "$" and line[1] == "cd" and line[2] == "..":
            current_directory = current_directory.parent

    global sizes 
    sizes = []
    main_directory.get_size()
    return sum([ size for size in sizes if size <= 100000])

            
def part2(input: List[str]) -> int:
        
    main_directory = Directory("/")
    current_directory = main_directory

    for line in input:
        line = line.split(" ")

        if line[0] == "$" and line[1] == "ls":
            continue
        elif line[0] == "dir":
            directory_name = line[1]
            if directory_name not in current_directory.dirs:
                current_directory.dirs[directory_name] = Directory(directory_name, current_directory)
        elif line[0].isdigit():
            current_directory.files.append(int(line[0]))
        elif line[0] == "$" and line[1] == "cd" and line[2] != "..":
            directory_name = line[2]
            if directory_name == "/":
                current_directory = main_directory
            else:
                current_directory = current_directory.dirs[directory_name]
        elif line[0] == "$" and line[1] == "cd" and line[2] == "..":
            current_directory = current_directory.parent

    global sizes 
    sizes = []

    max_memory = 70000000
    min_open = 30000000
    
    available = max_memory - main_directory.get_size()
    to_delete = min_open - available

    return min([ size for size in sizes if size >= to_delete])


def main():
    puzzle_input = read_file("day7")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == "__main__":
    main()
