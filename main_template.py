from untitled import *


class VentanaPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec_()
