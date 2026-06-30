from PyQt5.QtWidgets import QDialog
from PyQt5 import uic   
from estructuras.lineales.stack import Stack  

class DialogoPila(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_pila.ui", self)
        
        # Creamos la instancia aquí adentro de forma directa
        self.pila = Stack()  
        
        # Conexiones de tus botones
        self.pushButton.clicked.connect(self.agregar_elemento)
        self.popButton.clicked.connect(self.eliminar_elemento)
        self.topButton.clicked.connect(self.mostrar_tope)
        self.printButton.clicked.connect(self.imprimir_pila)

    def agregar_elemento(self):
        dato = self.inputLineEdit.text()
        
        if dato:
            self.pila.push(dato)
            self.inputLineEdit.clear()
            self.actualizar_contenido()

    def eliminar_elemento(self):
        eliminado = self.pila.pop()
        if eliminado:
            self.actualizar_contenido()
        else:
            self.consoleTextEdit.setText("No hay elementos para eliminar. Pila vacía.")

    def mostrar_tope(self):
        tope = self.pila.top_of_stack() 
        if tope is not None:
            self.consoleTextEdit.setText(f"Elemento en la cima: [ {tope} ]")
        else:
            self.consoleTextEdit.setText("La pila está vacía, no hay tope.")

    def imprimir_pila(self):
        self.actualizar_contenido()

    def actualizar_contenido(self):
        self.consoleTextEdit.setText("") 
        
        nodo_actual = self.pila.top
        texto_pila = ""
        
        while nodo_actual is not None:
            texto_pila += f"[{nodo_actual.data}] -> "
            nodo_actual = nodo_actual.next
            
        if texto_pila == "":
            texto_pila = "Pila vacía: [ ]"
        else:
            texto_pila += "None" 
            
        self.consoleTextEdit.setText(texto_pila)