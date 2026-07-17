from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5 import uic
from estructuras.aplicaciones.impresion import GestorImpresion

class DialogoImpresion(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_impresion.ui", self)
        
        self.gestor = GestorImpresion()
        
        # Conexión de botones
        self.btn_agregar.clicked.connect(self.agregar_trabajo)
        self.btn_imprimir.clicked.connect(self.procesar_trabajo)
        self.btn_frente.clicked.connect(self.consultar_frente)

    def actualizar_tabla_ui(self):
        # Paso 5: Actualizar la tabla de trabajos pendientes
        lista = self.gestor.obtener_lista_pendientes()
        self.tabla_pendientes.setRowCount(len(lista))
        
        for fila, t in enumerate(lista):
            self.tabla_pendientes.setItem(fila, 0, QTableWidgetItem(str(t.consecutivo)))
            self.tabla_pendientes.setItem(fila, 1, QTableWidgetItem(t.usuario))
            self.tabla_pendientes.setItem(fila, 2, QTableWidgetItem(t.documento))
            self.tabla_pendientes.setItem(fila, 3, QTableWidgetItem(str(t.paginas)))
            
        total = self.gestor.obtener_total_pendientes()
        self.lbl_total_pendientes.setText(f"Total de trabajos pendientes: {total}")

    def agregar_trabajo(self):
        usuario = self.txt_usuario.text()
        documento = self.txt_documento.text()
        paginas = self.txt_paginas.text()

        exito, msj = self.gestor.agregar_trabajo(usuario, documento, paginas)
        self.lbl_mensajes.setText(msj)

        if exito:
            self.txt_usuario.clear()
            self.txt_documento.clear()
            self.txt_paginas.clear()
            self.actualizar_tabla_ui()

    def procesar_trabajo(self):
        # Pasos 6, 7 y 8
        trabajo, msj = self.gestor.procesar_siguiente()
        self.lbl_mensajes.setText(msj)
        self.actualizar_tabla_ui()  # Corrección de llamada

    def consultar_frente(self):
        msj = self.gestor.consultar_frente()
        self.lbl_mensajes.setText(msj)