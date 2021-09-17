rows = int(input("Enter the total Number of Rows  : "))
columns = int(input("Enter the total Number of Columns  : "))
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if (j%2==0):
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()
