import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, 
                            QPushButton, QHBoxLayout, QGroupBox,
                            QGridLayout)
from PyQt5.QtGui import QIcon, QPixmap

import constants, button

class window(QWidget):

    c = constants.constants()

    def __init__(self):
        super().__init__()
        
        self.window_prosp()
        self.set_main_layout()

        self.show()

    def window_prosp(self):
        self.resize(self.c.WINDOW_WIDTH, self.c.WINDOW_HEIGHT)
        self.move(self.c.POS_X, self.c.POS_Y)
        self.setWindowTitle("Tamagotchi")

    def set_image(self):
        image_label = QLabel(self)
        layout = QHBoxLayout()
        self.middle_group_box = QGroupBox()

        pixmap = QPixmap('Images/heart.png')
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)
        self.middle_group_box.setLayout(layout)

    def set_buttons_top(self):
        self.top_group_box = QGroupBox()
        layout = QHBoxLayout()

        for i in range(4):
            btn = button.button()
            layout.addWidget(btn)

        self.top_group_box.setLayout(layout)
        
    def set_buttons_bottom(self):
        self.boottom_group_box = QGroupBox()
        layout = QHBoxLayout()

        for i in range(4):
            btn = button.button()
            btn.clicked.connect(btn.button_clicked)
            layout.addWidget(btn)

        self.boottom_group_box.setLayout(layout)
    
    def set_main_layout(self):
        self.set_image()
        self.set_buttons_top()
        self.set_buttons_bottom()

        main_layout = QGridLayout()
        main_layout.addWidget(self.top_group_box, 0, 0, 1, 2)
        main_layout.addWidget(self.middle_group_box, 1, 0, 1, 2)
        main_layout.addWidget(self.boottom_group_box, 2, 0, 1, 2)

        main_layout.setRowStretch(0, 1)
        main_layout.setRowStretch(1, 5)
        main_layout.setRowStretch(2, 1)

        self.setLayout(main_layout)

