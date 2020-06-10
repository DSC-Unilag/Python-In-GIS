def capitalize(string=input('Enter a text: >>>  ')):
    return '. '.join([s.capitalize() for s in string.split('. ')])

print(capitalize())