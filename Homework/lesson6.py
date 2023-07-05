#Task 1

user_input = input('Any sentence:\n')
sep_words = user_input.split()
end_dict = {}

for w in sep_words:
    if w in end_dict:
        end_dict[w] += 1
    else:
        end_dict[w] = 1

print(end_dict)

#Task 2

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_p = {}

for key in stock:
    total_price = stock[key] * prices[key]
    total_p[key] = total_price
    sorted_total_p = sorted(total_p.items())
print('Total price for stock: ', (total_p))

#Task 3

list_1 = [(i, i**2) for i in range(1, 11)]
print(list_1)


#Task 4

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

weekday_dict = {i+1: days for i, days in enumerate(weekdays)}
weekday_dict2 = {days: i for i, days in weekday_dict.items()}

print(weekday_dict, weekday_dict2, sep='\n')
