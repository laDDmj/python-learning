'''
#Task 1
name = input('Enter your name: ').lower()
surname = input('Enter your surname: ').lower()
domain = '@kobzar.com'

print(f'your email: ', name[0:1], surname, domain, sep='')
print(f'your second email: ', name, surname[0:3], domain, sep='')
print(f' yor third email: ', name,'_', surname, domain, sep='')
'''
'''
#Task 2
(не припиняється дія одразу, якщо age не цифра. 
Пробував: 1) while, break, та робити шось типу: 2) якщо не цифра - прінт, решта - виконуй)

name = input('What is your name? \n')
age = input('What is your age? \n')
bev = input('What do you want to drink? \n')

if age.isdigit():
    age = int(isdigit)

    if 14>age>18:
        print('Nah. Here is your energy drink')

    elif age<14:
        print('Come on! Only soda drink!')

    else:
            print('Here is your ', bev, '!', sep='')

else:
        print('Only digits for age!')
'''

# Task 3
'''
Transaction_ID = 'yu7i9om0iymn'
new_Transaction_ID = ';yu7i9om0iymn%'

valid_ID = new_Transaction_ID[1:len(new_Transaction_ID)-1]

print('Valid:', valid_ID==Transaction_ID)
'''

#Task 4
'''
transaction_ID = 'yu7i9om0iymn'
new_Transaction_ID = 'yu&7i9om&0iym&n'

valid_ID = new_Transaction_ID.replace('&','')
print('Valid:', valid_ID==transaction_ID)
'''