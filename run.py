import sys
from ver1 import Ui_MainWindow 
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class kinwriter(QMainWindow, Ui_MainWindow): 
    
    def __init__(self):

        super().__init__()

        self.setupUi(self)
        # self.timer = QTimer(self)
        # self.timer.setSingleShot(False)
        # self.timer.setInterval(5000) # in milliseconds, so 5000 = 5 seconds
        # # self.timer.timeout.connect(self.start_Macro)
        # self.timer.start()i0nscn2kdlr2k


        #print​(self.hasMouseTracking())


        self.show()



app = QApplication([])
sn = kinwriter()
QApplication.processEvents()
sys.exit(app.exec_())