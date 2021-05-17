from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from sqlprop import Acesso
from PyQt5 import QtGui

retorno = 1

class Cadastrologin(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Cadastro de login para Usuário")
        self.resize(250, 200)
        self.setWindowIcon(
            QtGui.QIcon(r'C:\Users\Rachid Elihimas\OneDrive - MGN - Gestão de Negócios\Área de Trabalho\mgnlogo.webp'))

        layout = QGridLayout()
        self.setLayout(layout)

        """Nome dos campos que indicaram para o usuário o que deve ser preenchido: """
        user = QLabel("Login: ")
        layout.addWidget(user, 0, 0)

        psswrd = QLabel("Senha: ")
        layout.addWidget(psswrd, 1, 0)

        prmss = QLabel("Permissao: ")
        layout.addWidget(prmss, 2, 0)

        """Campos para inserção dos dados"""
        self.lineuser = QLineEdit()
        layout.addWidget(self.lineuser, 0, 1)

        self.linepsswrd = QLineEdit()
        layout.addWidget(self.linepsswrd, 1, 1)

        self.lineprmss = QComboBox()
        self.lineprmss.addItem("Administrador")
        self.lineprmss.addItem("Usuário")
        self.lineprmss.addItem("Consulta")
        self.lineprmss.currentTextChanged.connect(self.combobox_changed)
        layout.addWidget(self.lineprmss, 2, 1)

        """Botão para envio dos dados para o banco"""
        button = QPushButton("Clique para enviar")
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button, 3, 1)

    def combobox_changed(self):
        text = self.lineprmss.currentText()

    def on_button_clicked(self):
            self.usuario = self.lineuser.text()
            self.senha = self.linepsswrd.text()
            self.permissao = self.lineprmss.text()

            if self.lineprmss.text() == "Adminitrador":
                self.permissao = 5
            elif self.lineprmss.text() == "Usuário":
                self.permissao = 3
            else:
                self.permissao = 1

            if self.lineuser.text() == '' or self.linepsswrd.text() == '':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.resize(200, 100)
                msg.setWindowTitle("Erro - Campo(s) Vazio(s)")
                msg.setText("Algum campo do cadastro está vazio e isso é uma ação não permitida.\n"
                            "Por favor, envie novamente com todos o campos preenchidos.")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()
            else:
                envio = Acesso()
                envio.cadastroUserLogin(self.usuario, self.senha, self.permissao)
                self.lineuser.clear()
                self.linepsswrd.clear()
                self.lineprmss.clear()
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
                    msg.setText("Cadastro Incorreto!")
                    msg.setStandardButtons(QMessageBox.Ok)
                    retval = msg.exec_()


app = QApplication(sys.argv)
screen = Cadastrologin()
screen.show()
sys.exit(app.exec_())
