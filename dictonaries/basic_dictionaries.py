# A dictionary is a collection, which is ordered, indexed, and won't allow duplicate values
# Note: As of Python 3.7 version dictionaries are ordered. In python below 3.6 are earlier are un-ordered. 

this_dict = {"name":"RAj", 'age':23, 'address':'India'}
print(this_dict)

#dict()
this_dict = {"name":"RAj", 'age':23, 'address':'India'}
print(len(this_dict)) # len() function is used to get the length of the dictionary. 

# Ducplicate values are not allowed
# Duplicate values will overwrite existing values.
this_dict = {"name":"RAj", 'age':23, 'address':'India', "age":24}
print(this_dict)

# The value can be any data type 
this_dict = {"name":"RAj", 'age':23, 'door_no': 20.3, 'boo':True}
print(type(this_dict))
print(this_dict)
