import random

for i in range(3):
    print(random.random())  # loop repeats for 3 times and executes random function everytime

print(random.random())  # random.random() prints random values between 0 and 1

for i in range(3):
    print(random.randint(10, 300))  # randint is used when we want random numbers between 2 intervals

members = ["Tony", "Steve","Thor","Nat","Banner"]
leader = random.choice(members)        # random.choice is used to pick a random person or thing from a list 
print(leader)
