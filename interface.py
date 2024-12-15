"""
File: inteface.py
Author: Evan
Date: 
Ce fichier contient l'interface utilisateur pour le jeu de morpion avec Tkinter.
"""

import tkinter as tk
from tkinter import messagebox
from game import MorpionGame
import random
import subprocess


class MorpionInterface:
    """
    Classe représentant l'interface utilisateur du jeu de morpion.
    """

    def __init__(self, root, against_bot=False):
        """
        Initialise une nouvelle instance de MorpionInterface.

        :param root: La fenêtre principale de l'application Tkinter.
        :param against_bot: Booléen indiquant si le jeu est contre un bot.
        """
        self.root = root
        self.root.title("Jeu de Morpion")
        self.game = MorpionGame()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.against_bot = against_bot
        self.create_widgets()

        self.menu_button = tk.Button(self.root, text="Menu", font=('normal', 20), command=self.return_to_menu)
        self.menu_button.grid(row=3, column=1, pady=10)

    def return_to_menu(self):
        """
        Retourne au menu principal.
        """
        subprocess.Popen(["python", "main.py"])
        self.root.destroy()
        # Ici, vous pouvez ajouter le code pour afficher le menu principal

    def create_widgets(self):
        """
        Crée les widgets de l'interface utilisateur.
        """
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2,
                                               command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, i, j):
        """
        Gère le clic sur un bouton.

        :param i: L'indice de la ligne du bouton cliqué.
        :param j: L'indice de la colonne du bouton cliqué.
        """
        if self.game.make_move(i, j):
            self.buttons[i][j]["text"] = self.game.current_player
            self.root.update_idletasks()  # Met à jour l'interface pour afficher le dernier coup
            if self.game.check_winner():
                messagebox.showinfo("Félicitations!", f"Le joueur {self.game.current_player} a gagné!")
                self.game.reset_game()
                self.reset_buttons()
            elif self.game.check_draw():
                messagebox.showinfo("Match nul", "Le jeu est un match nul!")
                self.game.reset_game()
                self.reset_buttons()
            else:
                self.game.switch_player()
                if self.against_bot and self.game.current_player == "O":
                    self.bot_move()

    def bot_move(self):
        """
        Effectue un mouvement aléatoire pour le bot.
        """
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.game.board[i][j] == ""]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.game.make_move(i, j)
            self.buttons[i][j]["text"] = self.game.current_player
            self.root.update_idletasks()  # Met à jour l'interface pour afficher le dernier coup
            if self.game.check_winner():
                messagebox.showinfo("Félicitations!", f"Le joueur {self.game.current_player} a gagné!")
                self.game.reset_game()
                self.reset_buttons()
            elif self.game.check_draw():
                messagebox.showinfo("Match nul", "Le jeu est un match nul!")
                self.game.reset_game()
                self.reset_buttons()
            else:
                self.game.switch_player()

    def reset_buttons(self):
        """
        Réinitialise les boutons de l'interface utilisateur.
        """
        for row in self.buttons:
            for button in row:
                button["text"] = ""