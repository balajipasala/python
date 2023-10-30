# accessing items 
this_dict = {"name":"Raj",'age':23, 'door_no': 20.3, 'boo':True}
print(this_dict["name"])

#Example2
this_dict = {"name":"Raj", 'age':23, 'door_no': 20.3, 'boo':True}
access = this_dict["age"]
print(access)

# get() is the another method of accessing items in the dict.
this_dict = {"name":"Raj", 'age':23, 'door_no': 20.3, 'boo':True}
access = this_dict.get('boo')
print(access)

# keys() method returns a list of all the keys in the dict. 
this_dict = {"name":"Raj", 'age':23, 'door_no': 20.3, 'boo':True}
key = this_dict.keys()
print(key)
this_dict["mobile_no"] = 82923
print(this_dict)

# values() method return a list of all the values in the dict.
this_dict = {"name":"Raj", 'age':23, 'door_no': 20.3, 'boo':True}
val = this_dict.values()
print(val)

#Items() method will return each item in a dict, as a tuple in a list
this_dict = {"name":"Raj", 'age':23, 'door_no': 20.3, 'boo':True}
item = this_dict.items()
print(item)

# Checking certain key is present in a dict or not 
this_dict = {"name":"Raj", 'age':23, 'door_no': 20.3, 'boo':True}
if 'name' in this_dict:
  print('yes avaliable')




