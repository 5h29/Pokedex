import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")

etiquette1 = tk.Label(fenetre, text="Widget 1")
etiquette2 = tk.Label(fenetre, text="Widget 2")
etiquette3 = tk.Label(fenetre, text="Widget 3")

etiquette1.pack()
etiquette2.pack()
etiquette3.pack()

fenetre.mainloop()