from GeradorPessoa import *
from estruturas.HashTable import HashTable
from estruturas.ListaNaoOrdenada import ListaNaoOrdenada
from estruturas.ListaOrdenada import ListaOrdenada
import timeit
import random


gerador = GeradorPessoa()   
qtd_conjunto_1 = 10
qtd_conjunto_2 = 100
qtd_conjunto_3 = 1000

hash_table_tempo_insercao = [None, None, None] 
hash_table_tempo_busca = [None, None, None] 

lista_ordenada_tempo_insercao = [None, None, None] 
lista_ordenada_tempo_busca = [None, None, None] 

lista_nao_ordenada_tempo_insercao = [None, None, None] 
lista_nao_ordenada_tempo_busca = [None, None, None] 

def gerarCpf():
    return f'{random.randint(100000000, 999999999)}'

def gerarPessoa():
    pessoaGerada = gerador.gerarPessoa()
    return pessoaGerada

def gerarInserirPessoasHashTable(hashTable):
    for _ in range(hashTable._tamanho):
        pessoa = gerarPessoa()
        hashTable.put(int(pessoa.cpf), pessoa)
        
def gerarInserirPessoasListaOrdenada(listaOrdenada, qtd_dados):
    for _ in range(qtd_dados):
        pessoa = gerarPessoa()
        listaOrdenada.add(pessoa)
        
def gerarInserirPessoasListaNaoOrdenada(listaNaoOrdenada, qtd_dados):
    for _ in range(qtd_dados):
        pessoa = gerarPessoa()
        listaNaoOrdenada.add(pessoa)

def testeInsercaoHashTableConjunt1():
    gerarInserirPessoasHashTable(hashTable_conjunto_1)

def testeInsercaoHashTableConjunt2():
    gerarInserirPessoasHashTable(hashTable_conjunto_2)

def testeInsercaoHashTableConjunt3():
    gerarInserirPessoasHashTable(hashTable_conjunto_3)

def testeInsercaoListaNaoOrdenadaConjunt1():
    gerarInserirPessoasListaNaoOrdenada(listaOrdenada_conjunto_1, qtd_conjunto_1)
    
def testeInsercaoListaNaoOrdenadaConjunt2():
    gerarInserirPessoasListaNaoOrdenada(listaOrdenada_conjunto_2, qtd_conjunto_2)
    
def testeInsercaoListaNaoOrdenadaConjunt3():
    gerarInserirPessoasListaNaoOrdenada(listaOrdenada_conjunto_3, qtd_conjunto_3)
    
def testeInsercaoListaOrdenadaConjunt1():
    gerarInserirPessoasListaOrdenada(listaNaoOrdenada_conjunto_1, qtd_conjunto_1)
    
def testeInsercaoListaOrdenadaConjunt2():
    gerarInserirPessoasListaOrdenada(listaNaoOrdenada_conjunto_2, qtd_conjunto_2)
    
def testeInsercaoListaOrdenadaConjunt3():
    gerarInserirPessoasListaOrdenada(listaNaoOrdenada_conjunto_3, qtd_conjunto_3)

def buscaSequencialListaNaoOrdenada(lista):
    cpf = f'{random.randint(100000000, 999999999)}'
    lista.search(cpf)
    
def buscaBinariaListaOrdenada(lista, tamanho):
    cpf = f'{random.randint(100000000, 999999999)}'
    lista.busca_binaria(cpf, 0, tamanho - 1)
    
def testeBuscaListaNaoOrdenadaConjunt1():
    buscaSequencialListaNaoOrdenada(listaNaoOrdenada_conjunto_1)
    
def testeBuscaListaNaoOrdenadaConjunt2():
    buscaSequencialListaNaoOrdenada(listaNaoOrdenada_conjunto_2)
    
def testeBuscaListaNaoOrdenadaConjunt3():
    buscaSequencialListaNaoOrdenada(listaNaoOrdenada_conjunto_3)

