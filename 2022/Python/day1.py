from utils import read_file
from typing import List

def part1(input: List[str]) -> int:
    totals = []
    current_sum = 0
    for str_num in input:
        if str_num == "":
            totals.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(str_num)

    return max(totals)

def part2(input: List[str]) -> int:
    totals = []
    current_sum = 0
    for str_num in input:
        if str_num == "":
            totals.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(str_num)
    sorted_totals = sorted(totals, reverse=True)
    return sum(sorted_totals[0:3])

def main():
    puzzle_input = read_file("day1")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == "__main__":
    main()
