class Nodo():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

nA = Nodo("A")
nB = Nodo("B")
nC = Nodo("C")
nD = Nodo("D")
nE = Nodo("E")
nF = Nodo("F")
nG = Nodo("G")
nH = Nodo("H")

nA.left_child = nB
nA.right_child = nC
nB.left_child = nD
nB.right_child = nE
nC.right_child = nF
nD.left_child = nG
nD.right_child = nF

def in_order(node):
    actual = node
    if actual is None:
        return
    in_order(actual.left_child)
    print(actual.data)
    in_order(actual.right_child)

def pre_order(node):
    actual = node
    if actual is None:
        return
    print(actual.data)
    pre_order(actual.left_child)
    pre_order(actual.right_child)

def post_order(node):
    actual = node
    if actual is None:
        return
    post_order(actual.left_child)
    post_order(actual.right_child)
    print(actual.data)

from collections import deque

def level_order(nodo):
    if not nodo:
        return

    queue = deque([nodo])

    while queue:
        nodo_actual = queue.popleft()
        print(nodo_actual.data, end=" ")

        if nodo_actual.izq:
            queue.append(nodo_actual.left)

        if nodo_actual.der:
            queue.append(nodo_actual.right)