from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from envioSQL import Acesso
from PyQt5 import QtGui

retorno = 1

class Cadastro(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Envio de Dados para o SQL")
        self.resize(450, 300)
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
        button = QPushButton("Clique para enviar")
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button, 10, 1)

        # self.parent = parent

    def on_button_clicked(self):
        # Nome, Endereço, Cidade, Companhia, DTCadastro
        self.nome = self.linenome.text()
        self.endereco = self.lineend.text()
        self.cidade = self.linecidade.text()
        self.companhia = self.linecomp.text()
        self.data = self.linedata.text()
        # envio = Acesso()
        # envio.envioclientetipo(self.nome, self.endereco, self.cidade, self.companhia, self.data)
        self.linenome.clear()
        self.lineend.clear()
        self.linecidade.clear()
        self.linecomp.clear()
        self.linedata.clear()
        if retorno == 1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.resize(200, 100)
            msg.setWindowTitle("Retorno Cadastro")
            msg.setText("Cadastro Realizado!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.resize(200, 100)
            msg.setWindowTitle("Retorno Cadastro")
            msg.setText("Usuário ou senha incorretos!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()


# app = QApplication(sys.argv)
# screen = Cadastro()
# screen.show()
# sys.exit(app.exec_())
