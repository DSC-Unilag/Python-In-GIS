# Assignment Operators
a = 5   # "="  assigns 5 to the variable a
b = 10  # "=" assigns 5 to the variable b
b += 5  # Adds 5 to the present value of b and stores it in b same as b = b + a
b -= 5  # Subtracts 5 from the present value of b and stores it in b same as b = b - a
b *= 2  # Multiplies the present value of b by 2 and stores it in b same as b = b * 2
b /= 4  # Divided the present value of b by 4 and stores the result in b same as b = b / 4
b %= 3  # same as b = b % 3
b //= 2 # same as b = b // 2
b *= 3 # Same as b = b * 3



# Arithmetic Operator
a + b  # "+" adds the variables a and b together
a - b  # "-" subtracts the variable b from a
a / b  # "/" divides a by b and returns  the result in decimal
a % b  # "%" returns the remainder of the division a/b(Modulus)
a //b  # "//" returns the whole number when a is divided by b (Floor division)
a * b # "*" computes a raised to the power of b

# Comparison Operator
#It returns True or False.
a == b # Checks if a and b has same value, returns True if yes otherwise False
a > b  # Checks if a is greater than b, returns True if yes otherwise False
a < b  # Chceks if a is less than b, returns True if yes otherwise False
a <= b # Checks if a is less than or equal to b, returns True if yes otherwise False
a >= b # Checks if a is greater than or equal to b, returns True if yes otherwise False
a != b # Checks if a is not eqaul to b, returns True if yes otherwise False

# Logical Operators
a and b # True if both a and b are true, False if otherwise
a or b  # True if atleast one of a and b is True, False if otherwise
not a   # True if a is False, False if otherwise

# Membership operator
## test for membership in a sequence, such as strings, lists, or tuples.
b = [1, 2, 3, 4, 5]
3 in b     # Returns True since 3 is present in b
2 not in b # Returns False since 2 is in list

# Identityy Operators
# Identity operators compare the memory locations of two objects

x = 1
y = 1
x is y 	   # Returns True since x and y points to the same object in memory
x is not y # Returns False since x and y points to the same object in memory




