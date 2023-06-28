import random
'''
#Task 1

random_list = []

r = 0
while r<10:

    generator = random.randint(1, 100)
    random_list.append(generator)
    r += 1

print('Max number is:', max(random_list), 'from', random_list)
'''
'''
#Task 2

random_list1 = []
random_list2 = []

r = 0

while r<10:

    generator_1 = random.randint(1, 11)
    generator_2 = random.randint(1, 11)

    random_list1.append(generator_1)
    random_list2.append(generator_2)
    
    r += 1

print('1st list:', random_list1, '\n2nd list:', random_list2)
print('intersection:',list(set(random_list1).intersection(set(random_list2))))
'''

list_n = list(range(1, 101))
result_list = []
#res_2 =[]

n = 0

while n<len(list_n):

    if list_n[n] % 7==0 and list_n[n] % 5!=0:
        result_list.append(list_n[n])
    #if list_n[n] % 5==0:
        #res_2.append(list_n[n])
    n += 1

print('Ta-Da:', result_list)
#print(sorted(list(set(result_list) - set(res_2))))