def testeBuscaListaOrdenadaConjunt1():
    buscaBinariaListaOrdenada(listaOrdenada_conjunto_1, qtd_conjunto_1)
    
def testeBuscaListaOrdenadaConjunt2():
    buscaBinariaListaOrdenada(listaOrdenada_conjunto_2, qtd_conjunto_2)
    
def testeBuscaListaOrdenadaConjunt3():
    buscaBinariaListaOrdenada(listaOrdenada_conjunto_3, qtd_conjunto_3)
    
def testeBuscaHashTableConjunt1():
    cpf = gerarCpf()
    hashTable_conjunto_1.get(int(cpf))
    
def testeBuscaHashTableConjunt2():
    cpf = gerarCpf()
    hashTable_conjunto_2.get(int(cpf))
    
def testeBuscaHashTableConjunt3():
    cpf = gerarCpf()
    hashTable_conjunto_3.get(int(cpf))
    
    
def testeTempoInsercao():
    tempo = timeit.timeit( stmt=testeInsercaoListaOrdenadaConjunt1, number=1)
    print(f'Tempo de duração do testeInsercaoListaOrdenadaConjunt1: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_1}')
    lista_ordenada_tempo_insercao[0] = tempo/qtd_conjunto_1

    tempo = timeit.timeit( stmt=testeInsercaoListaOrdenadaConjunt2, number=1)
    print(f'Tempo de duração do testeInsercaoListaOrdenadaConjunt2: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_2}')
    lista_ordenada_tempo_insercao[1] = tempo/qtd_conjunto_2

    tempo = timeit.timeit( stmt=testeInsercaoListaOrdenadaConjunt3, number=1)
    print(f'Tempo de duração do testeInsercaoListaOrdenadaConjunt3: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_3}')
    lista_ordenada_tempo_insercao[2] = tempo/qtd_conjunto_3

    tempo = timeit.timeit( stmt=testeInsercaoListaNaoOrdenadaConjunt1, number=1)
    print(f'Tempo de duração do testeInsercaoListaNaoOrdenadaConjunt1: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_1}')
    lista_nao_ordenada_tempo_insercao[0] = tempo/qtd_conjunto_1
        
    tempo = timeit.timeit( stmt=testeInsercaoListaNaoOrdenadaConjunt2, number=1)
    print(f'Tempo de duração do testeInsercaoListaNaoOrdenadaConjunt2: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_2}')
    lista_nao_ordenada_tempo_insercao[1] = tempo/qtd_conjunto_2

    tempo = timeit.timeit( stmt=testeInsercaoListaNaoOrdenadaConjunt3, number=1)
    print(f'Tempo de duração do testeInsercaoListaNaoOrdenadaConjunt3: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_3}')
    lista_nao_ordenada_tempo_insercao[2] = tempo/qtd_conjunto_3

    tempo = timeit.timeit( stmt=testeInsercaoHashTableConjunt1, number=1)
    print(f'Tempo de duração do testeInsercaoHashTableConjunt1: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_1}')
    hash_table_tempo_insercao[0] = tempo/qtd_conjunto_1
        
    tempo = timeit.timeit( stmt=testeInsercaoHashTableConjunt2, number=1)
    print(f'Tempo de duração do testeInsercaoHashTableConjunt2: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_2}')
    hash_table_tempo_insercao[1] = tempo/qtd_conjunto_2

    tempo = timeit.timeit( stmt=testeInsercaoHashTableConjunt3, number=1)
    print(f'Tempo de duração do testeInsercaoHashTableConjunt3: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_3}')
    hash_table_tempo_insercao[2] = tempo/qtd_conjunto_3
    
