import os

caminho = r'cadastros'

def cadastro(id, name, year, cpf, school, email, contact):
    with open(os.path.join(caminho, f'{name}.txt'), 'w+') as files:
        files.write(f'Id = {id}\n')
        files.write(f'Nome = {name}\n')
        files.write(f'Idade = {year}\n')
        files.write(f'CPF = {cpf}\n')
        files.write(f'Escolaridade = {school}\n')
        files.write(f'Email = {email}\n')
        files.write(f'Contato = {contact}\n')

def reading(name):
    with open(os.path.join(caminho, f'{name}.txt'), 'r') as files:
        files.seek(0)
        print(files.read())

def filesList():
    for root, diretories, files in os.walk(caminho):
        for item in files:
            print(item)