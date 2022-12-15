import numpy as np

quadrant_reference = np.repeat(np.repeat(np.arange(9).reshape(3,3), 3, axis=0), 3).reshape(9, 9)


def _check_quadrant(sudoku, element):
    """
    It checks if the number that points the parameter 'element' is valid only in the 3x3 corresponding quadrant.
    :param sudoku:
    :param element:
    :return: True: if it's valid / False: if it's not
    """
    row = element[0]
    column = element[1]
    value = sudoku[row, column]
    quadrant_number = quadrant_reference[row, column]

    quadrant_list = sudoku[quadrant_reference == quadrant_number]
    values_in_list = quadrant_list == value

    return not len(quadrant_list[values_in_list]) > 1


def _check_row(sudoku, element):
    """
    It checks if the number that points the parameter 'element' is valid only in the corresponding row.
    :param sudoku:
    :param element:
    :return: True: if it's valid / False: if it's not
    """
    row = element[0]
    column = element[1]
    value = sudoku[row, column]
    row_list = sudoku[row]

    return not len(row_list[row_list == value]) > 1


def _check_column(sudoku, element):
    """
    It checks if the number that points the parameter 'element' is valid only in the corresponding column.
    :param sudoku:
    :param element:
    :return: True: if it's valid / False: if it's not
    """
    row = element[0]
    column = element[1]
    value = sudoku[row, column]
    column_list = sudoku[:, column]

    return not len(column_list[column_list == value]) > 1


def check_number(sudoku, element):
    """
    It checks if the number that points the parameter 'element' is valid for that position.
    :param sudoku:
    :param element:
    :return: True: if it`s valid / False: if it's not
    """
    return _check_row(sudoku, element) and _check_column(sudoku, element) and _check_quadrant(sudoku, element)
    """
    if not _check_row(sudoku, element):
        return False
    if not _check_column(sudoku, element):
        return False
    if not _check_quadrant(sudoku, element):
        return False

    return True
    """


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




