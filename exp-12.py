prompt = ''
while prompt != "quit":
    prompt = input('>').casefold()
    if prompt == 'help':
        print(''' 
start - to start the car
stop - to stop the car
quit - to exit''')
    elif prompt == "start":
        print('Car started...Ready to go!')
    elif prompt == "stop":
        print('Car stopped.')
    elif prompt == "quit":
        break
    else:
        print("I don't understand that...")
