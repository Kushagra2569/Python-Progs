import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class display(QWidget):

    def __init__(self):
        super().__init__()
        self.ui()
        
    def ui(self):
        self.resize(700,150)
        self.move(300,300)
        self.setWindowTitle('Awesome')

        self.button = QPushButton('Play', self)
        self.button.move(80,50)
        self.button.resize(self.button.sizeHint())
        self.button.clicked.connect(self.msg)
        
        self.button.setToolTip('sample tooltip')

        btn1 = QPushButton('Pause',self)
        btn1.move(150,50)
        btn1.resize(btn1.sizeHint())
        btn1.clicked.connect(QCoreApplication.instance().quit)
        btn2 = QPushButton('Next',self)
        btn2.move(220,50)

        btn3 = QPushButton('Previous',self)
        btn3.move(10,50)
        self.show()
    def msg(self):
        print('testing stuff')
        m = QMessageBox()
        m.setText('testing')
        m.setWindowTitle('hey')
        m.exec_()

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    obj  = display()
    sys.exit(app.exec_())
