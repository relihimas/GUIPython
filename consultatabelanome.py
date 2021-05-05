import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui
import time

class TabelaNome(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consulta Usuário")
        self.resize(450, 350)
        self.setWindowIcon(
            QtGui.QIcon(r'C:\Users\Rachid Elihimas\OneDrive - MGN - Gestão de Negócios\Área de Trabalho\mgnlogo.webp'))

        layout = QGridLayout()
        self.setLayout(layout)

        """Nome dos campos que indicaram para o usuário o que deve ser preenchido: """
        nome = QLabel("Nome: ")
        layout.addWidget(nome, 0, 0)

        endereco = QLabel("Endereço: ")
        layout.addWidget(endereco, 1, 0)

        cidade = QLabel("Cidade: ")
        layout.addWidget(cidade, 2, 0)

        companhia = QLabel("Companhia: ")
        layout.addWidget(companhia, 3, 0)

        data = QLabel("Data Cadastro: ")
        layout.addWidget(data, 4, 0)

        """Campos para inserção dos dados"""
        self.linenome = QLineEdit()
        # self.linenome.returnPressed.connect(self.return_pressed)
        layout.addWidget(self.linenome, 0, 1)

        self.lineend = QLineEdit()
        # self.lineend.returnPressed.connect(self.return_pressed)
        layout.addWidget(self.lineend, 1, 1)

        self.linecidade = QLineEdit()
        # self.linecidade.returnPressed.connect(self.return_pressed)
        layout.addWidget(self.linecidade, 2, 1)

        self.linecomp = QLineEdit()
        # self.linecomp.returnPressed.connect(self.return_pressed)
        layout.addWidget(self.linecomp, 3, 1)

        self.linedata = QLineEdit()
        # self.linedata.returnPressed.connect(self.return_pressed)
        layout.addWidget(self.linedata, 4, 1)

        """Botão para envio dos dados para o banco"""
        button = QPushButton("Consultar")
        button.clicked.connect(self.consultadadosusuario)
        layout.addWidget(button, 10, 1)

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(175, 320, 200, 25)

        self.tabela_consultausuario = Tabela_Usuario()
        self.show()

    def consultadadosusuario(self):
        for i in range(101):
            time.sleep(0.05)
            self.pbar.setValue(i)

        self.tabela_consultausuario.show()

class Tabela_Usuario(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 - QTableWidget'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

    # Create table
    def createTable(self):
        self.tableWidget = QTableWidget()

        # Row count
        self.tableWidget.setRowCount(4)

        # Column count
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Name"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("City"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Aloysius"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Indore"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Alan"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Bhopal"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Arnavi"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Mandsaur"))

        # Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TabelaNome()
    sys.exit(app.exec_())
