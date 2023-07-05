#Task 1

def favourite_movie():
    movie = 'Pulp Fiction'
    return(movie)
print(favourite_movie())

#Task 2

def make_country(**kwargs):
    return kwargs

country = make_country(name='New Zealand', capital='Wellington')
print(country)


#2.1
def make_country(name, capital):
    country = {'name': name, 'capital': capital}
    return country
print(make_country('New Zealand', 'Wellington'))

#Task 3

def make_operation(operator, *args):
    result = args[0]
    rest_args = args[1:]
    if operator == '+':
        for argument in rest_args:
            result += argument
    elif operator == '-':
        for argument in rest_args:
            result -= argument
    elif operator == '*':
        for argument in rest_args:
            result *= argument
    elif operator == '/':
        for argument in rest_args:
            result /= argument

    return(result)
print(make_operation('-', 5, 5, -10, -20))

