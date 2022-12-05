from utils import read_file
from typing import List

"""
Oplossing: 
Itereer door de lijst van input van achter naar voren.
Stop bij de eerste a. als a verwijst naar andere wire, ga dan verder naar die wire. Dit  gaat door totdat de instructie een integer is. 
"""

def calc(signal, instructions: List[str]):
    i = 0
    if instructions[i].isdigit():
        return int(instructions[i])
    else:
        calc(signal, instructions)


def part1(input: List[str]) -> int:
    return 0

def part2(input: List[str]) -> int:
    return 0

def main():
    puzzle_input = read_file("dayx")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == "__main__":
    main()
