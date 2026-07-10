from PyQt5.QtWidgets import QDialog
from PyQt5 import uic   

from estructuras.lineales.queue import Queue

class DialogoQueue(QDialog):
    def __init__(self):
        super().__init__()
        # 1. Cargar la interfaz gráfica de la cola
        uic.loadUi("ui/dialogo_queue.ui", self)
        
        self.cola = Queue()
        
        self.btn_enqueue.clicked.connect(self.metodo_enqueue)
        self.btn_firsqueue.clicked.connect(self.metodo_first)
        self.btn_lastqueue.clicked.connect(self.metodo_last)
        self.btn_dequeue.clicked.connect(self.metodo_dequeue)
        self.btn_printqueue.clicked.connect(self.metodo_print)

    def metodo_enqueue(self):
        dato = self.txt_dato.text()
        
        if not dato.strip():
            self.lbl_resultado.setText("Por favor, ingresa un dato.")
            return
            
        mensaje = self.cola.enqueue(dato)
        self.lbl_resultado.setText(mensaje)
        
        # Limpiar la caja de texto para el siguiente dato
        self.txt_dato.clear()

    def metodo_dequeue(self):
        # Eliminar el elemento al inicio
        eliminado = self.cola.dequeue()
        self.lbl_resultado.setText(self.cola.resultado)

    def metodo_first(self):
        # Consultar el primero de la fila
        self.cola.firstQueue()
        self.lbl_resultado.setText(self.cola.resultado)

    def metodo_last(self):
        # Consultar el último de la fila
        self.cola.lastQueue()
        self.lbl_resultado.setText(self.cola.resultado)

    def metodo_print(self):
        self.cola.printQueue()
        self.lbl_resultado.setText(f"Cola actual: {self.cola.resultado}")