import os
name, score = input('Enter your name:>>>  '), input('Enter your score:>>>  ')

if 'golf.txt' in os.listdir():
    with open('golf.txt', 'a') as f:
        f.write(f"\n{name}{'='*(50-(len(name)+len(score)))}{score}")
else:
    with open('golf.txt', 'w') as f:
        f.write('Name=========================================Score')
        f.write(f"\n{name}{'='*(50-(len(name)+len(score)))}{score}")

with open('golf.txt') as f:
    g = f.readlines()

print(''.join(g))
'''
Implementation in functipn
def golf(name, score):
    if 'golf.txt' in os.listdir():
        with open('golf.txt', 'a') as f:
            f.write(f"\n{name}{'='*(50-(len(name)+len(score)))}{score}")
    else:
        with open('golf.txt', 'w') as f:
            f.write('Name=========================================Score')
            f.write(f"\n{name}{'='*(50-(len(name)+len(score)))}{score}")

    with open('golf.txt') as f:
        g = f.readlines()

    return ''.join(g)
'''