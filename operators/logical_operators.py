# Logical Operators 
'''
1)and - Returns True if both statements are True
2)or - Return True if any one statement is True
3)not - Return True, if statement is False, it opposite's the answer.
'''
# and 
val = 10
val1 = 20
val2 = 30
if (val < val1) and (val2 > val1): # both statements are True 
  print("Both statements are True")
else:
  print("Both statements are False")
  
# or
val = 10
val1 = 20
val2 = 30
if (val > val1) or (val2 > val1): # here one statement is False and other one is True 
  print("Both statements are True")
else:
  print("Both statements are False")
  
# not
val = 10
val1 = 20
val2 = 30
if (not(val < val1) and (val2 > val1)): # both statements are True 
  print("Both statements are True")
else:
  print("Both statements are False")
