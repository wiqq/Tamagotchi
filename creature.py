import time, constants

class creature(object):
    c = constants.constants()

    def __init__(self):
        self.growth = 1
        self.fed = 25 # 25%
        self.energy = 50.0 # 50%
        self.love = 10
        self.health = 70
        self.toilet_must = 10

        self.apple_count = 0
        self.banana_count = 0
        self.carrot_count = 0

        self.poop = False
        self.sleeping = False
        self.bad_condition = 0

        self.start_time = time.time()

    def growing(self):
        if(self.growing) < 5:
            self.growing += 1

    def get_love(self):
        return self.love

    def add_love(self):
        self.love += 10

        if(self.love > 100):
            self.love = 100
        
    def feed(self, food_size):
        self.fed += food_size
        if(self.fed > 100):
            self.fed = 100
            self.health -= 10

            self.toilet_must += 20
            if(self.toilet_must > 100):
                self.toilet_must = 100

    def give_apple(self):
        self.apple_count += 1
        self.banana_count = 0
        self.carrot_count = 0

        self.toilet_must += 4
        if(self.toilet_must > 100):
                self.toilet_must = 100
        self.feed(7)

    def give_banana(self):
        self.banana_count += 1
        self.apple_count = 0
        self.carrot_count = 0

        self.toilet_must += 8
        if(self.toilet_must > 100):
                self.toilet_must = 100
        self.feed(15)

    def give_carrot(self):
        self.carrot_count += 1
        self.apple_count = 0
        self.banana_count = 0

        self.toilet_must += 5
        if(self.toilet_must > 100):
                self.toilet_must = 100
        self.feed(10)

    def overfed(self):
        self.love -= 15
        if(self.love < 0):
            self.love = 0

        self.health -= 5
        if(self.health < 0):
            self.health = 0

    def stroke(self):
        self.love += 10
        if(self.love > 100):
            self.love = 100  

    def sleep(self):
        # print("Program trwal %s sekund" % round(time.time() - self.start_time, 2))
        if(self.energy > 30):
            return

        self.sleeping = True

    def actualise_parameters(self):
        bad_condition_count = 0

        if(self.actualise_fed() == 1):
            bad_condition_count += 1

        if(self.actualise_energy() == 1):
            bad_condition_count += 1

        if(self.actualise_love() == 1):
            bad_condition_count += 1

        if(self.poop == True):
            bad_condition_count += 1

        self.actualise_health(bad_condition_count)

        self.actualise_toilet_must()

    def actualise_fed(self):
        self.fed -= self.c.FED_CHANGE
        if(self.fed < 0):
            self.fed = 0
            return 1

    def actualise_energy(self):
        if(self.sleeping == True):
            self.energy += self.c.ENERGY_CHANGE_SLEEP
            if(self.energy > 100):
                self.energy = 100
                self.sleeping = False

        else:
            self.energy -= self.c.ENERGY_CHANGE_AWAKEN
            if(self.energy < 0):
                self.energy = 0
                return 1

    def actualise_love(self):
        self.love -= self.c.LOVE_CHANGE
        if(self.love < 10):
            if(self.love < 0):
                self.love = 0
            return 1

    def actualise_health(self, bad_condition_count):
        if(bad_condition_count == 0):
            self.health += self.c.HEALTH_CHANGE

        else:
            self.health -= self.c.HEALTH_CHANGE*bad_condition_count

    def actualise_toilet_must(self):
        self.toilet_must += self.c.TOILET_MUST_CHANGE
        if(self.toilet_must > 100):
            self.toilet_must = 100
