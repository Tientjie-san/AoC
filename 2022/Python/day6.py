from utils import read_file
from typing import List

def part1(input: List[str]) -> int:
    for i in range(len(input)-3):
        if len(set([input[i + n] for n in range(4)])) == 4:
            return i+4


def part2(input: List[str]) -> int:
    for i in range(len(input)-13):
        if len(set([input[i + n] for n in range(14)])) == 14:
            return i+14

def main():
    puzzle_input = "".join(read_file("day6"))
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == "__main__":
    main()
