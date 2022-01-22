import os
import pickle

#test

if os.path.isfile('./passList.pkl'):
    with open('passList.pkl', 'rb') as f:
        passList = pickle.load(f)
else:
    passList = {}
    print('No password file found, creating now...')


def savepass():
    with open('passList.pkl', 'wb') as f:
        pickle.dump(passList, f)


while 1:
    print('')
    print('Please select one the following:')
    print('1: Create/Overwrite password')
    print('2: Delete existing password')
    print('3: Read existing password')
    print('4: List all services')
    print('5: Exit')
    print('')

    operation = str(input())
    match operation:
        case '1':
            print('')
            serviceToSave = str(input('Service: '))
            passToSave = str(input('Password: '))
            passList[serviceToSave] = passToSave
            print('saved!')
            savepass()
            print('')
            input("Press Enter to continue...")
        case '2':
            print('')
            serviceToDelete = str(input('Service to delete: '))
            if serviceToDelete in passList:
                passList.pop(serviceToDelete)
                savepass()
                print('success!')
                print('')
                input("Press Enter to continue...")
            else:
                print(serviceToDelete + " doesn't exist! Please retry")
                print('')
                input("Press Enter to continue...")
        case '3':
            print('')
            serviceToCheck = str(input('Service: '))
            if serviceToCheck in passList:
                print("Password: " + passList[serviceToCheck])
            else:
                print(serviceToCheck + " Doesn't Exist!")
            print('')
            input("Press Enter to continue...")
        case '4':
            print('')
            print(list(passList.keys()))
            input("Press Enter to continue...")
        case '5':
            break

savepass()
