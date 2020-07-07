import tkinter as tk

root = tk.Tk()

def text_menu(root, text, color, linha, coluna):
    op_label = tk.Label(root, text=text ,bg=color)
    op_label.grid(row=linha, column=coluna)

def opcoes(stringvar: tk.StringVar, button: tk.Button):
    pass

main_title = tk.Label(root, text='Cadastre-se', bg='#fff', font=('Helvetica',12,'bold'))
main_title.grid(row=0, column=0, pady=(0, 20))

# menu principal
text_menu(root, '1 - Cadastrar', '#fff', 1, 0)
text_menu(root, '2 - Ler', '#fff', 2, 0)
text_menu(root, '3 - Sair', '#fff', 3, 0)

entry_stringvar = tk.StringVar()
entry = tk.Entry(root, bd=3, textvariable=entry_stringvar)
entry.grid(row=4, column=0)

button = tk.Button(root, text='Confirmar')
button.grid(row=5, column=0)
button.config(command=lambda: opcoes(entry_stringvar, button))

root.title('Cadastro de Pessoas')
root.config(bg='#fff', padx=20, pady=20)
root.mainloop()