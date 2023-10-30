# Slicing 
'''
you can return a range of character's in a string by using slicing, specify
the start and end index, seperated by colon, to return a part of string. 
'''

x = "Hello World!"
slicing = x[1:] # it will start from position 1 to end 
print(slicing) 

x = "Hello World!"
slicing = x[:1] # it will start from position 0 and ends at position 1(not included 
print(slicing) 

# Remember that the first character position start's from zero(0)
# Negative indexing

x = "Hello World!"
slicing = x[-5:-1] #negative index start from end of the string with -1 position  
print(slicing)  # [!] not included 

# -

x = "Hello World!"
slicing = x[0:4] 
print(slicing) 


# reverse a string
x = "Hello World!"
slicing = x[::-1] 
print(slicing) 

