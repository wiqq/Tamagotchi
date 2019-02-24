import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, 
                            QPushButton, QHBoxLayout, QGroupBox,
                            QGridLayout, QVBoxLayout, QProgressBar)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QTimer

import constants, creature, creatureInfo, timer, images

class window(QWidget):

    c = constants.constants()
    creature = creature.creature()
    creature_info = creatureInfo.creatureInfo()
    img = images.images()

    def __init__(self):
        super().__init__()

        self.love_iter = 0

        self.window_prosp()
        self.img.make_pixmaps()
        self.init_labels()
        self.init_timers()
        self.set_main_layout()

        self.show()

    def window_prosp(self):
        self.resize(self.c.WINDOW_WIDTH, self.c.WINDOW_HEIGHT)
        self.move(self.c.POS_X, self.c.POS_Y)
        self.setWindowTitle("Tamagotchi")

    def init_labels(self):
        self.bck_label = self.img.make_background(self)
        self.creature_label = self.img.show_creature(self)
        self.love_label = self.img.make_love_label(self)

    def init_timers(self):
        self.param_timer = QTimer(self)
        self.param_timer.timeout.connect(self.actualise_creature_parameters)
        self.param_timer.start(10000)

        self.move_timer = QTimer(self)
        self.move_timer.timeout.connect(self.img.move_creature)
        self.move_timer.start(100)

        self.love_timer = QTimer(self)
        self.love_timer.timeout.connect(self.show_love)

    def set_buttons_top(self):
        self.top_group_box = QGroupBox()
        layout = QHBoxLayout()

        food_button = QPushButton("Nakarm")
        food_button.clicked.connect(self.food_button_clicked)

        sleep_button = QPushButton("Połóż spać")
        sleep_button.clicked.connect(self.sleep_button_clicked)

        stroke_button = QPushButton("Pogłaszcz")
        stroke_button.clicked.connect(self.stroke_button_clicked)

        clean_button = QPushButton("Posprzątaj")
        clean_button.clicked.connect(self.clean_button_clicked)

        layout.addWidget(food_button)
        layout.addWidget(sleep_button)
        layout.addWidget(stroke_button)
        layout.addWidget(clean_button)

        self.top_group_box.setLayout(layout)
        
    def set_bottom_right_box(self):
        self.bottom_right_group_box = QGroupBox()
        
        label1 = QLabel("Najedzenie")
        label2 = QLabel("Energia")
        label3 = QLabel("Miłość")
        label4 = QLabel("Zdrowie")
        label5 = QLabel("Potrzeba kupy")

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)

        self.bottom_right_group_box.setLayout(layout)

    def set_bottom_left_box(self):
        self.boottom_group_box = QGroupBox()
        layout = QVBoxLayout()

        layout.addWidget(self.creature_info.make_fed_bar(self.creature.fed))
        layout.addWidget(self.creature_info.make_energy_bar(self.creature.energy))
        layout.addWidget(self.creature_info.make_love_bar(self.creature.love))
        layout.addWidget(self.creature_info.make_health_bar(self.creature.health))
        layout.addWidget(self.creature_info.make_toilet_must_bar(self.creature.toilet_must))

        self.boottom_group_box.setLayout(layout)
    
    def set_main_layout(self):
        self.set_buttons_top()
        self.set_bottom_right_box()
        self.set_bottom_left_box()

        main_layout = QGridLayout()
        main_layout.addWidget(self.top_group_box, 0, 0, 1, 2)
        main_layout.addWidget(self.boottom_group_box, 2, 1)
        main_layout.addWidget(self.bottom_right_group_box, 2, 0)

        main_layout.setRowStretch(0, 1)
        main_layout.setRowStretch(1, 5)
        main_layout.setRowStretch(2, 1)

        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 2)

        self.setLayout(main_layout) 

    def food_button_clicked(self):
        self.make_food_label()
        self.make_food_buttons()

    def make_food_label(self):
        self.creature_label = QLabel()
        self.creature_label.resize(150, 200)
        self.creature_label.move(self.c.POS_X + 180, self.c.POS_Y)

        self.creature_label.show()

    def make_food_buttons(self):
        apple_button = QPushButton("Jabłko")
        apple_button.setIcon(QIcon('Images/Food/jablko.png'))
        apple_button.clicked.connect(self.apple_button_clicked)

        banana_button = QPushButton("Banan")
        banana_button.setIcon(QIcon('Images/Food/banan.png'))
        banana_button.clicked.connect(self.banana_button_clicked)

        carrot_button = QPushButton("Marchewka")
        carrot_button.setIcon(QIcon('Images/Food/marchew.png'))
        carrot_button.clicked.connect(self.carrot_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(apple_button)
        layout.addWidget(banana_button)
        layout.addWidget(carrot_button)

        self.creature_label.setLayout(layout)

    def apple_button_clicked(self):
        if(self.creature.apple_count == 2):
            self.creature.overfed()
            self.creature_info.change_love_bar(self.creature.love)
            self.creature_info.change_health_bar(self.creature.health)
            return

        self.creature.give_apple()

        self.creature_info.change_fed_bar(self.creature.fed)
        self.creature_info.change_toilet_must_bar(self.creature.toilet_must)
        self.creature_info.change_health_bar(self.creature.health)

    def banana_button_clicked(self):
        if(self.creature.banana_count == 2):
            self.creature.overfed()
            self.creature_info.change_love_bar(self.creature.love)
            self.creature_info.change_health_bar(self.creature.health)
            return

        self.creature.give_banana()
        self.creature_info.change_fed_bar(self.creature.fed)
        self.creature_info.change_toilet_must_bar(self.creature.toilet_must)
        self.creature_info.change_health_bar(self.creature.health)

    def carrot_button_clicked(self):
        if(self.creature.carrot_count == 2):
            self.creature.overfed()
            self.creature_info.change_love_bar(self.creature.love)
            self.creature_info.change_health_bar(self.creature.health)
            return

        self.creature.give_carrot()
        self.creature_info.change_fed_bar(self.creature.fed)
        self.creature_info.change_toilet_must_bar(self.creature.toilet_must)
        self.creature_info.change_health_bar(self.creature.health)
    
    def sleep_button_clicked(self):
        self.creature.sleep()

    def stroke_button_clicked(self):
        self.creature.stroke()
        self.creature_info.change_love_bar(self.creature.love)
        self.start_showing_love()
        
    def clean_button_clicked(self):
        return True

    def actualise_creature_parameters(self):
        self.creature.actualise_parameters()

        self.creature_info.change_fed_bar(self.creature.fed)
        self.creature_info.change_energy_bar(self.creature.energy)
        self.creature_info.change_love_bar(self.creature.love)
        self.creature_info.change_health_bar(self.creature.health)
        self.creature_info.change_toilet_must_bar(self.creature.toilet_must)

    def start_showing_love(self):
        self.love_timer.start(100)
        self.move_timer.stop()

    def stop_showing_love(self):
        self.love_iter = 0
        self.img.stop_showing_love()

        self.love_timer.stop()
        self.move_timer.start(100)

    def show_love(self):
        self.love_iter += 1
        self.img.show_love(self.love_iter)

        if(self.love_iter == 36):
            self.stop_showing_love()
            return
