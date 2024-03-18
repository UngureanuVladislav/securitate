import tkinter as tk
from tkinter import filedialog
import io

# Definirea cheii și a listei de valori asociate
key = "vampir"
key_values = [21, 0, 12, 15, 8, 17]

def criptare_mesaj():
    cheie = key_entry.get().strip()
    mesaj = input_text.get("1.0", tk.END).strip()
    mesaj_criptat = ""
    for i, caracter in enumerate(mesaj):
        if caracter.isalpha():
            if caracter.islower():
                cod_caracter = ord(caracter)
                cod_caracter_criptat = (cod_caracter - ord('a') + ord(cheie[i % len(cheie)])) % 26 + ord('a')
                caracter_criptat = chr(cod_caracter_criptat)
                mesaj_criptat += caracter_criptat
            elif caracter.isupper():
                cod_caracter = ord(caracter)
                cod_caracter_criptat = (cod_caracter - ord('A') + ord(cheie[i % len(cheie)])) % 26 + ord('A')
                caracter_criptat = chr(cod_caracter_criptat)
                mesaj_criptat += caracter_criptat
        elif caracter == " ":
            if use_underscore.get() == 1:
                mesaj_criptat += "_"
            else:
                mesaj_criptat += caracter
        else:
            mesaj_criptat += caracter
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, mesaj_criptat)


def decriptare_mesaj():
    cheie = key_entry.get().strip()
    mesaj_criptat = input_text.get("1.0", tk.END).strip()
    mesaj_decriptat = ""
    for i, caracter in enumerate(mesaj_criptat):
        if caracter.isalpha():
            if caracter.islower():
                cod_caracter_criptat = ord(caracter)
                cod_caracter_decriptat = (cod_caracter_criptat - ord('a') - ord(cheie[i % len(cheie)])) % 26 + ord('a')
                caracter_decriptat = chr(cod_caracter_decriptat)
                mesaj_decriptat += caracter_decriptat
            elif caracter.isupper():
                cod_caracter_criptat = ord(caracter)
                cod_caracter_decriptat = (cod_caracter_criptat - ord('A') - ord(cheie[i % len(cheie)])) % 26 + ord('A')
                caracter_decriptat = chr(cod_caracter_decriptat)
                mesaj_decriptat += caracter_decriptat
        elif caracter == "_":
            if use_underscore.get() == 1:
                mesaj_decriptat += " "
            else:
                mesaj_decriptat += caracter
        else:
            mesaj_decriptat += caracter
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, mesaj_decriptat)

def salveaza_fisier():
    mesaj = output_text.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with io.open(file_path, "w", encoding="utf-8") as file:
            file.write(mesaj)

def deschide_fisier():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with io.open(file_path, "r", encoding="utf-8") as file:
            mesaj = file.read()
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, mesaj)

# Crearea interfeței grafice
root = tk.Tk()
root.title("Criptare și decriptare")
root.geometry("1000x1000")

# Eticheta pentru cheie
key_label = tk.Label(root, text="Introduceți cheia:")
key_label.pack()

# Caseta de text pentru cheie
key_entry = tk.Entry(root)
key_entry.pack()

# Eticheta pentru input
input_label = tk.Label(root, text="Introduceți sau deschideți mesajul:")
input_label.pack()

# Caseta de text pentru input
input_text = tk.Text(root, height=10, width=100)
input_text.pack()

# Buton pentru criptare
criptare_button = tk.Button(root, text="Criptare", command=criptare_mesaj)
criptare_button.pack()

# Buton pentru decriptare
decriptare_button = tk.Button(root, text="Decriptare", command=decriptare_mesaj)
decriptare_button.pack()

# Checkbox pentru folosirea "_" în loc de spațiu
use_underscore = tk.IntVar()
use_underscore_checkbutton = tk.Checkbutton(root, text="Utilizați '_' în loc de spațiu", variable=use_underscore)
use_underscore_checkbutton.pack()

# Eticheta pentru output
output_label = tk.Label(root, text="Rezultat:")
output_label.pack()

# Caseta de text pentru output
output_text = tk.Text(root, height=10, width=100)
output_text.pack()

# Buton pentru salvare
salvare_button = tk.Button(root, text="Salvează fișier", command=salveaza_fisier)
salvare_button.pack()

# Buton pentru deschidere
deschidere_button = tk.Button(root, text="Deschide fișier", command=deschide_fisier)
deschidere_button.pack()

root.mainloop()
