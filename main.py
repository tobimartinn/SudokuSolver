import grid
import tkinter as tk
from tkinter import ttk

# creates the main app
root = tk.Tk()
root.title('SudokuSolver')

# frame for the grid
grid_frame = ttk.Frame()
grid_frame.pack()

# grid
my_grid = grid.Grid()
my_grid.create_grid(grid_frame)

# solve button
solve_button = ttk.Button(root, text='solve', command=my_grid.solve)
solve_button.pack()

# run the main app
root.mainloop()
