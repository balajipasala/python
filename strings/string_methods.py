# String methods
#upper method is used to convert lower case letter's to upper case
text = 'lower case string'
result = text.upper() # .upper()
print(result)

# Lower case (Upper case to Lower case)
text = 'UPPER CASE TO LOWER CASE'
convertion = text.lower() #.lower()
print(convertion)

# strip method removes white spaces from beginnig and ending.
text = "   remove white spaces from beg and ending             "
print(text.strip()) # .strip()

# To replace a string with another string 
text = 'strive'
print(text.replace('strive', 'work hard to achieve something')) #.replace()

# split method splits the string into sub-strings if it finds separator

fruits = 'apple, banana mango range'
print(fruits.split(',')) # .split(separator, maxsplit)
print(fruits.split(" "))

# capitalize() 
# Converts the first character to upper case
text = 'converts the first character upper case '
print(text.capitalize())

#casefold (converts uppercase to lowercase similar to lower method)
text = 'I\'m Learning Docker'
print(text)

# center() method
text = 'AWS'
print(text.center(10, 'g'))

# count()
'''
count method will return the no of times the particular value appears 
in the string
'''
text = 'I love technology, technology has a great feature'
print(text.count('technology'))
