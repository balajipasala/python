# Example 
this_dict =  {
  "child1":{
      "name":"prabhas",
      "age": 22
      },
      "child2":{
          "name":'hello',
          "age":1998
          }
      }
  
print(this_dict)

# copying the dictionary
    
this_dict =  {
  "name":"raj",
  "age":22,
  }
another_dict = {
    "name":"ram",
    "age": 23
}
  
last_dict = {
    "name":"last",
    "age":22
}
final_combine = {
    "this_dict":this_dict,
    "another_dict":another_dict,
    "last_dict":last_dict
}
print(final_combine)
