import tkinter as tk
from tkinter import font

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")

# Chargement de la police personnalisée
police_lato = font.Font(family="Lato", size=12, weight="bold")

# Création d'un etiquette  avec la police persnnalisée
etiquette = tk.Label(fenetre, text="Bonjour, Tikinter!", font=police_lato)
etiquette.pack()

fenetre.mainloop()