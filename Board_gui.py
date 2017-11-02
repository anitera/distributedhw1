import tkinter
import numpy as np

class Board():
    def __init__(self):
        self.board = tkinter.Tk()
        w = tkinter.Canvas(self.board, width=630, height=630)
        self.canvas = w
        self.board_matrix = [[1 for k in range(9)] for k in range(9)]
        self.numbers_dict = {1 : 'blue', 2: 'green', 3: 'blue', 4: 'red', 5: 'black',
                             6: 'orange', 7: 'brown', 8: 'purple', 9: 'cyan'}
        # self.board.mainloop()
    
    def initialize_board(self):
        for i in range(9):
            for j in range(9):
                self.canvas.create_rectangle(70 * i, 70 * j, 70 * (i + 1), 70 * (j + 1))
                if i % 3 == 0:
                    self.canvas.create_line(0, i * 70, 9 * 70, i * 70, width=3)
                if j % 3 == 0:
                    self.canvas.create_line(j * 70, 0, j * 70, 9 * 70, width=3)
        self.canvas.pack()
        
    def show_board(self):
        self.board.mainloop()
    
    def set_board_numbers(self, matrix):
        self.board_matrix = matrix
        
    def draw_board_numbers(self):
        for i in range(len(self.board_matrix)):
            for j in range(len(self.board_matrix[0])):
                self.canvas.create_text(i * 70 + 35, j * 70 + 35, activefill = 'olive',
                                        fill = self.numbers_dict[int(self.board_matrix[i][j])],
                              font="Times 20 italic bold",
                              text=self.board_matrix[i][j])
matrix = []
for i in range(9):
    matrix.append(np.arange(1,10))
board = Board()
board.initialize_board()
board.set_board_numbers(matrix)
board.draw_board_numbers()
board.show_board()