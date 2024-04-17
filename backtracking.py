import copy
from typing import Optional
from variable_class import Variable

def empty_options(variables: list[Variable]) -> bool:
    is_empty_options = True
    column = 0
    while column < len(variables) and is_empty_options:
        if variables[column].possible_rows:
            is_empty_options = False
        column += 1
    return is_empty_options

def select_mrv(variables: list[Variable]) -> Optional[int]:
    can_continue = not empty_options(variables)
    if can_continue:
        min_domain_index = 0
        min_domain_len = len(variables[0].possible_rows)
        for column, var in enumerate(variables):
            if (var.row == -1 and len(var.possible_rows) > 0
                and len(var.possible_rows) <= min_domain_len):
                min_domain_index = column
                min_domain_len = len(var.possible_rows)
    else:
        min_domain_index =  None
    return min_domain_index

def forward_checking(variables: list[Variable], mrv_index: int, row: int) -> list[Variable]:
    new_variables = copy.deepcopy(variables)
    for column, var in enumerate(new_variables):
        var.possible_rows.discard(row)
        descending_diagonal = row + (mrv_index - column)
        var.possible_rows.discard(descending_diagonal)
        ascending_diagonal = row - (mrv_index - column)
        var.possible_rows.discard(ascending_diagonal)
    return new_variables

def solve_n_queens(variables: list[Variable], queens_to_place: int) -> Optional[list[Variable]]:
    if queens_to_place == 0:
        return variables
    mrv_index = select_mrv(variables)
    if mrv_index is not None:
        for row in variables[mrv_index].possible_rows:
            new_variables = forward_checking(variables, mrv_index, row)
            new_variables[mrv_index].row = row
            result = solve_n_queens(new_variables, queens_to_place - 1)
            if result is not None:
                return result
    return None
