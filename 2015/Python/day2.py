from utils import read_file
from typing import List

def part1(input: List[str]) -> int:
    for line in input:
        l,w,h = [int(num) for num in line.split("x")]
    return 0

def part2(input: List[str]) -> int:
    return 0

def main():
    puzzle_input = read_file("day2.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == "__main__":
    main()
