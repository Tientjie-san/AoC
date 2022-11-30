from typing import List

def read_file(filename: str) -> List[str]:
    with open(f"../Inputs/{filename}") as f:
        return [line.strip() for line in f]

