class Animal(object):
    birthdate = ''
    has_hair = False


class Mammal(Animal):
    has_hair = True
    num_legs = 4


class CatFancy(Mammal):
    "A mammal that thinks it's a people."
    name = ''
    personality = ''
    preferred_food = ''

    def __init__(self, name, num_legs, birthdate):
        self.name = name
        self.num_legs = num_legs
        self.birthdate = birthdate

    def __str__(self):
        return self.name

    def purrr(self, num_into_this=0):
        return 2*num_into_this
