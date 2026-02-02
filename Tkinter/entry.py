import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")

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

fenetre.mainloop()