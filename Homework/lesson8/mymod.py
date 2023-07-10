
def count_lines(name):
    with open('zhytynadainteresna.txt') as f:
        lines = len(f.readlines())
        return lines

file = 'zhytynadainteresna.txt'


def count_chars(name):
    with open('zhytynadainteresna.txt') as f:
        chars = len(f.read())
        return chars


def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    print(f'The number of lines in {file} is: {count_lines(file)}')
    print(f'The number of chars in {file} is: {count_chars(file)}')


if __name__== '__main__':
    file = input('Enter your file name: ')
    test(file)