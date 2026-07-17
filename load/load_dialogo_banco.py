from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic
from estructuras.aplicaciones.banco import SistemaBanco

class DialogoBanco(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_banco.ui", self)
        
        self.banco = SistemaBanco()
        
        # Conexiones de botones
        self.btn_turno.clicked.connect(self.solicitar_turno)
        self.btn_atender.clicked.connect(self.atender_siguiente)
        self.btn_cerrar.clicked.connect(self.cerrar_puertas)

    def actualizar_lista_ui(self):
        self.list_clientes.clear()
        lista_espera = self.banco.obtener_clientes_espera()
        for item in lista_espera:
            self.list_clientes.addItem(item)

    from PyQt5.QtWidgets import QDialog, QMessageBox  # Importas QMessageBox

# ... en tu método solicitar_turno:
    def solicitar_turno(self):
        exito, msj = self.banco.agregar_cliente()
        
        if exito:
            self.actualizar_lista_ui()
            self.txt_cliente.setText(str(self.banco.contador_turnos + 1))
            self.lbl_estado_banco.setText("")
        else:
            # Lanza una ventana flotante de advertencia
            QMessageBox.warning(self, "Atención", msj)

    def atender_siguiente(self):
        info, msj = self.banco.atender_cliente()
        if info:
            # Mostramos la info del cliente atendido al lado del botón Atender
            self.lbl_ultimo_atendido.setText(
                f"{info['turno']} - {info['hora_salida']} - {info['tiempo_espera']} seg"
            )
            # Actualizamos la lista de la interfaz
            self.actualizar_lista_ui()
            
            if not self.banco.banco_cerrado:
                self.lbl_estado_banco.setText("")
        else:
            # Si intentan atender pero la cola ya está vacía
            self.lbl_estado_banco.setText(msj)

    def cerrar_puertas(self):
        exito, resultado = self.banco.intentar_cerrar_banco()
        
        if not exito:
            # Aún hay clientes en la cola
            self.lbl_estado_banco.setText(resultado)
        else:
            self.lbl_estado_banco.setText("Banco cerrado exitosamente.")
            self.lbl_atendidos.setText(f"Clientes atendidos: {resultado['atendidos']}")
            self.lbl_promedio.setText(f"Tiempo promedio: {resultado['promedio']} seg")