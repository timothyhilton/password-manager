import os
import json

if os.path.isfile('./encryptedPassList.json'):
    with open('encryptedPassList.json', 'r') as infile:
        passList = json.load(infile)
        print(passList)
else:
    passList = {}
    print('No password file found, creating now...')


def savepass():
    passListOutput = json.dumps(passList)
    print(passListOutput)
    with open("encryptedPassList.json", "w") as outfile:
        outfile.write(passListOutput)


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
            print('Saved!')
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
            if str(list(passList.keys())) != '[]':
                print(list(passList.keys()))
            else:
                print('No services or passwords exist!')
            input("Press Enter to continue...")
        case '5':
            break

savepass()
