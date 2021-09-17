weight = int(input("Enter your Weight: "))
unit = input("(L)bs or(k)g: ")
if unit == ("L", "l"):
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif unit == "K" or unit == "k":
    converted = weight / 0.45
    print(f"You are {converted} pounds")
else:
    print("Wrong Unit")
