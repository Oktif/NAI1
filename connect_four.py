import numpy as np
import pandas as pd
from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax




class connectFour(TwoPlayerGame):

    def __init__(self, players=None):
        self.players = players
        self.width = 7
        self.height = 6
        self.board = [['.' for i in range(self.width)] for j in range(self.height)]
        self.current_player = 1
        self.marks = {1: 'X', 2: '0'}
        self.pos_dir = np.array([[[i, 0], [0, 1]] for i in range(6)] +
                                [[[0, i], [1, 0]] for i in range(7)] +
                                [[[i, 0], [1, 1]] for i in range(1, 3)] +
                                [[[0, i], [1, 1]] for i in range(4)] +
                                [[[i, 6], [1, -1]] for i in range(1, 3)] +
                                [[[0, i], [1, -1]] for i in range(3, 7)])

    def possible_moves(self):
        return [i for i in range(7) if self.board[0][i] == '.']

    def make_move(self, move):
        self.applyMove(move)

    def unmake_move(self, move):
        self.revertMove(move)

    def is_over(self):
        return self.win()  # Game stops when someone wins.

    def show(self):
        print(pd.DataFrame(self.board))

    def scoring(self):
        return 100 if self.win() else 0

    def applyMove(self, move):
        col = int(move)
        for row in self.board[::-1]:
            if row[col] == '.':
                row[col] = self.marks.get(self.current_player)
                break
    def revertMove(self, move):
        col = int(move)
        for row in self.board:
            if row[col] != '.':
                row[col] = '.'
                break

    def isWin(self, player):
        for (pos, dir) in self.pos_dir:
            in_a_row_count = 0
            x = pos[1]
            y = pos[0]
            while x in range(0, self.width) and y in range(0, self.height):
                if self.marks.get(player) == self.board[y][x]:
                    in_a_row_count += 1
                    if in_a_row_count >= 4:
                        return True
                else:
                    in_a_row_count = 0
                x += dir[1]
                y += dir[0]
        return False

    def win(self):
        return self.isWin(self.current_player)

    def lose(self):
        # przegrywasz kiedy oponent wygrywa
        return self.isWin(self.opponent_index)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ai_algo = Negamax(6)
    game = connectFour([Human_Player(), AI_Player(ai_algo)])
    game.play()