"""
File: main.py
Author: Evan
Date: game.py
Ce fichier contient la logique du jeu de morpion.
"""

class MorpionGame:
    """
    Classe représentant la logique du jeu de morpion.
    """

    def __init__(self):
        """
        Initialise une nouvelle instance de MorpionGame.
        """
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def make_move(self, i, j):
        """
        Effectue un mouvement sur le plateau de jeu.

        :param i: L'indice de la ligne.
        :param j: L'indice de la colonne.
        :return: True si le mouvement est valide, sinon False.
        """
        if self.board[i][j] == "":
            self.board[i][j] = self.current_player
            return True
        return False

    def check_winner(self):
        """
        Vérifie s'il y a un gagnant.

        :return: True si un joueur a gagné, sinon False.
        """
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        """
        Vérifie s'il y a un match nul.

        :return: True si le jeu est un match nul, sinon False.
        """
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def switch_player(self):
        """
        Change le joueur actuel.
        """
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        """
        Réinitialise le jeu.
        """
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"