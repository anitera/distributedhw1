try:
    import tkinter as tk
    from tkinter import *
except ImportError:
    import Tkinter as tk
    from Tkinter import *

try:
    import tkMessageBox as tkBox
except ImportError:
    from tkinter import messagebox as tkBox	
	
import numpy as np
import operator
from Generation import *
from client import *

class Board():
    def __init__(self, nick, matrix=None, table=None, finished=False):
        self.board = tk.Tk()
        self.cell_size = 60
        self.board_width = 15 * self.cell_size
        self.board_height = 9 * self.cell_size
        w = tk.Canvas(self.board, width=self.board_width, height=self.board_height)
        self.canvas = w
        if matrix is not None:
            self.board_matrix = matrix
        else:
            self.board_matrix = [[0 for k in range(9)] for k in range(9)]
        if table is not None:
            self.table = table
        else:
            self.table = dict()
            self.table[nick] = 0
        self.draw_table_score()
        self.numbers_dict = {1 : 'blue', 2: 'green', 3: 'magenta', 4: 'orangered', 5: 'limegreen',
                             6: 'orange', 7: 'brown', 8: 'purple', 9: 'darkcyan'}
        self.initialize_board()
        #self.head = 'Username: ' + nick + '\n' + 'host:port ' + host + ':' + str(port) + '\n' + 'Session ' + str(session_id) + '\n' + 'Users in game: ' + str(session_size)
        self.head = 'Username: ' + nick + '\n'
        self.lab = tk.Label(self.board, text = self.head, justify = 'right', fg = 'navy', font=('Helvetica', 14))
        self.lab.place(x = 11 * self.cell_size, y = 0.5 * self.cell_size)
        self.last_move = (0, (0, 0))
        self.finished = finished
        #some object with dictionary table_score
    
    
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
        
    def EnterVal(self, e, a, b, ent):
        value = e.get()
        if value in [str(i) for i in range(1,10)]:
            self.last_move = (value, (a, b))
            tkBox.showinfo("Thanks", "Your move is proceed")
            ent.destroy()
            self.board.destroy()
        else:
            tkBox.showerror("Incorrect format", "Please enter number from 1 to 9")
    
    def Click(self, x):
        cell_column = (x.x) // self.cell_size
        cell_row = (x.y) // self.cell_size
        enter_number = tk.Tk()
        enter_number.resizable(width=False, height=False)
        lab = tk.Label(enter_number, text = "Please, enter number that you want\n to put on " + str(cell_column) +
                       "-th column and " + str(cell_row) + "-th row",
                       justify = 'right', fg = 'navy', font=('Helvetica', 14))
        lab.pack()
        entry_number = tk.Entry(enter_number)
        entry_number.pack()
        button1 = tk.Button(enter_number, text = "Proceed",
                            command=lambda: self.EnterVal(entry_number, cell_column, cell_row, enter_number))
        button1.pack()
        #enter_number.mainloop()
        
    def draw_board_numbers(self):
        for i in range(len(self.board_matrix)):
            for j in range(len(self.board_matrix[0])):
                if self.board_matrix[i][j]:
                    self.canvas.create_text(i * self.cell_size + self.cell_size / 2,
                                            j * self.cell_size + self.cell_size / 2, activefill = 'olive',
                                            fill = self.numbers_dict[int(self.board_matrix[i][j])],
                                  font="Times 20 italic bold",
                                  text=int(self.board_matrix[i][j]))
                else:
                    self.canvas.create_text(i * self.cell_size + self.cell_size / 2,
                                            j * self.cell_size + self.cell_size / 2, activefill = 'olive',
                                            fill = "black",
                                  font="Times 20 italic bold",
                                  text="?", tags='clickable')
        self.canvas.tag_bind('clickable', '<Button-1>', self.Click)
        if self.finished:
            self.end_game()
        
    def draw_table_score(self):
        self.table_score_listbox = tk.Listbox(self.board)
        self.table_score_listbox.place(x = int(11.5 * self.cell_size), y = int(3 * self.cell_size))
        table_name = tk.Label(self.board, text="NAME    SCORE",fg = 'navy', font=('Helvetica', 13))
        table_name.place(x = int(11.5 * self.cell_size), y = int(2.6 * self.cell_size))
        users_counter = 0
        sorted_table = sorted((self.table).items(), key=operator.itemgetter(1), reverse=True)
        n = 32 # maximum length of nickname (used to make table better visually)
        for nick in sorted_table:
            s = ""
            for i in range(n - len(nick[0])):
                s += " "
            self.table_score_listbox.insert(users_counter, str(nick[0]) + s + str(nick[1]))
            users_counter += 1
            
    def set_table(self, table):
        self.table = table
        
    def end_game(self):
        sorted_table = sorted((self.table).items(), key=operator.itemgetter(1), reverse=True)
        tkBox.showinfo("Game is finished", "Winner is " + str(sorted_table[0][0]))
        self.board.destroy()

def return_board(nick, matrix, table_score, finished=False):
        # we need to send here matrix question from session and table_score
    #matrix_task, matrix_answer = return_question_and_answer()
    board = Board(nick, matrix, table_score, finished)
    board.initialize_board()
    board.set_board_numbers(matrix)
    board.draw_board_numbers()
    board.show_board()
    return board.last_move
