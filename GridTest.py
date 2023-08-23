import tkinter as tk
from tkinter import ttk
import numpy as np
from main import print_sudoku, sudoku_solver


class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.list = [[tk.IntVar(value=0) for y in range(9)] for y in [x for x in range(9)]] # revisar si se puede emprolijar
        self.solution = [[0 for y in range(9)] for y in [x for x in range(9)]]
        self.current_element = [0, 0]

    @property
    def np_list(self):
        return np.array([[y.get() for y in x] for x in self.list], dtype='uint8')

    def create_grid(self, where):
        for i in range(self.rows):
            for j in range(self.columns):
                entry = ttk.Entry(where, textvariable=self.list[i][j])
                entry.grid(row=i, column=j, padx=1, pady=1)

    def print_grid(self):
        print_sudoku(self.np_list)

    def solve(self):
        sudoku_solver(self.np_list, self.current_element, self.solution)
        for i in range(9):
            for j in range(9):
                self.list[i][j].set(self.solution[i][j])


# create the root window:
root = tk.Tk()
root.title('testing app')

# frame:
frame = ttk.Frame(root)
frame.pack()

# create the grid
# create_grid(root, 9, 9)
my_grid = Grid(9, 9)
my_grid.create_grid(frame)

# button:
button = tk.Button(root, text='print', command=my_grid.solve)
button.pack()

# run the main app
root.mainloop()
