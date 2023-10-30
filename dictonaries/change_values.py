# Change a values in a dict.
this_dict = {
  "name":"Raj",
  'age':23, 
  'door_no': 20.3, 
  'boo':True
}
this_dict['age'] = 22 # changed age 23 to 22
print(this_dict)

# the update() method will update the dictionary with the items from the given argument.
this_dict = {
  "name":"Raj",
  'age':23, 
  'door_no': 20.3, 
  'boo':True
}
this_dict.update({'friend':'thrilok'})
print(this_dict)
