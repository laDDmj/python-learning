#Task 1

def my_func():
    x = 'Here'
    y = 'We'
    z = 'Go'
    j = 14
    k = [3, 5, 7, 9]
    number_of_vars = len(locals())
    return number_of_vars

result = my_func()

print('Number of variables:', result)

#Task 2

def my_func1(a):
    def my_func2(b):
        return a * b
    return my_func2

a_in_f1 = my_func1(3)
result = a_in_f1(6)

print('Result: ', result)

#Task 3

def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)

def sqr_nums(nums):
        return [num**2 for num in nums]

def remove_negatives(nums):
        return [num for num in nums if num > 0]


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

result1 = choose_func(nums1, sqr_nums, remove_negatives)
assert result1 == [1, 4, 9, 16, 25]
print(result1)

result2 = choose_func(nums2, sqr_nums, remove_negatives)
assert result2 == [1, 3, 5]
print(result2)



