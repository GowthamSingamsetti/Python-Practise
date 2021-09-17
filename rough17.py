rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))
n=0
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        n=n+1
        print(n,end=' ')
    print()
