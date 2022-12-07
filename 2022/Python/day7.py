from utils import read_file
from typing import List

class Directory:
    def __init__(self, key: str):
        self.key: str = key
        self.dirs = set()
        self.files = []
    
    def __repr__(self):
        return f"{self.key} contains dictionaries:  {[dir.key for dir in self.dirs]} and has {self.files} files"

    def get_size(self):
        total = 0
        for dir in self.dirs:
            total += dir.get_size()
        total += sum(self.files)
        return total

def part1(input: List[str]) -> int:

    filesystem = dict()
    for line in input:
        line = line.split(" ")

        if line[0] == "$" and line[1] == "cd" and line[2] != "..":
            if line[2] not in filesystem:
                current_directory = Directory(line[2])
                filesystem[current_directory.key] = current_directory
            else:
                current_directory = filesystem[line[2]]
        if line[0] == "$" and line[1] == "ls":
            continue
        if line[0] == "dir":
            new_directory = Directory(line[1])
            if new_directory.key not in filesystem:
                filesystem[new_directory.key] = new_directory
            current_directory.dirs.add(new_directory)
        if line[0].isdigit():
            current_directory.files.append(int(line[0]))

    return sum(dir.get_size() for dir in filesystem.values() if dir.get_size() <= 100000)
        
        




            
    
def part2(input: List[str]) -> int:
    return 0

def main():
    puzzle_input = read_file("day7")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == "__main__":
    main()
