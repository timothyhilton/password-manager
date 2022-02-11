import os
import json
import io
from hashlib import sha256
import pyAesCrypt


def hashstr(hashed):
    return sha256(hashed.encode('utf-8')).hexdigest()


if os.path.isfile('./hashedMasterPassword.txt'):
    while 1:
        masterPassword = str(input('Master password: '))
        hashedMasterPassword = str(open('hashedMasterPassword.txt','r').readlines())
        if hashstr(masterPassword) == hashedMasterPassword.strip("[']"):
            print('Success!')
            break
        else:
            print('Try again')
else:
    masterPassword = str(input('No master password detected, please specify one now: '))
    hashedMasterFile = open("./hashedMasterPassword.txt", "w")

    hashedMasterFile.write(hashstr(masterPassword))
    hashedMasterFile.close()

if os.path.isfile('PassList.json'):
    print('FATAL ERROR: UNENCRYPTED PASS LIST DETECTED, PLEASE ONLY EXIT USING THE PROVIDED OPTION')
    input("By pressing enter, you agree that terminating the program both jeopardizes your security and also stops the "
          "program from saving correctly: ")

if os.path.isfile('EncryptedPassList.aes'):
    # use default buffer size
    bufferSize = 64 * 1024

    infile = "EncryptedPassList.aes"

    with open(infile, "rb") as fCiph:

        # initialize decrypted binary stream
        fDec = io.BytesIO()

        # get ciphertext length
        inputFileSize = os.stat(infile).st_size

        # decrypt stream
        pyAesCrypt.decryptStream(fCiph, fDec, masterPassword, bufferSize, inputFileSize)

        # print decrypted data
        thing = fDec.getvalue()
        print("Decrypted data:\n" + str(thing))
        #print(str(fDec.read()))
#    pyAesCrypt.decryptFile("EncryptedPassList.aes", "PassList.json", masterPassword)
#    with open('PassList.json', 'r') as infile:
        fDec.seek(0)
        passList = json.loads(fDec.read())
        print(str(passList))
else:
    passList = {}
    print('No password file found, creating now...')


def savepass():
    passListOutput = json.dumps(passList)
    with open("PassList.json", "w") as outfile:
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
pyAesCrypt.encryptFile("PassList.json", "EncryptedPassList.aes", masterPassword)
os.remove("PassList.json")
