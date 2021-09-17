# PYTHON program for bubble sort
print("PYTHON PROGRAM FOR BUBBLE SORT TECHNIQUE (Ascending Order)")
print("-"*70)
list = [12,4,45,67,98,34]
print("List before sorting" , list)
for i in range(0,6):
    flag = 0
    for j in range(0,5):
        if(list[j]>list[j+1]):
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
            flag = 1
    if(flag == 0):
        break;
print("\nList after sorting" , list)


print("PYTHON PROGRAM FOR BUBBLE SORT TECHNIQUE (Descending Order)")
print("-"*50)
list = [12,4,45,67,98,34]
print("List before sorting" , list)
for i in range(0,6):
    flag = 0
    for j in range(0,5):
        if(list[j]<list[j+1]):
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
            flag = 1
    if(flag == 0):
        break;
print("\nList after sorting" , list)

