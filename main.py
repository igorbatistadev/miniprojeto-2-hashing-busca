from HashTable import *
from GeradorPessoa import *

if __name__ == '__main__':
    gerador = GeradorPessoa()    
    pessoa = gerador.gerarPessoa()
    print(pessoa)
    print(gerador.gerarPessoa())
    print(gerador.gerarPessoa())
    print(gerador.gerarPessoa())
    print(gerador.gerarPessoa())
    
    
