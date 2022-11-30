from typing import List
from utils import read_file

def part1(input: List[str]) -> int:
    floor = 0
    for line in input:
        for char in line:
            if char == "(":
                floor += 1
            else:
                floor -= 1
    return floor

def part2(input: List[str]) -> int:
    floor = 0
    count = 0
    for line in input:
        for char in line:
            count += 1
            if char == "(":
                floor += 1
            else:
                floor -= 1
            
            if floor == -1:
                return count

    return count


def main():
    puzzle_input = read_file("day1")
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()