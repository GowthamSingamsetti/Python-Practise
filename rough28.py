class Robot:
    population=0
    def __init__(self, name):
        self.name = name
        print('(Initializing {0})'.format(self.name))
        Robot.population += 1
    def __del__(self):
        print('{0} is being destroyed!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} was the last one.'.format(self.name))
        else:
            print('There are still {0:d} robots working.'.format(Robot.population))
    def sayHi(self):
        print('Greetings, my masters call me {0}.'.format(self.name))
    def howMany():
        print('We have {0:d} robots.'.format(Robot.population))
    howMany = staticmethod(howMany)


d=Robot('R1-D1')
d.sayHi()
Robot.howMany()
d1=Robot('R2-D2')
d1.sayHi()
Robot.howMany()
print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
del d
del d1
Robot.howMany()
