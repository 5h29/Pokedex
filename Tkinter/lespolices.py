import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")

# Création d'une etiquette avec une police personnalisée
etiquette = tk.Label(fenetre, text="Bonjour, Tkinter!", font=("Arial", 14))
etiquette.pack()

etiquette = tk.Label(fenetre, text="Deuxième texte", font=("Lato", 14))
etiquette.pack()

fenetre.mainloop()