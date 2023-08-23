import numpy as np

quadrant_reference = np.repeat(np.repeat(np.arange(9).reshape(3, 3), 3, axis=0), 3).reshape(9, 9)


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


def sum_one(element):
    """
    It calculates the immediately subsequent element in the sudoku list WITHOUT taking into account if it's a zero or not.
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
    It calculates the next element in the sudoku list but taking into account if it's a zero or not.
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


def print_sudoku(sudoku):
    """
    Prints the sudoku in a prettier way.
    :param sudoku:
    :return: None
    """
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    for i in sudoku:
        print("|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")


def store_solution(sudoku, solution):
    """
    Stores the solution from the sudoku np array (immutable) to the mutable solution list.
    :param sudoku:
    :param solution:
    :return: None
    """
    for i in range(9):
        for j in range(9):
            solution[i][j] = sudoku[i, j]


def sudoku_solver(sudoku, solution, current_element=None):
    """
    Solves the 'sudoku', starting from the 'current_element' ([0,0] by default), and stores the solution in 'solution'.
    :param sudoku:
    :param current_element:
    :param solution:
    :return: True if the sudoku can be solved, False if not
    """
    if not current_element:
        current_element = [0, 0]

    current_row = current_element[0]
    current_column = current_element[1]

    if current_element == [0, 0]:
        if sudoku[current_row][current_column] != 0:
            current_element = calculate_next_el(sudoku, current_element)
            current_row = current_element[0]
            current_column = current_element[1]

    for i in range(9):
        sudoku[current_row][current_column] += 1
        if check_number(sudoku, current_element):
            next_element = calculate_next_el(sudoku, current_element)
            if next_element == [9, 0]:
                store_solution(sudoku, solution)
                return True
            else:
                if sudoku_solver(sudoku, solution, next_element):
                    return True
        else:
            pass
    else:
        sudoku[current_row][current_column] = 0
        return False


