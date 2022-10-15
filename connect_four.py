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

    def win(self):
        return self.isWon()

    def is_over(self):
        return self.win()  # Game stops when someone wins.

    def show(self):
        print(pd.DataFrame(self.board))

    def scoring(self):
        return 100 if game.win() else 0  # For the AI

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

    def loss_condition(self):
        for pos, direction in self.pos_dir:
            streak = 0
            while (0 <= pos[0] <= 5) and (0 <= pos[1] <= 6):
                if self.board[pos[0]][pos[1]] == self.marks.get(2):
                    streak += 1
                    if streak == 4:
                        return True

                else:
                    streak = 0
                pos = pos + direction
        return False

    def isWon(self):
        for pos, direction in self.pos_dir:
            streak = 0
            while (0 <= pos[0] <= 5) and (0 <= pos[1] <= 6):
                if self.board[pos[0]][pos[1]] == self.marks.get(1):
                    streak += 1
                    if streak == 4:
                        return True

                else:
                    streak = 0
                pos = pos + direction
        return False

    # Obliczanie punktacji
    def scoring(self):
        return -100 if self.loss_condition() else 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('starting in main')
    # Start a match (and store the history of moves when it ends)
    ai1 = Negamax(9)
    game = connectFour([Human_Player(), AI_Player(ai1)])
    # game = connectFour([Human_Player(), AI_Player(ai)])
    history = game.play()
