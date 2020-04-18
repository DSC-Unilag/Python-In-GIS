# tuple methods

# creating a tuple
my_first_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

'''
tuple values cannot be changed
accessing tuple values
this will print the first element in the tuple
'''
print(my_first_tuple[0]) #1

# still accessing tuple values
var1 = my_first_tuple[3]
var2 = my_first_tuple[-1]
print(var1) #4
print(var2) #10

# length of a tuple
print(len(my_first_tuple)) #10

# number of element occurence in a tuple
print(my_first_tuple.count(1)) #1

# getting index of tuple element
print(my_first_tuple.index(3)) #10

# NOTE:
# A tuple is immutable(i.e The elements in a tuple cannot be changed)
