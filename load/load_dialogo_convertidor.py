from PyQt5.QtWidgets import QDialog
from PyQt5 import uic   

from estructuras.aplicaciones.convertidor import ConvertidorInfixPostFix  

class DialogoConvertidor(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_convertidor.ui", self)
        
        self.convertidor = ConvertidorInfixPostFix()  
        
        # Variable para almacenar la posfija calculada temporalmente
        self.resultado_posfijo_actual = ""
        
        # Conexiones de los botones de la interfaz
        self.btn_convertir.clicked.connect(self.procesar_conversion)
        self.btn_evaluar.clicked.connect(self.procesar_evaluacion) # <- Nueva conexión

    def procesar_conversion(self):
        expresion_infija = self.txt_infija.text()
        
        if not expresion_infija.strip():
            self.lbl_resultado.setText("Ingresa una expresión válida.")
            return
            
        # 1. Convertir y guardar en la variable de la clase
        self.resultado_posfijo_actual = self.convertidor.convertir(expresion_infija)
        
        # 2. Mostrar la cadena posfija en la etiqueta existente
        self.lbl_resultado.setText(self.resultado_posfijo_actual)
        
        # Limpiar la etiqueta de evaluación por si había un cálculo anterior
        self.lbl_evaluacion.setText("Resultado numérico: ...")

    def procesar_evaluacion(self):  # <- Nuevo método
        # Validación por si el usuario presiona "Evaluar" sin haber convertido antes
        if not self.resultado_posfijo_actual:
            self.lbl_evaluacion.setText("Primero debes convertir una expresión.")
            return
            
        # 1. Evaluar usando la cadena posfija guardada
        resultado_numerico = self.convertidor.evaluar_posfija(self.resultado_posfijo_actual)
        
        # 2. Mostrar el valor matemático en la nueva etiqueta
        if resultado_numerico is not None:
            self.lbl_evaluacion.setText(f"Resultado numérico: {resultado_numerico}")
        else:
            self.lbl_evaluacion.setText("Error al evaluar la expresión.")