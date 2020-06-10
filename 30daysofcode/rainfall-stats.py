dict_ = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 
         8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
}

rainfalls = list(map(lambda x: float(x), input('Enter the rainfall of each monthes seperated by space: >> ').split(' ')))
print(f'Total rainfall is {sum(rainfalls)}\n\
Average monthly rainfall is {sum(rainfalls)/12} \n\
The month with the highest rainfall is {dict_.get(rainfalls.index(max(rainfalls))+1)} \n\
The month with the lowest rainfall is {dict_.get(rainfalls.index(min(rainfalls))+1)}')

'''
Implementataion in a function
def rain(rainfalls):
    dict_ = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 
         8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }

    rainfalls = list(map(lambda x: float(x), rainfalls.split(' ')))
    return 'Total rainfall is {sum(rainfalls)}\n\
Average monthly rainfall is {sum(rainfalls)/12} \n\
The month with the highest rainfall is {dict_.get(rainfalls.index(max(rainfalls))+1)} \n\
The month with the lowest rainfall is {dict_.get(rainfalls.index(min(rainfalls))+1)}'
'''
