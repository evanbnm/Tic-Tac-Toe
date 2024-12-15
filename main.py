# -*- coding: utf-8 -*-
"""
File: main.py
Author: Evan
Date: 
Ce fichier contient le code principal pour lancer le jeu de morpion.
"""

import tkinter as tk
from menu import Menu

def main():
    """
    Fonction principale pour lancer le menu du jeu de morpion.
    """
    root = tk.Tk()
    menu = Menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()