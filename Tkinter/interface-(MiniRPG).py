import tkinter as tk
from tkinter import messagebox

class joueur:
    def __init__(self, nom, vie, attaque):
        self.nom = nom
        self.vie = vie
        self.attaque = attaque

    def attaquer(self, ennemi):
        ennemi.vie -= self.attaque
        
class ennemi:
    def __init__(self, nom, vie, attaque):
        self.nom = nom
        self.vie = vie
        self.attaque = attaque

    def attaquer(self, joueur):
        joueur.vie -= self.attaque

fenetre = tk.Tk()
fenetre.title("Mini RPG/Visual Nouvel")

joueur = joueur("Héro", 100,30)
ennemi = ennemi("Grinch", 50, 5)

def attaquer_joueur():
    joueur.attaquer(ennemi)
    label_ennemi.config(text=f"Ennemi : {ennemi.nom} | Vie : {str(ennemi.vie)}")
    if ennemi.vie <= 0:
        messagebox.showinfo("Victoire", "Vous avez vaicu le monstre !")
        fenetre.quit()
    else:
        ennemi.attaquer(joueur)
        label_joueur.config(text=f"Joueur : {joueur.nom} | Vie : {str(joueur.vie)}")
        if joueur.vie<= 0:
            messagebox.showinfo("Défait", "Le monstre vous a vaincu !")
            fenetre.quit()

label_joueur = tk.Label(fenetre, text=f"Joueur : {joueur.nom} | Vie : {str(joueur.vie)}")
label_joueur.pack()

label_ennemi = tk.Label(fenetre, text=f"Ennemi : {ennemi.nom} | Vie : {str(ennemi.vie)}")
label_ennemi.pack()

bouton_attaquer = tk.Button(fenetre, text="attaquer", command=attaquer_joueur)
bouton_attaquer.pack()

fenetre.mainloop()