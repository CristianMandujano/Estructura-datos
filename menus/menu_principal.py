import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication 

from load.load_dialogo_banco import DialogoBanco
from load.load_dialogo_pila import DialogoPila
from load.load_dialogo_convertidor import DialogoConvertidor  
from estructuras.lineales.stack import Stack
from load.load_dialogo_queue import DialogoQueue

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ventana_principal.ui", self) 
        
        self.pila_global = Stack() 
        
        self.actionpila.triggered.connect(self.abrir_modulo_pila)
        self.actionsalir.triggered.connect(self.close)
        self.actionconvertidor.triggered.connect(self.abrir_modulo_convertidor)
        self.actioncola.triggered.connect(self.abrir_modulo_cola)
        self.actionbanco.triggered.connect(self.abrir_modulo_banco)

    def abrir_modulo_pila(self):
        print("Abriendo Pila...")
        self.ventana_pila = DialogoPila() 
        self.ventana_pila.exec_()
        
    def abrir_modulo_lista(self):
        # El que quedó pendiente de la clase que faltaste, lo dejamos pasar por ahora
        pass 

    def abrir_modulo_convertidor(self):
        print("Abriendo Convertidor Infijo a Posfijo...")
        self.ventana_convertidor = DialogoConvertidor()
        self.ventana_convertidor.exec_()

    def abrir_modulo_cola(self):
       print("Abriendo Cola...")
       ventana_cola = DialogoQueue()
       ventana_cola.exec_()

    def abrir_modulo_banco(self):
        print("Abriendo Banco...")
        ventana_banco = DialogoBanco()
        ventana_banco.exec_()
    
