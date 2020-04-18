# set methods
# we will be going over some of the methods in sets

# let's first create 2 sets
my_first_set = {1, 2, 3, 4, 5}
my_second_set = {6, 7, 8, 9, 10}

# this will add 6 to the set
my_first_set.add(6)
print(my_first_set) #{1, 2, 3, 4, 5, 6}

# this will remove 6 from the set
my_first_set.remove(6)
print(my_first_set) #{1, 2, 3, 4, 5}

# adding 2 sets
# recall that set does not store duplicates
# so if 2 values occur, it will only store 1
my_third_set = my_first_set|my_second_set
print(my_third_set) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# this will return all the elements that are in first set
# but not in the second set
my_third_set = my_first_set - my_second_set
print(my_third_set) #{1, 2, 3, 4, 5}

# this will print the length of a set
# note that this function works for lists too
print(len(my_first_set)) #5

# this will convert a list to a set with the set function
# this will also convert a set to a list with the list()
sample_list = [1,2,3,4,5]
sample_set = set(sample_list)
sample_list_2 = list(sample_set)

# clear set
# this will clear a set
my_first_set.clear()
print(my_first_set) #set()
