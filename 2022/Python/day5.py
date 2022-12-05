from collections import deque
from utils import read_file
from typing import List



def part1(input: List[str]) -> str:
    message = ""
    stacks = {
        1: deque(["S", "C", "V", "N"]),
        2: deque(["Z", "M", "J","H", "N" ,"S"]),
        3: deque(["M", "C", "T", "G", "J", "N", "D"]),
        4: deque(["T", "D", "F", "J", "W", "R","M"]),
        5: deque(["P","F","H"]),
        6: deque(["C","T","Z","H","J"]),
        7: deque(["D","P", "R","Q","F","S","L", "Z"]),
        8: deque(["C","S","L","H","D","F","P","W"]),
        9: deque(["D","S","M","P","F","N","G","Z"]),
    }

    for instruction in input:
        instruction = instruction.split(" ")
        n = int(instruction[1])
        a = int(instruction[3])
        b = int(instruction[5])
        for _ in range(n):
            stacks[b].append(stacks[a].pop())
    for i in range(1,10):
        message += stacks[i][-1]

    return message

def part2(input: List[str]) -> str:
    message = ""
    stacks = {
        1: deque(["S", "C", "V", "N"]),
        2: deque(["Z", "M", "J","H", "N" ,"S"]),
        3: deque(["M", "C", "T", "G", "J", "N", "D"]),
        4: deque(["T", "D", "F", "J", "W", "R","M"]),
        5: deque(["P","F","H"]),
        6: deque(["C","T","Z","H","J"]),
        7: deque(["D","P", "R","Q","F","S","L", "Z"]),
        8: deque(["C","S","L","H","D","F","P","W"]),
        9: deque(["D","S","M","P","F","N","G","Z"]),
    }

    for instruction in input:
        instruction = instruction.split(" ")
        n = int(instruction[1])
        a = int(instruction[3])
        b = int(instruction[5])
        temp_stack = deque()
        for _ in range(n):
            temp_stack.appendleft(stacks[a].pop())
        stacks[b].extend(temp_stack)
    for i in range(1,10):
        message += stacks[i][-1]

    return message

def main():
    puzzle_input = read_file("day5")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == "__main__":
    main()


