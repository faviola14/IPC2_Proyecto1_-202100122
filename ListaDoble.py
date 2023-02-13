from NodoDoble import Node

class DoubleLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.last = self.tail
            
            self.tail.next = new_node
            self.tail = new_node
    
    def print(self):
        if self.head == None:
            return
        datos = self.head
        print(datos.data)
        while datos.next:
            datos= datos.next
            print( datos.data)