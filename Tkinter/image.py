import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")

# Chargement d'une image
image = tk.PhotoImage(file="./img/paul-l'aliène.png")

# Création d'un bouton avec image
bouton = tk.Button(fenetre, image=image)
bouton.pack()

fenetre.mainloop()