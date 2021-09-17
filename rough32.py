#Sem End Co-4
'''
class Square():
    def __init__(self,side):
        self.side = side

    def Square_area(self):
        return (self.side*self.side)

    def Square_perimeter(self):
        return (4*self.side)


newSquare = Square(5)
print('Area = ', newSquare.Square_area(), 'Perimeter = ', newSquare.Square_perimeter())




class Triangle():
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def Triangle_area(self):
        return (self.base*self.height)/2


newTriangle = Triangle(5,10)
print('Area = ', newTriangle.Triangle_area())
n=5
for i in range(0,n):
    for j in range(0,i+1):
        print('*',end=' ')
    print('\n')





filename=input("Enter the file name : ")
with open(filename) as file:
    text=file.read()
    count_vowels = 0
    count_consonents = 0
    for char in text:
        if char in "aeiou":
            count_vowels += 1
        else:
            count_consonents += 1
print("Number of vowels = ",count_vowels)
print("Number of consonents = ",count_consonents)
print("Total Length of the file = ",len(text))
print("Percentage of vowels in the file =  ",((count_vowels)*100)/len(text),"%")
print("Percentage of consonents in the file =  ",((count_consonents)*100)/len(text),"%")







pi=3.14

def circle(r):
    return (pi*r*r,2*pi*r)


r=int(input("Enter radius = "))
(Area,Circumference)=circle(r)
print("Area of circle is =",Area)
print("Circumference of circle is =",Circumference)




class ABC:
    def __init__(self,name,val):
        self.name=name
        self.val=val
    def __repr__(self):
        return repr(self.val)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.val - obj.val


obj=ABC("Ramesh",10)
print("The representation of the obj is",repr(obj))
print("The length of the string in object is",len(obj))
obj1=ABC("Suresh",1)
val=obj.__cmp__(obj1)
print(val)



class ABC():
    CLASS_VAR = 0
    def __init__(self , val):
        ABC.CLASS_VAR += 1
        self.val = val
        print("Object Variable Value = " , val)
        print("The CLASS VARIABLE value is : " , ABC.CLASS_VAR)
    #  print("The CLASS VARIABLE value is : “ , CLASS_VAR)---This gives error

obj1 = ABC(10)






from abc import ABC, abstractmethod
class Car(ABC):
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")
class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")




# Driver code
t= Tesla ()
t.mileage()

s = Suzuki()
s.mileage()


class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 0

    # A member method that changes
    # __hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)


# Driver code
myObject = MyClass()
myObject.add(2)
myObject.add(5)

# This line causes error
print(myObject.__hiddenVariable)







class myclass:
    __hiddenvarible=0
    def add(self,increment):
        self.__hiddenvarible += increment
        print(self.__hiddenvarible)

obj=myclass()
print(obj.add(2))



class sample:
    name = "ramesh"
    age = 20


obj1=sample()
print(obj1.name)'''



x=[[12, 7, 3],
   [5, 6, 8],
   [1, 2 , 4]]
y=[[17, 8, 1],
   [5, 1, 8],
   [7, 1 , 1]]
result=[[0, 0, 0],
   [0, 0, 0],
   [0, 0 , 0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] - y[i][j]
for r in result:
    print(r)




