import tkinter
class Board():
    def __init__(self):
        self.board = tkinter.Tk()
        w = tkinter.Canvas(self.board, width=630, height=630)
        w.pack()
        self.board_matrix = [[1 for k in range(9)] for k in range(9)]
        for i in range(9):
            for j in range(9):
                w.create_rectangle(70 * i, 70 * j, 70 * (i + 1), 70 * (j + 1))
                if i % 3 == 0:
                    w.create_line(0, i * 70, 9 * 70, i * 70, width=3)
                if j % 3 == 0:
                    w.create_line(j * 70, 0, j * 70, 9 * 70, width=3)
        self.draw_board(w)
        self.board.mainloop()
        
    def draw_board(self, w):
        for i in range(len(self.board_matrix)):
            for j in range(len(self.board_matrix[0])):
                w.create_text(i * 70 + 35, j * 70 + 35, fill="darkblue",font="Times 20 italic bold",
                              text=self.board_matrix[i][j])
        
board = Board()