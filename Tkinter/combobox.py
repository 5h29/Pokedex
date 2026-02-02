import tkinter as tk
from tkinter import ttk

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")

# Création d'une combobox
combobox = ttk.Combobox(fenetre)
combobox.pack()

# Ajout d'éléments à la combobox
combobox['values'] = ('Option 1', 'Option 2', 'Option3')

fenetre.mainloop()