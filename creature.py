
class creature:
    def __init__(self):
        self.growth = 1
        self.fed = 25 # 25%
        self.energy = 50.0 # 50%
        self.love = 50
        self.health = 70
        self.toilet_must = 10

        self.poop = False

    def growing(self):
        if(self.growing) < 5:
            self.growing += 1

    def actualise_param(self, fed_dec, ener_dec, love_dec):
        self.fed -= fed_dec
        self.energy -= ener_dec
        self.love -= love_dec
    
    def actualice_toilet_must(self, must_change):
        if(self.fed > 80):
            self.toilet_must += must_change*1.5
        elif(self.fed > 50 ):
            self.toilet_must += must_change
        elif(self.fed > 30):
            self.toilet_must += must_change*0.5

    def actualise_health(self, health_change):
        self.health += health_change
    
    def do_poop(self):
        self.poop = True
        self.toilet_must = 0

    def eat(self, food_type):
        last_fed = self.fed
        self.fed += food_type
        if(self.fed) > 100:
            self.fed = 100
            self.do_poop()
            self.actualise_health(-10)
        
        
