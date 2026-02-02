import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Pokedex")
fenetre.geometry("1024x500")

etiquette = tk.Label(fenetre, text="Pokedex", font=("Arial", 28))
etiquette.pack()

fenetre.mainloop()