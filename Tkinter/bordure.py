import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")

# Création d'un cardre avec une bordure personnalisée 
cadre = tk.Frame(fenetre, bd=8, relief="sunken")
cadre.pack()

# Ajout d'un bouton dans le cardre
bouton = tk.Button(cadre, text="Cliquez-moi!")
bouton.pack()

fenetre.mainloop()