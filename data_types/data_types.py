# Data types in python
'''
1)Text data type :-  str,
2)numbers:- int, float, complex
3)sequence data type:- list,tuple,range
4)mapping data type:- dictionary
5)set data type:- set, frozenset
6)bool = bool
7)binary data type:- bytes, bytearrya, memoryview
'''

'''
A string is a sequence of characters and surronded with either single 
quotes(' ') are double quotes(" ").

'''
a = 'hello world' #text data type
print(a)
print(type(a))

# Numbers data types
'''
integer (int or integer is a whole number, positive number or negative number
without decimal points with length of unlimited. 
'''
b = 10 # positive integer
print(b)
print(type(b))

c = -29 #Negetive integer
print(c)
print(type(c))

# float or floating point 
'''
float or floating point is number, positive, negative with atleast one or more
decimal points 
'''
num = 25.23 # positive integer
print(num)
print(type(num))

num1 = -25.5 #Negetive float
print(num1)
print(type(num1))

# sequence data types 

fruits = ['apple', 'banana', 52] # list
print(fruits)
print(type(fruits))

# tuple
comp_languages = ('python', 'go', 'sql')
print(comp_languages)
print(type(comp_languages))

# mapping data type
# dictionary
age = {'guna':22, 'thrilok':22}
print(age)
print(type(age))

# set data type
# set

sports = {'cricket', 'shuttle', 'football', 'cricket', 'shuttle'}
print(sports)
print(type(sports))

# frozenset 

sports = frozenset({'cricket', 'shuttle', 'football', 'cricket', 'shuttle'})
print(sports)
print(type(sports))

# bool

'''
will return True or False 
'''
val = True
print(val)
print(type(val))

#binary data types 
# bytes

x = bytes("hello")
print(x)
print(type(x))

#bytearray
y = bytearray(73)
print(y)
print(type(y))

#memoryview

z = memoryview(bytes(100))
print(z)
print(type(z))
