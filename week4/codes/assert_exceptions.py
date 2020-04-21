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
    
    Returns 10 * num
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
