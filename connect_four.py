import numpy as np
from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

class GameController(TwoPlayerGame):
    def __init__(self, players, board = None):
#Tworzenie graczy
        self.players = players
#Tworzenie planszy z i kolumnami i j wierszami
        self.board = board if (board != None) else (
            np.array([[0 for i in range (7)] for j in range(6)]))
#Ustawienie kto zacznie grę
        self.nplayer = 1
#Tworzenie pozycji planszy
        self.pos_dir = np.array([[[i, 0], [0, 1]] for i in range(6)] +
                                [[[0, i], [1, 0]] for i in range(7)] +
                                [[[i, 0], [1, 1]] for i in range(1, 3)] +
                                [[[0, i], [1, 1]] for i in range(4)] +
                                [[[i, 6], [1, -1]] for i in range(1, 3)] +
                                [[[0, i], [1, -1]] for i in range(3, 7)])
#Definiowanie możliwych ruchów
    def possible_moves(self):
        return [i for i in range(7) if (self.board[:, i].min() == 0)]
#Kontrolowanie ruchów
    def make_move(self, column):
        line = np.argmin(self.board[:, column] != 0)
        self.board[line, column] = self.nplayer
#Wyświetlanie planszy
    def show(self):
        print('\n' + '\n'.join(
            ['0 1 2 3 4 5 6', 13 * '-'] +
            [' '.join([['.','O','X'][self.board[5 - j][i]]
            for i in range(7)]) for j in range(6)]))
#Sprawdzanie przegranej
    def loss_condition(self):
        for pos, direction in self.pos_dir:
            streak = 0
            while (0 <= pos[0] <= 5) and (0 <= pos[1] <=6):
                if self.board[pos[0], pos[1]] == self.nopponent:
                    streak += 1
                    if streak == 4:
                        return True

                else:
                    streak = 0

                pos = pos + direction

        return False
#Sprawdzanie czy gra skonczona
    def is_over(self):
        return (self.board.min() > 0) or self.loss_condition()
#Obliczanie punktacji
    def scoring(self):
        return -100 if self.loss_condition() else 0
#Funkcja gry
if __name__ == '__main__':
#Algorytmy
    algo_neg = Negamax(5)
    algo_neg_2 = Negamax(14)
#Rozpoczęcie gry
    game = GameController([AI_Player(algo_neg), AI_Player(algo_neg_2)])
    game.play()
#Wyświetlanie wyniku
    if game.loss_condition():
        print('\nPlayer',game.nopponent,'wins')
    else:
        print('\nIts a draw.')


