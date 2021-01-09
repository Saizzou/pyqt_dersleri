from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

''' Ilk ders icin cok fazla bir karmasa yaratmayalim. Asagidaki kodu kopyalayin
ve uygulamayi calistirin! Biraz incelemeye calisin ve olabildigince anlamaya 
calisin. Tek tek elemanlari inceleyecegiz siradaki derslerde. '''

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Koddunyam.net")

        label = QLabel("PyQT5!!!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("Arac Menusu")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("bug.png"), "Button1", self)
        button_action.setStatusTip("Bu senin 1ci butonun")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("bug.png"), "Button2", self)
        button_action2.setStatusTip("Bu senin 2ci button")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Merhabalar"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))


    def onMyToolBarButtonClick(self, s):
        print("Tikla ve Terminale bak!", s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()