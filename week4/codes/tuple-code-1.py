# tuple methods

# creating a tuple
my_first_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# tuple values cannot be changed
# accessing tuple values
# this will print the first element in the tuple
print(my_first_tuple[0])

# still accessing tuple values
var1 = my_first_tuple[3]
var2 = my_first_tuple[-1]
print(var1)
print(var2)

# length of a tuple
print(len(my_first_tuple))

# number of element occurence in a tuple
print(my_first_tuple.count(1))

# getting index of tuple element
print(my_first_tuple.index(3))
