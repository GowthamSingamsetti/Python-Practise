#Sem End Co-2
'''# Python code to remove duplicate elements
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))





test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

# Printing original keys-value lists
print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))

# using naive method
# to convert lists to dictionary
res = {}
for key in test_keys:
    for value in test_values:
        res[key] = value
        test_values.remove(value)
        break

    # Printing resultant dictionary
print("Resultant dictionary is : " + str(res))






name1 = 'John'
name2 = 'john'
name3 = 'doe'
name4 = 'Doe'

print("Are name1 and name2 equal ?")
print (name1 == name2)

print("Are name1 and name3 different ?")
print (name1 != name3)

print("Is name1 less than or equal to name2 ?")
print (name1 <= name2)

print("Is name3 greater than or equal to name2 ?")
print (name3 >= name2)

print("Is name4 less than name1 ?")
print (name4 < name1)

country=["Brazil","Russia","India" ,"China", "South africa"]

is_member = input("Enter the name of the country: ")

if is_member in country:

    print(is_member, "is a member of the BRICS")

else:

    print(is_member, "is not a member of BRICS")


def is_abecdarian(s):
    index = 0
    while index < len(s)-1:
        if s[index + 1] < s[index]:
            return False
        index += 1
    return True

print(is_abecdarian('babcd'))
print(is_abecdarian('abcz'))




#abecedarian series
str1 = "ABCDEFGH"
str2="are"
for letter in str1:
    print((letter + str2),end=' ')


#PAN card validation

name = input("Enter your name : ")
if name.isalpha() == False:
    print("Invalid Name, Sorry you cannot proceed.")
else:
    pan_card_no = input("Enter your PAN card number : ")
    if pan_card_no.isalnum() == False:
        print("Invalid PAN card Number, Sorry you cannot proceed.")
print("Please check, "+name+", your PAN card number is : "+pan_card_no)


Tup = (-10,1,5,8,-6,-2)
newTup = ()
for i in Tup:
    if i>0:
        newTup += (i,)
print(newTup)'''