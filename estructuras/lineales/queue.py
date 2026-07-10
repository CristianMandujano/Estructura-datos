from estructuras.lineales.lista_enlazada_simple import Linkedlist

class Queue:
    def __init__(self):
        self.lista = Linkedlist()
        self.resultado = ""

    def enqueue(self, data):
        # Insertar al final → comportamiento FIFO
        self.lista.insert_at_end(data)
        self.resultado = f"Elemento {data} agregado a la cola."
        return self.resultado

    def dequeue(self):
        # Eliminar al inicio → comportamiento FIFO
        if self.lista.head is None:
            self.resultado = "La cola está vacía, no se puede eliminar."
            return None
        eliminado = self.lista.head.data
        self.lista.delete_at_beginning() 
        self.resultado = f"Elemento {eliminado} eliminado de la cola."
        return eliminado

    def firstQueue(self):
        if self.lista.head is None:
            self.resultado = "La cola está vacía."
            return None
        self.resultado = f"El primer elemento es: {self.lista.head.data}"
        return self.lista.head.data

    def lastQueue(self):
        if self.lista.head is None:
            self.resultado = "La cola está vacía."
            return None
        temp = self.lista.head
        while temp.next is not None:
            temp = temp.next
        self.resultado = f"El último elemento es: {temp.data}"
        return temp.data

    def printQueue(self):
        if self.lista.head is None:
            self.resultado = "La cola está vacía."
            return self.resultado
        elementos = []
        temp = self.lista.head
        while temp is not None:
            elementos.append(str(temp.data))
            temp = temp.next
        self.resultado = " -> ".join(elementos)
        return self.resultado

    def isEmpty(self):
        return self.lista.head is None