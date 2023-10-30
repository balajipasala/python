# string methods
# .title()
# converts first character of each word into uppercase.
txt = "welcome to my world"
print(txt.title())

# .isupper returns True or False.
txt = "welcome to my world"
print(txt.isupper())

# .islower also returns True or False.
txt = "welcome to my world"
print(txt.islower())

#isalpha (Returns True if all the character's in the string are alphabets(a-z).
txt = "welcome to my world"
print(txt.isalpha())

#isnumeric returns True if all the character's in the string numbers.
txt = "154615"
print(txt.isnumeric())

#endswith return's True if the specified value present at the ending of the string.
txt = "so, this is the example about endswith method."
print(txt.endswith('.'))

#startswith returns True if the specified value present at the begining of the string.
txt = "so, this is the example about endswith method."
print(txt.startswith('s'))

#swapcase converts upper case to lower case and lower case to uppercase
txt = 'Example for swapcase METHOD IN StrINgs'
print(txt.swapcase())

#isspace returns True if all the characters are white space 

'''
join method syntax

string.join(iterable)

join method takes all the items in an iterable and joins them into a string
'''

ls = ['append', 'clear', 'insert']
st = ' # '.join(ls)
print(st)
txt = "    "
print(txt.isspace())

# difference between find() method and index() method
'''
find method returns -1 if specified value not present
index method will through an error if specified value is not present
'''
txt = "hello world"
print(txt.find('q'))
print(txt.index('d'))
