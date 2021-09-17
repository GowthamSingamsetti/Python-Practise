customers = {
    "name": "ramesh, suresh",
    "age": (20, 50),
    "place": "vij, hyd"
}
customers["blood"] = "O, AB"
print(customers["name"])
print(customers["age"])
print(customers.get("address", "25th street"))  #here address is not there in there in the dictionary so we set default
print(customers["blood"])
print(customers.get("blood"))
for i in customers:
    print(i * 3)

# numbers = (1, 2, 3, 5)
# x, y, z, a = numbers
# print(a)
