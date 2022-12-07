from CommonFunctions import check_number, calculate_next_el
import numpy as np


def print_sudoku(sudoku):
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    for i in sudoku:
        print("|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")


current_element = [0, 0]





def sudoku_solver(sudoku, current_element):
    current_row = current_element[0]
    current_column = current_element[1]

    if current_element == [0,0]:
        if sudoku[current_row][current_column] != 0:
            current_element = calculate_next_el(sudoku, current_element)
            current_row = current_element[0]
            current_column = current_element[1]

    for i in range(9):
        sudoku[current_row][current_column] += 1
        if check_number(sudoku, current_element):
            next_element = calculate_next_el(sudoku, current_element)
            if next_element == [9, 0]:
                print_sudoku(sudoku)
                return True
            else:
                if sudoku_solver(sudoku, next_element):
                    return True
        else:
            pass
    else:
        sudoku[current_row][current_column] = 0
        return False


sudoku = [[0, 0, 0, 0, 0, 4, 0, 2, 8],
          [4, 0, 6, 0, 0, 0, 0, 0, 5],
          [1, 0, 0, 0, 3, 0, 6, 0, 0],
          [0, 0, 0, 3, 0, 1, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 1, 4, 0],
          [0, 0, 0, 7, 0, 9, 0, 0, 0],
          [0, 0, 2, 0, 1, 0, 0, 0, 3],
          [9, 0, 0, 0, 0, 0, 5, 0, 7],
          [6, 7, 0, 4, 0, 0, 0, 0, 0]]

sudok2 = [[5, 0, 2, 0, 8, 0, 0, 0, 0],
          [0, 7, 0, 5, 0, 1, 0, 9, 0],
          [0, 0, 0, 2, 0, 0, 0, 0, 0],
          [4, 0, 0, 6, 0, 0, 0, 0, 7],
          [0, 1, 8, 0, 7, 0, 9, 6, 0],
          [7, 0, 0, 0, 0, 2, 0, 0, 4],
          [0, 0, 0, 0, 0, 3, 0, 0, 0],
          [0, 2, 0, 9, 0, 5, 0, 3, 0],
          [0, 0, 0, 0, 6, 0, 4, 0, 2]]

sudoku2 = np.array([[5, 0, 2, 0, 8, 0, 0, 0, 0],
                    [0, 7, 0, 5, 0, 1, 0, 9, 0],
                    [0, 0, 0, 2, 0, 0, 0, 0, 0],
                    [4, 0, 0, 6, 0, 0, 0, 0, 7],
                    [0, 1, 8, 0, 7, 0, 9, 6, 0],
                    [7, 0, 0, 0, 0, 2, 0, 0, 4],
                    [0, 0, 0, 0, 0, 3, 0, 0, 0],
                    [0, 2, 0, 9, 0, 5, 0, 3, 0],
                    [0, 0, 0, 0, 6, 0, 4, 0, 2]], dtype='uint8')



sudoku_solver(sudok2, current_element)









