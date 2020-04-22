def KelvinToFahrenheit(Temperature: float) -> float:
    '''
    A function that takes in a temperature valu in Kelvin and converts it to Fahrenheit

    Parameter: Temperature: Float or int
                            Temperature in Kelvin

    Returns: The temperature in Fahrenheit or Assertion Error if Temperature is lower than 0
    '''
    assert (Temperature >= 0),"Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273)) # 32.0
print(int(KelvinToFahrenheit(505.78))) # 451
# print(KelvinToFahrenheit(-5))
# Traceback (most recent call last):
#   File "c:/Users/user/Desktop/SEG With Python/Python-In-GIS/week4/codes/assert_exceptions.py", line 6, in <module>
#     print(KelvinToFahrenheit(-5))
#   File "c:/Users/user/Desktop/SEG With Python/Python-In-GIS/week4/codes/assert_exceptions.py", line 2, in KelvinToFahrenheit
#     assert (Temperature >= 0),"Colder than absolute zero!"
# AssertionError: Colder than absolute zero!

def mult(num: int) -> int:
    '''
    A function named mult that multiplies a number by 10

    Parameters: num:-- int
                Number to be multiplied by 10
        
    Returns 10 * num if input is a number, else returns "Invalid input, input should be an integer"
    '''
    try:
        num = int(num)
    except:
        return "Error: Invalid input, Input should be  integer"
    else:
        return 10 * num

print(mult(10)) # 100
print(mult('Babatunde')) # Error: Invalid input, Input should be  integer
print(mult([1, 2, 3, 4])) # Error: Invalid input, Input should be  integer
print(mult(20)) # 200


def divide(num_1: int, num_2: int) -> int:
    '''
    A function named divide that divides two numbers and return the results

    Parameters: num_1:-- int
                    The numerator
               num_2: int
                    The denominator
    
    Returns num_1/ num_2 if num_2 is 0 returns "num_2 can't be 0", else returns "Invalid Input"
    '''
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
        res = num_1 / num_2
    except ZeroDivisionError: # if denominator is 0
        return "denominator can't be 0"
    except:
        return "Error: Invalid input, Input should be  integer"
    else:
        return res

print(divide(10, 5)) # 100
print(divide('Babatunde', 3)) # Error: Invalid input, Input should be  integer
print(divide([1, 2, 3, 4], 12)) # Error: Invalid input, Input should be  integer
print(divide(20, 0)) # denominator can't be 0


def add(a: int, b: int) -> int:
    try:
        a = float(a)
        b = float(b)
        c = a + b
        c = round(c, 3)
    except TypeError:
        return "Input should be integer now"
    except ValueError:
        return f"Input should be integer"
    else:
        return f"Sum of {a} and {b} is {c}"

print(add(1, 2)) # Sum of 1.0 and 2.0 is 3.0
print(add(4.6, 7.8)) # Sum of 4.6 and 7.8 is 12.4
print(add(4.56, [1])) # Input should be integer now
print(add('a', 'b')) # Input should be integer

def sub(a, b):
    try:
        c = a - b
    except Exception as e: # e is the error message.
        return "Invalid Input. "+str(e).capitalize()
    else:
        return c

print(sub(1, 2)) # -1
print(sub(1, 'a')) # Invalid Input. Unsupported operand type(s) for +: 'int' and 'str'



