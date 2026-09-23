import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGroupBox, QFormLayout, QLineEdit, QComboBox, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView, QListWidget, 
    QStatusBar, QLabel, QSplitter
)
from PySide6.QtCore import Qt

class ClinicUIWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Atención Clínica - Módulo de Control de Estructuras")
        self.resize(1150, 720)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # ---------------------------------------------------------
        # BARRA DE MENÚ SUPERIOR
        # ---------------------------------------------------------
        menubar = self.menuBar()
        menu_archivo = menubar.addMenu("Archivo")
        menu_archivo.addAction("Exportar Historial")
        menu_archivo.addAction("Salir")
        menubar.addMenu("Configuración")
        menubar.addMenu("Ayuda")

        # ---------------------------------------------------------
        # PARTE SUPERIOR: 3 COLUMNAS (CAPTURA | LISTA | COLA)
        # ---------------------------------------------------------
        top_splitter = QSplitter(Qt.Orientation.Horizontal)

        # 1. PANEL DE CAPTURA
        grp_captura = QGroupBox("1. REGISTRO DE PACIENTE")
        layout_captura = QVBoxLayout(grp_captura)

        form_layout = QFormLayout()
        self.txt_id = QLineEdit()
        self.txt_id.setPlaceholderText("Ej. PAC-001")
        self.txt_nombre = QLineEdit()
        self.txt_nombre.setPlaceholderText("Ej. Juan Pérez")
        self.cmb_prioridad = QComboBox()
        self.cmb_prioridad.addItems(["🔴 Alta (Urgencia)", "🟡 Media (Especialidad)", "🟢 Baja (General)"])

        form_layout.addRow("Folio / ID:", self.txt_id)
        form_layout.addRow("Nombre:", self.txt_nombre)
        form_layout.addRow("Prioridad:", self.cmb_prioridad)

        layout_captura.addLayout(form_layout)
        layout_captura.addStretch()

        self.btn_registrar = QPushButton("🟢 Registrar y Encolar")
        self.btn_limpiar = QPushButton("🧹 Limpiar Campos")
        layout_captura.addWidget(self.btn_registrar)
        layout_captura.addWidget(self.btn_limpiar)

        # 2. SEGUNDA COLUMNA: LISTA ENLAZADA DE REGISTRADOS
        grp_lista = QGroupBox("2. EXPEDIENTES (Lista Enlazada)")
        layout_lista = QVBoxLayout(grp_lista)

        self.tbl_expedientes = QTableWidget(3, 3)
        self.tbl_expedientes.setHorizontalHeaderLabels(["ID", "Paciente", "Estatus"])
        self.tbl_expedientes.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # Datos de prueba para simular la Lista Enlazada
        self.tbl_expedientes.setItem(0, 0, QTableWidgetItem("PAC-001"))
        self.tbl_expedientes.setItem(0, 1, QTableWidgetItem("Carlos Gómez"))
        self.tbl_expedientes.setItem(0, 2, QTableWidgetItem("En Lista"))

        layout_lista.addWidget(self.tbl_expedientes)

        nav_layout = QHBoxLayout()
        self.btn_ant = QPushButton("◀ Anterior")
        self.btn_sig = QPushButton("Siguiente ▶")
        nav_layout.addWidget(self.btn_ant)
        nav_layout.addWidget(self.btn_sig)
        layout_lista.addLayout(nav_layout)

        # 3. TERCERA COLUMNA: COLA DE PRIORIDAD (TURNOS DE ESPERA)
        grp_cola = QGroupBox("3. SALA DE ESPERA (Cola de Prioridad)")
        layout_cola = QVBoxLayout(grp_cola)

        self.list_cola = QListWidget()
        self.list_cola.addItems([
            "1. [🔴 Alta] PAC-002 - María López (Llegada: 10:00 AM)",
            "2. [🟡 Media] PAC-001 - Carlos Gómez (Llegada: 09:55 AM)",
            "3. [🟢 Baja] PAC-003 - Ana Rodríguez (Llegada: 10:05 AM)"
        ])
        layout_cola.addWidget(self.list_cola)

        self.btn_llamar = QPushButton("⚡ Llamar a Consulta (Desencolar)")
        layout_cola.addWidget(self.btn_llamar)

        # Agregar las 3 columnas al Splitter superior
        top_splitter.addWidget(grp_captura)
        top_splitter.addWidget(grp_lista)
        top_splitter.addWidget(grp_cola)
        top_splitter.setSizes([300, 420, 430])

        # ---------------------------------------------------------
        # PARTE INFERIOR: PILA DE PACIENTES ATENDIDOS
        # ---------------------------------------------------------
        grp_pila = QGroupBox("4. HISTORIAL DE PACIENTES ATENDIDOS (Pila - LIFO)")
        layout_pila = QVBoxLayout(grp_pila)

        self.list_pila = QListWidget()
        self.list_pila.addItems([
            "⬆️ [TOP DE LA PILA] Atendido 10:15 AM | ID: PAC-000 | Paciente: Roberto Díaz | Diagnóstico: Receta entregada",
            "⬇️ [Elemento - 1] Atendido 09:45 AM | ID: PAC-099 | Paciente: Sofia Hernández | Diagnóstico: Chequeo general",
            "⬇️ [Elemento - 2] Atendido 09:30 AM | ID: PAC-098 | Paciente: Pedro Torres | Diagnóstico: Tensión arterial"
        ])
        layout_pila.addWidget(self.list_pila)

        # Splitter Vertical para separar la parte superior de la Pila inferior
        main_splitter = QSplitter(Qt.Orientation.Vertical)
        main_splitter.addWidget(top_splitter)
        main_splitter.addWidget(grp_pila)
        main_splitter.setSizes([460, 200])

        main_layout.addWidget(main_splitter)

        # BARRA DE ESTADO
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Expedientes activos: 3 | Pacientes en espera: 3 | Atendidos en Pila: 3")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClinicUIWindow()
    window.show()
    sys.exit(app.exec())