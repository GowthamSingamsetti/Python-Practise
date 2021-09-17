try:
    age = int(input('Enter your age: '))
    income = 2000
    risk = income / age
    print(risk)
except ValueError:
    print('Enter a value')
except ZeroDivisionError:
    print('Invalid value')
