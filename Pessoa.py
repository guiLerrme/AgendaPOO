class Pessoa():
    def __init__(self, nome, idade, cpf, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        
    def __str__(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | CPF: {self.cpf} | Telefone: {self.telefone}"
