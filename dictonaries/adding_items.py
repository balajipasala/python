#adding items 
this_dict = {
  "name":"raj",
  'age':23, 
  'door_no': 20.3, 
  'boo':True
}
this_dict["friend"] = 'Thrilok'
print(this_dict)

# update() method will update the dict with items from the arguments
this_dict = {
  "name":"raj",
  'age':23, 
  'door_no': 20.3, 
  'boo':True
}
this_dict.update({'father':'Gopal Raju'})
print(this_dict)
