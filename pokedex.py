import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import filedialog

fenetre = tk.Tk()
fenetre.title("Pokédex")
fenetre.geometry("387x310")
fenetre.configure(bg="#FF0000")

class Pokemon:
    def __init__(self, number, name, type, abilities, image_path=None):
        self.number = number
        self.name = name
        self.type = type
        self.abilities = abilities
        self.image_path = image_path

pokemons = [
    Pokemon("1", "Tygnon", "Combat", "Poing-Karaté, Ultimapoing", "img/Tygnon.png"),
    Pokemon("2", "Triopikeur", "Sol", "Tunnel, Séisme", "img/Triopikeur.png"),
    Pokemon("3", "Têtarte", "Eau", "Pistolet à O, Hypnose", "img/Têtarte.png"),
    Pokemon("4", "Tentacruel", "Eau / Poison", "Acide, Hydrocanon", "img/Tentacruel.png"),
    Pokemon("5", "Taupiqueur", "Sol", "Tunnel, Griffe", "img/Taupiqueur.png"),
    Pokemon("6", "Tartard", "Eau / Combat", "Poing-Karaté, Surf", "img/Tartard.png"),
    Pokemon("7", "Stari", "Eau", "Charge, Pistolet à O", "img/Stari.png"),
    Pokemon("8", "Soporifik", "Psy", "Hypnose, Choc Mental", "img/Soporifik.png"),
    Pokemon("9", "Smogogo", "Poison", "Explosion, Gaz Toxik", "img/Smogogo.png"),
    Pokemon("10", "Scarabrute", "Insecte", "Taillade, Force", "img/Scarabrute.png"),
    Pokemon("11", "Saquedeneu", "Plante", "Fouet Lianes, Poudre Dodo", "img/Saquedeneu.png"),
    Pokemon("12", "Sablaireau", "Sol", "Tranche, Tunnel", "img/Sablaireau.png"),
    Pokemon("13", "Roucoups", "Normal / Vol", "Vive-Attaque, Tornade", "img/Roucoups.png"),
    Pokemon("14", "Rattatac", "Normal", "Morsure, Vive-Attaque", "img/Rattatac.png"),
    Pokemon("15", "Rapasdepic", "Normal / Vol", "Furie, Bec Vrille", "img/Rapasdepic.png"),
    Pokemon("16", "Ramoloss", "Eau / Psy", "Pistolet à O, Bâillement", "img/Ramoloss.png"),
    Pokemon("17", "Rafflesia", "Plante / Poison", "Poudre Dodo, Tranch’Herbe", "img/Rafflesia.png"),
    Pokemon("18", "Ptitard", "Eau", "Pistolet à O, Hypnose", "img/Ptitard.png"),
    Pokemon("19", "Ptéra", "Roche / Vol", "Ultralaser, Vol", "img/Ptéra.png"),
    Pokemon("20", "Psykokwak", "Eau", "Choc Mental, Pistolet à O", "img/Psykokwak.png"),
    Pokemon("21", "Porygon", "Normal", "Conversion, Laser Glace", "img/Porygon.png"),
    Pokemon("22", "Ponyta", "Feu", "Flammèche, Charge", "img/Ponyta.png"),
    Pokemon("23", "Poissoroy", "Eau", "Picpic, Surf", "img/Poissoroy.png"),
    Pokemon("24", "Poissirène", "Eau", "Picpic, Pistolet à O", "img/Poissirène.png"),
    Pokemon("25", "Piafabec", "Normal / Vol", "Picpic, Furie", "img/Piafabec.png"),
    Pokemon("26", "Persian", "Normal", "Griffe, Tranche", "img/Persian.png"),
    Pokemon("27", "Parasect", "Insecte / Plante", "Spore, Taillade", "img/Parasect.png"),
    Pokemon("28", "Paras", "Insecte / Plante", "Griffe, Spore", "img/Paras.png"),
    Pokemon("29", "Papilusion", "Insecte / Vol", "Choc Mental, Tornade", "img/Papilusion.png"),
    Pokemon("30", "Otaria", "Eau", "Pistolet à O, Onde Boréale", "img/Otaria.png"),
    Pokemon("31", "Osselait", "Sol", "Massd’Os, Charge", "img/Osselait.png"),
    Pokemon("32", "Ossatueur", "Sol", "Massd’Os, Séisme", "img/Ossatueur.png"),
    Pokemon("33", "Ortide", "Plante / Poison", "Acide, Tranch’Herbe", "img/Ortide.png"),
    Pokemon("34", "Nosferalto", "Poison / Vol", "Ultrason, Morsure", "img/Nosferalto.png"),
    Pokemon("35", "Noeunoeuf", "Plante / Psy", "Hypnose, Canon Graine", "img/Noeunoeuf.png"),
    Pokemon("36", "Noadkoko", "Plante / Psy", "Psyko, Tranch’Herbe", "img/Noadkoko.png"),
    Pokemon("37", "Nidorino", "Poison", "Double Pied, Morsure", "img/Nidorino.png"),
    Pokemon("38", "Nidorina", "Poison", "Griffe, Double Pied", "img/Nidorina.png"),
    Pokemon("39", "Nidoqueen", "Poison / Sol", "Séisme, Empal’Korne", "img/Nidoqueen.png"),
    Pokemon("40", "Mystherbe", "Plante / Poison", "Charge, Fouet Lianes", "img/Mystherbe.png"),
    Pokemon("41", "Minidraco", "Dragon", "Draco-Rage, Enroulement", "img/Minidraco.png"),
    Pokemon("42", "Mimitoss", "Insecte / Poison", "Choc Mental, Poudre Dodo", "img/Mimitoss.png"),
    Pokemon("43", "Miaouss", "Normal", "Griffe, Jackpot", "img/Miaouss.png"),
    Pokemon("44", "Mélofée", "Fée", "Berceuse, Écrasement", "img/Mélofée.png"),
    Pokemon("45", "Mélodelfe", "Fée", "Psyko, Écrasement", "img/Mélodelfe.png"),
    Pokemon("46", "Magnéton", "Électrique / Acier", "Éclair, Sonicboom", "img/Magnéton.png"),
    Pokemon("47", "Magnéti", "Électrique / Acier", "Éclair, Charge", "img/Magnéti.png"),
    Pokemon("48", "Magmar", "Feu", "Lance-Flammes, Poing Feu", "img/Magmar.png"),
    Pokemon("49", "Mackogneur", "Combat", "Dynamopoing, Projection", "img/Mackogneur.png"),
    Pokemon("50", "Machopeur", "Combat", "Poing-Karaté, Projection", "img/Machopeur.png"),
    Pokemon("51", "M. Mime", "Psy / Fée", "Psyko, Mur Lumière", "img/M. Mime.png"),
    Pokemon("52", "Lokhlass", "Eau / Glace", "Laser Glace, Surf", "img/Lokhlass.png"),
    Pokemon("53", "Lippoutou", "Glace / Psy", "Choc Mental, Poing Glace", "img/Lippoutou.png"),
    Pokemon("54", "Leveinard", "Normal", "Écrasement, Soin", "img/Leveinard.png"),
    Pokemon("55", "Lamantine", "Eau / Glace", "Laser Glace, Surf", "img/Lamantine.png"),
    Pokemon("56", "Krabby", "Eau", "Écrasement, Pince-Masse", "img/Krabby.png"),
    Pokemon("57", "Krabboss", "Eau", "Guillotine, Pince-Masse", "img/Krabboss.png"),
    Pokemon("58", "Kokiyas", "Eau", "Pistolet à O, Repli", "img/Kokiyas.png"),
    Pokemon("59", "Kicklee", "Combat", "Pied Sauté, Ultimawashi", "img/Kicklee.png"),
    Pokemon("60", "Kangourex", "Normal", "Poing Comète, Écrasement", "img/Kangourex.png"),
    Pokemon("61", "Kadabra", "Psy", "Psyko, Choc Mental", "img/Kadabra.png"),
    Pokemon("62", "Kabutops", "Roche / Eau", "Tranche, Hydrocanon", "img/Kabutops.png"),
    Pokemon("63", "Kabuto", "Roche / Eau", "Griffe, Pistolet à O", "img/Kabuto.png"),
    Pokemon("64", "Insécateur", "Insecte / Vol", "Taillade, Vive-Attaque", "img/Insécateur.png"),
    Pokemon("65", "Hypotrempe", "Eau", "Pistolet à O, Charge", "img/Hypotrempe.png"),
    Pokemon("66", "Hypocéan", "Eau", "Surf, Laser Glace", "img/Hypocéan.png"),
    Pokemon("67", "Herbizarre", "Plante / Poison", "Fouet Lianes, Tranch’Herbe", "img/Herbizarre.png"),
    Pokemon("68", "Grotadmorv", "Poison", "Détritus, Gaz Toxik", "img/Grotadmorv.png"),
    Pokemon("69", "Grolem", "Roche / Sol", "Séisme, Explosion", "img/Grolem.png"),
    Pokemon("70", "Grodoudou", "Normal / Fée", "Berceuse, Plaquage", "img/Grodoudou.png"),
    Pokemon("71", "Gravalanch", "Roche / Sol", "Jet-Pierres, Explosion", "img/Gravalanch.png"),
    Pokemon("72", "Galopa", "Feu", "Nitrocharge, Lance-Flammes", "img/Galopa.png"),
    Pokemon("73", "Flagadoss", "Eau / Psy", "Surf, Psyko", "img/Flagadoss.png"),
    Pokemon("74", "Feunard", "Feu", "Lance-Flammes, Onde Folie", "img/Feunard.png"),
    Pokemon("75", "Férosinge", "Combat", "Poing-Karaté, Colère", "img/Férosinge.png"),
    Pokemon("76", "Fantominus", "Spectre / Poison", "Léchouille, Hypnose", "img/Fantominus.png"),
    Pokemon("77", "Excelangue", "Normal", "Léchouille, Écrasement", "img/Excelangue.png"),
    Pokemon("78", "Empiflor", "Plante / Poison", "Tranch’Herbe, Acide", "img/Empiflor.png"),
    Pokemon("79", "Élektek", "Électrique", "Poing Éclair, Éclair", "img/Élektek.png"),
    Pokemon("80", "Électrode", "Électrique", "Explosion, Étincelle", "img/Électrode.png"),
    Pokemon("81", "Ectoplasma", "Spectre / Poison", "Ball’Ombre, Hypnose", "img/Ectoplasma.png"),
    Pokemon("82", "Dracolosse", "Dragon / Vol", "Ultralaser, Draco-Rage", "img/Dracolosse.png"),
    Pokemon("83", "Draco", "Dragon", "Draco-Rage, Enroulement", "img/Draco.png"),
    Pokemon("84", "Doduo", "Normal / Vol", "Furie, Picpic", "img/Doduo.png"),
    Pokemon("85", "Dodrio", "Normal / Vol", "Furie, Picpic", "img/Dodrio.png"),
    Pokemon("86", "Dardargnan", "Insecte / Poison", "Dard-Nuée, Taillade", "img/Dardargnan.png"),
    Pokemon("87", "Crustabri", "Eau / Glace", "Laser Glace, Hydrocanon", "img/Crustabri.png"),
    Pokemon("88", "Colossinge", "Combat", "Poing-Karaté, Colère", "img/Colossinge.png"),
    Pokemon("89", "Coconfort", "Insecte / Poison", "Armure, Charge", "img/Coconfort.png"),
    Pokemon("90", "Chrysacier", "Insecte", "Armure, Charge", "img/Chrysacier.png"),
    Pokemon("91", "Chétiflor", "Plante / Poison", "Fouet Lianes, Acide", "img/Chétiflor.png"),
    Pokemon("92", "Chenipan", "Insecte", "Charge, Sécrétion", "img/Chenipan.png"),
    Pokemon("93", "Canarticho", "Normal / Vol", "Tranche, Picpic", "img/Canarticho.png"),
    Pokemon("94", "Boustiflor", "Plante / Poison", "Acide, Tranch’Herbe", "img/Boustiflor.png"),
    Pokemon("95", "Aspicot", "Insecte / Poison", "Dard-Venin, Sécrétion", "img/Aspicot.png"),
    Pokemon("96", "Arbok", "Poison", "Morsure, Intimidation", "img/Arbok.png"),
    Pokemon("97", "Amonita", "Roche / Eau", "Pistolet à O, Repli", "img/Amonita.png"),
    Pokemon("99", "Amonistar", "Roche / Eau", "Hydrocanon, Laser Glace", "img/Amonistar.png"),
    Pokemon("100", "Alakazam", "Psy", "Psyko, Choc Mental", "img/Alakazam.png"),
    Pokemon("101", "Akwakwak", "Eau", "Pistolet à O, Choc Mental", "img/Akwakwak.png"),
    Pokemon("102", "Aéromite", "Insecte / Poison", "Tornade, Choc Mental", "img/Aéromite.png")
]

