secret_number = 9
guess_count = 1
guess_limit = 3
while guess_count <= guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won")
        break                 #break because to break after correct guess
    else:
        print(f'this is chance no:{guess_count-1}')
else:
    print("you lost :(")