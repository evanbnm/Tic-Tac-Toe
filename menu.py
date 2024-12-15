"""
File: menu.py
Author: Evan
Date: 
Ce fichier contient le menu principal pour choisir le mode de jeu.
"""

import tkinter as tk
from interface import MorpionInterface

class Menu:
    """
    Classe représentant le menu principal du jeu de morpion.
    """

    def __init__(self, root):
        """
        Initialise une nouvelle instance de Menu.

        :param root: La fenêtre principale de l'application Tkinter.
        """
        self.root = root
        self.root.title("Menu Principal")
        self.create_widgets()

    def create_widgets(self):
        """
        Crée les widgets du menu principal.
        """
        tk.Label(self.root, text="Choisissez le mode de jeu", font=('normal', 20)).pack(pady=20)
        tk.Button(self.root, text="Jouer contre un autre joueur", font=('normal', 15), command=self.play_against_player).pack(pady=10)
        tk.Button(self.root, text="Jouer contre un bot", font=('normal', 15), command=self.play_against_bot).pack(pady=10)

    def play_against_player(self):
        """
        Lance le jeu contre un autre joueur.
        """
        self.root.destroy()
        root = tk.Tk()
        game_interface = MorpionInterface(root)
        root.mainloop()

    def play_against_bot(self):
        """
        Lance le jeu contre un bot.
        """
        self.root.destroy()
        root = tk.Tk()
        game_interface = MorpionInterface(root, against_bot=True)
        root.mainloop()