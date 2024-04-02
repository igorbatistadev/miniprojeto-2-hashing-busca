from estruturas.Noh import Noh

class ListaNaoOrdenada:
    def __init__(self): 
        self.head = None
        
    def is_empty(self): 
        return self.head == None
    
    def add(self,item):
        temp = Noh(item)
        temp.setNext(self.head)
        self.head = temp
    
    def __len__(self):
        return self.size()
    
    def size(self):
        atual = self.head
        contador = 0
        while atual != None:
            contador = contador + 1
            atual = atual.getNext()
        return contador
    
    def search(self,cpf):
        atual = self.head #atual == temp
        encontrou = False
        while atual != None and not encontrou:
            if atual.getData().cpf == cpf:
                encontrou = True
            else:
                atual = atual.getNext()
        return encontrou
    
    def remove(self,cpf):
        atual = self.head
        anterior = None
        encontrou = False
        while not encontrou: #percorre a lista
            if atual.getData().cpf == cpf:
                encontrou = True
            else:
                anterior = atual
                atual = atual.getNext()
        if anterior == None:
            self.head = atual.getNext()
        else:
            anterior.setNext(atual.getNext())