def update_list():
    listbox.delete(0, tk.END)
    for p in pokemons:
        listbox.insert(tk.END, p.name)

def show_details(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        p = pokemons[index]
        details_label.config(text=f"Nombre : {p.number}\nNom : {p.name}\nType : {p.type}\nCapacités : {p.abilities}")

        if p.image_path:
            try:
                img = Image.open(p.image_path)
                img = img.resize((120, 120))
                photo = ImageTk.PhotoImage(img)
                image_label.config(image=photo)
                image_label.image = photo
            except:
                image_label.config(image="", text="Image non trouvée")
        else:
            image_label.config(image="", text="Pas d'image")

def add_pokemon():
    number = entry_number.get()
    name = entry_name.get()
    type = entry_type.get()
    abilities = entry_abilities.get()
    image_path = entry_image.get()

    if name == "":
        messagebox.showwarning("Le nom est obligatoire !")
        return
    if number == "":
        number = "0"
    if type == "":
        type = "Aucun type"
    if abilities == "":
        abilities = "Aucune capacité"

    pokemons.append(Pokemon(number, name, type, abilities, image_path))
    update_list()
    entry_number.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_abilities.delete(0, tk.END)
    entry_image.delete(0, tk.END)
    entry_type.delete(0, tk.END)

def browse_image():
    chemin = filedialog.askopenfilename(
        filetypes=[("Images", "*.png *.jpg *.jpeg *.gif")]
    )
    if chemin:
        entry_image.delete(0, tk.END)
        entry_image.insert(0, chemin)

tk.Label(fenetre, text="ID :", bg="#FF0000").grid(row=3, column=0, sticky="w")
entry_number = tk.Entry(fenetre)
entry_number.grid(row=3, column=0, padx=70, sticky="w")

tk.Label(fenetre, text="Nom :", bg="#FF0000").grid(row=4, column=0, sticky="w")
entry_name = tk.Entry(fenetre)
entry_name.grid(row=4, column=0, padx=70, sticky="w")

tk.Label(fenetre, text="Type :", bg="#FF0000").grid(row=5, column=0, sticky="w")
entry_type = tk.Entry(fenetre)
entry_type.grid(row=5, column=0, padx=70, sticky="w")

tk.Label(fenetre, text="Capacités :", bg="#FF0000").grid(row=6, column=0, sticky="w")
entry_abilities = tk.Entry(fenetre)
entry_abilities.grid(row=6, column=0, padx=70, sticky="w")

tk.Label(fenetre, text="Image :", bg="#FF0000").grid(row=7, column=0, sticky="w")
entry_image = tk.Entry(fenetre, width=20)
entry_image.grid(row=7, column=0, padx=70, sticky="w")
browse_button = tk.Button(fenetre, text="Parcourir", command=browse_image, bg="#000000", fg="#FFFFFF")
browse_button.grid(row=7, column=1, sticky="w")

add_button = tk.Button(fenetre, text="Ajouter Pokémon", command=add_pokemon, bg="#000000", fg="#FFFFFF")
add_button.grid(row=8, column=0, sticky="w",)

listbox = tk.Listbox(fenetre, width=20, height=11, bg="#FF0000")
listbox.grid(row=0, column=1)
listbox.bind("<<ListboxSelect>>", show_details)

image_label = tk.Label(fenetre, bg="#FF0000")
image_label.grid(row=0, column=0, sticky=tk.N)

details_label = tk.Label(fenetre, text="", justify=tk.LEFT, bg="#FF0000")
details_label.grid(row=0, column=0, sticky=tk.S)

update_list()

fenetre.mainloop()