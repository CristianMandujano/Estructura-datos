# Simulación de Cola de Impresión (Estructura FIFO)

## Descripción del Algoritmo
La simulación administra trabajos de impresión garantizando el principio **FIFO** (*First In, First Out*). 

1. **Captura y Validación:** Se verifican los campos de usuario, documento y páginas ($\ge 1$).
2. **Creación del Objeto:** Se crea una instancia de `TrabajoImpresion` con un consecutivo único autoincrementable.
3. **Encolado (`enqueue`):** El trabajo se inserta al final de la cola mediante la clase `Queue`.
4. **Desencolado (`dequeue`):** Al procesar un trabajo, se retira el elemento ubicado al frente de la cola y se actualizan los componentes visuales (`QTableWidget` y contador).

## Uso de la Clase Queue (Composición)
La clase `GestorImpresion` contiene una instancia de la clase `Queue` como un atributo interno (`self.cola_impresion = Queue()`), cumpliendo con la regla de **composición en POO**.

### Operaciones Utilizadas:
* **`enqueue(dato)`**: Añade un nuevo `TrabajoImpresion` al final de la cola.
* **`dequeue()`**: Remueve y retorna el objeto `TrabajoImpresion` del frente.
* **`isEmpty()`**: Verifica si la cola carece de elementos antes de intentar un `dequeue`.
* **Recorrido / Tamaño**: Se recorren los nodos desde la cabeza (`head`) para actualizar la tabla y contar los trabajos pendientes dinámicamente.