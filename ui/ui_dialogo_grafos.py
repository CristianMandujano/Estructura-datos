# ui/ui_dialogo_grafos.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox, 
    QLabel, QLineEdit, QPushButton, QComboBox, QTabWidget, 
    QGraphicsView, QTableWidget, QPlainTextEdit
)
from PySide6.QtCore import Qt

class Ui_GraphWidget(object):
    def setupUi(self, GraphWidget):
        GraphWidget.setObjectName("GraphWidget")
        GraphWidget.resize(850, 650)
        
        self.mainLayout = QVBoxLayout(GraphWidget)

        # 1. Título
        self.lblTitle = QLabel("Grafos no dirigidos", GraphWidget)
        font = self.lblTitle.font()
        font.setPointSize(16)
        font.setBold(True)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.lblTitle)

        # Layout superior
        self.controlsLayout = QHBoxLayout()

        # 2. Grupo Vértices
        self.grpVertices = QGroupBox("Vértices", GraphWidget)
        self.gridLayoutVertices = QGridLayout(self.grpVertices)
        
        self.txtVertex = QLineEdit(self.grpVertices)
        self.txtVertex.setPlaceholderText("Nombre del vértice")
        self.btnAddVertex = QPushButton("Agregar vértice", self.grpVertices)
        self.cmbVertex = QComboBox(self.grpVertices)
        self.btnDeleteVertex = QPushButton("Eliminar vértice", self.grpVertices)

        self.gridLayoutVertices.addWidget(self.txtVertex, 0, 0)
        self.gridLayoutVertices.addWidget(self.btnAddVertex, 0, 1)
        self.gridLayoutVertices.addWidget(self.cmbVertex, 1, 0)
        self.gridLayoutVertices.addWidget(self.btnDeleteVertex, 1, 1)
        self.controlsLayout.addWidget(self.grpVertices)

        # 3. Grupo Arcos
        self.grpEdges = QGroupBox("Arcos", GraphWidget)
        self.gridLayoutEdges = QGridLayout(self.grpEdges)
        
        self.lblOrigin = QLabel("Vértice 1", self.grpEdges)
        self.lblDestination = QLabel("Vértice 2", self.grpEdges)
        self.cmbOrigin = QComboBox(self.grpEdges)
        self.cmbDestination = QComboBox(self.grpEdges)
        self.btnAddEdge = QPushButton("Agregar arco", self.grpEdges)
        self.btnDeleteEdge = QPushButton("Eliminar arco", self.grpEdges)

        self.gridLayoutEdges.addWidget(self.lblOrigin, 0, 0)
        self.gridLayoutEdges.addWidget(self.cmbOrigin, 0, 1)
        self.gridLayoutEdges.addWidget(self.btnAddEdge, 0, 2)
        self.gridLayoutEdges.addWidget(self.lblDestination, 1, 0)
        self.gridLayoutEdges.addWidget(self.cmbDestination, 1, 1)
        self.gridLayoutEdges.addWidget(self.btnDeleteEdge, 1, 2)
        self.controlsLayout.addWidget(self.grpEdges)

        self.mainLayout.addLayout(self.controlsLayout)

        # 4. Pestañas de Representaciones
        self.tabWidget = QTabWidget(GraphWidget)
        
        # Pestaña 1: Visual
        self.tabVisual = QWidget()
        self.layoutTab1 = QVBoxLayout(self.tabVisual)
        self.graphicsViewGraph = QGraphicsView(self.tabVisual)
        self.btnRedrawGraph = QPushButton("Redibujar grafo", self.tabVisual)
        self.layoutTab1.addWidget(self.graphicsViewGraph)
        self.layoutTab1.addWidget(self.btnRedrawGraph)
        self.tabWidget.addTab(self.tabVisual, "Representación visual")

        # Pestaña 2: Matriz
        self.tabMatrix = QWidget()
        self.layoutTab2 = QVBoxLayout(self.tabMatrix)
        self.tblAdjacencyMatrix = QTableWidget(self.tabMatrix)
        self.layoutTab2.addWidget(self.tblAdjacencyMatrix)
        self.tabWidget.addTab(self.tabMatrix, "Matriz de adyacencia")

        # Pestaña 3: Lista Adyacencia
        self.tabList = QWidget()
        self.layoutTab3 = QVBoxLayout(self.tabList)
        self.txtAdjacencyList = QPlainTextEdit(self.tabList)
        self.txtAdjacencyList.setReadOnly(True)
        self.layoutTab3.addWidget(self.txtAdjacencyList)
        self.tabWidget.addTab(self.tabList, "Lista de adyacencia")

        # Pestaña 4: Lista Arcos
        self.tabEdges = QWidget()
        self.layoutTab4 = QVBoxLayout(self.tabEdges)
        self.tblEdges = QTableWidget(self.tabEdges)
        self.layoutTab4.addWidget(self.tblEdges)
        self.tabWidget.addTab(self.tabEdges, "Lista de arcos")

        main_layout_add = self.mainLayout.addWidget(self.tabWidget)

        # 5. Pie de página
        self.footerLayout = QHBoxLayout()
        self.lblGraphStatus = QLabel("Vértices: 0 | Arcos: 0", GraphWidget)
        self.btnClearGraph = QPushButton("Limpiar grafo", GraphWidget)

        self.footerLayout.addWidget(self.lblGraphStatus)
        self.footerLayout.addStretch()  
        self.footerLayout.addWidget(self.btnClearGraph)

        self.mainLayout.addLayout(self.footerLayout)