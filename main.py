# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |

# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def print_sudoku(sudoku):
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    for i in sudoku:
        print("|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")


current_element = [0, 0]


diction = {0: [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
        1: [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]],
        2: [[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 6], [2, 7], [2, 8]],
        3: [[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]],
        4: [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]],
        5: [[3, 6], [3, 7], [3, 8], [4, 6], [4, 7], [4, 8], [5, 6], [5, 7], [5, 8]],
        6: [[6, 0], [6, 1], [6, 2], [7, 0], [7, 1], [7, 2], [8, 0], [8, 1], [8, 2]],
        7: [[6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 5], [8, 3], [8, 4], [8, 5]],
        8: [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]}


def check_cuadrant(list, element):
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
        if (list[row][column] == list[actual_row][actual_column]) and (element != value):
            return True
        else:
            continue

    return False


def check_number(list, element):
    current_row = element[0]
    current_column = element[1]
    #check row:
    for i in range(9):
        if (list[current_row][i] == list[current_row][current_column]) and (current_column != i):
            return False
    #check column:
    for i in range(9):
        if (list[i][current_column] == list[current_row][current_column]) and (current_row != i):
            return False
    #check cuadrant:
    if check_cuadrant(list, element):
        return False

    return True


def sum_one(element):
    current_column = element[1]
    current_row = element[0]
    next_column = current_column + 1
    modulus = next_column % 9
    if next_column == modulus:
        current_column = next_column
    else:
        current_column = modulus
        current_row += 1

    next_element = [current_row, current_column]
    return next_element


def calculate_next_el(list, current_element):
    next_element = [current_element[0], current_element[1]]
    next_element = sum_one(next_element)
    if next_element == [9, 0]:
        return next_element
    if (list[next_element[0]][next_element[1]] == 0):
        return next_element
    else:
        return calculate_next_el(list, next_element)


def sudoku_solver(list, current_element):
    current_row = current_element[0]
    current_column = current_element[1]

    for i in range(9):
        list[current_row][current_column] += 1
        if check_number(list, current_element):
            next_element = calculate_next_el(list, current_element)
            if next_element == [9, 0]:
                print_sudoku(list)
                return True
            else:
                if sudoku_solver(list, next_element):
                    return True
        else:
            pass
    else:
        list[current_row][current_column] = 0
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

sudoku_solver(sudoku, current_element)








