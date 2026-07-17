from datetime import datetime
from estructuras.lineales.queue import Queue

class Cliente:
    def __init__(self, numero_turno):
        self.turno = numero_turno
        self.hora_ingreso = datetime.now()

    def get_hora_ingreso_str(self):
        return self.hora_ingreso.strftime("%H:%M:%S")

class SistemaBanco:
    def __init__(self):
        self.cola_espera = Queue()
        self.contador_turnos = 0
        self.clientes_atendidos = 0
        self.tiempo_total_espera = 0  
        self.banco_cerrado = False

    def agregar_cliente(self):
        # Si el banco ya se cerró, rechazamos el ingreso
        if self.banco_cerrado:
            return False, "¡El banco ya está cerrado! No se permiten más clientes."

        self.contador_turnos += 1
        nuevo_cliente = Cliente(self.contador_turnos)
        self.cola_espera.enqueue(nuevo_cliente)
        
        return True, f"Cliente con turno {nuevo_cliente.turno} ingresó a las {nuevo_cliente.get_hora_ingreso_str()}"
    def atender_cliente(self):
        if self.cola_espera.isEmpty():
            return None, "No hay clientes en la cola."

        # Extraemos el cliente de la cola (FIFO)
        cliente = self.cola_espera.dequeue()
        hora_atencion = datetime.now()
        
        # Cálculo de tiempo de espera en segundos
        tiempo_espera = int((hora_atencion - cliente.hora_ingreso).total_seconds())
        self.tiempo_total_espera += tiempo_espera
        self.clientes_atendidos += 1

        info_atencion = {
            "turno": cliente.turno,
            "hora_salida": hora_atencion.strftime("%H:%M:%S"),
            "tiempo_espera": tiempo_espera
        }
        return info_atencion, f"Atendiendo turno {cliente.turno} (Espera: {tiempo_espera} seg)"

    def obtener_clientes_espera(self):
        # Recorremos la lista enlazada interna para listar clientes
        elementos = []
        temp = self.cola_espera.lista.head
        while temp is not None:
            c = temp.data
            elementos.append(f"Turno {c.turno} - {c.get_hora_ingreso_str()}")
            temp = temp.next
        return elementos

    def intentar_cerrar_banco(self):
        self.banco_cerrado = True
        if not self.cola_espera.isEmpty():
            return False, "Aún hay clientes por atender."
        
        promedio = 0
        if self.clientes_atendidos > 0:
            promedio = round(self.tiempo_total_espera / self.clientes_atendidos, 1)

        return True, {
            "atendidos": self.clientes_atendidos,
            "promedio": promedio
        }