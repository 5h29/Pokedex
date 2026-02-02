import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")

# Création d'une liste déroulente
listbox = tk.Listbox(fenetre)
listbox.pack()

# Ajout d'elements à la liste déroulente
listbox.insert(tk.END, "Elément 1")
listbox.insert(tk.END, "Elément 2")
listbox.insert(tk.END, "Elément 3")

fenetre.mainloop()