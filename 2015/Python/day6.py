from utils import read_file
from typing import List

def part1(input: List[str]) -> int:
    
    lights = [0 for _ in range(1000000)]
    for line in input:
        instruction = line.split(",")
        x1 = int(instruction[0].split(" ")[-1])
        y1 = int(instruction[1].split(" ")[0])
        x2 = int(instruction[1].split(" ")[-1])
        y2 = int(instruction[2])
        for i in range(x1, x2+1):
            i = i*1000

            for j in range(y1, y2+1):
                idx = i + j
        
                if instruction[0].split(" ")[0] == "toggle":
                    if lights[idx] == 0:
                        lights[idx] = 1
                    else:
                        lights[idx] = 0

                elif instruction[0].split(" ")[1] == "on":
                    lights[idx] = 1
                else:
                    lights[idx] = 0

    return sum(lights)

def part2(input: List[str]) -> int:

    lights = [0 for _ in range(1000000)]
    for line in input:
        instruction = line.split(",")
        x1 = int(instruction[0].split(" ")[-1])
        y1 = int(instruction[1].split(" ")[0])
        x2 = int(instruction[1].split(" ")[-1])
        y2 = int(instruction[2])
        for i in range(x1, x2+1):
            i = i*1000

            for j in range(y1, y2+1):
                idx = i + j
        
                if instruction[0].split(" ")[0] == "toggle":
                    lights[idx] += 2

                elif instruction[0].split(" ")[1] == "on":
                    lights[idx] += 1
                else:
                    lights[idx] = max(0, lights[idx]-1)

    return sum(lights)

def main():
    puzzle_input = read_file("day6")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == "__main__":
    main()
