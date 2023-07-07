#Task 1

user_name = input('Enter your name and surname:\n')
user_age = input('How old are you:\n')

credit_sum = 2000

if not user_age.isdigit():

    exit('Error! Use digits format to your age!')

user_a = int(user_age)

if user_a < 18 or user_a > 80:
    print('Sorry, but you out of credit conditions!')
    exit()

user_job = input('Do you have current work? Print y/n :\n').lower()

if user_job == 'y':
    user_income = input('Your total income is about:\n')

    if not user_income.isdigit():
        exit('Error! Use digits format to your income!')

    else:
        user_i = int(user_income)
        first_digit = (int(str(user_income[0])))
        user_credit = credit_sum * first_digit + credit_sum + user_i
        print('We have', user_credit, 'for you!')

elif user_job == 'n':
    print('We have', credit_sum, 'for you!')

else:
    print('Unknown command, please enter y or n.')

#Task 2