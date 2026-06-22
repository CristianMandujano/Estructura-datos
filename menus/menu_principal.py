from estructuras.lineales.lista_enlazada_simple import Linkedlist

class MenuPrincipal(object):
    def __init__(self):
        self.lista_enlazada = Linkedlist()
  
    def mostrar_menu(self):
        print("Menú Principal")
        print("1. Agregar Inicio")
        print("2. Agregar Final")
        print("3. Buscar")
        print("4. Imprimir")
        print("5. Eliminar Al Inicio")
        print("6. Eliminar Al Final")
        print("7. Salir")

    def ejecutar_opcion(self, opcion):
        if opcion == "1":
            dato = input("Ingrese el dato a agregar al inicio: ")
            self.lista_enlazada.insert_at_beginning(dato)
            print(f"El dato '{dato}' ha sido agregado al inicio de la lista.")
        elif opcion == "2":
            dato = input("Ingrese el dato a agregar al final: ")
            self.lista_enlazada.insert_at_end(dato)
            print(f"El dato '{dato}' ha sido agregado al final de la lista.")
        elif opcion == "3":
            dato = input("Ingrese el dato a buscar: ")
            encontrado = self.lista_enlazada.search(dato)
            if encontrado:
                print(f"El dato '{dato}' se encuentra en la lista.")
            else:
                print(f"El dato '{dato}' no se encuentra en la lista.")
        elif opcion == "4":
            print("Contenido de la lista enlazada:")
            self.lista_enlazada.print_linked_list()
        elif opcion == "5":
            self.lista_enlazada.delete_at_beginning()
            print("Nodo eliminado del inicio de la lista.")
        elif opcion == "6":
            self.lista_enlazada.delete_at_end()
            print("Nodo eliminado del final de la lista.")
        elif opcion == "7":
            print("Saliendo del programa. ¡Hasta luego!")
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

    def iniciar(self):
        while True:
            self.mostrar_menu()
            try:
                opcion = input("Seleccione una opción: ")
                if opcion == "7":
                    self.ejecutar_opcion(opcion)
                    break
                self.ejecutar_opcion(opcion)
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número correspondiente a las opciones del menú.")


