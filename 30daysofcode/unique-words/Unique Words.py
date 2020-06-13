#Unique Words
#Write a program that opens a specified text file 
# then displays a list of all the unique words found in the file.
#Hint: Store each word as an element of a set.

my_file = open(r'C:\Users\User\Desktop\python-projects\python_projects\unique-words.txt', 'r')
my_set = set()
for items in my_file:
    my_set.add(items.rstrip('\n'))
print(my_set)
