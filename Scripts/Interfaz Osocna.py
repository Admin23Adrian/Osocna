from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread
from componentes import *
import sys
from proceso2 import envio_documentacion
from confirmar import confirmar


# Clase Principal de la interfaz grafica.
class Interfaz(QMainWindow):
    def __init__(self):
        super().__init__()

        self.componentes = MainWindow()
        self.componentes.setupUi(self)

        # fecha para campo fecha
        self.fecha = ""
        # Boton de enviar la docuementacion a osocna
        self.componentes.btn_enviar.clicked.connect(self.mostrarMensaje)
        # Boton de confirmar
        self.componentes.btn_confirmar.clicked.connect(self.confirmar)
        self.show()
    
    def mostrarMensaje(self):
        self.fecha = self.componentes.input_fecha.text()
        if self.fecha != "":
            envio_documentacion(self.fecha)


    def confirmar(self):
        confirmar(self.fecha)
        self.componentes.mensaje_final.setText("Documentos en la Extranet del cliente!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    interfaz = Interfaz()
    interfaz.show()
    sys.exit(app.exec_())