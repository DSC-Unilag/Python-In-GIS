dict_ = {('red', 'blue'): 'purple', ('red', 'yellow'): 'orange', ('blue', 'yellow'): 'green'}
color=input('Enter two colors seperated by space:  >>> ')
print(dict_.get(tuple(color.split(' ')), 'Error'))