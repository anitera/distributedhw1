try:
    import tkinter as tk
    from tkinter import *
except ImportError:
    import Tkinter as tk
    from Tkinter import *
import numpy as np
from Generation import *

class Board():
    def __init__(self):
        self.board = tk.Tk()
        self.cell_size = 60
        self.board_width = 15 * self.cell_size
        self.board_height = 9 * self.cell_size
        w = tk.Canvas(self.board, width=self.board_width, height=self.board_height)
        self.canvas = w
        self.board_matrix = [[1 for k in range(9)] for k in range(9)]
        self.numbers_dict = {1 : 'blue', 2: 'green', 3: 'magenta', 4: 'orangered', 5: 'limegreen',
                             6: 'orange', 7: 'brown', 8: 'purple', 9: 'darkcyan'}
    
    def initialize_board(self):
        for i in range(9):
            for j in range(9):
                self.canvas.create_rectangle(self.cell_size * i, self.cell_size * j,
                                             self.cell_size * (i + 1), self.cell_size * (j + 1))
                if i % 3 == 0:
                    self.canvas.create_line(0, i * self.cell_size, 9 * self.cell_size,
                                            i * self.cell_size, width=3)
                if j % 3 == 0:
                    self.canvas.create_line(j * self.cell_size, 0, j * self.cell_size,
                                            9 * self.cell_size, width=3)
        self.canvas.pack()
        
    def show_board(self):
        self.board.mainloop()
    
    def set_board_number(self, i, j, value):
        self.board_matrix[i][j] = value
    
    def set_board_numbers(self, matrix):
        self.board_matrix = matrix
        
    def draw_board_numbers(self):
        for i in range(len(self.board_matrix)):
            for j in range(len(self.board_matrix[0])):
                if self.board_matrix[i][j]:
                    self.canvas.create_text(i * self.cell_size + self.cell_size / 2,
                                            j * self.cell_size + self.cell_size / 2, activefill = 'olive',
                                            fill = self.numbers_dict[int(self.board_matrix[i][j])],
                                  font="Times 20 italic bold",
                                  text=self.board_matrix[i][j])

matrix_task, matrix_answer = return_question_and_answer()
board = Board()
board.initialize_board()
board.set_board_numbers(matrix_task)
board.draw_board_numbers()
board.show_board()
