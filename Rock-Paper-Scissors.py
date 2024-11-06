from time import sleep
from os import system
from random import randint
while True:
    system('cls')
    print("Let's play Rock Paper Scissors, shall we?")
    sleep(2)
    print("Follow the instructions below:")
    sleep(2)
    print("At the same moment, we'll say an option, the rules are:")
    sleep(1)
    print('[>] = wins over')
    print('Rock > Scissors')
    print('Scissors > Paper')
    print('Paper > Rock')
    sleep(2)
    print('Now, we can play. Pick one option, and we will see who wins')
    print("[1] Rock [2] Paper [3] Scissors")
    sleep(2)
    user_choice = input('Your option: ')
    if user_choice == '1':
        bot_choice = 'Paper'
        print(f'{bot_choice}! Oh, I win! That was a good game.')
        break
    if user_choice == '2':
        bot_choice = 'Scissors'
        print(f'{bot_choice}! Oh, I win! That was a good game.')
        break
    if user_choice == '3':
        bot_choice = 'Rock'
        print(f'{bot_choice}! Oh, I win! That was a good game.')
        break
    if user_choice != '1' and user_choice != '2' and user_choice != '3':
        system('cls')
        print('Please, select a valid option')
        sleep(3)