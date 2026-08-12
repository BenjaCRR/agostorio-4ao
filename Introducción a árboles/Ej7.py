#7) Explicá con tus palabras qué es una expresión aritmética, y utilizá un árbol para representar 
#   la siguiente expresión: [(2 + 6) / 8] * (9 - 2)

# Una función aritmética es un conjunto de números y símbolos que, combinados, resultan en un único valor.


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

Raiz = Nodo("*") 

Raiz.right = Nodo("-")
Raiz.left = Nodo("/")

Raiz.right.left = Nodo(9)
Raiz.right.right = Nodo(2)
Raiz.left.left =Nodo ("+")
Raiz.left.right = Nodo(8)

Raiz.left.left.left.left = Nodo(2)
Raiz.left.left.left.right = Nodo(6)

def calc (Nodo):
    if Nodo.data=="+":
        return calc(Nodo.left) + calc(Nodo.right)
    elif Nodo.data=="-":
        return calc(Nodo.left) - calc(Nodo.right)
    elif Nodo.data=="*":
        return calc(Nodo.left) * calc(Nodo.right)
    elif Nodo.data=="/":
        return calc(Nodo.left)/calc(Nodo.right)
    else:
        return Nodo.data