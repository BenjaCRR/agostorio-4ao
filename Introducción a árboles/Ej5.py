# 5) Armá el siguiente árbol binario con la clase Nodo del punto anterior.
#     A
#    B    F
#  C   E   G
# D

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None
        
Raiz = Nodo("A") 

Raiz.left = Nodo("B")
Raiz.right = Nodo("F")

Raiz.left.left = Nodo("C")
Raiz.left.right = Nodo("E")
Raiz.right.left = Nodo("G")

Raiz.left.left.left = Nodo ("D") 