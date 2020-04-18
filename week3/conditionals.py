# Conditionals with one conditionals

x,y =2,8 # Variable definition

if(x < y): # Checks if x is smaller than y
	st= "x is less than y" # Creates a new variable
    
print(st)
# x is less than y -- output, what happens if the condition isn't met?
 
# Conditionals with two conditionals

x,y =8,4
	
if(x < y): # Checks if x is less than y
	st= "x is less than y"
else: # If x is not less than y
	st= "x is greater than y"
print (st)
# x is greater than y -- output

# Conditionals with more than 2 statements

x,y =8,8
	
if(x < y):
	st= "x is less than y"
else:
	st= "x is greater than y"
print(st)
# x is greater than y, but x and y are the same so there's a logical error in our code, we need to add an extra condition!
x,y =8,8
	
if(x < y):
	st= "x is less than y"
elif (x == y):
	st= "x is same as y"
else:
	st="x is greater than y"
print(st)
## x is same as y -- output
##N/B: We can have as many elif statements but we need to begin it with an if statement and end it with an else statement