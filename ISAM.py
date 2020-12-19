class Nodo:
    def __init__(self, valor, lst= None):
        self.valor = valor
        self.lst = lst

class ISAM:
    def __init__(self):
        self.root = []
    
    def insert(self, valor):
        self.root = self.__add(valor, self.root, 0)
    
    def __add(self, valor, pivote, nivel):
        if nivel < 11:
            if len(pivote)<3:
                pivote.append(Nodo(valor,[]))
                return self.sort(pivote)
            else:
                if valor < pivote[0].valor:
                    pivote[0].lst = self.sort(self.__add(valor, pivote[0].lst, nivel + 1))
                elif pivote[0].valor <= valor < pivote[1].valor:
                    pivote[1].lst = self.sort(self.__add(valor, pivote[1].lst, nivel + 1))
                else:
                   pivote[2].lst = self.sort(self.__add(valor, pivote[2].lst,nivel + 1))
                return pivote
        else:
            pivote.append(Nodo(valor, None))
            return pivote
            

    def sort(self, array):
        arreglo = array
        for i in range(len(arreglo)-1,0,-1):
            for j in range(i):
                if arreglo[j].valor > arreglo[j+1].valor:
                    temp = arreglo[j]
                    arreglo[j] = arreglo[j+1]
                    arreglo[j+1] = temp
        return arreglo

    def print(self):
        self.__print(self.root, "raiz")
    
    def __print(self, lst, padre):
        if lst:
            print("Padre:", padre, "hijos", [i.valor for i in lst])
            for i in lst:
                self.__print(i.lst, i.valor)
            


t= ISAM()
t.insert(7)
t.insert(20)
t.insert(30)
t.insert(40)
t.insert(18)
t.insert(14)
t.insert(8)
t.insert(12)
t.insert(35)
t.insert(25)
t.insert(15)
t.insert(6)
t.insert(9)
t.insert(3)
t.insert(2)

t.print()