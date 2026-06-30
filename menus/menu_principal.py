import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication 

# 1. IMPORTAMOS tu nuevo diálogo desde la carpeta load
from load.load_dialogo_pila import DialogoPila
from load.load_dialogo_convertidor import DialogoConvertidor  # <-- NUEVA IMPORTACIÓN

from estructuras.lineales.stack import Stack

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_ventana_principal.ui", self) 
        
        self.pila_global = Stack() 
        
        self.actionpila.triggered.connect(self.abrir_modulo_pila)
        self.actionsalir.triggered.connect(self.close)
        self.actionconvertidor.triggered.connect(self.abrir_modulo_convertidor)
        
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
