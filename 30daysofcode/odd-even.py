def even_odd(n):
    return True if n%2==0 else False

def generate():
    from random import choices
    random = choices(range(1, 1000), k=100)
    even = len(list(filter(even_odd, random)))
    return f'Number of even numbers is {even} and that of odd is {100-even}.'
print(generate())