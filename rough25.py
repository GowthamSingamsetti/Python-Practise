'''def small(a,b):
    if a>=b:
        return b
    else:
        return a


sum=lambda x,y:x+y
diff=lambda x,y:x-y
print(small(sum(2,44),diff(10,4)))





def letterfreq(filename,letter):
    file=open(filename,'r')
    text=file.read()
    return text.count(letter)

print(letterfreq('details.txt','d'))





def multiply(*args):
    y=1
    for num in args:
        y *= num
    print(y)


multiply(5,7)
multiply(5,10)



fileName = input("Enter the file to check: ").strip()

infile = open(fileName, "r")
vowels = set("AEIOUaeiou")
cons = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
text = infile.read().split()

countV = 0
for V in text:
    if V in vowels:
        countV += 1

countC = 0
for C in text:
    if C in cons:
        countC += 1

print("The number of Vowels is: ",countV,"\nThe number of consonants is: ",countC)'''