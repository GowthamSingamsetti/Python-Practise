print(ord("4"))
x = 10
y = 10

print(x % y)
x="ncjj"
print(x[::-1])

print(3%10)

n = int(input("Enter number: "))
rev = 0
while (n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
print("Reverse of the number:", rev)