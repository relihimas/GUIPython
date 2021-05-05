from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys
from MainWindow import MainWindow

class Loginpage(QWidget):
    def __init__(self):
      super().__init__()
      self.setWindowIcon(QtGui.QIcon(r'C:\Users\Rachid Elihimas\OneDrive - MGN - Gestão de Negócios\Área de Trabalho\mgnlogo.webp'))
      self.setWindowTitle('MGN - Login')
      self.resize(250, 100)
      self.MainWindow = MainWindow()

      layout = QGridLayout()
      usuario = QLabel('Usuário:')
      senha = QLabel('Senha:')
      layout.addWidget(usuario, 0, 0)
      layout.addWidget(senha, 1, 0)

      self.lineusuario = QLineEdit()
      self.lineusuario.setPlaceholderText('Informe seu nome de usuário')
      layout.addWidget(self.lineusuario, 0, 1)

      self.linesenha = QLineEdit()
      self.linesenha.setPlaceholderText('Informe sua senha')
      self.linesenha.setEchoMode(QLineEdit.Password)
      layout.addWidget(self.linesenha, 1, 1)

      botaologin = QPushButton('Login')
      botaologin.clicked.connect(self.press_login)
      layout.addWidget(botaologin, 2, 0, 2, 2)
      self.setLayout(layout)

    def press_login(self):
      self.loginuser = self.lineusuario.text()
      self.loginpswrd = self.linesenha.text()
      self.lineusuario.clear()
      self.linesenha.clear()
      if self.loginuser == 'rachid' and self.loginpswrd == 'rachid':
        self.MainWindow.show()
      else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.resize(200, 100)
        msg.setWindowTitle("MGN - Login")
        msg.setText("Usuário ou senha incorretos!")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()



app = QApplication(sys.argv)
login = Loginpage()
login.show()
sys.exit(app.exec_())
