# Python filter() function example    
numbers = [ 1, -2, 3, -4, 5, -6 ]  
  
# Using filter() to remove negative numbers from the list  
result = list(filter(lambda x: x >= 0, numbers))  
  
# Printing the result  
print(result)  