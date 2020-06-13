#write a series of random numbers to a file
#numbers should be in the range of 1 - 500
#user should specify how many numbers the file will hold

#set the filename as a global variable
FILENAME = r'C:\Users\User\Desktop\python-projects\python_projects\random-number.txt'

#i set the mode to append, so previous data will not be lost 
my_file = open(FILENAME, 'a')
user_choice = int(input('how many numbers should be stored in the file?: '))

#create a list to hold the numbers entered by the user
num_list = []

for num in range(0,user_choice):
    user_num = (input('write numbers between 1 and 500: '))
    num_list.append(user_num)
    my_file.write(user_num + '\n')
my_file.close()

my_file = open(FILENAME, 'r')
print('output')
print(my_file.read())