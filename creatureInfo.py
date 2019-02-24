from PyQt5.QtWidgets import QProgressBar

import constants

class creatureInfo():    
    c = constants.constants()

    def make_fed_bar(self, fed_val):
        self.fed = QProgressBar()
        self.fed.setRange(0, 100)
        self.fed.setValue(fed_val)
        self.fed.setStyleSheet(self.c.WARNING_STYLE)

        return self.fed

    def make_energy_bar(self, energy_val):
        self.energy = QProgressBar()
        self.energy.setRange(0, 100)
        self.energy.setValue(energy_val)
        self.energy.setStyleSheet(self.c.WARNING_STYLE)

        return self.energy

    def make_love_bar(self, love_val):
        self.love = QProgressBar()
        self.love.setRange(0, 100)
        self.love.setValue(love_val)
        self.love.setStyleSheet(self.c.ALARM_STYLE)

        return self.love

    def make_health_bar(self, health_val):
        self.health = QProgressBar()
        self.health.setRange(0, 100)
        self.health.setValue(health_val)
        self.health.setStyleSheet(self.c.GOOD_STYLE)

        return self.health

    def make_toilet_must_bar(self, toilet_must_val):
        self.toilet_must = QProgressBar()
        self.toilet_must.setRange(0, 100)
        self.toilet_must.setValue(toilet_must_val)
        self.toilet_must.setStyleSheet(self.c.GOOD_STYLE)

        return self.toilet_must



    def change_fed_bar(self, fed_val):
        if(fed_val <= 20):
            self.fed.setStyleSheet(self.c.ALARM_STYLE)
        elif(fed_val <= 50):
            self.fed.setStyleSheet(self.c.WARNING_STYLE)
        else:
            self.fed.setStyleSheet(self.c.GOOD_STYLE)

        self.fed.setValue(fed_val)

    def change_energy_bar(self, energy_val):
        if(energy_val <= 20):
            self.energy.setStyleSheet(self.c.ALARM_STYLE)
        elif(energy_val <= 50):
            self.energy.setStyleSheet(self.c.WARNING_STYLE)
        else:
            self.energy.setStyleSheet(self.c.GOOD_STYLE)

        self.energy.setValue(energy_val)

    def change_love_bar(self, love_val):
        if(love_val <= 20):
            self.love.setStyleSheet(self.c.ALARM_STYLE)
        elif(love_val <= 50):
            self.love.setStyleSheet(self.c.WARNING_STYLE)
        else:
            self.love.setStyleSheet(self.c.GOOD_STYLE)

        self.love.setValue(love_val)

    def change_health_bar(self, health_val):
        if(health_val <= 20):
            self.health.setStyleSheet(self.c.ALARM_STYLE)
        elif(health_val <= 50):
            self.health.setStyleSheet(self.c.WARNING_STYLE)
        else:
            self.health.setStyleSheet(self.c.GOOD_STYLE)

        self.health.setValue(health_val)

    def change_toilet_must_bar(self, toilet_must_val):
        if(toilet_must_val >= 85):
            self.toilet_must.setStyleSheet(self.c.ALARM_STYLE)
        elif(toilet_must_val >= 60):
            self.toilet_must.setStyleSheet(self.c.WARNING_STYLE)
        else:
            self.toilet_must.setStyleSheet(self.c.GOOD_STYLE)

        self.toilet_must.setValue(toilet_must_val)
