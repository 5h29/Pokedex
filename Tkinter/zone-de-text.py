import tkinter as tk

def afficher_texte(event):
    contenu = zone_texte.get("1.0", tk.END)
    print(contenu)

fenetre = tk.Tk()
zone_texte = tk.Text(fenetre)
zone_texte.pack()
zone_texte.bind("<Key>", afficher_texte)
fenetre.mainloop()