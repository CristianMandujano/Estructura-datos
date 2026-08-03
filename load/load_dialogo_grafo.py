import math
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QFont, QPainter, QPen
from PySide6.QtWidgets import (
    QAbstractItemView, QGraphicsEllipseItem, QGraphicsLineItem,
    QGraphicsScene, QGraphicsTextItem, QMessageBox, QTableWidgetItem
)
from estructuras.no_lineales.grafos import Graph

class MainController: # O el nombre de tu clase de ventana
    def setup_graph(self):
        """Llamar a esto en el __init__ de tu controlador."""
        self.graph = Graph()
        self.graph_scene = QGraphicsScene(self)
        self.graphicsViewGraph.setScene(self.graph_scene)
        
        self.configure_graph_interface()
        self.configure_graph_events()
        self.update_graph_view()

    def configure_graph_interface(self):
        self.tblAdjacencyMatrix.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblEdges.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.txtAdjacencyList.setReadOnly(True)
        self.tblEdges.setColumnCount(2)
        self.tblEdges.setHorizontalHeaderLabels(["Vértice 1", "Vértice 2"])
        self.graphicsViewGraph.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.graphicsViewGraph.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def configure_graph_events(self):
        self.btnAddVertex.clicked.connect(self.add_vertex)
        self.btnDeleteVertex.clicked.connect(self.delete_vertex)
        self.btnAddEdge.clicked.connect(self.add_edge)
        self.btnDeleteEdge.clicked.connect(self.delete_edge)
        self.btnClearGraph.clicked.connect(self.clear_graph)
        self.btnRedrawGraph.clicked.connect(self.draw_graph)
        self.txtVertex.returnPressed.connect(self.add_vertex)

    def add_vertex(self):
        vertex = self.txtVertex.text()
        try:
            was_added = self.graph.add_vertex(vertex)
            if not was_added:
                QMessageBox.information(self, "Vértice existente", "El vértice ya se encuentra registrado.")
                return
            self.txtVertex.clear()
            self.txtVertex.setFocus()
            self.update_graph_view()
        except ValueError as error:
            QMessageBox.warning(self, "No fue posible agregar el vértice", str(error))

    def delete_vertex(self):
        vertex = self.cmbVertex.currentText()
        if not vertex:
            QMessageBox.warning(self, "Dato requerido", "Seleccione el vértice que desea eliminar.")
            return
        response = QMessageBox.question(
            self, "Confirmar eliminación",
            f"¿Desea eliminar el vértice {vertex}?\n\nTambién se eliminarán todos sus arcos.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if response == QMessageBox.StandardButton.Yes:
            self.graph.remove_vertex(vertex)
            self.update_graph_view()

    def add_edge(self):
        v1 = self.cmbOrigin.currentText()
        v2 = self.cmbDestination.currentText()
        if not v1 or not v2:
            QMessageBox.warning(self, "Datos requeridos", "Seleccione los dos vértices del arco.")
            return
        try:
            was_added = self.graph.add_edge(v1, v2)
            if not was_added:
                QMessageBox.information(self, "Arco existente", f"El arco entre {v1} y {v2} ya existe.")
                return
            self.update_graph_view()
        except ValueError as error:
            QMessageBox.warning(self, "No fue posible agregar el arco", str(error))

    def delete_edge(self):
        v1 = self.cmbOrigin.currentText()
        v2 = self.cmbDestination.currentText()
        if not v1 or not v2:
            QMessageBox.warning(self, "Datos requeridos", "Seleccione los dos vértices del arco.")
            return
        was_removed = self.graph.remove_edge(v1, v2)
        if not was_removed:
            QMessageBox.warning(self, "Arco inexistente", f"No existe un arco entre {v1} y {v2}.")
            return
        self.update_graph_view()

    def update_graph_view(self):
        self.update_vertex_comboboxes()
        self.update_adjacency_matrix()
        self.update_adjacency_list()
        self.update_edge_list()
        self.draw_graph()
        self.update_graph_status()
        self.update_graph_controls()

    def update_vertex_comboboxes(self):
        vertices = self.graph.get_vertices()
        sel_v = self.cmbVertex.currentText()
        sel_v1 = self.cmbOrigin.currentText()
        sel_v2 = self.cmbDestination.currentText()

        self.cmbVertex.clear()
        self.cmbOrigin.clear()
        self.cmbDestination.clear()

        self.cmbVertex.addItems(vertices)
        self.cmbOrigin.addItems(vertices)
        self.cmbDestination.addItems(vertices)

        if sel_v in vertices: self.cmbVertex.setCurrentText(sel_v)
        if sel_v1 in vertices: self.cmbOrigin.setCurrentText(sel_v1)
        if sel_v2 in vertices: self.cmbDestination.setCurrentText(sel_v2)

    def update_adjacency_matrix(self):
        vertices, matrix = self.graph.get_adjacency_matrix()
        size = len(vertices)
        self.tblAdjacencyMatrix.clear()
        self.tblAdjacencyMatrix.setRowCount(size)
        self.tblAdjacencyMatrix.setColumnCount(size)
        self.tblAdjacencyMatrix.setHorizontalHeaderLabels(vertices)
        self.tblAdjacencyMatrix.setVerticalHeaderLabels(vertices)

        for r_idx, row in enumerate(matrix):
            for c_idx, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                item.setTextAlignment(int(Qt.AlignmentFlag.AlignCenter))
                self.tblAdjacencyMatrix.setItem(r_idx, c_idx, item)

        self.tblAdjacencyMatrix.resizeColumnsToContents()
        self.tblAdjacencyMatrix.resizeRowsToContents()

    def update_adjacency_list(self):
        adjacency_list = self.graph.get_adjacency_list()
        lines = [f"{v}: {', '.join(adj) if adj else 'Sin conexiones'}" for v, adj in adjacency_list.items()]
        self.txtAdjacencyList.setPlainText("\n".join(lines))

    def update_edge_list(self):
        edges = self.graph.get_edges()
        self.tblEdges.clearContents()
        self.tblEdges.setRowCount(len(edges))
        self.tblEdges.setColumnCount(2)
        self.tblEdges.setHorizontalHeaderLabels(["Vértice 1", "Vértice 2"])

        for r_idx, (v1, v2) in enumerate(edges):
            i1 = QTableWidgetItem(v1)
            i2 = QTableWidgetItem(v2)
            i1.setTextAlignment(int(Qt.AlignmentFlag.AlignCenter))
            i2.setTextAlignment(int(Qt.AlignmentFlag.AlignCenter))
            self.tblEdges.setItem(r_idx, 0, i1)
            self.tblEdges.setItem(r_idx, 1, i2)

        self.tblEdges.resizeColumnsToContents()
        self.tblEdges.resizeRowsToContents()

    def draw_graph(self):
        self.graph_scene.clear()
        vertices = self.graph.get_vertices()
        edges = self.graph.get_edges()
        w, h = 700, 500
        self.graph_scene.setSceneRect(0, 0, w, h)

        if not vertices:
            txt = QGraphicsTextItem("El grafo no contiene vértices.")
            font = QFont()
            font.setPointSize(14)
            txt.setFont(font)
            txt.setDefaultTextColor(QColor(100, 100, 100))
            rect = txt.boundingRect()
            txt.setPos((w - rect.width()) / 2, (h - rect.height()) / 2)
            self.graph_scene.addItem(txt)
            self.graphicsViewGraph.fitInView(self.graph_scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
            return

        cx, cy = w / 2, h / 2
        v_radius = 25
        layout_radius = min(w, h) / 2 - 70
        v_positions = {}

        if len(vertices) == 1:
            v_positions[vertices[0]] = (cx, cy)
        else:
            step = (2 * math.pi) / len(vertices)
            for i, v in enumerate(vertices):
                angle = -math.pi / 2 + i * step
                v_positions[v] = (cx + layout_radius * math.cos(angle), cy + layout_radius * math.sin(angle))

        # Dibujar arcos
        pen_edge = QPen(QColor(90, 90, 90))
        pen_edge.setWidth(2)
        for v1, v2 in edges:
            x1, y1 = v_positions[v1]
            x2, y2 = v_positions[v2]
            line = QGraphicsLineItem(x1, y1, x2, y2)
            line.setPen(pen_edge)
            line.setZValue(0)
            self.graph_scene.addItem(line)

        # Dibujar vértices
        pen_v = QPen(QColor(30, 80, 140))
        pen_v.setWidth(2)
        brush_v = QBrush(QColor(210, 230, 250))
        font_v = QFont()
        font_v.setBold(True)
        font_v.setPointSize(11)

        for v in vertices:
            x, y = v_positions[v]
            circle = QGraphicsEllipseItem(x - v_radius, y - v_radius, v_radius * 2, v_radius * 2)
            circle.setPen(pen_v)
            circle.setBrush(brush_v)
            circle.setZValue(1)
            self.graph_scene.addItem(circle)

            text = QGraphicsTextItem(v)
            text.setFont(font_v)
            text.setDefaultTextColor(QColor(20, 20, 20))
            t_rect = text.boundingRect()
            text.setPos(x - t_rect.width() / 2, y - t_rect.height() / 2)
            text.setZValue(2)
            self.graph_scene.addItem(text)

        self.graphicsViewGraph.fitInView(self.graph_scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

    def update_graph_status(self):
        self.lblGraphStatus.setText(f"Vértices: {self.graph.vertex_count()} | Arcos: {self.graph.edge_count()}")

    def update_graph_controls(self):
        vc = self.graph.vertex_count()
        ec = self.graph.edge_count()
        self.cmbVertex.setEnabled(vc > 0)
        self.btnDeleteVertex.setEnabled(vc > 0)
        self.cmbOrigin.setEnabled(vc > 0)
        self.cmbDestination.setEnabled(vc > 0)
        self.btnAddEdge.setEnabled(vc >= 2)
        self.btnDeleteEdge.setEnabled(ec > 0)
        self.btnClearGraph.setEnabled(vc > 0)
        self.btnRedrawGraph.setEnabled(vc > 0)

    def clear_graph(self):
        if self.graph.is_empty():
            QMessageBox.information(self, "Grafo vacío", "El grafo no contiene elementos.")
            return
        res = QMessageBox.question(
            self, "Limpiar grafo", "¿Desea eliminar todos los vértices y arcos?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if res == QMessageBox.StandardButton.Yes:
            self.graph.clear()
            self.update_graph_view()