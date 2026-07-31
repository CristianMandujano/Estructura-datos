from estructuras.lineales.stack import Stack
from estructuras.no_lineales.node_expression import NodeExpression


class ExpressionTree:

    def __init__(self):
        self.root = None

    def build_expression_tree(self, expression):
        operadores = {"+", "-", "*", "/", "^", "%"}
        pila = Stack()
        tokens = expression.strip().split()

        for token in tokens:
            nodo = NodeExpression(token)

            if token in operadores:
                if pila.is_empty():
                    return None

                der = pila.pop()

                if pila.is_empty():  # <-- ESTA VALIDACIÓN EVITA EL CASO "3 +"
                    return None

                izq = pila.pop()

                nodo.right = der.data if hasattr(der, "data") else der
                nodo.left = izq.data if hasattr(izq, "data") else izq

                pila.push(nodo)
            else:
                pila.push(nodo)

        if pila.is_empty():
            return None

        raiz_pop = pila.pop()
        # Misma verificación para la raíz final
        self.root = raiz_pop.data if hasattr(raiz_pop, "data") else raiz_pop

        if not pila.is_empty():
            return None

        return self.root
    
    def inorder_parenthesized(self):
        return self._inorder_parenthesized(self.root)

    def _inorder_parenthesized(self, node):
        if node is None:
            return ""
        if node.left is None and node.right is None:
            return str(node.value)
        izq = self._inorder_parenthesized(node.left)
        der = self._inorder_parenthesized(node.right)
        return f"({izq} {node.value} {der})"

    def preorder(self):
        elementos = []
        self._preorder(self.root, elementos)
        return " ".join(elementos)

    def _preorder(self, node, elementos):
        if node:
            elementos.append(str(node.value))
            self._preorder(node.left, elementos)
            self._preorder(node.right, elementos)

    def postorder(self):
        elementos = []
        self._postorder(self.root, elementos)
        return " ".join(elementos)

    def _postorder(self, node, elementos):
        if node:
            self._postorder(node.left, elementos)
            self._postorder(node.right, elementos)
            elementos.append(str(node.value))