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