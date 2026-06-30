from PyQt5.QtWidgets import QDialog
from PyQt5 import uic   

# Importamos el convertidor que procesa la lógica con la pila
from estructuras.aplicaciones.convertidor import ConvertidorInfixPostFix  

class DialogoConvertidor(QDialog):
    def __init__(self):
        super().__init__()
        # Cargamos tu nueva interfaz desde la carpeta ui
        uic.loadUi("ui/dialogo_convertidor.ui", self)
        
        # Instanciamos la clase del convertidor (POO)
        self.convertidor = ConvertidorInfixPostFix()  
        
        # Conexión del botón único que creaste
        self.btn_convertir.clicked.connect(self.procesar_conversion)

    def procesar_conversion(self):
        # 1. Capturamos la expresión infija de tu QLineEdit
        expresion_infija = self.txt_infija.text()
        
        # Validación por si el usuario le pica al botón sin escribir nada
        if not expresion_infija.strip():
            self.lbl_resultado.setText("Ingresa una expresión válida.")
            return
            
        # 2. Ejecutamos el método de conversión de nuestra clase lógica
        resultado_posfijo = self.convertidor.convertir(expresion_infija)
        
        # 3. Mostramos el resultado en tu QLabel personalizado
        self.lbl_resultado.setText(resultado_posfijo)