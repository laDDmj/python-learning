import random

'''
#Task 1
import random

generator = random.randint(2, 11)

user_guess = input('Choose the number between 1 and 10: ')


if user_guess.isdigit():
    guess_number = int(user_guess)

    if guess_number==generator:
        print('Congratulation, you are wizzard!')

    elif 1<guess_number >10:
        print('Slow down!')

    else:
        print('Pff..Just another muggle')



else:
    print('Wrong symbols')
'''
'''
#Task 2


user_name = input('What is your name? ')
user_age = input('How old are you? ')

if user_age.isdigit():
    user_age=int(user_age)
    print('Hello', user_name, 'on your next birthday you’ll be', user_age+1, 'years.')

else:
    print('use digit as the age format')
'''
'''
initial_string = input('Enter any word: ')
number_of_strings = 5
i = 0

while i < number_of_strings:
    random_string = random.sample(initial_string, k=len(initial_string))

    print(random_string)
    i += 1
'''