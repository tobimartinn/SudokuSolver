import tkinter as tk
from tkinter import ttk
import numpy as np
from commonFunctions import print_sudoku, sudoku_solver


class Grid:
    def __init__(self):
        self.rows = 9
        self.columns = 9
        # self.list1 = [[tk.IntVar(value=0) for y in range(9)] for y in [x for x in range(9)]] (deprecated)
        self.list = [[tk.IntVar(value=0) for _ in range(9)] for _ in range(9)]
        self.solution = [[0 for y in range(9)] for y in [x for x in range(9)]]
        self.current_element = [0, 0]

    @property
    def np_list(self):
        return np.array([[y.get() for y in x] for x in self.list], dtype='uint8')

    def create_grid(self, where):
        where.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1, uniform='a')
        where.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1, uniform='a')

        for i in range(self.rows):
            for j in range(self.columns):
                entry = ttk.Entry(where, textvariable=self.list[i][j], width=3, justify='center')
                entry.grid(row=i, column=j, ipadx=10, ipady=10)

    def print_grid(self):
        print_sudoku(self.np_list)

    def solve(self):
        sudoku_solver(self.np_list, self.solution, self.current_element)
        for i in range(9):
            for j in range(9):
                self.list[i][j].set(self.solution[i][j])
