#Task 1
#Write a decorator that prints a function with arguments passed to it.
#NOTE! It should print the function, not the result of its execution!

def logger(func):
    def wrapper(*args):
        arg_list = [str(arg) for arg in args]
        result = ', '.join(arg_list)
        print(f'Your {func.__name__} func with arguments:({result}),', sep='')
        return func(*args)
    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(3, 5)
square_all(3, 5, 7)

#Task 2
#Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

def stop_words(func):
    def wrapper(*args):
        words_list = ['pepsi', 'BMW']
        result = func(*args).split()
        modified_words = ['*' if word in words_list else word for word in result]
        modified_text = ' '.join(modified_words)
        return modified_text
    return wrapper

#Працює
@stop_words
def test():
    return f'pepsi and BMW'
print(test())

#У другому випадку виводить зірочкою всі, окрім останнього бо стоїть знак оклику.
#Використавши метод: "if word.rstrip('!')" можна ігнорувати, але результат не співпаде з "assert.." бо ігнорується той самий "!"
@stop_words
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW!'

print(create_slogan('Dima'))

assert create_slogan("Dima") == "Dima drinks * in his brand new *!"

#Task 2
#Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

def stop_words(func):
    def wrapper(*args):
        words_list = ['pepsi', 'BMW']
        result = func(*args)
        for word in words_list:
            if word in words_list:
                words_modified = result.replace(word.lower(), '*')
            return words_modified
        return words_list
    return wrapper

@stop_words
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW!'

print(create_slogan('Dima'))



def stop_words(func):
    def wrapper(*args):
        words_list = ['pepsi', 'BMW']
        replacement = '*'
        words = func(*args).split()
        for i in range(len(words)):
            if words[i] in words_list:
                words[i] = replacement
        result = ' '.join(words)
        return result
    return wrapper

@stop_words
def test():
    return 'pepsi and BMW!'

print(test())

@stop_words
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW!'

print(create_slogan('Dima'))


#Task 3
def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args):
          if not isinstance(args[0], type_):
            print(f'Error! Needed type is: {type_.__name__}')
            return False
          if len(args[0]) > max_length:
            print(f'Error! Length of argument is greater than {max_length} symbols')
            return False
          if not all(symbol in args[0] for symbol in contains):
            print(f'Error! There is no needed symbols: {contains}')
            return False

          return func(*args)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('Dim@S05 ddf'))

assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

#Task 2

def stop_words(words: list):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            for word in words:
                result = result.replace(word, '*')
            return result
        return wrapper
    return decorator



@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) ->str:
    return f'{name} drinks pepsi in his brand new BMW!'

assert create_slogan('Steve') == 'Steve drinks * in his brand new *!'

print(create_slogan('Steve'))