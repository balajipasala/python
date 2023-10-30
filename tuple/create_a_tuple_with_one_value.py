'''
To create a tuple with one value you have to add a comma after the one value,
otherwise Python thinks  that it is not a tuple
'''
this_tuple = ('mango',)  # Tuple
print(this_tuple)
print(type(this_tuple))

this_tuple = ('mango')  # Not Tuple
print(this_tuple)
print(type(this_tuple)) #string

# Tuple can be any data type

data_type = ('string', 20, 65.233, True)
print(data_type)
print(type(data_type))

# Tuple Constructor 
constructor = tuple(('one', 'two', 'three'))
print(constructor)
print(type(constructor))