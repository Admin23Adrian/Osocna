from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread
from componentes import *
import sys


# Clase Principal de la interfaz grafica.
class Interfaz(QMainWindow):
    def __init__(self):
        super().__init__()

        self.componentes = MainWindow()
        self.componentes.setupUi(self)
        self.componentes.btn_enviar.clicked.connect(self.mostrarMensaje)

        self.show()
    
    def mostrarMensaje(self):
        print("Clickado desde Iniciar!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    interfaz = Interfaz()
    interfaz.show()
    sys.exit(app.exec_())