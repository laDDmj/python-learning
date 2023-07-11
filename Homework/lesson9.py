#Task 1

def oops():
    raise IndexError('It seems like IndexError.')

def calls_error():
    try:
        return oops()
    except IndexError:
        print('There no such index.')
    #except KeyError:
        #print('Key Error')

calls_error()

#Task 2

a = input('Enter first number:\n')
b = input('Enter second number:\n')

def my_func():
    try:
        af = float(a)
        bf = float(b)
        result = ((af ** 2) / bf)
        return result

    except ZeroDivisionError:
        raise ZeroDivisionError('You cannot divide by zero.')
    except ValueError:
        raise ValueError('It seems like nothing to calculate, enter 2 numbers.')

print(my_func())

