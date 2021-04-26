from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from envioSQL import Acesso

class Window(QWindow):
    def __init__(self):
        QWindow.__init__(self)
        self.setTitle("GUI de Teste")
        self.resize(400, 300)


envio = Acesso()
envio.envioclientetipo()

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
