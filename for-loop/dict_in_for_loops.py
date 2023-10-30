'''
for loops in dictionaries
'''

my_dict = {
    'key1':'value1',
    'key2':'value2',
    
}

for i in my_dict:
    print(i)
    
for i in my_dict.keys(): # keys method will only return key values
    print(i)
    
for i in my_dict.values():
    print(i)
    
for i in my_dict.items():
    print(i)
    
# unpacking 

for key, value in my_dict.items():
    print(key,  value)
