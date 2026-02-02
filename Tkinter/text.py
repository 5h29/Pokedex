import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")

# Création d'une zone de texte
zone_text = tk.Text(fenetre)
zone_text.pack()

fenetre.mainloop()