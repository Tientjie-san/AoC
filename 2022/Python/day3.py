from utils import read_file
from typing import List
import string

def part1(input: List[str]) -> int:
    total_priorities = 0
    for sacks in input:
        common_items = set()
        total_items = len(sacks)
        half_idx = int(total_items/2)
        p1 = sacks[0:half_idx]
        p2 = sacks[half_idx:total_items]
        for char in p1:
            if char in p2 and char not in common_items: 
                common_items.add(char)
                total_priorities += string.ascii_letters.index(char) + 1


    return total_priorities

def part2(input: List[str]) -> int:
    total_priorities = 0
    for i in range(0, len(input)-2, 3):
        g1 = input[i]
        g2 = input[i+1]
        g3 = input[i+2]
        for char in g1:
            if char in g2 and char in g3:
                total_priorities += string.ascii_letters.index(char) + 1
                break


    return total_priorities

def main():
    puzzle_input = read_file("day3")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == "__main__":
    main()
