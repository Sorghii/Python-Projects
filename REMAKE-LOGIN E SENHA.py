from time import sleep
from os import system
from random import randint
login = False
print('To access th message, you must log into your account.')
print('If you already have an account, type "1", if you do not have one, type "2"')
henrique = input('')
while henrique == '1':
    print('Sorry, but i cant save your datas from previous runs, this option is just symbolic, sorry for the situation, try again.')
    sleep(3)
    system('cls')   
    print('To access th message, you must log into your account.')
    print('If you already have an account, type "1", if you do not have one, type "2"')
    henrique = input()
    sleep(3)
while henrique == '2':
    system('cls')
    print('To register, fill in the fields below with your information')
    accountreg = input('E-mail or username: ') 
    passwordreg = input('Password: ')
    confirm = input('Confirm your password: ')
    if passwordreg != confirm:
        print('The password confirmation must be the same as the password.')
        sleep(3)
        system('cls')
    else:
        code = randint(100000, 999999)
        print('Your emergency code is: ', code)
        print('Note the code, you will not be able to access it again.')
        print('When you have already noted, write below anything')
        ready = input('')
        sleep(1)
        blocked = False
        while login == False:
            system('cls')
            print('LOGIN WITH YOUR INFORMATION BELOW')
            accountlog = input('E-mail or username: ') 
            passwordlog = input('Password: ')
            if accountlog != accountreg and blocked == True:
                print('Emergency code incorrect, your account has been permanently blocked.')
            else:
                if accountlog != accountreg:
                    print('Email or username not found, fill in the fields with valid information.')
                else:
                    if passwordlog != passwordreg:
                        print('Incorrect password, to access your account, write your emergency code below:')
                        confirmcode = int(input(''))
                        if confirmcode != code:
                            print('')
                            print('Emergency code incorrect, your account has been temporarily blocked. Try again later.')
                            blocked = True
                        else:
                            changer = False
                            while changer == False:
                                print('')
                                passwordlog = input('New password: ')
                                confirmchanger = input('Confirm the new password: ')
                                if passwordlog != confirmchanger:
                                    print('The password confirmation must be the same as the password.')
                                    sleep(3)
                                    system('cls')
                                else:
                                    print('You have been changed your password, try to login again.')
                                    changer = True
                                    sleep(3)
                                    system('cls')
            login = True                        
    break
if henrique != '1' and henrique != '2':
    print('You chose an incorrect option, try again later.')
if login == True:
    print('Writing...')
    sleep(5)
    system('cls')
    print('This is my first code that not is just a simple "1, 2, 3, 4". So, thank you for testing this. Please report to me any problems found in the code, bye bye!')      