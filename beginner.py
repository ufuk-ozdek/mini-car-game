started = False
while True:
    car = input('> ').lower()
    if car == 'help':
        print('''start - to start the car
stop - to  stop the car
quit - to  exit ''')

    elif car == 'start' and started == False:
        print('Car started... Ready to go ! ')
        started = True
    elif car == 'start' and started == True:
        print('Car is already started')
    elif car == 'stop' and started == True:
        print('Car stopped.')
        started = False
    elif car == 'stop' and started == False:
        print('Car is already stopped')
    elif car == 'quit':
        break
    else:
        print("I don't understand that...")
