from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QAbstractAnimation, QRect

import constants, math

class images():
    c = constants.constants()
    iterator = 0
    creature_pos_x = c.MOV_X_0
    creature_pos_y = c.MOV_Y_0
    creature_dir = True #right direction

    image_table = ['Images/background_light.png',
                        'Images/heart.png',
                        'Images/heart2.png',
                        'Images/Newborn/newborn_right.png',
                        'Images/Newborn/newborn_left.png',
                        'Images/Newborn/newborn.png']
    pixmaps = []
    creature_pixmaps = []

    def make_pixmaps(self):
        a = len(self.image_table)
        for i in range(a):
            self.pixmaps.insert(i, QPixmap(self.image_table[i]))

    def make_background(self, QWidget):
        self.bck_label = QLabel(QWidget)

        self.bck_pixmap = self.pixmaps[self.c.BACKGR_LIGHT]
        self.bck_label.setPixmap(self.bck_pixmap)
        self.bck_label.resize(self.bck_pixmap.width(), self.bck_pixmap.height())
        self.bck_label.move(self.c.MOV_X_0, self.c.BACKGROUND_Y)

        return self.bck_label

    def show_creature(self, QWidget):
        self.creature_label = QLabel(QWidget)

        self.creature_pixmap = self.pixmaps[self.c.NEWB_RIGHT]
        self.creature_label.setPixmap(self.creature_pixmap)
        self.creature_label.resize(self.creature_pixmap.width(), self.creature_pixmap.height())
        self.creature_label.move(self.creature_pos_x, self.creature_pos_y)

        return self.creature_label

    def make_love_label(self, QWidget):
        self.love_label = QLabel(QWidget)
        self.love_label.resize(22, 22)
        self.love_label.move(self.c.WINDOW_WIDTH/2 + 20, self.c.MOV_Y_0 - 20)
        return self.love_label

    def show_love(self, iter):
        self.love_label.show()

        if(iter % 6 == 0 or iter % 6 == 1 or iter % 6 == 2):
            love_pixmap = self.pixmaps[self.c.HEART1]
        else:
            love_pixmap = self.pixmaps[self.c.HEART2]

        self.love_label.setPixmap(love_pixmap)
        self.creature_to_mid()

    def stop_showing_love(self):
        self.love_label.hide()

        if(self.creature_dir == True):
            self.creature_pixmap = self.pixmaps[self.c.NEWB_RIGHT]
        else:
            self.creature_pixmap = self.pixmaps[self.c.NEWB_LEFT]

        self.creature_label.setPixmap(self.creature_pixmap)

    def move_creature(self):
        if(self.creature_dir == True):
            self.creature_pos_x += 3

            if(self.creature_pos_x >= self.c.MOV_WIDTH):
                self.creature_pos_x = self.c.MOV_WIDTH
                self.creature_dir = False
                self.creature_pixmap = self.pixmaps[self.c.NEWB_LEFT]
                self.creature_label.setPixmap(self.creature_pixmap)
                return

            self.creature_pos_y = (self.c.MOV_Y_0 - 
                                    math.sin(((self.creature_pos_x - self.c.MOV_X_0))
                                    *3*math.pi/100)*self.c.SIN_PROPORTION)
            self.creature_label.move(self.creature_pos_x, self.creature_pos_y)

        else:
            self.creature_pos_x -= 3

            if(self.creature_pos_x <= self.c.MOV_X_0):
                self.creature_pos_x = self.c.MOV_X_0
                self.creature_dir = True
                self.creature_pixmap = self.pixmaps[self.c.NEWB_RIGHT]
                self.creature_label.setPixmap(self.creature_pixmap)
                return

            self.creature_pos_y = (self.c.MOV_Y_0 -
                                    math.sin(((self.creature_pos_x - self.c.MOV_X_0))
                                    *3*math.pi/100)*self.c.SIN_PROPORTION)
            self.creature_label.move(self.creature_pos_x, self.creature_pos_y)
    
    def creature_to_mid(self):
        self.creature_label.move(self.c.WINDOW_WIDTH/2, self.c.MOV_Y_0)
        self.creature_pixmap = self.pixmaps[self.c.NEWB_CENTR]
        self.creature_label.setPixmap(self.creature_pixmap)
        
#TODO zrobić osobną listę obrazków stworka, podstawić do funkcji
#TODO zmieniać obrazki w tej liście kiedy będą się zmieniać z rośnięciem