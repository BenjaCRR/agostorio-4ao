class Nodo:
    def __init__(self, data):
        self.data = data
        self.r_child = None
        self.l_child = None

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
    
    
class node:
    def __init__ (self, data):
        self.data=data
        self.left=None
        self.right=None
class Stack:
    def __init__(self):
        self.elements = []
    def push (self, item):
        self.element.append(item)
    def pop(self):
            return elements.self.pop()
    
def parser (expression):
    class expression_split():
        stack=Stack()
        for char in chars:
            if char in "/,*,+,-":
                node=Nodo(char)
                node.right =stack.pop()
                node.left =stack.pop()
            else: 
                node.push=stack.pop()
                stack.push(node)
        return stack.pop

def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print (node.data)

def calc (node):
    if node.data=="+":
        return calc(node.left) + calc(node.right)
    elif node.data=="-":
        return calc(node.left) - calc(node.right)
    elif node.data=="*":
        return calc(node.left) * calc(node.right)
    elif node.data=="/":
        return calc(node.left)/calc(node.right)
    else:
        return node.data
    