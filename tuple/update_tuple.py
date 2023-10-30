# Update Tuple 
'''
Tuple is unchangeable means you can't change the value once tuple is created,
this is also called as immutable.
'''
# There are times when you want to add a value into a tuple
# example 

this_tuple = ('mango', "apple", 'orange')
convert = list(this_tuple) # convert tuple into list
print(convert)
convert[1] = 'banana' # add changes
print(convert)
this_tuple = tuple(convert) # convert it back into tuple
print(this_tuple)


# you can remove a values from a the tuple, but you can delete entire tuple using del keyword
this_tuple = ('mango', "apple", 'orange')
del this_tuple

