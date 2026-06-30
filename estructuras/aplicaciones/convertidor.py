import sys
import os

#Dado que no identifique el error le pedi a la ia que forzara a buscar la ruta correcta
#  Esto fuerza a Python a buscar desde la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from estructuras.lineales.stack import Stack


class ConvertidorInfixPostFix:
    def __init__(self):
        self.pila = Stack()
        # Diccionario de precedencia (+ y - valen 1, * y / valen 2, $ vale 3)
        self.precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '$': 3}

    def es_operador(self, caracter):
        return caracter in self.precedencia

    def convertir(self, expresion_infija):
        # Asegurar que la pila inicie vacía
        while not self.pila.is_empty():
            self.pila.pop()
            
        cadena_posfija = []
        expresion_limpia = expresion_infija.replace(" ", "")

        for elemento in expresion_limpia:
            # a) Si es operando (letra o número)
            if elemento.isalnum():
                cadena_posfija.append(elemento)
                
            # b) Si es paréntesis de apertura
            elif elemento == '(':
                self.pila.push(elemento)
                
            # c) Si es paréntesis de cierre
            elif elemento == ')':
                while not self.pila.is_empty() and self.pila.top_of_stack() != '(':
                    nodo_extraido = self.pila.pop()
                    if nodo_extraido is not None:
                        cadena_posfija.append(nodo_extraido.data)
                
                # Sacar el '(' de la pila
                if not self.pila.is_empty() and self.pila.top_of_stack() == '(':
                    self.pila.pop()
                    
            # d) Si es un operador
            elif self.es_operador(elemento):
                while (not self.pila.is_empty() and 
                       self.pila.top_of_stack() != '(' and 
                       self.pila.top_of_stack() is not None and
                       self.precedencia.get(self.pila.top_of_stack(), 0) >= self.precedencia[elemento]):
                    
                    nodo_extraido = self.pila.pop()
                    if nodo_extraido is not None:
                        cadena_posfija.append(nodo_extraido.data)
                
                self.pila.push(elemento)

        # 4. Vaciar lo que quede en la pila al terminar
        while not self.pila.is_empty():
            nodo_extraido = self.pila.pop()
            if nodo_extraido is not None:
                cadena_posfija.append(nodo_extraido.data)

        return "".join(cadena_posfija)