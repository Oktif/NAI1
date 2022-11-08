import math

import numpy as np
import pandas as pd
from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

'''Definicja gry - klasa connectFour dziedziczy po obiekcie TwoPlayerGame z frameworku easyAI
    Po zdefiniowaniu jej zasad temu frameworkowi jesteśmy w stanie uzyskać AI, które posługując się algorytmem Negamax będzie 
    starało się uzyskać jak najlepszy wynik i tym samym ograniczyć zyski przeciwnika.
'''
class connectFour(TwoPlayerGame):

    def __init__(self, players=None):
        '''Inicjalizacja graczy - parametr "players" przyjmujemy podczas wywołania obiektu klasy i oznacza obiekty graczy.
        Możemy tutaj ustawić który gracz jest człowiekiem, a którym steruje ai i jaki jest jego algorytm.'''
        self.players = players
        '''zaczyna gracz nr 1'''
        self.current_player = 1
        '''definiujemy żetony przypisane do graczy'''
        self.marks = {1: 'X', 2: '0'}

        '''Inicjalizacja "planszy" i jej parametrów'''
        self.width = 7
        self.height = 6
        self.board = [['.' for i in range(self.width)] for j in range(self.height)]

        '''Współrzędne pomocnicze dla funkcji iswin oznaczają zakresy, w których sprawdzamy
        czy graczom udało się ułożyć cztery żetony z rzędu.
        Kolejno - pierwsze dwa dla kolumn oraz rzędów, trzeci i czwarty - skos opadajacy (jego koniec jest "niżej" niż początek), czwarty i piąty skos idący ku górze.'''
        self.pos_dir = np.array([[[i, 0], [0, 1]] for i in range(self.height)] +
                                [[[0, i], [1, 0]] for i in range(self.width)] +
                                [[[i, 0], [1, 1]] for i in range(1, math.floor(self.height / 2))] +
                                [[[0, i], [1, 1]] for i in range(math.ceil(self.width / 2))] +
                                [[[i, 6], [1, -1]] for i in range(1, math.floor((self.height / 2)))] +
                                [[[0, i], [1, -1]] for i in range(math.floor((self.height / 2)), self.width)])

    def possible_moves(self):
        '''Zwraca listę możliwych ruchów czyli kolumn, w których aktualnie możemy umieścić nasze "żetony".'''
        return [i for i in range(7) if self.board[0][i] == '.']

    def is_over(self):
        '''Definicja momentu zakończenia gry - gra kończy się, gdy wygrywa gracz lub przeciwnik,
         ale też gdy skończą się dostępne ruchy i gra zostaje nierozstrzygnięta'''
        return self.win() or self.lose() or len(self.possible_moves()) == 0

    def show(self):
        '''Metoda wyświetlająca planszę w konsoli'''
        print(pd.DataFrame(self.board))

    def scoring(self):
        '''Metoda zwracająca AI punktację dla danej sytuacji na planszy'''
        if self.win():
            return 100
        if self.lose():
            return -100
        return 0

    def make_move(self, move):
        '''Metoda wykonująca ruch wybrany przez gracza, używana także przez AI do stosowania kolejnych ruchów.'''
        col = int(move)
        for row in self.board[::-1]:
            if row[col] == '.':
                row[col] = self.marks.get(self.current_player)
                break

    def unmake_move(self, move):
        '''Metoda pomocnicza - wskazuje mechanizm cofnięcia ruchu po jego wykonaniu w ramach algorytmu,
        pozwala przyśpieszyć pracę AI.'''
        col = int(move)
        for row in self.board:
            if row[col] != '.':
                row[col] = '.'
                break

    def isWin(self, player):
        '''Metoda sprawdzająca, czy na planszy znajdują się cztery jednakowe żetony ułożone pod rząd przez aktualnego gracza
        zwraca true jeśli warunek jest spełniony.'''
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
        '''Warunek wygranej - zwraca true jeśli aktualny gracz wygrał'''
        return self.isWin(self.current_player)

    def lose(self):
        '''Definicja przegranej - zwraca true jeśli przeciwnik wygrał.'''
        return self.isWin(self.opponent_index)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''Wybór algorytmu dla gracza ai'''
    ai_algo = Negamax(6)
    '''Ustanowienie obiektu gry, podanie mu graczy w parametrze'''
    game = connectFour([Human_Player(), AI_Player(ai_algo)])
    '''Uruchomienie gry'''
    game.play()
