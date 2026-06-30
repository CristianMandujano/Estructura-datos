import sys
from PyQt5.QtWidgets import QApplication
from menus.menu_principal import MenuPrincipal

def main():
    app = QApplication(sys.argv)
    
    # Instanciamos y mostramos el menú principal gráfico
    ventana_sistema = MenuPrincipal()
    ventana_sistema.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()