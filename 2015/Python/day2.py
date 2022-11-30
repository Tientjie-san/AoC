import math
from statistics import median
from utils import read_file
from typing import List

def part1(input: List[str]) -> int:
    total_surface = 0
    for line in input:
        l,w,h = [int(num) for num in line.split("x")]
        surface = 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
        total_surface += surface 

    return total_surface

def part2(input: List[str]) -> int:
    total_ribbon = 0
    for line in input:
        l,w,h = [int(num) for num in line.split("x")]
        ribbon = l*w*h + 2*min(l,w,h) + 2* median([l,w,h])
        total_ribbon += ribbon 

    return total_ribbon

def main():
    puzzle_input = read_file("day2")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == "__main__":
    main()
