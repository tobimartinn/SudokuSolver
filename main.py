from CommonFunctions import check_number, calculate_next_el


def print_sudoku(sudoku):
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    for i in sudoku:
        print("|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")


current_element = [0, 0]


def store_solution(sudoku, solution):
    for i in range(9):
        for j in range(9):
            solution[i][j] = sudoku[i, j]


def sudoku_solver(sudoku, current_element, solution):
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
                # print_sudoku(sudoku)
                return True
            else:
                if sudoku_solver(sudoku, next_element, solution):
                    return True
        else:
            pass
    else:
        sudoku[current_row][current_column] = 0
        return False
