import copy
from typing import Optional
from variable_class import Variable

def empty_options(variables: list[Variable]) -> bool:
    is_empty_options = True
    i = 0
    while i < len(variables) and is_empty_options:
        if variables[i].possible_values:
            is_empty_options = False
        i += 1
    return is_empty_options

def select_mrv(variables: list[Variable]) -> Optional[int]:
    can_continue = not empty_options(variables)
    if can_continue:
        min_domain_index = 0
        min_domain_len = len(variables[0].possible_values)
        for i, var in enumerate(variables):
            if var.value == -1 and len(var.possible_values) > 0 and len(var.possible_values) <= min_domain_len:
                min_domain_index = i
                min_domain_len = len(var.possible_values)
    else:
        min_domain_index =  None
    return min_domain_index

def forward_checking(variables: list[Variable], mrv_index: int, value: int) -> list[Variable]:
    new_variables = copy.deepcopy(variables)
    for column, var in enumerate(new_variables):
        var.possible_values.discard(value)
        descending_diagonal = value + (mrv_index - column)
        var.possible_values.discard(descending_diagonal)
        ascending_diagonal = value - (mrv_index - column)
        var.possible_values.discard(ascending_diagonal)
    return new_variables

def solve_n_queens(variables: list[Variable], queens_to_place: int) -> Optional[list[Variable]]:
    if queens_to_place == 0:
        return variables
    mrv_index = select_mrv(variables)
    if mrv_index is not None:
        for value in variables[mrv_index].possible_values:
            new_variables = forward_checking(variables, mrv_index, value)
            new_variables[mrv_index].value = value
            result = solve_n_queens(new_variables, queens_to_place - 1)
            if result is not None:
                return result
    return None
