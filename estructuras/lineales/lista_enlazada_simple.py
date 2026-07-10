from estructuras.lineales.nodo import Node

class Linkedlist(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        #Paso 1: Crear un nuevo nodo con el dato proporcionado
        new_node = Node(data)

        #paso 2: Verificar si la lista está vacía
        if self.head is None and self.tail is None:
        #Paso 3: Si la lista está vacía, el nuevo nodo se convierte en la cabeza y la cola de la lista
            self.head = new_node
            self.tail = new_node
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
    def insert_at_end(self, data):
            new_node = Node(data)
            if self.head:
                self.tail.next = new_node
                self.tail = new_node
            else:
                self.head = new_node
                self.tail = new_node

    def search(self, data):
            #Paso 1: Comenzar desde la cabeza de la lista
            temp= self.head
            #Paso 2: Recorrer la lista mientras el nodo actual no sea nulo
            while temp:
                #Paso 3: Comparar el dato del nodo actual con el dato buscado
                if temp.data == data:
                    #Paso 4: Si se encuentra el dato, retornar True
                    return True
                else:
                    #Paso 5: Si no se encuentra el dato, avanzar al siguiente nodo
                    temp = temp.next
            #Paso 6: Si se recorre toda la lista y no se encuentra el dato, retornar False
            return False

    def delete_at_beginning(self):
          if self.head is None:
            print("La lista está vacía. No se puede eliminar ningún nodo.")
            return
          else:
            temp = self.head
            self.head = self.head.next
            
          if self.head is None:
                self.tail = None
                
          del temp

    def delete_at_end(self):
        if self.head is None:
            print("La lista está vacía. No se puede eliminar ningún nodo.")
            return
        elif self.head == self.tail:
            # Si la lista tiene solo un nodo, eliminarlo y actualizar la cabeza y la cola a None
            temp = self.head
            self.head = None
            self.tail = None
            del temp
        else:
            # Paso 1: Recorrer la lista hasta llegar al penúltimo nodo
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            # Paso 2: Guardar el nodo actual de la cola en una variable temporal
            last_node = self.tail
            # Paso 3: Actualizar la cola de la lista para que apunte al penúltimo nodo
            self.tail = temp
            # Paso 4: Establecer el siguiente del nuevo último nodo a None
            self.tail.next = None
            # Paso 5: Eliminar el nodo temporal para liberar memoria
            del last_node
            