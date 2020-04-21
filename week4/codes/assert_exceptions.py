def KelvinToFahrenheit(Temperature):
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

def mult():
    '''
    A function named mult that multiplies a number by 10

    Parameters: None
    
    Returns 10 * the input of the user.
    
    @author: Babatunde Koiki
    
    Created on: 21-04-2020
    '''
    try:
    inp = int(input('Enter an Integer: '))
    
    except TypeError:
    print("Error: Invalid input, Input should be  integer")
    else:
    print(inp * 10)