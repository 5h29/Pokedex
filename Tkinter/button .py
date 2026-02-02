import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")

def clic_bouton():
    print("Le bouton a été cliqué!")

# Creation d'un bouton
bouton = tk.Button(fenetre, text="cliquez-moi", command=clic_bouton)
bouton.pack()

fenetre.mainloop()