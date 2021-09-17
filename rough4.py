lst1 = []
lst2 = []
n = int(input("No of elements in list= "))
for i in range(1,n+1):
    ele1 = int(input(f'List 1 ele {i}= '))
    cube = ele1 ** 3
    lst1.append(cube)
for i in range(1,n+1):
    ele2 = int(input(f'List 2 ele {i}= '))
    cube = ele2 ** 3
    lst2.append(cube)
print(lst1)
print(lst2)