from dis import Instruction
from utils import read_file
from typing import List

class Worker:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def work(self, instructions: List[str]):
        visited_houses = set()
        visited_houses.add((self.x, self.y))
        for instruction in instructions:
            if instruction == "<":
                self.x -= 1
            elif instruction == ">":
                self.x += 1
            elif instruction =="^":
                self.y += 1 
            else:
                self.y -= 1
            visited_houses.add((self.x, self.y))
        return visited_houses

def part1(input: List[str]) -> int:
    
    instructions = input[0]
    worker = Worker()
    visited_houses = set()
    visited_houses = worker.work(instructions)
    
    return len(visited_houses)

def part2(input: List[str]) -> int:
    instructions = input[0]
    santa = Worker()
    robot = Worker()
    santa_instructions = [instruction for idx, instruction in enumerate(instructions) if idx %2 == 0 ]
    robot_instructions = [instruction for idx, instruction in enumerate(instructions) if idx %2 != 0 ]
    visited_houses_santa = santa.work(santa_instructions)
    visited_houses_robot = robot.work(robot_instructions)
    
    return len(visited_houses_santa.union(visited_houses_robot))

def main():
    puzzle_input = read_file("day3")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == "__main__":
    main()
