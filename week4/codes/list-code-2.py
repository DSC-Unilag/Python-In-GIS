'''
list methods
A method is an inbuilt functionality in a class or data structure
we will be going over some of the methods in lists
'''
# let's first create 2 lists
my_first_list = [1, 2, 3, 4, 5]
my_second_list = [6, 7, 8, 9, 10]

'''
just to recap we access list elements with indexes
0 is the first value in the list and 1 is the second
'''
print(my_first_list[0]) #1

# python also supports negative index and -1 is the last element

print(my_first_list[-1]) #5

# adding a new element to a list
my_first_list.append(6)
my_first_list.append(7)

# the list should have values 6 and 7 in it

print(my_first_list) #[1, 2, 3, 4, 5, 6, 7]

'''
removing an element from a list
method 1 - this will remove the first occurence of the element
this will remove
'''
my_first_list.remove(1)
print(my_first_list) #[2, 3, 4, 5, 6, 7]

'''
method 2 - this will remove an element at a given index
we will remove the element at index 2 (third element)
'''
my_first_list.pop(2)
print(my_first_list) #[2, 3, 5, 6, 7]

'''
method 3 - this will remove an element at a given index
we will remove the first element in the list
'''
del my_first_list[0]
print(my_first_list) #[3, 5, 6, 7]

'''
clear all elements in a list
this will delete all the elements in a list
'''
my_second_list.clear()
print(my_second_list) #[]
