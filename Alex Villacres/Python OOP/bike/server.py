class Bike(object):
    def __init__(self, name, price, speed): #POSITIONAL ARGUMENT
        print 'Created new bike!'
        self.price = price
        self.speed = speed
        self.name = name
        self.miles = 0

    def displayInfo(self):
        print '{} = Price: {}, Max Speed: {}, Miles: {}'.format(self.name, self.price, self.speed, self.miles)
        return self

    def riding(self):
        print 'Riding'
        self.miles += 10
        print '{} Miles ridden: {}'.format(self.name, self.miles)
        return self

    def reverse(self):
        print 'Reversing'
        if self.miles > 0:
            self.miles -= 5
        print '{} reversing: {} miles'.format(self.name, self.miles)
        return self


bike1 = Bike('bike1', '$100', '20mph')
bike2 = Bike('bike2', '$200', '25mph')
bike3 = Bike('bike3', '$300', '30mph')

# Bike 1's activities
bike1.riding().riding().riding().reverse().displayInfo()

# Bike 2's activities
bike2.riding().riding().reverse().reverse().displayInfo()

# Bike 3's activities
bike3.reverse().reverse().reverse().displayInfo()
