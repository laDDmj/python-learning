'''
Task 1
Запрограмуйте програму калькулятор, яка буде приймати від користувача введення 2-х чисел
та вид математичної операції (+, -, *, /).
Виведіть результат операції та продовжуйте виконання калькулятора, поки користувач не введе символ "q" для виходу.

'''

'''while True:
    reply = input('Please enter two strings and math operation or q if you want to quit: ')
    if reply.lower() == 'q':
        break
    elif len(reply.split(' '))!=3:
        print('add more digits')
        continue

    else:
        my_list = reply.split(' ')
        if(my_list[0].isdigit() and my_list[1].isdigit()):

            if my_list[2]=='+':
                print(int(my_list[0]) + int(my_list[1]))
            elif my_list[2]=='-':
                print(int(my_list[0]) - int(my_list[1]))
            elif my_list[2]=='*':
                print(int(my_list[0]) * int(my_list[1]))
            elif my_list[2]=='/':
                print(int(my_list[0]) / int(my_list[1]))
            else:
                print('invalid operation')
                '''

'''
Task 2
Знову генеруємо пошту для працівника, але тепер всі дані містяться в списку:sunglasses:
["name", "surname", "domain"]'''
'''
sunglasses = ['Kira', 'Nikituk', '@otakoyi.com']
print(f'{sunglasses[0][0].lower()}{sunglasses[1].lower()}{sunglasses[2]}')
'''

'''
Task 3
Те ж саме завдання із генеруванням пошти, але тепер у вас декілька працівників (нехай буде 5). 
Спробуйте використати вкладені списки
'''

'''
employees = [['Kira', 'Nikituk', '@otakoyi.com'], ['Dmytro', 'Ladutko', '@otakoyi.com'], ['Anastasiia', 'Andriiva', '@otakoyi.com']]

for employee in employees:

    print(f'{employee[0][0].lower()}{employee[1].lower()}{employee[2].lower()}')
'''
'''git config --global user.name "John Doe"
git config --global user.email'
'''

'''
Task 4

Створіть програму для керування списком продуктів в інтернет-магазині. Кожен продукт може мати назву,
ціну та кількість на складі. Реалізуйте можливість користувачу додавати нові продукти, оновлювати інформацію
про продукти та виводити список доступних продуктів за певними критеріями (наприклад, за ціною або наявністю на складі).

'''
'''
my_dict = {'milk':{'price': 30,'quantity': 75}, 'bread':{'price': 20,'quantity': 180}}
my_dict['meat']={'price': 200,'quantity': 15}
my_dict['milk']['price']=35
for key,value in my_dict.items():
    print(key,': ', value['price'])
'''

'''
Task 5

Напишіть програму для керування списком завдань. Кожне завдання може мати назву,
опис, пріоритет та статус (наприклад, "виконується", "в очікуванні", "завершено").
Реалізуйте можливість додавання нових завдань, оновлення статусу завдань та виведення списку завдань за пріоритетом.
'''

my_tasks = {'github':{'description':'create token', 'priority':1, 'status':'comleted'}, 'python':{'description':'install pycharm', 'priority':2, 'status':'pending'},'homework':{'description':'upload to lms', 'priority':3, 'status':'pending'}}
my_tasks['dinner']={'description':'go cafe', 'priority':1, 'status':'pending'}
my_tasks['dinner']['status']='completed'
#sorted_dict = dict(sorted(my_tasks.items()))
#for key,value in sorted(my_tasks, key=my_tasks['priority'].get, reverse=True):
#витягнути велюз, велюз від велюз