def testeTempoBusca():
    tempo = timeit.timeit( stmt=testeBuscaListaOrdenadaConjunt1, number=1)
    print(f'Tempo de duração do testeBuscaListaOrdenadaConjunt1: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_1}')
    lista_ordenada_tempo_busca[0] = tempo/qtd_conjunto_1

    tempo = timeit.timeit( stmt=testeBuscaListaOrdenadaConjunt2, number=1)
    print(f'Tempo de duração do testeBuscaListaOrdenadaConjunt2: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_2}')
    lista_ordenada_tempo_busca[1] = tempo/qtd_conjunto_2

    tempo = timeit.timeit( stmt=testeBuscaListaOrdenadaConjunt3, number=1)
    print(f'Tempo de duração do testeBuscaListaOrdenadaConjunt3: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_3}')
    lista_ordenada_tempo_busca[2] = tempo/qtd_conjunto_3

    tempo = timeit.timeit( stmt=testeBuscaListaNaoOrdenadaConjunt1, number=1)
    print(f'Tempo de duração do testeBuscaListaNaoOrdenadaConjunt1: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_1}')
    lista_nao_ordenada_tempo_busca[0] = tempo/qtd_conjunto_1
        
    tempo = timeit.timeit( stmt=testeBuscaListaNaoOrdenadaConjunt2, number=1)
    print(f'Tempo de duração do testeBuscaListaNaoOrdenadaConjunt2: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_2}')
    lista_nao_ordenada_tempo_busca[1] = tempo/qtd_conjunto_2

    tempo = timeit.timeit( stmt=testeBuscaListaNaoOrdenadaConjunt3, number=1)
    print(f'Tempo de duração do testeBuscaListaNaoOrdenadaConjunt3: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_3}')
    lista_nao_ordenada_tempo_busca[2] = tempo/qtd_conjunto_3
    
    tempo = timeit.timeit( stmt=testeBuscaHashTableConjunt1, number=1)
    print(f'Tempo de duração do testeBuscaHashTableConjunt1: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_1}')
    hash_table_tempo_busca[0] = tempo/qtd_conjunto_1
    
    tempo = timeit.timeit( stmt=testeBuscaHashTableConjunt2, number=1)
    print(f'Tempo de duração do testeBuscaHashTableConjunt2: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_2}')
    hash_table_tempo_busca[1] = tempo/qtd_conjunto_2
    
    tempo = timeit.timeit( stmt=testeBuscaHashTableConjunt3, number=1)
    print(f'Tempo de duração do testeBuscaHashTableConjunt3: {tempo}')
    print(f'Tempo médio: {tempo/qtd_conjunto_3}')
    hash_table_tempo_busca[2] = tempo/qtd_conjunto_3

if __name__ == '__main__':
    pessoa = gerarPessoa()
    hashTable_conjunto_1 = HashTable(qtd_conjunto_1)
    hashTable_conjunto_2 = HashTable(qtd_conjunto_2)
    hashTable_conjunto_3 = HashTable(qtd_conjunto_3)
    
    listaOrdenada_conjunto_1 = ListaOrdenada()
    listaOrdenada_conjunto_2 = ListaOrdenada()
    listaOrdenada_conjunto_3 = ListaOrdenada()
    
    listaNaoOrdenada_conjunto_1 = ListaNaoOrdenada()
    listaNaoOrdenada_conjunto_2 = ListaNaoOrdenada()
    listaNaoOrdenada_conjunto_3 = ListaNaoOrdenada()
    
    testeTempoInsercao()
    testeTempoBusca()
    
    print('hash_table_tempo_insercao =', hash_table_tempo_insercao)
    print('hash_table_tempo_busca =', hash_table_tempo_busca)
    
    print('lista_ordenada_tempo_insercao =', lista_ordenada_tempo_insercao)
    print('lista_ordenada_tempo_buca =', lista_ordenada_tempo_busca)
    
    print('lista_nao_ordenada_tempo_insercao =', lista_nao_ordenada_tempo_insercao)
    print('lista_nao_ordenada_tempo_busca =', lista_nao_ordenada_tempo_busca)
    

