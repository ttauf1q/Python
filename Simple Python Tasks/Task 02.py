
started = False
while True:
    print('> ')
    i = input()

    if i.upper() == 'HELP':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif i.upper() == 'START':
        if started:
            print('Car is already started!')
        else:
            started = True
            print('Car started ... Ready to go!')
    elif i.upper() == 'STOP':
        if not started:
            print('Car is already stopped!!')
        else:
            started = False
            print('Car stopped..')
    elif i.upper() == 'QUIT':
        break
    else:
        print("I don't understand that...")




