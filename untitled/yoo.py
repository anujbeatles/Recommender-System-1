import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 400)
        self.setWindowTitle("Just Do It, Anuj")
        self.setWindowIcon(QtGui.QIcon('RSI-MACD-Paint.png'))

        extractAction = QtGui.QAction('&Chris Martin', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('LEAVE!')
        extractAction.triggered.connect(self.close_app)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Hell No", self)
        btn.setGeometry(50,50,100,66)
        btn.clicked.connect(self.close_app)
        btn.resize(btn.minimumSizeHint())

        self.show()

    def close_app(self):
        print('Sick!')
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()

    sys.exit(app.exec())

run()