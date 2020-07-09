import tkinter as tk

def datesfile(StringVar: tk.StringVar, button: tk.Button):
    pass

def ler():
    root = tk.Tk()
    
    entry_stringVar = tk.StringVar()
    entry = tk.Entry(root, bd=3, textvariable=entry_stringVar)
    entry.grid(row=0, column=0)

    button = tk.Button(root, text='Confirmar')
    button.grid(row=0, column=1)
    button.config(command=lambda: datesfile(entry_stringVar, button))

    root.title('Lista de Cadastros')
    root.mainloop()