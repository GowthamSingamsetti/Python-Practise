numbers = [5, 2, 5, 2, 2]
for x_count in numbers:   #No of x in each line is x_count
    output = ''
    for count in range(x_count):  # range beacause 5 numbers 0,1,2,3,4 in x_count are executed
        output += 'F'
    print(output)
