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

my_function("Emil") # TypeError: my_function() missing 1 required positional argument: 'lname'

# Default Parameter Value
# If we call the function without argument, it uses the default value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden") # I am from Sweden
my_function # I am from Norway
my_function() # I am from Norway
my_function("Brazil")# I am from Brazil