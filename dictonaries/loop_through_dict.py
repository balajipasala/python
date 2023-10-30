# looping through the dict.
# The Del keyword deletes the entire dict.
this_dict =  {
  "name":"raj", 
  "age":22,
  "address":"vrk",
  "b.e.cse":75
}
for i in this_dict:
  print(i) # Will return keys
  
this_dict =  {
  "name":"raj", 
  "age":22,
  "address":"vrk",
  "b.e.cse":75
}
for i in this_dict:
  print(this_dict[i]) # Return values
  
 # You can also use values() method to return a dict values. 
this_dict =  {
  "name":"raj", 
  "age":22,
  "address":"vrk",
  "b.e.cse":75
}
for i in this_dict.values():
    print(i) # returns values
    
# You can also use keys() method to return a dict keys. 
this_dict =  {
  "name":"raj", 
  "age":22,
  "address":"vrk",
  "b.e.cse":75
}
for i in this_dict.keys():
    print(i) # returns keys
    
    
this_dict =  {
  "name":"raj", 
  "age":22,
  "address":"vrk",
  "b.e.cse":75
}
for i, j in this_dict.items(): # returns both keys and values
    print(i, j) # returns both keys and values

this_dict = {
  
  "name" : "Thundersoft",
  "plot_no": 45,
  "location" : "Hyderabad"
}

for i , j in this_dict.items():
  print(str(i) + ":" + str(j))