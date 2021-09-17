class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


person1 = Person("Tony")
person1.talk()
print(person1.name)

person2 = Person("Natasha")
person2.talk()
