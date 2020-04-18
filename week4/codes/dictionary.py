# Creating a Dictionary 
# with Integer Keys 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 

# Creating a Dictionary 
# with Mixed keys 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 


## Output --- 
## Dictionary with the use of Integer Keys: 
## {1: 'Geeks', 2: 'For', 3: 'Geeks'}

## Dictionary with the use of Mixed Keys: 
## {1: [1, 2, 3, 4], 'Name': 'Geeks'}

# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 

# Creating a Dictionary 
# with dict() method 
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 

# Creating a Dictionary 
# with each item as a Pair 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 



# Create and print a dictionary

thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
print(thisdict)

#Get the value of the "model" key
x = thisdict["model"]

'''
There is also a method called get() that will give you the same result
Get the value of the "model" key
'''

x = thisdict.get("model")

#Change the "year" to 2018

thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
thisdict["year"] = 2018
print(thisdict)

'''
You can also use the values() function to return values of a dictionary
The code will print out all the values in the key value pair in the dictionary
'''
for x in thisdict.values():
  print(x)

#Loop through both keys and values, by using the items() function
for x, y in thisdict.items():
  print(x, y)

#Print the number of items in the dictionary
print(len(thisdict))

#Adding an item to the dictionary is done by using a new index key and assigning a value to it
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
thisdict["color"] = "red"
print(thisdict)

#Creating a new dictionary and adding a new key: value pair to it
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
thisdict["color"] = "red"
print(thisdict) # {"brand": "Ford","model": "Mustang","year": 1964, "color": "red"}

# Looping through our dictionary
for key in thisdict: # This loops through alll the key 
  print(key, thisdict[key]) 
# Output ---
# brand, Ford
# model, Mustang
# year, 1964
# color, red

# Looping through the key and values
  # Turns the dictionary to a list of tuple where each tuple is a key value pair
for key, value in thisdict.items():
  print(key, value)
# Output ---
# brand, Ford
# model, Mustang
# year, 1964
# color, red

# Looping through the keys only
for key in thisdict.keys():
    print(key)
# Output ---
# brand
# model
# year
# color

# Looping through the values only
for value in thisdict.values():
    print(value)
# Output ---
# Ford
# Mustang
# 1964
# red