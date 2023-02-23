import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijk1lmnopgrstuvwxyZABCDEFGHI JKLMNOPQRSTUVWXYZ ! @£$%*&*().,?0123456789'

number = input('How many passwords do you want to generate?\n')
number = int(number)

length = input('Input the length of your passwords: ')
length = int(length)

print('\nHere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)