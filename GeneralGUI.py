from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from envioSQL import Acesso


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Envio de Dados para o SQL")           #título
        # self.setWindowIcon()                            ícone
        # self.setFixedHeight(500)                        altura
        # self.setFixedWidth(400)                         largura

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


    def on_button_clicked(self):
        print("The button was pressed!")
        # Nome, Endereço, Cidade, Companhia, DTCadastro
        self.nome = self.linenome.text()
        self.endereco = self.lineend.text()
        self.cidade = self.linecidade.text()
        self.companhia = self.linecomp.text()
        self.data = self.linedata.text()
        envio = Acesso()
        envio.envioclientetipo(self.nome, self.endereco, self.cidade, self.companhia, self.data)
        print("Envio com sucesso!!")
        self.linenome.clear()
        self.lineend.clear()
        self.linecidade.clear()
        self.linecomp.clear()
        self.linedata.clear()

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
