#Sem End Co-3
'''pi = 3.14


def Circle(r):
    return (pi * r * r, 2 * pi * r)


radius = float(input("Enter the Radius: "))
(area, circum) = Circle(radius)
print("Area of the circle = ", area)
print("Circumference of the circle = ", circum)



def letterfreq(filename,letter):
    file=open(filename,'r')
    text=file.read()
    return text.count(letter)

print(letterfreq('details.txt','d'))


def compare(x,y):
    if(x==y):
        print("Both the numbers are equal")
    else:
        print("Both the numbers are not equal")


x=int(input("Enter 1st number = "))
y=int(input("Enter 2nd number = "))
compare(x,y)



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
len((text),"%")


def swap_numbers(a, b):
    temp = a
    a = b
    b = temp

    print("After Swapping two Number: num1 = {0} and num2 = {1}".format(a, b))


num1 = float(input(" Please Enter the First Value : "))
num2 = float(input(" Please Enter the Second Value : "))

print("Before Swapping two Number: num1 = {0} and num2 = {1}".format(num1, num2))
swap_numbers(num1, num2)


def sum(*args):
    sum=0
    for num in args:
        if(num>0):
            sum += num
    return sum


print(sum(1,2,3,-3,-2))


def small(a,b):
    if(a<b):
        return a
    else:
        return b
summ = lambda x,y: x+y

diff = lambda x,y: x-y


print("Smaller of two numbers = ",small(summ(-3,-2),diff(-1,2)))




def find_Evenodd(num):
    if num %2 == 0:
        return 1
    else:
        return 0


num = int(input("Enter a number to check even or odd: "))
if find_Evenodd(num):
    print("It is an even number")
else:
    print("It is an odd number")'''




def add(*args):
    '''Function returns the sum of values passed to it'''
    sum=0
    for i in args:
        sum += i
    return sum

print(add.__doc__)
print("Sum = ",add(2,3,5,5))




a = "Rolls Royce "
b = str(194.8)
print(a + b)
