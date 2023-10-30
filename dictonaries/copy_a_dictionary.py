# copying the dictionary
    
this_dict =  {
  "name":"raj", 
  "age":22,
  "address":"vrk",
  "b.e.cse":75
}
cp = this_dict.copy()
print(cp)

# another way of copying dictionary using dict datatype

this_dict =  {
  "name":"raj", 
  "age":22,
  "address":"vrk",
  "b.e.cse":75
}
cp = dict(this_dict)
print(cp)
