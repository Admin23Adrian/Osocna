from PyQt5 import QtCore, QtGui, QtWidgets
import imagenes

class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        MainWindow.setStyleSheet("#fondo {\n"
"    background-color: qlineargradient(spread:pad, x1:0.140541, y1:0.665, x2:0.455, y2:0.448818, stop:0 rgba(7, 219, 131, 255), stop:0.998782 rgba(12, 197, 121, 255));\n"
"}\n"
"\n"
"#cont_izq {\n"
"    background-color: #00a957; \n"
"}\n"
"\n"
"#cont_der {\n"
"    background-color: #eaeaea;\n"
"}\n"
"\n"
"#titulo {\n"
"    font-size: 28px;\n"
"    font-family: Poppins;\n"
"    color: #c5f9e4;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"#icono {\n"
"    image: url(:/imgs/imagenes/ajustes.svg);\n"
"    background-size: content;\n"
"}\n"
"\n"
"#desc_enviados, #desc_confirmados {\n"
"    font-size: 22px;\n"
"    font-family: Nunito Sans;\n"
"    color: #eee;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"#cant_env, #cant_conf {\n"
"    font-family: Cascadia Code;\n"
"    font-size: 30px;\n"
"    color: #EEE;\n"
"}\n"
"\n"
"#input_fecha {\n"
"    border-radius: 15px;\n"
"    padding-left:20px;\n"
"    border: 1px solid #cbcbcb;\n"
"    font-family: Poppins;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"#lbl_fecha {\n"
"    font-size: 14px;\n"
"    color: #00a957;\n"
"    font-family: Nunito Sans;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"#calendario {\n"
"    image: url(:/imgs/imagenes/schedule.svg);\n"
"    background-size: content;\n"
"}\n"
"\n"
"#btn_enviar {\n"
"    border-style:None;\n"
"    font-family: Nunito Sans;\n"
"    font-size: 19px;\n"
"    background-color: #eab029;\n"
"    color: #EEE;\n"
"    font-weight: 600;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"#btn_confirmar {\n"
"    border-style:None;\n"
"    font-family: Nunito Sans;\n"
"    font-size: 19px;\n"
"    background-color: #00a957;\n"
"    color: #EEE;\n"
"    font-weight: 600;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"#mensaje_final {\n"
"    font-family: Nunito Sans;\n"
"    font-size: 16px;\n"
"    color: #f24c4d;    \n"
"    font-weight: 600;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fondo = QtWidgets.QFrame(self.centralwidget)
        self.fondo.setGeometry(QtCore.QRect(0, 0, 800, 550))
        self.fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fondo.setObjectName("fondo")
        self.contenedor = QtWidgets.QFrame(self.fondo)
        self.contenedor.setGeometry(QtCore.QRect(60, 60, 680, 430))
        self.contenedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contenedor.setObjectName("contenedor")
        self.cont_izq = QtWidgets.QFrame(self.contenedor)
        self.cont_izq.setGeometry(QtCore.QRect(0, 0, 340, 430))
        self.cont_izq.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cont_izq.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cont_izq.setObjectName("cont_izq")
        self.titulo = QtWidgets.QLabel(self.cont_izq)
        self.titulo.setGeometry(QtCore.QRect(0, 30, 340, 91))
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setWordWrap(True)
        self.titulo.setObjectName("titulo")
        self.mensajes = QtWidgets.QFrame(self.cont_izq)
        self.mensajes.setGeometry(QtCore.QRect(0, 269, 340, 161))
        self.mensajes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mensajes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mensajes.setObjectName("mensajes")
        self.desc_enviados = QtWidgets.QLabel(self.mensajes)
        self.desc_enviados.setGeometry(QtCore.QRect(0, 0, 170, 51))
        self.desc_enviados.setAlignment(QtCore.Qt.AlignCenter)
        self.desc_enviados.setObjectName("desc_enviados")
        self.desc_confirmados = QtWidgets.QLabel(self.mensajes)
        self.desc_confirmados.setGeometry(QtCore.QRect(170, 0, 170, 51))
        self.desc_confirmados.setAlignment(QtCore.Qt.AlignCenter)
        self.desc_confirmados.setObjectName("desc_confirmados")
        self.cant_env = QtWidgets.QLabel(self.mensajes)
        self.cant_env.setGeometry(QtCore.QRect(0, 50, 170, 61))
        self.cant_env.setAlignment(QtCore.Qt.AlignCenter)
        self.cant_env.setObjectName("cant_env")
        self.cant_conf = QtWidgets.QLabel(self.mensajes)
        self.cant_conf.setGeometry(QtCore.QRect(170, 50, 170, 61))
        self.cant_conf.setAlignment(QtCore.Qt.AlignCenter)
        self.cant_conf.setObjectName("cant_conf")
        self.icono = QtWidgets.QLabel(self.cont_izq)
        self.icono.setGeometry(QtCore.QRect(110, 140, 100, 100))
        self.icono.setText("")
        self.icono.setObjectName("icono")
        self.cont_der = QtWidgets.QFrame(self.contenedor)
        self.cont_der.setGeometry(QtCore.QRect(340, 0, 340, 430))
        self.cont_der.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cont_der.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cont_der.setObjectName("cont_der")
        self.input_fecha = QtWidgets.QLineEdit(self.cont_der)
        self.input_fecha.setGeometry(QtCore.QRect(70, 180, 211, 31))
        self.input_fecha.setObjectName("input_fecha")
        self.lbl_fecha = QtWidgets.QLabel(self.cont_der)
        self.lbl_fecha.setGeometry(QtCore.QRect(80, 156, 191, 21))
        self.lbl_fecha.setObjectName("lbl_fecha")
        self.calendario = QtWidgets.QLabel(self.cont_der)
        self.calendario.setGeometry(QtCore.QRect(124, 40, 100, 100))
        self.calendario.setText("")
        self.calendario.setObjectName("calendario")
        self.btn_enviar = QtWidgets.QPushButton(self.cont_der)
        self.btn_enviar.setGeometry(QtCore.QRect(14, 330, 151, 41))
        self.btn_enviar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_enviar.setObjectName("btn_enviar")
        self.btn_confirmar = QtWidgets.QPushButton(self.cont_der)
        self.btn_confirmar.setGeometry(QtCore.QRect(175, 330, 151, 41))
        self.btn_confirmar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_confirmar.setObjectName("btn_confirmar")
        self.mensaje_final = QtWidgets.QLabel(self.cont_der)
        self.mensaje_final.setGeometry(QtCore.QRect(16, 230, 311, 71))
        self.mensaje_final.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.mensaje_final.setAlignment(QtCore.Qt.AlignCenter)
        self.mensaje_final.setWordWrap(True)
        self.mensaje_final.setObjectName("mensaje_final")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo.setText(_translate("MainWindow", "Indexador de facturas Comisarios Navales"))
        self.desc_enviados.setText(_translate("MainWindow", "Enviados:"))
        self.desc_confirmados.setText(_translate("MainWindow", "Confirmados:"))
        # self.cant_env.setText(_translate("MainWindow", "100"))
        # self.cant_conf.setText(_translate("MainWindow", "100"))
        self.input_fecha.setPlaceholderText(_translate("MainWindow", "dd.mm.aaaa"))
        self.lbl_fecha.setText(_translate("MainWindow", "Fecha Facturacion"))
        self.btn_enviar.setText(_translate("MainWindow", "Enviar"))
        self.btn_confirmar.setText(_translate("MainWindow", "Confirmar"))
        # self.mensaje_final.setText(_translate("MainWindow", "Los documentos ya se encuentran disponibles en la extranet del cliente"))
