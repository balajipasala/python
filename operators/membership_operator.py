# Membership operators
'''
Membership operators are used to check certain sequence is present in the object
are not  
'''
x = ["Docker", "Azure", "Linux"]
print("Linux" in x)

'''
not in membership operator returns True if the specified value is not present in
the object 
'''
x = ["Docker", "Azure", "Linux"]
print("Linux" not in x) # False 

'''
Membeship operator:-

Returns True, if a sequence with the specified value present in the object.

'''


x = ['hello', 'world']
if 'hello' in x:
    print("Returns True, if a sequence with a specified value present in the object.")
else:
    print('It\'s not a Membership operator')
