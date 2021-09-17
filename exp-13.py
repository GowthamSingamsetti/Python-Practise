prompt = ''
started = False
while prompt != "quit":
    prompt = input('>').casefold()
    if prompt == 'help':
        print(''' 
start - to start the car
stop - to stop the car
quit - to exit''')
    elif prompt == "start":
        if started:
            print('Car has already started')
        else:
            started = True
            print('Car started...Ready to go!')
    elif prompt == "stop":
        if not started:
            print('Car has already stopped.')
        else:
            print('Car stopped')
    elif prompt == "quit":
        break
    else:
        print("I don't understand that...")




