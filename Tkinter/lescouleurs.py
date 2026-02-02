import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")

# Création d'un bouton avec un couleur de fond personnalisée
bouton = tk.Button(fenetre, text="Cliquez-moi!", bg="#000", fg="Blue")
bouton.pack()

fenetre.mainloop()