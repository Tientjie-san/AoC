from utils import read_file
from typing import List
import hashlib

def part1(input: List[str]) -> int:

    prefix = input[0]
    i = 0

    while True:

        hash_result = hashlib.md5((prefix + str(i)).encode())
        digested_hash = list(hash_result.digest())
        if digested_hash[0] == 0 and digested_hash[1] == 0 and digested_hash[2] <= 0X0F:
            return i
        
        i += 1

def part2(input: List[str]) -> int:
    
    prefix = input[0]
    i = 0

    while True:

        hash_result = hashlib.md5((prefix + str(i)).encode())
        digested_hash = list(hash_result.digest())
        if digested_hash[0] == 0 and digested_hash[1] == 0 and digested_hash[2] == 0:
            return i
        
        i += 1

def main():
    puzzle_input = read_file("day4")
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == "__main__":
    main()
