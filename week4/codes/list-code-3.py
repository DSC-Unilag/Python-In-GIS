# list methods 2
# we will be going over some uses of lists

# let's first create 2 lists
my_first_list = [1, 2, 3, 4, 5]
my_second_list = [6, 7, 8, 9, 10]

# reversing a list
my_first_list.reverse()
print(my_first_list) #[5, 4, 3, 2, 1]

# sorting a list
my_second_list.sort()
print(my_second_list) #[6, 7, 8, 9, 10]

# adding 2 lists then sorting it at the instance using the sorted() method
my_third_list = my_first_list + my_second_list
print(sorted(my_third_list)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# counting elements
# we will count the number of occurences of a element
# this should return the number of times 6 is in the list
print(my_second_list.count(6)) #1

# get index of element
# we will get the index of where 6 is in our list
print(my_second_list.index(6)) #0

# splicing lists
# splicing means selecting only a part of a list
# this will assign all the elements from index 3 to index 8
spliced_list = my_third_list[3:8]
print(spliced_list) #[2, 1, 6, 7, 8]

# this will assign the first 5 elements in the list to spliced_list
spliced_list = my_first_list[:5]
print(spliced_list) #[5, 4, 3, 2, 1]

# this will assign all the elements from index 5 to the end
spliced_list = my_first_list[5:]
print(spliced_list) #[]

# lists are good to work with loops
# this will print out all the elements in the list one by one wtih every character in a new line.
for i in my_first_list:
    print(i)
