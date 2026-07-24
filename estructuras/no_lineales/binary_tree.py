class NodeTree:
    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

class BinaryTree:
    def __init__(self):
         self.root = None

    def insertar(self, value):
         self.root = self._insertar(self.root, value)

    def _insertar(self, node, value):
        if node is None:
           return NodeTree(value)
        if value < node.value:
           node.left = self._insertar(node.left, value)
        elif value > node.value:
           node.right = self._insertar(node.right, value)
        else:
           print("El valor ya existe en el árbol.")
        return node
    
    def buscar(self, value):
        return self._buscar(self.root, value)
    
    def _buscar(self, node, value):
        if node is None:
           return False
        if value == node.value:
           return True
        if value < node.value:
           return self._buscar(node.left, value)
        else:
           return self._buscar(node.right, value)
        
    def preorden(self):
        self._preorden(self.root)
        print()
    
    def _preorden(self, node):
        if node is not None:
            print(node.value, end=" ")
            self._preorden(node.left)
            self._preorden(node.right)

    def inorden(self):
        self._inorden(self.root)
        print()

    def _inorden(self, node):
        if node is not None:
            self._inorden(node.left)
            print(node.value, end=" ")
            self._inorden(node.right)

    def posorden(self):
        self._posorden(self.root)
        print()

    def _posorden(self, node):
        if node is not None:
            self._posorden(node.left)
            self._posorden(node.right)
            print(node.value, end=" ")

    def contar_nodos(self):
        """Método público que inicia el conteo desde la raíz."""
        return self._contar_nodos(self.root)

    def _contar_nodos(self, node):
        """Método auxiliar recursivo."""
        if node is None:
            return 0
        
        return 1 + self._contar_nodos(node.left) + self._contar_nodos(node.right)