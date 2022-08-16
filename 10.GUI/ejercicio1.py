import tkinter as tk

window = tk.Tk()
window.geometry("300x200")


def reset_radio():
    lista_radio[v.get()].deselect()


# window.columnconfigure()

label1 = tk.Label(window, text="Escoge la opción adecuada:")
label1.pack(fill='x')
v = tk.IntVar()

opciones = [('Opción 1.', 0), ('Opción 2.', 1), ('Opción 3.', 2)]

lista_radio = []
for opcion in opciones:
    r = tk.Radiobutton(window, text=opcion[0], variable=v, value=opcion[1])
    r.deselect()
    r.pack(padx=5, pady=5)
    lista_radio.append(r)

button = tk.Button(window, text="Reinicia la lista",
                   command=reset_radio).pack(padx=5, pady=5)

window.mainloop()
