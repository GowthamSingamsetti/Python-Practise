print("Hello World")
Marks = {'Raju':[97,89,94,90],'Ramu':[92,91,94,87],'Ajay':[67,99,88,90]}
tot = 0
Tot_marks = Marks.copy()
for key, val in Marks.items():
    tot = sum(val)
    Tot_marks[key]=tot
print(Tot_marks)
max = 0
Topper = ''
for key, val in Tot_marks.items():
    if val>max:
        max = val
        Topper=key
print("Topper is : ", Topper, "With Marks = ", max)