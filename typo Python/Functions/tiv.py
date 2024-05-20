import tkinter as tk
import tkinter.messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.board = [' ']*9
        self.current_player = 'X'

        # Create buttons
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.window, text=' ', command=lambda i=i: self.make_move(i), font=('Arial', 24), width=5, height=2)
            self.buttons.append(button)
            button.grid(row=i//3, column=i%3)

    def make_move(self, square):
        if self.board[square] == ' ':
            self.board[square] = self.current_player
            self.buttons[square]['text'] = self.current_player
            if self.check_win():
                tkinter.messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.window.quit()
            elif ' ' not in self.board:
                tkinter.messagebox.showinfo("Game Over", "The game is a draw!")
                self.window.quit()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False

if __name__ == "__main__":
    game = TicTacToe()
    game.window.mainloop()
