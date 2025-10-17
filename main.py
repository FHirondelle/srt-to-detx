from br_fonctions import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

dirpath = os.path.abspath(os.getcwd())

root = tk.Tk()
root.title("Convertisseur .srt en .detx")

frame = ttk.Frame(root, width=800, height=500, padding=10)
frame.grid(columnspan=3, rowspan=2)

label = ttk.Label(frame, text="Sélectionnez un fichier .srt à convertir.")

button = ttk.Button(frame, text="Sélectionner", command=lambda: select_file())

label_fini = ttk.Label(frame, text="Conversion terminée")

button_recommencer = ttk.Button(frame, text="Convertir un autre fichier", command=lambda: start())


def start(l=label, b=button, fini=label_fini, recommence=button_recommencer):
    fini.grid_forget()
    recommence.grid_forget()
    l.grid(column=0, row=0)
    b.grid(column=5, row=0)

def select_file(l=label, b=button, fini=label_fini, recommence=button_recommencer):
    srtfile = filedialog.askopenfilename(filetypes=[("fichiers srt", "*.srt")], initialdir=dirpath)
    br_text = traitement(srtfile)
    detx_file = filedialog.asksaveasfilename(filetypes=[("fichiers detx", "*.detx")], defaultextension=".detx", initialdir=dirpath)
    with open(detx_file, 'w') as detx:
        detx.write(br_text)
    l.grid_forget()
    b.grid_forget()
    fini.grid(column=2, row=0)
    recommence.grid(column=2, row=2)


    
start()

root.mainloop()