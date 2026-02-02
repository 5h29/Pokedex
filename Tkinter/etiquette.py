import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")

etiquette = tk.Label(fenetre, text="Bonjour, Tkinter!")
etiquette.pack()

etiquette2 = tk.Label(fenetre, text="Autre texte")
etiquette2.pack()

fenetre.mainloop()