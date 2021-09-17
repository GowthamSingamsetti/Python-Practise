class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Hi, How are you?")


person1 = Person("Tony")
print(person1.name)
person1.name = "Stark"
print(person1.name)
person1.talk()
