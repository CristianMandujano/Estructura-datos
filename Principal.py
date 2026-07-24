from estructuras.no_lineales.binary_tree import BinaryTree

def mostrar_menu():
    print("\n--- MENÚ ÁRBOL BINARIO ---")
    print("1. Insertar valor")
    print("2. Buscar valor")
    print("3. Recorrido Preorden")
    print("4. Recorrido Inorden")
    print("5. Recorrido Posorden")
    print("6. Contar nodos en el árbol")
    print("7. Salir")

tree = BinaryTree()

while True:
    mostrar_menu()
    option = input("Selecciona una opción: ")

    if option == "1":
        try:
            value = int(input("Ingresa el valor que deseas insertar: "))
            tree.insertar(value)
            print("Operación realizada.")
        except ValueError:
            print("Debes ingresar un número entero.")

    elif option == "2":
        try:
            value = int(input("Ingresa el valor que deseas buscar: "))
            if tree.buscar(value):
                print("El valor se encuentra en el árbol.")
            else:
                print("El valor no se encuentra en el árbol.")
        except ValueError:
            print("Debes ingresar un número entero.")

    elif option == "3":
        print("Recorrido en preorden:")
        tree.preorden()

    elif option == "4":
        print("Recorrido en inorden:")
        tree.inorden()

    elif option == "5":
        print("Recorrido en posorden:")
        tree.posorden()

    elif option == "6":
        print(f"Total de nodos en el árbol: {tree.contar_nodos()}") 
        
    elif option == "7":
        print("Programa finalizado.")
        break
       
    else:
        print("Opción no válida. Intenta nuevamente.")


#30. ¿Cuál es la función de la clase NodeTree? Es un nodo que representa cada elemento del árbol binario, almacenando un valor y referencias a sus "hijos"
#31. ¿Qué representa el atributo root?la raiz del arbol
#32. ¿Qué significa que un nodo tenga como hijo el valor None?que esa rama esta vacia 
#33. ¿Cuál es el caso base del método _insertar?ocurre cuando se llega a un nodo que es none 
#34. ¿Qué sucede cuando _insertar encuentra una posición vacía?crea una nueva instancia de NodeTree con el valor a insertar y la retorna, estableciendo así el nuevo nodo en esa posición del árbol.
#35. ¿Por qué se utiliza return node al final del método _insertar?para devolver el nodo actualizado despues de insertar
#36. ¿Qué sucede cuando se intenta insertar un valor repetido?se muestra un mensaje indicando que el valor ya existe en el árbol
#37. ¿Cómo decide el método buscar si debe continuar a la izquierda o a la derecha? Compara el valor buscado con el valor del nodo actual: si es menor, continúa a la izquierda; si es mayor, continúa a la derecha.
#38. ¿Cuál es el caso base de la búsqueda?ocurre cuando se llega a un nodo que es none
#39. ¿Cuál es el caso base de los recorridos?ocurre cuando se llega a un nodo que es none
#40. ¿En qué momento se muestra la raíz en el recorrido preorden?al principio
#41. ¿En qué momento se muestra la raíz en el recorrido inorden?en el medio
#42. ¿En qué momento se muestra la raíz en el recorrido posorden?al final
#43. ¿Por qué el recorrido inorden muestra los valores ordenados?por la propiedad que hace que los valores menores se inserten a la izquierda y los mayores a la derecha, lo que garantiza que al recorrer el árbol en inorden, se visiten primero los nodos con valores menores, luego la raíz y finalmente los nodos con valores mayores, resultando en una secuencia ordenada.
#44. ¿Qué sucede si los valores se insertan de menor a mayor?se crea un árbol desequilibrado, donde cada nodo solo tiene un hijo, lo que afecta el rendimiento de las operaciones.
#45. ¿Cuál es la diferencia entre el while del menú y las llamadas utilizadas dentro de la clase BinaryTree? El while del menú controla el flujo del programa y permite al usuario interactuar con las opciones, mientras que las llamadas a los métodos de la clase BinaryTree realizan las operaciones reales sobre el árbol.
#46. ¿Qué parte del programa evita que se ingresen letras cuando se solicita un número? La validación con try-except y la conversión a entero (int()) evitan que se ingresen letras.
#47. ¿Por qué la forma del árbol depende del orden de inserción? Porque en un árbol binario de búsqueda, los valores se insertan en función de su relación con los nodos existentes, afectando así la estructura general del árbol.
#48. ¿Por qué desde el menú no se debe acceder directamente a tree.root? Porque esto violaría el encapsulamiento y podría llevar a errores si se manipula directamente la raíz del árbol.
#49. ¿Qué función cumplen los métodos _preorden, _inorden y _posorden? Estos métodos implementan los recorridos respectivos del árbol binario, visitando los nodos en diferentes órdenes para mostrar su contenido.

#Modificacion nodo. Simplemente se agrego una nueva funcion que permite contar la cantidad de nodos en el arbol, la cual se llama contar y retorna un entero con la cantidad de nodos si es que hay en el arbol claramente.