started = False
while True:
    command = input('> ').lower()
    if command == 'help':
        print('''start - to start the command
stop - to  stop the command
quit - to  exit ''')

    elif command == 'start':
        if started:
            print('Car is already started')
        elif not started:
            print('Car started... Ready to go !')
            started = True
    elif command == 'stop':
        if started:
            print('Car stopped')
            started = False
        elif not started:
            print('Car is already stopped')
    elif command == 'quit':
        break
    else:
        print("I don't understand that...")
