series = list(map(lambda x: float(x), input('Enter the series of 20 numbers seperated by space: >> ').split(' ')))
print(f"The minimum number in the series is {min(series)}\n\
The maximum number in the series is {max(series)}\n\
The total number in the series is {sum(series)}\n\
The average value of the series is {sum(series)/len(series)}\n")

'''
Implementation in fucntion
    def series_(series):
        series = list(map(lambda x: float(x), series.split()))
        return f"The minimum number in the series is {min(series)}\n\
    The maximum number in the series is {max(series)}\n\
    The total number in the series is {sum(series)}\n\
    The average value of the series is {sum(series)/len(series)}\n"
'''