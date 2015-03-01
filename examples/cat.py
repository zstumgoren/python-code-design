class Cat(object):
    "A mammal that thinks it's a people."
    name = ''
    num_legs = 4  # default
    birthdate = ''
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

if __name__ == '__main__':

    cat1 = Cat('Fluffy', 3, '2015-02-01')
    print '%s says hi.' % (cat1)
    print '%s purrs at level %d' % (cat1, cat1.purrr(3),)
    print '%s has %d legs.' % (cat1, cat1.num_legs)
