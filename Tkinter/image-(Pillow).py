import tkinter as tk
from PIL import ImageTk, Image

fenetre = tk.Tk()
fenetre.title("Ma première fenetre Tkinter")
fenetre.geometry("1024x500")

# Chargement de l'image
image = ImageTk.PhotoImage(Image.open("./img/paul-l'aliène.png"))

# Création d'un widget Label pour afficher l'image
label_image = tk.Label(fenetre, image=image)
label_image.pack()

fenetre.mainloop()