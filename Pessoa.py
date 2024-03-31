class Pessoa:
    def __init__(self, cpf, nome, telefone, senha):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.senha = senha
        
    def __str__(self):
        return f"CPF: {self.cpf}, Nome: {self.nome}, Telefone: {self.telefone}, Senha: {self.senha}"