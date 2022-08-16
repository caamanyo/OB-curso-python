import tkinter as tk

win = tk.Tk()

win.geometry("300x200")

label1 = tk.Label(win, text="¿Cuál es tu fruta favorita?")
label1.pack(fill='x')

lista = ['manzanas', 'peras', 'platanos', 'kiwis']

l = tk.StringVar(value=lista)

dropbox = tk.Listbox(win, listvariable=l, height=len(lista)).pack()

win.mainloop()