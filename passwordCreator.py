def pwd():
    isupper = 0
    islower = 0
    y = ''
    x = input('Please enter a password. It must be 8 characters long '
              + '\n contains 1 uppercase letter '
              + '\n contains 1 lowercase letter '
              + '\n contains a digit '
              + '\n password: ')
    if len(x) >= 8:
        for i in x:
            if i.isupper() == True:
                isupper = 1
            if i.islower() == True:
                islower = 1
    while(y != x):
        
        y = input('Please retype the password: ')
    return x
print(pwd())
    
