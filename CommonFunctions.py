import numpy as np

diction = {0: [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
        1: [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]],
        2: [[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 6], [2, 7], [2, 8]],
        3: [[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]],
        4: [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]],
        5: [[3, 6], [3, 7], [3, 8], [4, 6], [4, 7], [4, 8], [5, 6], [5, 7], [5, 8]],
        6: [[6, 0], [6, 1], [6, 2], [7, 0], [7, 1], [7, 2], [8, 0], [8, 1], [8, 2]],
        7: [[6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 5], [8, 3], [8, 4], [8, 5]],
        8: [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]}


def check_quadrant(sudoku, element):
    """
    It checks if the number that points the parameter 'element' is valid only in the 3x3 corresponding quadrant.
    :param sudoku:
    :param element:
    :return: True: if it's valid / False: if it's not
    """
    actual_row = element[0]
    actual_column = element[1]
    actual_key = 0

    for key, value in diction.items():
        for i in value:
            if element == i:
                actual_key = key
                break

    for value in diction[actual_key]:
        row = value[0]
        column = value[1]
        if (sudoku[row][column] == sudoku[actual_row][actual_column]) and (element != value):
            return True
        else:
            continue

    return False


def check_number(sudoku, element):
    """
    It checks if the number that points the parameter 'element' is valid for that position.
    :param sudoku:
    :param element:
    :return: True: if it`s valid / False: if it's not
    """
    current_row = element[0]
    current_column = element[1]
    # check row:
    for i in range(9):
        if (sudoku[current_row][i] == sudoku[current_row][current_column]) and (current_column != i):
            return False
    # check column:
    for i in range(9):
        if (sudoku[i][current_column] == sudoku[current_row][current_column]) and (current_row != i):
            return False
    # check quadrant:
    if check_quadrant(sudoku, element):
        return False

    return True


def sum_one(element):
    """
    It calculates the immediately subsequent element in the sudoku list WITHOUT taking into account if it`s a zero or not.
    :param element:
    :return: the index of the immediately subsequent element
    """
    # 'element' is a list of two elements with the following information: [row, column]
    current_row = element[0]
    current_column = element[1]
    next_column = current_column + 1
    modulus = next_column % 9
    if next_column == modulus:
        current_column = next_column
    else:
        current_column = modulus
        current_row += 1

    next_element = [current_row, current_column]
    return next_element




def calculate_next_el(sudoku, current_element):
    """
    It calculates the next element in the sudoku list but taking into account if it`s a zero or not.
    :param sudoku:
    :param current_element:
    :return: The index of the next (valid) element
    """
    next_element = [current_element[0], current_element[1]]
    next_element = sum_one(next_element)
    if next_element == [9, 0]:
        return next_element
    if sudoku[next_element[0]][next_element[1]] == 0:
        return next_element
    else:
        return calculate_next_el(sudoku, next_element)




