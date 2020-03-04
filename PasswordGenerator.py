import random

chars = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
        + '\n123456789!@#$%^&*()?+= ')
length = input('Welcome to the Random Password Generator! '
              + '\nPlease enter password length? ')
length = int(length)
print('Here are your Passwords: ')
for p in range(1,11):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
print('Thank you for using the Random Password Generator. ')





















