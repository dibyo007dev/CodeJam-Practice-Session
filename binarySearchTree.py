class Node:
    def __init__(self,val):
        self.lchild = None
        self.rchild = None
        self.data = val

def binary_insert(root,node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.lchild is None:
                root.lchild = node
            else:
                binary_insert(root.lchild, node)
        else:
            if root.rchild is None:
                root.rchild = node
            else:
                binary_insert(root.rchild,node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.lchild)
    print (root.data)
    in_order_print(root.rchild)

def pre_order_print(root):
    if not root:
        return
    print (root.data)
    pre_order_print(root.lchild)
    pre_order_print(root.rchild)


r = Node(3)
binary_insert(r, Node(7))
binary_insert(r, Node(4))
binary_insert(r, Node(10))

print("in order:")
in_order_print(r)

print("pre order")
pre_order_print(r)