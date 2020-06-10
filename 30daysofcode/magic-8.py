from random import choice

while True:
    a=input('Enter your question:>>>  ')
    if a != '':
        with open('magic-8.txt') as f:
            f = list(map(lambda  x: x[:-2 ] if '\n' in x else x, f.readlines()))
        print(choice(f))
    if input('Do you want to quit, q to quit: >>>') == 'q':
        break