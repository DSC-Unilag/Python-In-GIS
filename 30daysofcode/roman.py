num = int(input('Enter a number between 1 and 10: >>>  '))
dict_ = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7:'VII', 8: 'VIII', 9: 'IX', 10: 'X'}
print(dict_.get(num, 'Error, number should be btween 1 and 10'))