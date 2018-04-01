class Node:
    def __init__(self,val):
        self.val = val
        self.next = None  # initially pointer used to point nothing

    def traverse(self):
        node = self
        while node!= None:
            print(node.val)
            node = node.next

if __name__ == "__main__":

    node1 = Node(10)
    node2 = Node(99)
    node3 = Node(11)
    node4 = Node(33)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    node1.traverse()