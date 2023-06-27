#Task 1 - done with input in prev. practice

#Task 2
'''
customer_name = input('Enter your name: ')

i=0
while i<5:
    print(customer_name, 'do you need our support?')
    i += 1
else:
    print('Wish you a nice shopping, ', customer_name,'!', sep='')
'''

#Task 3

'''
customer_name = input('Enter your name: ')

while True:

    customer_answer = input(f'{customer_name}, do you need our support "yes/no": \n')

    if customer_answer.lower() == 'no':
        print('Goodbye!')

else:
    customer_answer = input(f'{customer_name}, do you need our support "yes/no": \n')
'''

#Task 4

customer_name = input('Enter your name:\n')
quantity = input('Your quant number is: \n')

if quantity.isdigit():
    quantity=int(quantity)

    if quantity ==3:
        print('Here is your bonus ruler!')

    elif quantity==5:
        print('Here is your pencil!')

    elif quantity % 3==0 and quantity % 5==0:
        print('This bonus ruler and pencil now yours!!!')

    else:
        print('Maybe next time!')
else:
    print('Enter a correct number!')