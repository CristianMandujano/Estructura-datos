import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui.ui_dialogo_grafos import Ui_GraphWidget
from load.load_dialogo_grafo import MainController

class MainWindow(QWidget, Ui_GraphWidget, MainController):
    def __init__(self):
        super().__init__()
        # Carga la vista directamente sin archivos .ui externos
        self.setupUi(self)
        self.setWindowTitle("Práctica de Grafos No Dirigidos")
        
        # Conecta la lógica del grafo
        self.setup_graph()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
    
    """
1. ¿Por qué la matriz de adyacencia es simétrica? por que el grafo es no dirigido, lo que significa que si hay un arco de un vértice A a un vértice B, también hay un arco de B a A. Por lo tanto, la relación de adyacencia es bidireccional, lo que se refleja en la simetría de la matriz.
2. ¿Qué representa el valor 1 dentro de la matriz? representa la existencia de un arco entre dos vértices. Si la posición (i, j) de la matriz contiene un 1, significa que hay un arco que conecta el vértice i con el vértice j.
3. ¿Qué representa el valor 0? representa la ausencia de un arco entre dos vértices. Si la posición (i, j) de la matriz contiene un 0, significa que no hay un arco que conecte el vértice i con el vértice j.
4. ¿Por qué la diagonal principal contiene ceros? porque un vértice no puede conectarse a sí mismo en un grafo simple.
5. ¿Qué ocurre en la matriz cuando se agrega un vértice sin conexiones? se agrega una nueva fila y columna con ceros, ya que no hay arcos conectando ese vértice con otros.
6. ¿Por qué cada arco aparece en las listas de adyacencia de dos vértices? porque el grafo es no dirigido, lo que significa que cada arco tiene dos extremos y ambos vértices son vecinos del otro.
7. ¿Por qué la lista de arcos muestra cada conexión una sola vez? porque cada par de vértices conectados se representa como un único arco en la lista, independientemente de la dirección.
8. ¿Qué cambios se producen al eliminar un vértice conectado? se eliminan todas las conexiones asociadas a ese vértice, lo que afecta las matrices y listas correspondientes.
9. ¿Qué representación facilita consultar los vecinos de un vértice? la lista de adyacencia, ya que permite acceder rápidamente a los vértices conectados a un vértice específico.
10. ¿Qué representación permite revisar todas las posibles conexiones? la matriz de adyacencia, ya que muestra todas las relaciones entre los vértices.
11. ¿Qué estructura de Python se utiliza para almacenar el grafo? una lista de listas o un diccionario de listas.
12. ¿Qué relación tiene la lista de adyacencia con las listas estudiadas? es similar a una lista enlazada, pero cada nodo apunta a una lista de sus vecinos.
13. ¿Por qué la posición de los círculos no modifica el grafo? porque la posición es solo una representación visual y no afecta las relaciones entre los vértices.
14. ¿Cómo se determina si debe dibujarse una línea? si hay una conexión entre dos vértices en el grafo.
15. ¿Por qué los arcos se dibujan antes que los vértices? para que los vértices estén sobre los arcos en la representación visual.
16. ¿Qué función cumple el QGraphicsScene? actúa como un contenedor para los elementos gráficos y gestiona su interacción.
17. ¿Qué función cumple el QGraphicsView? proporciona una vista del QGraphicsScene y maneja la visualización y manipulación de los elementos gráficos.
18. ¿Por qué todas las representaciones deben actualizarse después de cada operación? para mantener la coherencia entre las diferentes formas de representar el grafo y reflejar correctamente los cambios realizados."""
    