from estructuras.lineales.nodo import Node

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
      new_node = Node(data)        
      new_node.next = self.top
      self.top = new_node


    def pop(self):
        # Versión Pila Vacía: "si top es none la lista está vacía..."
        if self.top is None:
            print("Error: La lista está vacía y no hay nada que eliminar.")
            return None
            
        # Versión Lista Llena / Con elementos:
        # Crear una variable temp, ahí guardamos el dato del nodo top
        temp = self.top
        
        # quitar referencia del next y hacer que top avance un lugar con top=top.next
        self.top = self.top.next
        
        # Imprimir el valor de temp para mostrar el dato que quedó sin referencia y se eliminará
        print(f"Se eliminó el nodo con el dato: {temp.data}")
        
        # return temp
        return temp


    def top_of_stack(self):
        # Si top = none: la lista está vacía
        if self.top is None:
            print("La lista está vacía.")
            return None
            
        # imprimir la referencia de top ya que siempre apunta al dato que está hasta arriba de la pila
        print(f"El elemento en el Tope es: {self.top.data}")
        return self.top.data


    def print_stack(self):
        # (Validación por si acaso está vacía)
        if self.top is None:
            print("La pila está vacía: [ ]")
            return

        # crear una variable temp para iniciarla en el valor actual
        # así el temp inicia en el primer nodo
        temp = self.top
        
        print("Contenido de la pila:")
        
        # y hacemos que avance al siguiente imprimiendo el dato en cada uno hasta que sea igual a none que es donde termina la pila
        while temp is not None:
            print(f"[{temp.data}]", end=" -> ")
            temp = temp.next # temp = temp.next para avanzar como en tu dibujo
            
        print("None")