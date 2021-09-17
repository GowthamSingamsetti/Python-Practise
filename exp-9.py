name = input("Enter your Name: ")

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a max of 50 characters")
else:
    print("You name is awesome")
