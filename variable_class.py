from dataclasses import dataclass

@dataclass
class Variable:
    value: int
    possible_values: set[int]
