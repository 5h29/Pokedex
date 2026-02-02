import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")

# Variablepour stocker la selection du bouton radio
selection_var = tk.StringVar()

# Création de boutons radio
bouton_radio1 = tk.Radiobutton(fenetre, text="option 1", variable=selection_var, value="option 1")
bouton_radio1.pack()

bouton_radio2 = tk.Radiobutton(fenetre, text="option 2", variable=selection_var, value="option 2")
bouton_radio2.pack()

fenetre.mainloop()