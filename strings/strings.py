# Strings in python
''' 
A sequence of character's is know as strings. 
'''
# Single line string
x = 'one'
print(x)
print(type(x))

# Multiline strings 
y = """ so this is about multiline strings in python.
python is a dynamically typed programming language """
print(y)
print(type(y))

# Strings are arrays
''' 
Like many other programming languages, strings in python are a array
of bytes representing a unicode character's.
However python does not have character data type, so even a single 
character is known as a string with the length of 1.
'''
 
# To access a element's in a string we can use square brackers[]

elements = "accessing elements"
print(elements[2]) # remember that first character is a position of 0

# Looping through a string
looping = 'looping through a string'
for x in looping:
	print(x)


# To check if a certain phrase or character is present in a string.
phrase = 'Python supports for scripting'
print('scripting' in phrase) # in keyword is used 

# Using if condition 
phrase = 'Python supports for scripting'
if 'scripting' in phrase:
	print('yes! present')

# Length function is used to get the length of the string.
length = 'get the length of the string'
count = len(length)
print(count)

# To check if a certain phrase or character is not present in a string.

phrase = 'Python supports for scripting'
print('programming' not in phrase) # not in keyword is used 


