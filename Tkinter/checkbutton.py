import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")

# Variable pour stocker l'etat de la case à cocher
case_cocher_var = tk.IntVar()

# Création d'une case à cocher
case_cocher = tk.Checkbutton(fenetre, text="Cocher", variable=case_cocher_var)
case_cocher.pack()

fenetre.mainloop()