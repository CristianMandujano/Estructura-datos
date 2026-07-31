import os
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QFont, QPen
from PyQt5.QtWidgets import QDialog, QGraphicsScene, QMessageBox
from estructuras.no_lineales.build_expression_tree import ExpressionTree


class LoadDialogoArbolExpresion(QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_arbol_expresion.ui", self)


        self.arbol = ExpressionTree()

        # Crear la escena para el QGraphicsView
        self.scene = QGraphicsScene(self)
        self.vista_grafica.setScene(self.scene)
        self.btn_construir.clicked.connect(self.procesar_expresion)

    def procesar_expresion(self):
        texto = self.input_expresion.text().strip()

        if not texto:
            QMessageBox.warning(
                self, "Atención", "Por favor ingresa una expresión postfija."
            )
            return

        # Intentar construir el árbol
        raiz = self.arbol.build_expression_tree(texto)

        if raiz is None:
            QMessageBox.critical(
                self,
                "Error de Sintaxis",
                "La expresión es inválida. Revisa los operandos y operadores.",
            )
            self.lbl_inorden.setText("Inorden (Infija): Error")
            self.lbl_preorden.setText("Preorden (Prefija): Error")
            self.lbl_postorden.setText("Posorden (Postfija): Error")
            self.scene.clear()
        else:
            # Obtener y mostrar recorridos
            infija = self.arbol.inorder_parenthesized()
            prefija = self.arbol.preorder()
            postfija = self.arbol.postorder()

            self.lbl_inorden.setText(
                f"Inorden (Infija parentizada):  {infija}"
            )
            self.lbl_preorden.setText(f"Preorden (Prefija):  {prefija}")
            self.lbl_postorden.setText(f"Posorden (Postfija):  {postfija}")

            # Dibujar el árbol en la interfaz
            self.dibujar_arbol(raiz)

    # --- LÓGICA PARA DIBUJAR EL ÁRBOL GRÁFICAMENTE ---
    def dibujar_arbol(self, raiz):
        self.scene.clear()
        if not raiz:
            return

        radio_nodo = 22
        distancia_vertical = 60
        ancho_inicial = 180

        self._dibujar_nodo(
            raiz, 0, 0, ancho_inicial, radio_nodo, distancia_vertical
        )
        self.scene.setSceneRect(
            self.scene.itemsBoundingRect().adjusted(-20, -20, 20, 20)
        )

    def _dibujar_nodo(self, nodo, x, y, ancho_hijo, radio, dist_y):
        if nodo is None:
            return

        # Conexiones hacia los hijos (líneas)
        if nodo.left:
            x_izq = x - ancho_hijo
            y_izq = y + dist_y
            self.scene.addLine(x, y, x_izq, y_izq, QPen(QColor("#94A3B8"), 2))
            self._dibujar_nodo(
                nodo.left, x_izq, y_izq, ancho_hijo / 2, radio, dist_y
            )

        if nodo.right:
            x_der = x + ancho_hijo
            y_der = y + dist_y
            self.scene.addLine(x, y, x_der, y_der, QPen(QColor("#94A3B8"), 2))
            self._dibujar_nodo(
                nodo.right, x_der, y_der, ancho_hijo / 2, radio, dist_y
            )

        # Círculo del nodo
        self.scene.addEllipse(
            x - radio,
            y - radio,
            radio * 2,
            radio * 2,
            QPen(QColor("#2563EB"), 2),
            QBrush(QColor("#EFF6FF")),
        )

        # Texto del operador o número
        texto = self.scene.addText(str(nodo.value))
        texto.setFont(QFont("Segoe UI", 10, QFont.Bold))
        rect_texto = texto.boundingRect()
        texto.setPos(x - rect_texto.width() / 2, y - rect_texto.height() / 2)