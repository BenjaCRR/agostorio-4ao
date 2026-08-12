# 6) Implementá todos los algoritmos de recorrido vistos en clase (in-order, post-order, pre-order,
#    level-order) y utilizalos para recorrer el árbol del punto anterior.


class Nodo:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def in_order(node):
    actual = node
    if actual is None:
        return
    in_order(actual.left)
    print(actual.data, end=" ")
    in_order(actual.right)

def pre_order(node):
    actual = node
    if actual is None:
        return
    print(actual.data, end=" ")
    pre_order(actual.left)
    pre_order(actual.right)

def post_order(node):
    actual = node
    if actual is None:
        return
    post_order(actual.left)
    post_order(actual.right)
    print(actual.data, end=" ")

def level_order(raiz):
    if not raiz:
        return []
    
    resultado = []
    cola = [raiz]
    
    while cola:
        actual = cola.pop(0)
        resultado.append(actual.data)
        
        if actual.left:
            cola.append(actual.left)
        if actual.right:
            cola.append(actual.right)
            
    return resultado

if __name__ == "__main__":
    Raiz = Nodo("A") 

    Raiz.left = Nodo("B")
    Raiz.right = Nodo("F")

    Raiz.left.left = Nodo("C")
    Raiz.left.right = Nodo("E")
    Raiz.right.left = Nodo("G")

    Raiz.left.left.left = Nodo("D") 

    print("In-Order:")
    in_order(Raiz) 
    print("")
    print("Pre-Order:")
    pre_order(Raiz)
    print("")  
    print("Post-Order:")
    post_order(Raiz) 
    print("")
    print("Level-order:")
    print(level_order(Raiz))
