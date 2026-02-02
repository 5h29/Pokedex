import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")


etiquette1 = tk.Label(fenetre, text="Widget 1")
etiquette2 = tk.Label(fenetre, text="Widget 2")
etiquette3 = tk.Label(fenetre, text="Widget 3")

etiquette1.grid(row=0, column=0)
etiquette2.grid(row=0, column=1)
etiquette3.grid(row=1, column=0, columnspan=2)

fenetre.mainloop()