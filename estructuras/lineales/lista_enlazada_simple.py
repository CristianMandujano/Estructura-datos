from estructuras.lineales.nodo import Node

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tile = None

    def insert_at_beginning(self, data):
        #Paso 1: Crear un nuevo nodo con el dato proporcionado
        new_node = Node(data)

        #paso 2: Verificar si la lista está vacía
        if self.head is None and self.tile is None:
        #Paso 3: Si la lista está vacía, el nuevo nodo se convierte en la cabeza y la cola de la lista
            self.head = new_node
            self.tile = new_node
        else:
            #Si la lista no está vacía, el nuevo nodo se convierte en la nueva cabeza de la lista
            new_node.next = self.head
            #Luego, la cabeza de la lista se actualiza para apuntar al nuevo nodo
            self.head = new_node
        def print_linked_list(self):
            temp = self.head
            print("Head -> ", end="")
            while temp is not None:
                print(temp.data, "->", end="")
                temp = temp.next
            print("<- Tail")