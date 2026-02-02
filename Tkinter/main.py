import tkinter as tk
from tkinter import ttk

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")

# Définition de la taille de la fenètre
fenetre.geometry("1024x500") # Largeur: 1024 pixels, Hauteur: 768 pixels

def clic_bouton():
    print("Le bouton a été cliqué!")

# Creation d'un bouton
bouton = tk.Button(fenetre, text="cliquez-moi", command=clic_bouton)
bouton.pack()

etiquette = tk.Label(fenetre, text="Bonjour, Tkinter!")
etiquette.pack()

etiquette2 = tk.Label(fenetre, text="Autre texte")
etiquette2.pack()

# Fonction pour récupérer la valeur du champ de saisie def obtenir_valeur():
def obtenir_valeur():
    valeur = champ_saisie.get()
    print("La valeur saisie est :", valeur)

# Création d'un champ de saisie
champ_saisie = tk.Entry(fenetre)
champ_saisie.pack()

# Création d'un bouton pour récupérer la valeur saisie
bouton = tk.Button(fenetre, text="Obtenir la valeur", command=obtenir_valeur)
bouton.pack()

# Création d'une liste déroulente
listbox = tk.Listbox(fenetre)
listbox.pack()

# Ajout d'elements à la liste déroulente
listbox.insert(tk.END, "Elément 1")
listbox.insert(tk.END, "Elément 2")
listbox.insert(tk.END, "Elément 3")

# Variable pour stocker l'etat de la case à cocher
case_cocher_var = tk.IntVar()

# Création d'une case à cocher
case_cocher = tk.Checkbutton(fenetre, text="Cocher", variable=case_cocher_var)
case_cocher.pack()

# Variablepour stocker la selection du bouton radio
selection_var = tk.StringVar()

# Création de boutons radio
bouton_radio1 = tk.Radiobutton(fenetre, text="option 1", variable=selection_var, value="option 1")
bouton_radio1.pack()

bouton_radio2 = tk.Radiobutton(fenetre, text="option 2", variable=selection_var, value="option 2")
bouton_radio2.pack()

# Création d'une combobox
combobox = ttk.Combobox(fenetre)
combobox.pack()

# Ajout d'éléments à la combobox
combobox['values'] = ('Option 1', 'Option 2', 'Option3')

fenetre.mainloop()