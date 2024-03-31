from Pessoa import Pessoa
import random
import csv
import string

class GeradorPessoa:
    
    def __init__(self):
        self._lista_nomes = self._extrair_nomes_de_csv('nomes-censos-ibge.csv')
    
    def gerarPessoa(self):
        cpf = self._gerarCPF()
        nome = self._gerarNome()
        telefone = self._gerarTelefone()
        senha = self._gerarSenha()
        return Pessoa(cpf, nome, telefone, senha)
    
    def _gerarCPF(self):
        cpf = [random.randint(0, 9) for x in range(9)]                              
                                                                                
        for _ in range(2):                                                          
            val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11                                                                 
            cpf.append(11 - val if val > 1 else 0)                                  
                                                                                    
        return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)
    
    def _gerarNome(self):
        nome = random.choice(self._lista_nomes)
        return nome
    
    def _gerarTelefone(self):
        ddd = random.randint(11, 99) 
        numero = '9'
        for _ in range(8):  
            numero += str(random.randint(0, 9))
        return f"({ddd}) {numero[:5]}-{numero[5:]}"
    
    def _gerarSenha(self):
        caracteres = string.ascii_letters + string.digits
        senha = ''.join(random.choices(caracteres, k=12))
        return senha
    
    def _extrair_nomes_de_csv(self, nome_arquivo):
        nomes = []
        with open(nome_arquivo, newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            for linha in leitor_csv:
                nomes.append(linha['Nome'])
        return nomes