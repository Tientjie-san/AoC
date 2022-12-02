from utils import read_file
from typing import List
    
def part1(input: List[str]) -> int:
    # rock = 1 , paper =2, scissor = 3, L = 0, W = 6 D = 3
    score_combinations = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6 
    }
    total_score = 0
    for round  in input:
        total_score += score_combinations[round]

    return total_score

def part2(input: List[str]) -> int:
    # X = lose, Y = draw, z = win
    responses = {
        "A X": "C",
        "A Y": "A",
        "A Z": "B",
        "B X": "A",
        "B Y": "B",
        "B Z": "C",
        "C X": "B",
        "C Y": "C",
        "C Z": "A" 
    }

    values = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    
    total_scores = 0

    for round in input:
        total_scores += values[responses[round]] + values[round[-1]]

    return total_scores

def main():
    puzzle_input = read_file("day2")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == "__main__":
    main()
