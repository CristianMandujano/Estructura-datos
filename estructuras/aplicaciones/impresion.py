from estructuras.lineales.queue import Queue  # Composición: Queue como atributo

class TrabajoImpresion:
    def __init__(self, consecutivo: int, usuario: str, documento: str, paginas: int):
        self.consecutivo = consecutivo
        self.usuario = usuario
        self.documento = documento
        self.paginas = paginas

class GestorImpresion:
    def __init__(self):
        # Composición estricta: tiene una instancia de Queue (no hereda de ella)
        self.cola_impresion = Queue()
        self.contador_consecutivo = 0

    def agregar_trabajo(self, usuario: str, documento: str, paginas_str: str):
        # 1. Recibir y validar datos
        if not usuario.strip() or not documento.strip():
            return False, "Error: El usuario y el documento no pueden estar vacíos."
        
        try:
            paginas = int(paginas_str)
            if paginas < 1:
                return False, "Error: El número de páginas debe ser mayor a 0."
        except ValueError:
            return False, "Error: Ingrese un número de páginas válido."

        # 2 y 3. Asignar consecutivo de llegada y crear TrabajoImpresion
        self.contador_consecutivo += 1
        nuevo_trabajo = TrabajoImpresion(self.contador_consecutivo, usuario.strip(), documento.strip(), paginas)
        
        # 4. Agregar al final mediante enqueue
        self.cola_impresion.enqueue(nuevo_trabajo)
        return True, f"Trabajo #{nuevo_trabajo.consecutivo} ('{nuevo_trabajo.documento}') agregado a la cola."

    def procesar_siguiente(self):
        # 6. Comprobar que la cola no esté vacía
        if self.cola_impresion.isEmpty():
            # 9. Informar sin generar excepción
            return None, "La cola de impresión está vacía. No hay trabajos pendientes."

        # 7. Retirar elemento mediante dequeue
        trabajo = self.cola_impresion.dequeue()
        
        # 8. Mensaje con documento procesado
        msj = f"Imprimiendo Trabajo #{trabajo.consecutivo}: '{trabajo.documento}' ({trabajo.paginas} pág.) de {trabajo.usuario}."
        return trabajo, msj

    def consultar_frente(self):
        if self.cola_impresion.isEmpty():
            return "La cola está vacía."
        
        # Consultar frente (peek/front)
        frente = self.cola_impresion.lista.head.data
        return f"Trabajo Actual en Frente: #{frente.consecutivo} - '{frente.documento}' ({frente.usuario})"

    def obtener_lista_pendientes(self):
        # Recorrido de la cola para actualizar la tabla (Paso 5)
        elementos = []
        temp = self.cola_impresion.lista.head
        while temp is not None:
            elementos.append(temp.data)
            temp = temp.next
        return elementos

    def obtener_total_pendientes(self):
        contador = 0
        temp = self.cola_impresion.lista.head
        while temp is not None:
            contador += 1
            temp = temp.next
        return contador