m = int(input("Enter the total Number of Rows  : "))
n = int(input("Enter the total Number of Columns  : "))

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if (i == 1 or i == m or j == 1 or j == n):
            print(n, end=' ')
        elif (i==int(n/2)+1 and j==int(m/2)+1):
            print(n-2, end=' ')
        else:
            print(n-1, end=' ')
    print('')
