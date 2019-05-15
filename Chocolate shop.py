print('''Welcome to SNCY chocolate shop

There are our special today.
''')
ans=input('''
Do you want to try it? 

Yes or No?
''')
if ans.lower() == 'yes':
    print('''
    There are two type of chocolate
    
    Do you want Black chocolate (B) or White chocolate (W)? 
    ''')
    type_of_chocolate=input('B or W? ')
    if type_of_chocolate.upper() == 'B':
        print('Okay , it is RM 10')
        ans=input('Do you want it? yes or no ')
        if ans.lower() == 'yes':
            print('Thank you , Welcome back!')
        elif ans.lower() == 'no':
            print("It's okay , thank you~")
    elif type_of_chocolate.upper() == 'W':
        print('Okay , it is RM 8')
        ans=input('Do you want it? yes or no ')
        if ans.lower() == 'yes':
            print('Thank you , Welcome back!')
        elif ans.lower() == 'no':
            print("It's okay , thank you")
elif ans.lower()== "no":
    print('Thank you , Welcome back!')
else:
    print('I do not get you....')
input('It is SNCY Chocolate shop , Do you feel good? ')

