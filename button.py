import constants
from PyQt5.QtWidgets import QPushButton, QLabel, QRadioButton, QGroupBox
from PyQt5.QtCore import pyqtSlot

class button(QPushButton):
    c = constants.constants()
    def __init__(self):
        super().__init__()
        self.setText("Nakarm")
        self.setDefault(False)

        self.clicked.connect(self.button_clicked)

        self.show()
        
    def button_clicked(self):
        self.make_label()
        
    def make_label(self):
        self.label = QLabel()#"lol")
        self.label.resize(200, 100)
        self.label.move(self.c.POS_X + 150, self.c.POS_Y + 120)

        self.label.show()