def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

#here max is changed maximum. because max is built in function and
# we are redifining it or changing the meaning which is a bad practise