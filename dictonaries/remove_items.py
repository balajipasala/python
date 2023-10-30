# Removing items 
# The pop() method will remove the item with specified key
this_dict =  {
  "name":"Raj", 
  "age":22,
  "address":"vrk",
  "b.e.cse":75
}
this_dict.pop('age')
print(this_dict)

# The popitem() method will remove last inserted item in Python 3.7 version, before 3.6 or earlier version it will remove random item 
this_dict =  {
  "name":"Raj", 
  "age":22,
  "address":"vrk",
  "b.e.cse":75
}
this_dict.popitem()
print(this_dict)

# The clear method clears the entire dict. 
this_dict =  {
  "name":"Raj", 
  "age":22,
  "address":"vrk",
  "b.e.cse":75
}
this_dict.clear()
print(this_dict)

# The Del keyword deletes the entire dict.
this_dict =  {
  "name":"Raj", 
  "age":22,
  "address":"vrk",
  "b.e.cse":75
}
del this_dict
