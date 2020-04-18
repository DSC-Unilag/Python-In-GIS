# We call a function  by writing the function name and adding parenthesis and putting the parameter, here no parameter
def my_function():
    print("Hello from a function")
my_function() # Hello from a function

# Adding Parameters to our Function
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil") # Emil Refsnes
my_function("Tobias") # Tobias Refsnes
my_function("Linus") # Linus Refsnes

# This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes") # Emil Refsnes

# If you try to call the function with 1 or 3 arguments, you will get an error:

def my_function(fname, lname):
  print(fname + " " + lname)

# my_function("Emil") # TypeError: my_function() missing 1 required positional argument: 'lname'

# Default Parameter Value
# If we call the function without argument, it uses the default value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden") # I am from Sweden
my_function # I am from Norway
my_function() # I am from Norway
my_function("Brazil")# I am from Brazil

# Return Values
# To let a function return a value, use the return statement

def my_function(x):
  return 5 * x

print(my_function(3)) # 15
print(my_function(5)) # 25
print(my_function(9)) # 45

# Pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition 
# with no content, put in the pass statement to avoid getting an error

def myfunction():
  pass

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6) 
# Output ---
# 1
# 3
# 6
# 10
# 15
# 21

### LAMBDA FUNCTIONS
# A lambda function that adds 10 to the number passed in as an argument, and print the result:
x = lambda a : a + 10
print(x(5)) # 15
print(x(4)) # 14

# A lambda function can have more than 1 argument
x = lambda a, b : a * b
print(x(5, 6)) # 30
print(x(11, 7)) # 77

def myfunc(n):
  return lambda a : a ** n

mydoubler = myfunc(2) # 2 is the argument of myfunc
mytripler = myfunc(3) # 3 is the argument of myfunc


print(mydoubler(11)) # 121, 11 is the value assigned to a
print(mytripler(11)) # 1331, 11 is the value assigned to a

## MAP FUNCTION
## You'll notice that I'm using the list function before printing, this is because map returns a map object

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x) # <map object at 0x016B3050>
print(list(x)) # [5, 6, 6]

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(x) # <map object at 0x016B3090>
print(list(x)) # ['appleorange', 'bananalemon', 'cherrypineapple']

## ZIP FUNCTION
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(zipped)  # Holds an iterator object <zip object at 0x7fa4831153c8>
print(type(zipped)) # <class 'zip'>
print(list(zipped)) # [(1, 'a'), (2, 'b'), (3, 'c')]