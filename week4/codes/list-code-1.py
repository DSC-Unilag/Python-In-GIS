# saving my name, gender and age normally
name = "This is my name"
gender = "This is my gender"
age = "This is my age"

'''
we had to use 3 different variables to store 3 different values
but we will change this by using a list that has the ability to
store multiple values in one variable
'''
my_first_list = []

'''
we will now store our data in our list
the key thing about lists is that they are created with square brackets []
and their values are seperated by comma
note that there is no end to the number of elements in a list
'''
my_first_list = ["My Name", "My Gender", "My Age"]

'''
accessing list elements
let's say I wanted to print my name from the list
the first element in the list is accessed with index 0
'''
print(my_first_list[0]) #My name

'''
or assign my gender to a variable
the second element in the list is accessed with index 1 and we start counting
'''
my_gender = my_first_list[1]

print(my_gender) #My Gender

'''
you can assign all your variables to the list instead
because the list has 3 elements, python knows what to do
'''
name, gender, age = my_first_l

print(my_first_list) #['My Name', 'My Gender', 'My Age']
