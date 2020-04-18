# Python program to illustrate 
# while loop 
count = 0 
while (count < 3):     
    count = count + 1
    print("Hello Geek") 

## Output ---
### Hello Geek
### Hello Geek
### Hello Geek

#Python program to illustrate 
# combining else with while 
count = 0
while (count < 3):	 
	count = count + 1
	print("Hello Geek") 
else: 
	print("In Else Block") 

## Output --
### Hello Geek
### Hello Geek
### Hello Geek
### In Else Block                                       

print("List Iteration") 
l = ["geeks", "for", "geeks"] 
for i in l: 
    print(i) 
       
# Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("geeks", "for", "geeks") 
for i in t: 
    print(i) 
       
# Iterating over a String 
print("\nString Iteration")     
s = "Geeks"
for i in s : 
    print(i) 
       
# Iterating over dictionary 
print("\nDictionary Iteration")    
d = dict()  
d['xyz'] = 123
d['abc'] = 345
for i in d : 
    print("%s  %d" %(i, d[i])) 

## Output --
## List Iteration
## geeks 
## for 
## geeks

##  Tuple Iteration
## geeks 
## for 
## geeks

## String Iteration
## G
## e
## e
## k
## s

## Dictionary Iteration
## xyz  123
## abc  345

# Python program to illustrate 
# Iterating by index 

list = ["geeks", "for", "geeks"] 
for index in range(len(list)): 
	print (list[index])

## output --
## geeks 
## for
## geeks


 ## Continue
# Prints all letters except 'e' and 's' 
for letter in 'geeksforgeeks': 
	if letter == 'e' or letter == 's': 
		continue
	print ('Current Letter :', letter)                  
	var = 10

## Output
## Current Letter : g
## Current Letter : k
## Current Letter : f
## Current Letter : o
## Current Letter : r
## Current Letter : g
## Current Letter : k

# Break statement
for letter in 'geeksforgeeks': 

	# break the loop as soon it sees 'e' 
	# or 's' 
	if letter == 'e' or letter == 's': 
		break

print ('Current Letter :', letter)

## Output
# Current Letter : e

## Pass statement
# An empty loop 
for letter in 'geeksforgeeks': 
	pass
print('Last Letter :', letter)

## Output
# Last Letter : s

