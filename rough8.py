
X = [[45,7,31],
    [14 ,57,86],
    [78 ,8,9]]

Y = [[15,78,1],
    [36,72,37],
    [4,58,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):

   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)