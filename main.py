from classes import People
from banco import reading, filesList
from random import randint
from utils.utils import cpfValidation, emailValidation, phoneValidation

while True:
    print(' ==== CADASTROS DE PESSOAS ====')
    print("""
    1 - cadastrar
    2 - Ler
    3 - Sair
    """)
    op = int(input('Digite sua escolha: '))
    print('===============================')
    if op == 1:
        id = randint(10000, 99999)
        name = str(input('Digite seu nome: ')).strip().upper()
        year = int(input('Digite sua idade: '))
        while True:
            cpf = str(input('Digite seu CPF: '))
            if cpfValidation(cpf):
                print('CPF Válido!')
                break
            else:
                print('CPF Inválido, digite novamente!')
        school = str(input('Digite sua escolaridade: ')).strip().upper()
        while True:
            email = str(input('Digite seu email: ')).strip().upper()
            if emailValidation(email):
                print('Email Válido!')
                break
            else:
                print('Email Inválido, digite novamente!')
        while True:
            phone = str(input(r'Digite seu numero de telefone/celular: '))
            if phoneValidation(phone):
                print('Phone Válido!')
                break
            else:
                print('Phone Inválido, digite novamente!')
        pessoa = People(id, name, year, cpf, school, email, phone)
        pessoa.cadastrar()
    elif op == 2:
        print('=-'*20)
        print('Lista de todos os arquivos!')
        filesList()
        print('=-'*20)
        read = str(input('deseja ler o cadastro de quem: ')).strip().upper()
        reading(read)
    elif op == 3:
        print('Obrigado pelo seu cadastro!')
        break