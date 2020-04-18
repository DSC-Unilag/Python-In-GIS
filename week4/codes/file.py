import mymodule
import mymodule as mx
from mymodule import person1

# There are several built-in modules in Python, which you can import whenever you like.
# Import and use the platform module
import platform

mymodule.greeting("Jonathan") # Hello Jonathan

a = mymodule.person1["age"]
print(a) # 36

a = mx.person1["age"] # Using aliasing
print(a)


x = platform.system()
print(x) # Windows

# There is a built-in function to list all the function names (or variable names) in a module. 
x = dir(platform)
print(x)

print(person1['age']) # 36