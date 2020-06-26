from banco import cadastro

class People:
    def __init__(self, id, name, year, cpf, school, email, contact):
        self.id = id
        self.name = name
        self.year = year
        self.cpf = cpf
        self.school = school
        self.email = email
        self.contact = contact

    def cadastrar(self):
        cadastro(self.id, self.name, self.year, self.cpf, self.school, self.email, self.contact)

        