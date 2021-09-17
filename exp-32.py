class Mammal:
    def walk(self):
        print("It can walk")


class Dog(Mammal):
    def bark(self):
        print("It can bark.")


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
