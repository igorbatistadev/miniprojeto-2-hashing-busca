from estruturas.Noh import Noh

class ListaOrdenada:
    def __init__(self): 
        self.head = None
        self.length = 0    
    
    def is_empty(self): 
        return self.head == None
    
    def add(self,item):
        atual = self.head
        anterior = None
        parar = False
        while atual != None and not parar:
            if atual.getData().cpf > item.cpf:
                parar = True
            else:
                anterior = atual
                atual = atual.getNext()
        
        temp = Noh(item)
        if anterior == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(atual)
            anterior.setNext(temp)
        
        self.length += 1
    
    def size(self):
        return self.length
    
    def search(self,item):
        atual = self.head #atual == temp
        encontrou = False
        parar = False
        while atual != None and not encontrou and not parar:
            if atual.getData().cpf == item.cpf:
                encontrou = True
            else:
                if atual.getData().cpf > item.cpf:
                    parar = True
                else:
                    atual = atual.getNext()
        return encontrou
    
    def remove(self,item):
        atual = self.head
        anterior = None
        encontrou = False
        while not encontrou:
            if atual.getData().cpf == item.cpf:
                encontrou = True
            else:
                anterior = atual
                atual = atual.getNext()
        if anterior == None:
            self.head = atual.getNext()
        else:
            anterior.setNext(atual.getNext())
        
        self.length -= 1
        
    def get(self, index):
        if index < 0:
            return None
        
        atual = self.head
        contador = 0
        while atual is not None and contador < index:
            atual = atual.getNext()
            contador += 1
        
        if contador == index and atual is not None:
            return atual.getData()
        else:
            return None
            
    def busca_binaria(self, cpf, inicio, fim):
        if fim < inicio:
            return False
        
        meio = (inicio + fim) // 2
        item_meio = self.get(meio) 
        
        if item_meio is None:
            return False
        
        if item_meio.cpf == cpf:
            return True
        elif item_meio.cpf < cpf:
            return self.busca_binaria(cpf, meio + 1, fim)
        else:
            return self.busca_binaria(cpf, inicio, meio - 1)
        