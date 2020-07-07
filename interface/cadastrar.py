import tkinter as tk


def campo(root, borda, textstringvar, linha, coluna):
    entry = tk.Entry(root, bd=borda, textvariable=textstringvar)
    entry.grid(row=linha, column=coluna)

def texto(root, text, color, linha, coluna):
    text = tk.Label(root, text=text, bg=color)
    text.grid(row=linha, column=coluna)

def create_file(name, year, cpf, school, email, phone):
    pass

def cadastrar():
    root = tk.Tk()

    texto(root, 'Name:','#fff', 1,0)
    name_stringvar = tk.StringVar()
    campo(root, 3, name_stringvar, 1,1)

    texto(root, 'Year:','#fff', 2,0)
    year_stringvar = tk.StringVar()
    campo(root, 3, year_stringvar, 2,1)

    texto(root, 'cpf:','#fff', 3,0)
    cpf_stringvar = tk.StringVar()
    campo(root, 3, cpf_stringvar, 3,1)

    texto(root, 'School:','#fff', 4,0)
    school_stringvar = tk.StringVar()
    campo(root, 3, school_stringvar, 4,1)

    texto(root, 'Email:','#fff', 5,0)
    email_stringvar = tk.StringVar()
    campo(root, 3, email_stringvar, 5,1)

    texto(root, 'Phone:','#fff', 6,0)
    phone_stringvar = tk.StringVar()
    campo(root, 3, phone_stringvar, 6,1)

    button = tk.Button(root, text='Confirmar')
    button.grid(row=7, column=1)
    button.config(command=lambda: create_file(name_stringvar, year_stringvar,cpf_stringvar,school_stringvar, email_stringvar, phone_stringvar))

    root.title('Dados pessoais')
    root.config(bg='#fff', padx=20, pady=20)
    root.mainloop()