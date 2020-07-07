import tkinter as tk

root = tk.Tk()

def opcoes(root, text, color, linha, coluna):
    op_label = tk.Label(root, text=text ,bg=color)
    op_label.grid(row=linha, column=coluna)


main_title = tk.Label(root, text='Cadastre-se', bg='#fff', font=('Helvetica',12,'bold'))
main_title.grid(row=0, column=0, pady=(0, 20))

# menu principal
opcoes(root, '1 - Cadastrar', '#fff', 1, 0)
opcoes(root, '2 - Ler', '#fff', 2, 0)
opcoes(root, '3 - Sair', '#fff', 3, 0)



root.title('Cadastro de Pessoas')
root.config(bg='#fff', padx=20, pady=20)
root.mainloop()