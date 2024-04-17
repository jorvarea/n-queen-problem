from dataclasses import dataclass

@dataclass
class Variable:
    row: int
    possible_rows: set[int]
