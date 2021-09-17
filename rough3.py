
print('Select any operation')
print('''
        1.)Add
        2.)Subtract
        3.)Multiply
        4.)Divide
        ''')
choice = int(input('Enter your choice: '))
x = int(input())
y = int(input())
if (choice == 1):
    print("The sum is = ",x+y)
if (choice == 2):
    print("The difference is = ",x-y)
if (choice == 3):
    print("The multiplication is = ",x*y)
if (choice == 4):
    print("The division is = ",x/y)
