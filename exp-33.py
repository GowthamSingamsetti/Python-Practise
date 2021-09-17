class Mammal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} can walk")


class Dog(Mammal):
    def bark(self):
        print("It can bark.")


class Cat(Mammal):
    pass


dog1 = Dog("Tommy")
dog1.walk()
dog1.bark()

cat1 = Cat("Sophie")
cat1.walk()

dog2 = Dog("")
dog2.walk()
