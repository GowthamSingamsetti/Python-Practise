#Sem End Co-1
#count of even numbers in a range
'''
start=int(input("Starting Point: "))
end=int(input("End Point: "))
num = start+1
count=0
while(num!=end):
    if(num%2==0):
        count=count+1
        print(num)
    num +=1
print("count = ",count)
a = float(input(" Please Enter the First Value a: "))
b = float(input(" Please Enter the Second Value b: "))

if(a > b):
    print("{0} is Greater than {1}".format(a, b))
elif(b > a):
    print("{0} is Greater than {1}".format(b, a))
else:
    print("Both a and b are Equal")

start=int(input("Starting Point: "))
end=int(input("End Point: "))
count=0
for num in range(start+1, end):
    if(num%2==0):
        count +=1
        print(num)
print(count)

x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
import math
num=int(input("Enter number = "))
while(1):
    if(num == 999):
        break
    elif (num<0):
        print("Square root of negative numbers cannot be calculated")
        continue
    else:
        print("Square root of",num," = ",math.sqrt(num))
        break

number = int(input("Please Enter any Number: "))

for i in range(1, number + 1):
    print (i, end = '  ')'''
