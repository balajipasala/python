# identity operators are used to check both variable objects are same or not 
# is 
x = ["python", "git", "aws"]
y = ["python", "git", "aws"]
print(x is y) # False because values are same but not the objects
z = x
print(z is x) # Returns True because both objects are same z and x.
print(x is z) # True 

# is not return True if both variable objects are not same 
x = ["python", "git", "aws"]
y = ["python", "git", "aws"]
z = x
print(z is not x) # Returns False because both variable objects are same 
print(x is not y) # Returns True because both variables are diff objects 
