

class Data():
    
    def CargarArchivo(pathCSV):
        archivo=open(pathCSV,"r")
        for linea in archivo.readlines():
            print (linea)

        archivo.close()


    

# Luis Espino 2020

        #Copia de git del ingeniero solo implemente ELIMINAR
        #201800516  - Mynor Saban 

class Node:
    def __init__(self, value):
        self.value  = value
        self.left   = None
        self.right  = None
        self.height = 0   #altura 

class AVLTree:
    def __init__(self):
        self.root = None

    #add
        
    def add(self, value):
        self.root = self._add(value, self.root)
    
    def _add(self, value, tmp):
        if tmp is None: # SI esta vacio la raiz solola devuelve
            return Node(value)        
        elif value>tmp.value:  # es mayor que la raiz
            #ingresa al nodo derecho del padre
            tmp.right=self._add(value, tmp.right)
            #calcula la altura para nivelar
            if (self.height(tmp.right)-self.height(tmp.left))==2: # si es igual a 2 no esta equilibrado
                if value>tmp.right.value:
                    tmp = self.srr(tmp)
                else:
                    tmp = self.drr(tmp)
        else:
            tmp.left=self._add(value, tmp.left)
            if (self.height(tmp.left)-self.height(tmp.right))==2:
                if value<tmp.left.value:
                    tmp = self.srl(tmp)
                else:
                    tmp = self.drl(tmp)
        r = self.height(tmp.right)
        l = self.height(tmp.left)
        m = self.maxi(r, l)
        tmp.height = m+1
        return tmp

    def height(self, tmp):
        if tmp is None:
            return -1
        else:
            return tmp.height
        
    def maxi(self, r, l):
        return (l,r)[r>l]   

    #rotations

    def srl(self, t1):
        t2 = t1.left
        t1.left = t2.right
        t2.right = t1
        t1.height = self.maxi(self.heigh(t1.left), self.height(t1.right))+1
        t2.height = self.maxi(self.heigh(t2.left), t1.height)+1
        return t2

    def srr(self, t1):
        t2 = t1.right
        t1.right = t2.left
        t2.left = t1
        t1.height = self.maxi(self.height(t1.left), self.height(t1.right))+1
        t2.height = self.maxi(self.height(t2.left), t1.height)+1
        return t2
    
    def drl(self, tmp):
        tmp.left = srr(tmp.left)
        return srl(tmp)
    
    def drr(self, tmp):
        tmp.right = srl(tmp.right)
        return srr(tmp)

    #traversals

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, tmp):
        if tmp:
            print(tmp.value,end = ' ')
            self._preorder(tmp.left)            
            self._preorder(tmp.right)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, tmp):
        if tmp:
            self._inorder(tmp.left)
            print(tmp.value,end = ' ')
            self._inorder(tmp.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, tmp):
        if tmp:
            self._postorder(tmp.left)            
            self._postorder(tmp.right)
            print(tmp.value,end = ' ')
           
    def Eliminar(self,value):
        self.root=self._eliminar(value,self.root)
    
    def _eliminar(self,value,nodo):
        if(nodo is None):
            print("arbol vacio")
        elif nodo.value<value:
            nodo.right=self._eliminar(value,nodo.right)
        elif nodo.value>value:
            nodo.left=self._eliminar(value,nodo.left)
        else:
            
            print("\n**al metodo de eliminar\n")
            aux = nodo #copio el nodo para desdenlazar de los otros nodos
            nodo=self.masIzquierda(aux.right)
            nodo.right= self.DeleteNodo(aux.right)
            nodo.left=aux.left

        # calcula la altura para hacer un balanceo
        nodo.height = self.maxi(self.height(nodo.left), self.height(nodo.right))+1
      
        return self.balanceo(nodo)
            


    def masIzquierda(self,x):
        #toma el nodo mas minimo el mas a la izquierda
        if x.left is None:
            return x
        return masIzquierda(x.left)

    def DeleteNodo(self,nodo):
        #desenlaza el nodo de los demas
        if nodo.left is None:
            return nodo.right
        nodo.left=self.DeleteNodo(nodo.left)
        nodo.height = self.maxi(self.height(nodo.left), self.height(nodo.right))+1
        #cuando ya lo desinstalo entonces tiene que balancear otra vez  como se ingreso
        return self.balanceo(nodo)

    def balanceo(self,x):
        #envia el factor para obtener los niveles
        if self.factor(x)>1:
            if self.factor(x.right)<0:
                x.right= self.srr(x.right)
            x=self.srl(x)
        elif self.factor(x)<-1:
            if self.factor(x.left)>0:
                x.left= self.srl(x.left)
            x=self.srr(x)

        return x


    def factor(self,tmp):
        return (self.height(tmp.right)-self.height(tmp.left))
    
    



    def grafo(self):
        if self.root !=None:
            print("digraph G { ")
            print('graph [ordering="out"];\n randkdir=TB;\n')
            
            self._grafo(self.root)
            print("\n}")
            
    

    def _grafo(self,actual):
        if actual:
            self._grafo(actual.left)
            self._grafo( actual.right )
            if actual.left:
                print(str(actual.value)+"->"+str(actual.left.value))
            if actual.right:
                print(str(actual.value)+"->"+str(actual.right.value))
            
    
        



#init
t = AVLTree()

#add
t.add(5)
t.add(10)
t.add(20)
t.add(25)
t.add(30)
t.add(35)
t.add(50)
print(" Grafo sin eliminar")
t.grafo()
#print traversals
#t.preorder()
print("\nimprime en orden ")
t.inorder()
#print()
#t.postorder()
print("\n ELIMINA EL 10 ")
t.Eliminar(50)
print("\nimprime en orden ")
t.inorder()
print("\nGrafo eliminando el 10")
t.grafo()
