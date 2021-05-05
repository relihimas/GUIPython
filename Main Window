import sys
import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from cadastrousuario import Cadastro
from PyQt5 import QtGui
from calendario import Calendar


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.cadastro_widget = Cadastro()
        self.calendar = Calendar()

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        self.setWindowTitle("Painel Principal")

        self.setWindowIcon(
            QtGui.QIcon(r'C:\Users\Rachid Elihimas\OneDrive - MGN - Gestão de Negócios\Área de Trabalho\mgnlogo.webp'))

        file = bar.addMenu("Arquivo")
        consulta = bar.addMenu("Consulta")
        cadastro = bar.addMenu("Cadastro")
        ajuda = bar.addMenu("Ajuda")

        consulta.addAction("Consulta Usuário")
        # consulta.triggered.connect()

        cadastro.addAction("Cadastrar Usuário")
        cadastro.triggered.connect(self.cadastro)

    def cadastro(self):
        self.cadastro_widget.show()


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

