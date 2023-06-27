#Task 1
'''

st = 'hydrogen'

if  len(st)<2:

    print()
    #print('Empty String')
    #print(st)

elif len(st)==2:

    print(2*st)

else:

    print(st[0:2]+st[-2:])
'''

#Task 2
'''

number = '9999999991'

if number.isdigit() and len(number)== 10:
    print("This number ""'",number,"'"' is valid', sep='')
else:
    print("Unvalid value. Please be sure that it consist of 10 digits.")
'''

#Task 3
'''
print('Expression: (225/15 + 196/14 - 256/16) ** 2')

answer = 169
user_answer = int(input('What is your answer: '))

if user_answer == answer:

        print('Georgeous!')

else:
        print('Wrong guess, try again.')
'''
#Task 4

'''
name = 'dmitrii'
name1 = input('What is your name: ')

if name1.lower() == name:
    print(name==name1.lower())

else:
    print('wrong')
'''
