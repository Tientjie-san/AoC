from utils import read_file
from typing import List

def atleast_three_vowel(word: str):

    vowels = "aeiou"
    count = 0 
    for c in word:
        if c in vowels: 
            count += 1
    return count >= 3

def double_letter(word:str):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return True
    
    return False

def not_contain_bad_sub(word:str):
    baddies = ["ab", "cd", "pq", "xy"]
    for bad in baddies:
        if bad in word:
            return False
    return True

def nice_pair(word:str):
    pairs = [word[i:i+2]for i in range(len(word)-1) ]
    for i in range(len(pairs)-1):
        if pairs[i] in pairs[i+2:]:
            return True
    return False

def repeat_inbetween(word:str):
    for i in range(len(word)-2):
        if word[i] == word[i+2]:
            return True
    return False



def part1(input: List[str]) -> int:
    count = 0
    for word in input:
        if atleast_three_vowel(word) and double_letter(word) and not_contain_bad_sub(word):
            count += 1
    return count


def part2(input: List[str]) -> int:
    count = 0
    for word in input:
        if nice_pair(word) and repeat_inbetween(word):
            count += 1
    return count

def main():
    puzzle_input = read_file("day5")
    print(part1(puzzle_input))
    print(part2(puzzle_input))
    print(nice_pair("qjhvhtzxzqqjkmpb"))
    print(nice_pair("xxyxx"))


if __name__ == "__main__":
    main()
